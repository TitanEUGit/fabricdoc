"""
Share all Fabric connections with the Fabric-Migration-US-Source service principal.
Object ID: 4f525be9-0582-4e24-87dc-98812d526001
Application ID: 28d90760-5394-4a6b-8af5-b9e364c29b99
"""
import os, json, requests, sys, time

ENV_PATH = "/home/obaliuta/titan/fabricdevws/localdev/.env"
FABRIC_API = "https://api.fabric.microsoft.com/v1"

SP_NAME = "Fabric-Migration-US-Source"
SP_OBJECT_ID = "4f525be9-0582-4e24-87dc-98812d526001"
SP_APP_ID = "28d90760-5394-4a6b-8af5-b9e364c29b99"
PRINCIPAL_TYPE = "ServicePrincipal"
ROLE = "User"

OBALIUTA_ID = "002d4af6-ad12-442f-91fa-ce5aded47968"

def load_token():
    tokens = {}
    with open(ENV_PATH) as f:
        for line in f:
            line = line.strip()
            if "=" in line and not line.startswith("#"):
                k, v = line.split("=", 1)
                tokens[k] = v
    return tokens.get("FABRIC_ACCESS_TOKEN")

def fabric_headers(token):
    return {"Authorization": "Bearer " + token, "Content-Type": "application/json"}

def list_connections(token):
    all_connections = []
    url = FABRIC_API + "/connections"
    page = 0
    while url:
        page += 1
        resp = requests.get(url, headers=fabric_headers(token))
        if resp.status_code != 200:
            print("ERROR listing connections:", resp.status_code, resp.text[:500])
            break
        data = resp.json()
        conns = data.get("value", [])
        all_connections.extend(conns)
        print("  Page", page, "- fetched", len(conns), "connections (total:", len(all_connections), ")")
        ct = data.get("continuationToken")
        url = (FABRIC_API + "/connections?continuationToken=" + ct) if ct else None
    return all_connections

def get_role_assignments(token, conn_id):
    url = FABRIC_API + "/connections/" + conn_id + "/roleAssignments"
    resp = requests.get(url, headers=fabric_headers(token))
    if resp.status_code == 200:
        return resp.json().get("value", [])
    return []

def add_role_assignment(token, conn_id, principal_id, principal_type, role):
    url = FABRIC_API + "/connections/" + conn_id + "/roleAssignments"
    body = {
        "principal": {
            "id": principal_id,
            "type": principal_type
        },
        "role": role
    }
    resp = requests.post(url, headers=fabric_headers(token), json=body)
    return resp.status_code, resp.text

def main():
    fab_token = load_token()
    if not fab_token:
        print("ERROR: No FABRIC_ACCESS_TOKEN in .env")
        sys.exit(1)

    # STEP 1: List all connections
    print("=" * 80)
    print("STEP 1: Listing all Fabric connections...")
    print("=" * 80)
    connections = list_connections(fab_token)
    print("\nTotal connections found:", len(connections))

    shareable = [c for c in connections if c.get("connectivityType") == "ShareableCloud"]
    personal = [c for c in connections if c.get("connectivityType") == "PersonalCloud"]
    other = [c for c in connections if c.get("connectivityType") not in ("ShareableCloud", "PersonalCloud")]
    print("  ShareableCloud:", len(shareable))
    print("  PersonalCloud:", len(personal), "(cannot be shared)")
    if other:
        print("  Other:", len(other))

    # STEP 2: Share all ShareableCloud connections with the service principal
    print("\n" + "=" * 80)
    print("STEP 2: Sharing", len(shareable), "ShareableCloud connections with", SP_NAME)
    print("  Object ID:", SP_OBJECT_ID)
    print("  Principal Type:", PRINCIPAL_TYPE)
    print("  Role:", ROLE)
    print("=" * 80)

    success = 0
    skipped_already = 0
    skipped_no_reshare = 0
    failed = 0
    errors = []

    for i, conn in enumerate(shareable):
        conn_name = conn.get("displayName", "N/A")
        conn_id = conn["id"]

        # Check existing role assignments
        assignments = get_role_assignments(fab_token, conn_id)

        # Check if SP already has access
        already_has = False
        caller_can_reshare = False
        for a in assignments:
            p = a.get("principal", {})
            pid = p.get("id", "")
            role = a.get("role", "")

            if pid == SP_OBJECT_ID:
                already_has = True

            if pid == OBALIUTA_ID and role in ("Owner", "UserWithReshare"):
                caller_can_reshare = True

        if already_has:
            skipped_already += 1
            continue

        if not caller_can_reshare:
            skipped_no_reshare += 1
            continue

        # Share
        status, text = add_role_assignment(fab_token, conn_id, SP_OBJECT_ID, PRINCIPAL_TYPE, ROLE)
        if status in (200, 201):
            success += 1
            if (success % 20) == 0:
                print("  ... shared", success, "connections so far")
        else:
            failed += 1
            error_msg = text[:500]
            errors.append({"name": conn_name, "id": conn_id, "status": status, "error": error_msg})
            if status == 429:
                print("  Rate limited! Waiting 30 seconds...")
                time.sleep(30)

    # RESULTS
    print("\n" + "=" * 80)
    print("RESULTS")
    print("=" * 80)
    print("Service Principal:", SP_NAME)
    print("Object ID:", SP_OBJECT_ID)
    print("Application ID:", SP_APP_ID)
    print()
    print("Total connections:", len(connections))
    print("  ShareableCloud:", len(shareable))
    print("  PersonalCloud:", len(personal), "(not sharable)")
    if other:
        print("  Other:", len(other))
    print()
    print("Sharing results (ShareableCloud only):")
    print("  Successfully shared:", success)
    print("  Skipped (SP already has access):", skipped_already)
    print("  Skipped (caller lacks reshare permission):", skipped_no_reshare)
    print("  Failed:", failed)

    if errors:
        print("\nFailed connections:")
        for e in errors:
            print("  -", e["name"], "(" + e["id"] + ")")
            print("    Status:", e["status"])
            print("    Error:", e["error"][:300])

    # Save summary
    summary = {
        "service_principal": SP_NAME,
        "sp_object_id": SP_OBJECT_ID,
        "sp_app_id": SP_APP_ID,
        "principal_type": PRINCIPAL_TYPE,
        "role_assigned": ROLE,
        "total_connections": len(connections),
        "shareable_cloud": len(shareable),
        "personal_cloud": len(personal),
        "successfully_shared": success,
        "skipped_already_has_access": skipped_already,
        "skipped_no_reshare_permission": skipped_no_reshare,
        "failed": failed,
        "errors": errors
    }
    out_path = "/mnt/c/Users/OBaliuta/OneDrive - Titan Machinery Inc/Desktop/fabric documentation/share_connections_sp_result.json"
    with open(out_path, "w") as f:
        json.dump(summary, f, indent=2)
    print("\nFull results saved to share_connections_sp_result.json")

if __name__ == "__main__":
    main()
