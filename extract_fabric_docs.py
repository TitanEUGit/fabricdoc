import os
import sys
import json
import time
import requests
from pathlib import Path
from msal import PublicClientApplication

# Output directory
OUTPUT_DIR = Path(r"c:\Users\OBaliuta\OneDrive - Titan Machinery Inc\Desktop\fabric documentation")
WORKSPACES_DIR = OUTPUT_DIR / "Workspaces"
WORKSPACES_DIR.mkdir(parents=True, exist_ok=True)

# Titan Machinery Tenant and Power BI First-Party Client ID
TENANT_ID = "b99e8d15-ec60-4e7d-9387-253b0b6c7136"
CLIENT_ID = "ea73c801-9257-459d-854c-223686b2450c" # Power BI Desktop App ID (Conditional Access Compliant)

# Excluded Workspace Name
EXCLUDED_WORKSPACE_NAME = "BI_TMEU_Testspace"

def get_tokens():
    """Acquires tokens for Fabric and Power BI APIs using MSAL with Titan Machinery tenant."""
    authority = f"https://login.microsoftonline.com/{TENANT_ID}"
    app = PublicClientApplication(CLIENT_ID, authority=authority)

    accounts = app.get_accounts()
    token_pbi = None
    token_fabric = None

    if accounts:
        print("Found cached MSAL account. Acquiring tokens silently...")
        res_pbi = app.acquire_token_silent(["https://analysis.windows.net/powerbi/api/.default"], account=accounts[0])
        res_fab = app.acquire_token_silent(["https://api.fabric.microsoft.com/.default"], account=accounts[0])
        if res_pbi and "access_token" in res_pbi:
            token_pbi = res_pbi["access_token"]
        if res_fab and "access_token" in res_fab:
            token_fabric = res_fab["access_token"]

    if not token_pbi or not token_fabric:
        print("Acquiring tokens interactively via browser...")
        res_pbi = app.acquire_token_interactive(
            scopes=["https://analysis.windows.net/powerbi/api/.default"],
            port=8080
        )
        if "access_token" in res_pbi:
            token_pbi = res_pbi["access_token"]
            
        res_fab = app.acquire_token_interactive(
            scopes=["https://api.fabric.microsoft.com/.default"],
            port=8081
        )
        if "access_token" in res_fab:
            token_fabric = res_fab["access_token"]

    return token_fabric or token_pbi, token_pbi or token_fabric

def make_request(url, token, retries=3):
    if not token:
        return None
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    for attempt in range(retries):
        try:
            resp = requests.get(url, headers=headers, timeout=30)
            if resp.status_code == 200:
                return resp.json()
            elif resp.status_code == 429: # Rate limited
                retry_after = int(resp.headers.get("Retry-After", 5))
                time.sleep(retry_after)
            else:
                print(f"API Error [{resp.status_code}] for {url}: {resp.text[:200]}")
                return None
        except Exception as e:
            print(f"Request exception for {url}: {e}")
            time.sleep(2)
    return None

def sanitize_filename(name):
    invalid_chars = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']
    for char in invalid_chars:
        name = name.replace(char, '_')
    return name.strip()

def extract_all():
    token_fabric, token_pbi = get_tokens()
    if not token_pbi:
        print("ERROR: Failed to acquire Power BI / Fabric access token.")
        sys.exit(1)

    print("Fetching Fabric & Power BI Workspaces...")
    # Power BI Groups API
    pbi_ws_data = make_request("https://api.powerbi.com/v1.0/myorg/groups", token_pbi)
    pbi_groups = pbi_ws_data.get("value", []) if pbi_ws_data else []

    # Fabric Workspaces API
    fabric_ws_data = make_request("https://api.fabric.microsoft.com/v1/workspaces", token_fabric)
    workspaces = fabric_ws_data.get("value", []) if fabric_ws_data else []

    ws_map = {}
    for grp in pbi_groups:
        grp_id = grp.get("id")
        grp_name = grp.get("name", "")
        if grp_name.strip() == EXCLUDED_WORKSPACE_NAME:
            print(f"Skipping excluded workspace: {grp_name}")
            continue
        ws_map[grp_id] = {
            "id": grp_id,
            "name": grp_name,
            "description": grp.get("description", ""),
            "type": "Power BI Workspace",
            "capacityId": grp.get("capacityId", ""),
            "isReadOnly": grp.get("isReadOnly", False),
            "fabric_items": [],
            "pbi_datasets": [],
            "pbi_reports": [],
            "pbi_dashboards": [],
            "pbi_dataflows": []
        }

    for ws in workspaces:
        ws_id = ws.get("id")
        ws_name = ws.get("displayName", "")
        if ws_name.strip() == EXCLUDED_WORKSPACE_NAME:
            continue
        if ws_id in ws_map:
            ws_map[ws_id]["type"] = ws.get("type", "Fabric Workspace")
            ws_map[ws_id]["description"] = ws.get("description", ws_map[ws_id]["description"])
            ws_map[ws_id]["capacityId"] = ws.get("capacityId", ws_map[ws_id]["capacityId"])
        else:
            ws_map[ws_id] = {
                "id": ws_id,
                "name": ws_name,
                "description": ws.get("description", ""),
                "type": ws.get("type", "Fabric Workspace"),
                "capacityId": ws.get("capacityId", ""),
                "isReadOnly": False,
                "fabric_items": [],
                "pbi_datasets": [],
                "pbi_reports": [],
                "pbi_dashboards": [],
                "pbi_dataflows": []
            }

    print(f"\nTotal Workspaces to document (excluding {EXCLUDED_WORKSPACE_NAME}): {len(ws_map)}")

    all_schedules = []
    all_lineage = []

    for ws_id, ws in ws_map.items():
        print(f"\n--- Extracting details for Workspace: {ws['name']} ({ws_id}) ---")
        
        # 1. Native Fabric Items
        items_data = make_request(f"https://api.fabric.microsoft.com/v1/workspaces/{ws_id}/items", token_fabric)
        if items_data and "value" in items_data:
            ws["fabric_items"] = items_data["value"]
            print(f"  Found {len(ws['fabric_items'])} native Fabric items.")

        # 2. Power BI Datasets (Semantic Models)
        datasets_data = make_request(f"https://api.powerbi.com/v1.0/myorg/groups/{ws_id}/datasets", token_pbi)
        if datasets_data and "value" in datasets_data:
            datasets = datasets_data["value"]
            for ds in datasets:
                ds_id = ds.get("id")
                
                # Refresh Schedule
                sched = make_request(f"https://api.powerbi.com/v1.0/myorg/groups/{ws_id}/datasets/{ds_id}/refreshSchedule", token_pbi)
                ds["refreshSchedule"] = sched
                if sched and sched.get("enabled"):
                    all_schedules.append({
                        "workspace": ws['name'],
                        "item_name": ds.get("name"),
                        "item_type": "Semantic Model / Dataset",
                        "days": ", ".join(sched.get("days", [])) if sched.get("days") else "Daily",
                        "times": ", ".join(sched.get("times", [])) if sched.get("times") else "N/A",
                        "timeZone": sched.get("localTimeZoneId", "UTC")
                    })

                # Refresh History
                history = make_request(f"https://api.powerbi.com/v1.0/myorg/groups/{ws_id}/datasets/{ds_id}/refreshes?$top=5", token_pbi)
                ds["refreshHistory"] = history.get("value", []) if history else []

                # Data Sources
                datasources = make_request(f"https://api.powerbi.com/v1.0/myorg/groups/{ws_id}/datasets/{ds_id}/datasources", token_pbi)
                ds["datasources"] = datasources.get("value", []) if datasources else []
                
                for src in ds["datasources"]:
                    all_lineage.append({
                        "workspace": ws['name'],
                        "source": src.get("datasourceType", "Data Source"),
                        "connection": str(src.get("connectionDetails", {})),
                        "target_model": ds.get("name"),
                        "target_type": "Semantic Model"
                    })

            ws["pbi_datasets"] = datasets
            print(f"  Found {len(datasets)} Datasets/Semantic Models.")

        # 3. Power BI Reports
        reports_data = make_request(f"https://api.powerbi.com/v1.0/myorg/groups/{ws_id}/reports", token_pbi)
        if reports_data and "value" in reports_data:
            reports = reports_data["value"]
            ws["pbi_reports"] = reports
            print(f"  Found {len(reports)} Power BI Reports.")
            for rpt in reports:
                all_lineage.append({
                    "workspace": ws['name'],
                    "source": rpt.get("datasetId", "Semantic Model"),
                    "connection": "Dataset Link",
                    "target_model": rpt.get("name"),
                    "target_type": "Power BI Report"
                })

        # 4. Power BI Dataflows
        dataflows_data = make_request(f"https://api.powerbi.com/v1.0/myorg/groups/{ws_id}/dataflows", token_pbi)
        if dataflows_data and "value" in dataflows_data:
            ws["pbi_dataflows"] = dataflows_data["value"]
            print(f"  Found {len(ws['pbi_dataflows'])} Dataflows.")

        # 5. Power BI Dashboards
        dashboards_data = make_request(f"https://api.powerbi.com/v1.0/myorg/groups/{ws_id}/dashboards", token_pbi)
        if dashboards_data and "value" in dashboards_data:
            ws["pbi_dashboards"] = dashboards_data["value"]
            print(f"  Found {len(ws['pbi_dashboards'])} Dashboards.")

    # Generate Markdown documentation files
    generate_documentation(ws_map, all_schedules, all_lineage)

def generate_documentation(ws_map, all_schedules, all_lineage):
    print("\nGenerating Markdown Documentation Files...")
    
    # 1. Workspaces Individual Documentation
    for ws_id, ws in ws_map.items():
        safe_name = sanitize_filename(ws["name"])
        doc_path = WORKSPACES_DIR / f"{safe_name}.md"
        
        content = f"# Workspace Documentation: {ws['name']}\n\n"
        content += f"**Workspace ID**: `{ws['id']}`  \n"
        content += f"**Type**: `{ws['type']}`  \n"
        content += f"**Capacity ID**: `{ws['capacityId'] if ws['capacityId'] else 'Shared / Pro'}`  \n"
        content += f"**Description**: {ws['description'] if ws['description'] else 'No description provided.'}\n\n"
        
        content += "---\n\n## 1. Executive Summary & Newcomer Overview\n"
        content += f"This document contains operational and technical details for the **{ws['name']}** workspace. "
        content += "It is designed to give new team members full visibility into key items, data models, report lineage, and refresh schedules.\n\n"
        
        # Fabric Items Table
        content += "## 2. Native Fabric Items Inventory\n\n"
        if ws["fabric_items"]:
            content += "| Item Name | Item Type | Item ID | Description |\n"
            content += "| :--- | :--- | :--- | :--- |\n"
            for item in ws["fabric_items"]:
                desc = item.get("description", "") or "-"
                content += f"| **{item.get('displayName')}** | `{item.get('type')}` | `{item.get('id')}` | {desc} |\n"
        else:
            content += "*No native Fabric items (Lakehouses, Warehouses, Pipelines, Notebooks) found in this workspace.*\n"
        content += "\n"

        # Semantic Models / Datasets Table
        content += "## 3. Semantic Models (Datasets) & Refresh Schedules\n\n"
        if ws["pbi_datasets"]:
            for ds in ws["pbi_datasets"]:
                content += f"### Semantic Model: {ds.get('name')}\n"
                content += f"- **Dataset ID**: `{ds.get('id')}`\n"
                content += f"- **Target Storage Mode**: `{ds.get('targetStorageMode', 'Import / Default')}`\n"
                content += f"- **Is Refreshable**: `{ds.get('isRefreshable', False)}`\n"
                content += f"- **Configured By**: `{ds.get('configuredBy', 'N/A')}`\n\n"

                sched = ds.get("refreshSchedule")
                if sched:
                    enabled = sched.get("enabled", False)
                    status_str = "ENABLED ✅" if enabled else "DISABLED ❌"
                    days = ", ".join(sched.get("days", [])) if sched.get("days") else "Daily"
                    times = ", ".join(sched.get("times", [])) if sched.get("times") else "N/A"
                    tz = sched.get("localTimeZoneId", "UTC")
                    content += f"**Configured Refresh Schedule** ({status_str}):\n"
                    content += f"- **Frequency**: {days}\n"
                    content += f"- **Scheduled Times**: `{times}` ({tz})\n\n"
                else:
                    content += "*No refresh schedule configured.*\n\n"

                # Data Sources
                datasources = ds.get("datasources", [])
                if datasources:
                    content += "**Connected Data Sources (Lineage)**:\n"
                    for src in datasources:
                        content += f"- Type: `{src.get('datasourceType')}` | Connection: `{src.get('connectionDetails')}`\n"
                    content += "\n"

                # Recent Refresh Execution History
                history = ds.get("refreshHistory", [])
                if history:
                    content += "**Recent Refresh History (Last 5 Runs)**:\n"
                    content += "| Start Time | End Time | Status | Refresh Type | Service Exception |\n"
                    content += "| :--- | :--- | :--- | :--- | :--- |\n"
                    for run in history:
                        st = run.get("startTime", "")[:19].replace("T", " ")
                        et = run.get("endTime", "")[:19].replace("T", " ") if run.get("endTime") else "-"
                        status = run.get("status", "Unknown")
                        rtype = run.get("refreshType", "ViaApi/Scheduled")
                        err = run.get("serviceExceptionJson", "") or "-"
                        if len(err) > 50:
                            err = err[:47] + "..."
                        content += f"| {st} | {et} | `{status}` | `{rtype}` | {err} |\n"
                    content += "\n"
        else:
            content += "*No semantic models/datasets found in this workspace.*\n\n"

        # Reports Table
        content += "## 4. Power BI Reports Inventory\n\n"
        if ws["pbi_reports"]:
            content += "| Report Name | Report ID | Dataset ID | Web URL |\n"
            content += "| :--- | :--- | :--- | :--- |\n"
            for rpt in ws["pbi_reports"]:
                url = rpt.get("webUrl", "#")
                content += f"| **{rpt.get('name')}** | `{rpt.get('id')}` | `{rpt.get('datasetId')}` | [Open Report]({url}) |\n"
        else:
            content += "*No Power BI reports found in this workspace.*\n"
        content += "\n"

        # Dataflows & Dashboards
        content += "## 5. Dataflows & Dashboards\n\n"
        if ws["pbi_dataflows"]:
            content += "**Dataflows**:\n"
            for df in ws["pbi_dataflows"]:
                content += f"- **{df.get('name')}** (ID: `{df.get('objectId')}`)\n"
        if ws["pbi_dashboards"]:
            content += "**Dashboards**:\n"
            for db in ws["pbi_dashboards"]:
                content += f"- **{db.get('displayName')}** (ID: `{db.get('id')}`)\n"
        if not ws["pbi_dataflows"] and not ws["pbi_dashboards"]:
            content += "*No dataflows or dashboards in this workspace.*\n"

        content += "\n---\n\n## 6. Newcomer Operational Runbook & Notes\n"
        content += f"- **Primary Contact / Owner**: Refer to workspace access settings in Power BI portal.\n"
        content += f"- **Troubleshooting**: If a refresh fails in `{ws['name']}`, inspect the failure log under section 3 above and check upstream data gateway connectivity.\n"

        with open(doc_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Wrote workspace doc: {doc_path}")

    # 2. Master Index File (00_Master_Index.md)
    idx_path = OUTPUT_DIR / "00_Master_Index.md"
    idx_content = "# Microsoft Fabric & Power BI Master Workspace Index\n\n"
    idx_content += "Welcome to the Titan Machinery Fabric & Power BI Documentation Hub. "
    idx_content += "This documentation suite provides a complete, structured overview of all Fabric items, Power BI reports, data lineage, and refresh schedules.\n\n"
    idx_content += "> [!NOTE]\n> Workspace `BI_TMEU_Testspace` is strictly excluded from this documentation.\n\n"
    
    idx_content += "## Document Navigation Hub\n\n"
    idx_content += "- 📋 [01. Workspaces Catalog](01_Workspaces_Catalog.md) - Summary inventory of all workspaces and capacity metrics.\n"
    idx_content += "- ⏰ [02. Refresh Schedules & Operations](02_Refresh_Schedules_&_Operations.md) - Master timetable of all automated refreshes.\n"
    idx_content += "- 🔗 [03. Data Lineage & Dependencies](03_Data_Lineage_&_Dependencies.md) - Visual and tabular lineage maps.\n"
    idx_content += "- 🚀 [04. Newcomer Transition Guide](04_Newcomer_Transition_Guide.md) - Onboarding guide and operational workflows.\n\n"

    idx_content += "## Workspaces Directory Overview\n\n"
    idx_content += "| Workspace Name | Type | Fabric Items | Datasets | Reports | Detailed Doc |\n"
    idx_content += "| :--- | :--- | :--- | :--- | :--- | :--- |\n"
    for ws_id, ws in ws_map.items():
        safe_name = sanitize_filename(ws["name"])
        idx_content += f"| **{ws['name']}** | `{ws['type']}` | {len(ws['fabric_items'])} | {len(ws['pbi_datasets'])} | {len(ws['pbi_reports'])} | [View Documentation](Workspaces/{safe_name}.md) |\n"

    with open(idx_path, "w", encoding="utf-8") as f:
        f.write(idx_content)
    print(f"Wrote Master Index: {idx_path}")

    # 3. Workspaces Catalog (01_Workspaces_Catalog.md)
    cat_path = OUTPUT_DIR / "01_Workspaces_Catalog.md"
    cat_content = "# Workspaces & Capacity Catalog\n\n"
    cat_content += "This catalog details all active workspaces across the organization.\n\n"
    cat_content += "| Workspace Name | Workspace ID | Type | Capacity ID | Fabric Items | Reports |\n"
    cat_content += "| :--- | :--- | :--- | :--- | :--- | :--- |\n"
    for ws_id, ws in ws_map.items():
        cap = ws["capacityId"] if ws["capacityId"] else "Shared / Pro"
        cat_content += f"| **{ws['name']}** | `{ws['id']}` | `{ws['type']}` | `{cap}` | {len(ws['fabric_items'])} | {len(ws['pbi_reports'])} |\n"

    with open(cat_path, "w", encoding="utf-8") as f:
        f.write(cat_content)
    print(f"Wrote Workspaces Catalog: {cat_path}")

    # 4. Refresh Schedules (02_Refresh_Schedules_&_Operations.md)
    sched_path = OUTPUT_DIR / "02_Refresh_Schedules_&_Operations.md"
    sched_content = "# Master Refresh Schedules & Operations Matrix\n\n"
    sched_content += "This master schedule lists all configured automated dataset and pipeline refreshes across all workspaces.\n\n"
    sched_content += "| Workspace | Item Name | Item Type | Days | Scheduled Times | Timezone |\n"
    sched_content += "| :--- | :--- | :--- | :--- | :--- | :--- |\n"
    if all_schedules:
        for s in all_schedules:
            sched_content += f"| **{s['workspace']}** | {s['item_name']} | `{s['item_type']}` | {s['days']} | `{s['times']}` | {s['timeZone']} |\n"
    else:
        sched_content += "| *No scheduled refreshes configured across workspaces.* | | | | | |\n"

    with open(sched_path, "w", encoding="utf-8") as f:
        f.write(sched_content)
    print(f"Wrote Refresh Schedules: {sched_path}")

    # 5. Data Lineage (03_Data_Lineage_&_Dependencies.md)
    lin_path = OUTPUT_DIR / "03_Data_Lineage_&_Dependencies.md"
    lin_content = "# Data Lineage & Dependencies Map\n\n"
    lin_content += "This document tracks how data flows from source systems into semantic models and downstream reports.\n\n"
    lin_content += "## Lineage Overview Diagram (Mermaid)\n\n"
    lin_content += "```mermaid\ngraph LR\n"
    lin_content += "    subgraph Upstream Data Sources\n"
    lin_content += "        SQL[SQL Server / Azure SQL]\n"
    lin_content += "        DL[Data Lake / OneLake]\n"
    lin_content += "        API[Web APIs / External]\n"
    lin_content += "    end\n"
    lin_content += "    subgraph Fabric & Power BI\n"
    lin_content += "        LH[Lakehouses / Warehouses]\n"
    lin_content += "        SM[Semantic Models / Datasets]\n"
    lin_content += "        RPT[Power BI Reports]\n"
    lin_content += "    end\n"
    lin_content += "    SQL --> LH\n    DL --> LH\n    LH --> SM\n    SM --> RPT\n"
    lin_content += "```\n\n"
    lin_content += "## Complete Lineage Connections Table\n\n"
    lin_content += "| Workspace | Upstream Source | Connection | Target Item | Target Type |\n"
    lin_content += "| :--- | :--- | :--- | :--- | :--- |\n"
    if all_lineage:
        for l in all_lineage:
            lin_content += f"| **{l['workspace']}** | `{l['source']}` | `{l['connection'][:30]}` | **{l['target_model']}** | `{l['target_type']}` |\n"
    else:
        lin_content += "| *No explicit data source connections extracted.* | | | | |\n"

    with open(lin_path, "w", encoding="utf-8") as f:
        f.write(lin_content)
    print(f"Wrote Lineage Map: {lin_path}")

    # 6. Newcomer Guide (04_Newcomer_Transition_Guide.md)
    guide_path = OUTPUT_DIR / "04_Newcomer_Transition_Guide.md"
    guide_content = "# Newcomer Transition & Onboarding Guide\n\n"
    guide_content += "Welcome! This guide is designed to help a newcomer quickly get up to speed with Titan Machinery's Fabric & Power BI environment.\n\n"
    guide_content += "## 1. Key Operational Concepts\n"
    guide_content += "- **Fabric Workspaces**: Logical containers holding Lakehouses, Data Pipelines, Notebooks, Semantic Models, and Power BI Reports.\n"
    guide_content += "- **OneLake & Direct Lake Mode**: Datasets configured with Direct Lake mode read directly from Delta tables in OneLake without needing import refresh steps.\n"
    guide_content += "- **Import Mode Datasets**: Refreshed on a schedule (documented in `02_Refresh_Schedules_&_Operations.md`).\n\n"
    guide_content += "## 2. Common Maintenance Workflows\n"
    guide_content += "### Monitoring Daily Refreshes\n"
    guide_content += "1. Open `02_Refresh_Schedules_&_Operations.md` to see expected daily refresh windows.\n"
    guide_content += "2. In the Power BI Service, navigate to the specific Workspace.\n"
    guide_content += "3. Check dataset Refresh History for any `Failed` status.\n\n"
    guide_content += "### Handling Refresh Failures\n"
    guide_content += "1. Inspect the error payload under the individual workspace documentation file (`Workspaces/<Workspace_Name>.md`).\n"
    guide_content += "2. Check On-Premises Data Gateway status if the source is on-prem SQL/Oracle/Excel.\n"
    guide_content += "3. Re-run dataset refresh manually via the Power BI portal or REST API.\n\n"

    with open(guide_path, "w", encoding="utf-8") as f:
        f.write(guide_content)
    print(f"Wrote Newcomer Guide: {guide_path}")

    print("\n✅ Documentation Extraction & Generation Complete!")

if __name__ == "__main__":
    extract_all()
