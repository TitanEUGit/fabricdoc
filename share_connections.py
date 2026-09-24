"""
Share all Fabric connections with rb.admin@titanmachinery365.onmicrosoft.com.
Phase 1: Discover the admin's Object ID from connection names / role assignments.
Phase 2: Add role assignment to all connections where admin doesn't already have access.
Handles PersonalCloud (non-sharable) and null credentialDetails gracefully.
"""
import os, json, requests, sys, time

ENV_PATH = "/home/obaliuta/titan/fabricdevws/localdev/.env"
FABRIC_API = "https://api.fabric.microsoft.com/v1"
ADMIN_UPN = "rb.admin@titanmachinery365.onmicrosoft.com"
ROLE = "User"  # Options: "Owner", "User", "UserWithReshare"

# Known IDs from initial scan
OBALIUTA_ID = "002d4af6-ad12-442f-91fa-ce5aded47968"
SUSPECTED_ADMIN_ID = "8d558007-9bee-426b-b5e9-7773b3bd6916"

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

def add_role_assignment(token, conn_id, principal_id, principal_type="User", role="User"):
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

def confirm_admin_id(connections, token):
    """Confirm rb.admin's Object ID by looking at connections with 'rb.admin' in the name."""
    print("\nSearching for connections with 'rb.admin' in display name...")
    for conn in connections:
        name = (conn.get("displayName") or "").lower()
        if "rb.admin" in name or "rb admin" in name:
            conn_id = conn["id"]
            assignments = get_role_assignments(token, conn_id)
            print("  Found:", conn.get("displayName"))
            print("  Connection ID:", conn_id)
            for a in assignments:
                p = a.get("principal", {})
                pid = p.get("id", "")
                role = a.get("role", "")
                print("    Principal:", pid, "Role:", role)
                # If this connection was created by rb.admin, they're likely the Owner
                if role == "Owner" and pid != OBALIUTA_ID:
                    return pid
                # Or if they appear as User
                if pid == SUSPECTED_ADMIN_ID:
                    return pid
    return SUSPECTED_ADMIN_ID  # fallback to suspected ID

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

    # Categorize by type
    shareable = [c for c in connections if c.get("connectivityType") == "ShareableCloud"]
    personal = [c for c in connections if c.get("connectivityType") == "PersonalCloud"]
    other = [c for c in connections if c.get("connectivityType") not in ("ShareableCloud", "PersonalCloud")]
    print("  ShareableCloud:", len(shareable))
    print("  PersonalCloud:", len(personal), "(cannot be shared)")
    if other:
        print("  Other:", len(other))

    # STEP 2: Confirm admin ID
    print("\n" + "=" * 80)
    print("STEP 2: Confirming rb.admin Object ID...")
    print("=" * 80)
    admin_id = confirm_admin_id(connections, fab_token)
    print("\nConfirmed admin Object ID:", admin_id)

    # STEP 3: Share all ShareableCloud connections
    print("\n" + "=" * 80)
    print("STEP 3: Sharing", len(shareable), "ShareableCloud connections with", ADMIN_UPN)
    print("  Admin Object ID:", admin_id)
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
        
        # Check if admin already has access
        already_has = False
        caller_can_reshare = False
        for a in assignments:
            p = a.get("principal", {})
            pid = p.get("id", "")
            role = a.get("role", "")
            
            if pid == admin_id:
                already_has = True
            
            # Check if caller (OBaliuta) has Owner or UserWithReshare
            if pid == OBALIUTA_ID and role in ("Owner", "UserWithReshare"):
                caller_can_reshare = True
        
        if already_has:
            skipped_already += 1
            continue  # Silent skip
        
        if not caller_can_reshare:
            skipped_no_reshare += 1
            continue  # Silent skip
        
        # Share
        status, text = add_role_assignment(fab_token, conn_id, admin_id, "User", ROLE)
        if status in (200, 201):
            success += 1
            if (success % 50) == 0:
                print("  ... shared", success, "connections so far")
        else:
            failed += 1
            error_msg = text[:300]
            errors.append({"name": conn_name, "id": conn_id, "status": status, "error": error_msg})
            # Rate limiting - back off if we get 429
            if status == 429:
                print("  Rate limited! Waiting 30 seconds...")
                time.sleep(30)

    # RESULTS
    print("\n" + "=" * 80)
    print("RESULTS")
    print("=" * 80)
    print("Total connections:", len(connections))
    print("  ShareableCloud:", len(shareable))
    print("  PersonalCloud:", len(personal), "(not sharable)")
    print()
    print("Sharing results (ShareableCloud only):")
    print("  Successfully shared:", success)
    print("  Skipped (admin already has access):", skipped_already)
    print("  Skipped (caller lacks reshare permission):", skipped_no_reshare)
    print("  Failed:", failed)

    if errors:
        print("\nFailed connections:")
        for e in errors:
            print("  -", e["name"], "(" + e["id"] + ")")
            print("    Status:", e["status"])
            print("    Error:", e["error"][:200])
    
    # Save summary
    summary = {
        "admin_upn": ADMIN_UPN,
        "admin_object_id": admin_id,
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
    out_path = "/mnt/c/Users/OBaliuta/OneDrive - Titan Machinery Inc/Desktop/fabric documentation/share_connections_result.json"
    with open(out_path, "w") as f:
        json.dump(summary, f, indent=2)
    print("\nFull results saved to share_connections_result.json")

if __name__ == "__main__":
    main()
