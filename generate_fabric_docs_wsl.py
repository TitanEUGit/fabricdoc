import os
import sys
import json
import time
import requests
from pathlib import Path

# Output directory (local Windows Desktop path via WSL2 mount)
OUTPUT_DIR = Path("/mnt/c/Users/OBaliuta/OneDrive - Titan Machinery Inc/Desktop/fabric documentation")
WORKSPACES_DIR = OUTPUT_DIR / "Workspaces"
WORKSPACES_DIR.mkdir(parents=True, exist_ok=True)

# Excluded Workspace Name & ID
EXCLUDED_WORKSPACE_NAME = "BI_TMEU_Testspace"
EXCLUDED_WORKSPACE_ID = "ccc6c233-e839-48c2-9d8d-f01bc502dd0b"

ENV_PATH = "/home/obaliuta/titan/fabricdevws/localdev/.env"

def load_tokens():
    tokens = {}
    if os.path.exists(ENV_PATH):
        with open(ENV_PATH) as f:
            for line in f:
                if "=" in line and not line.startswith("#"):
                    k, v = line.strip().split("=", 1)
                    tokens[k] = v
    fab = tokens.get("FABRIC_ACCESS_TOKEN", "")
    pbi = tokens.get("POWERBI_ACCESS_TOKEN", "")
    return fab or pbi, pbi or fab

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
            elif resp.status_code == 429:
                retry_after = int(resp.headers.get("Retry-After", 5))
                time.sleep(retry_after)
            else:
                return None
        except Exception as e:
            time.sleep(2)
    return None

def sanitize_filename(name):
    invalid_chars = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']
    for char in invalid_chars:
        name = name.replace(char, '_')
    return name.strip()

def extract_and_generate():
    token_fabric, token_pbi = load_tokens()
    if not token_fabric and not token_pbi:
        print("ERROR: Tokens not found in .env")
        sys.exit(1)
        
    print("Fetching Fabric and Power BI Workspaces...")
    
    # Fetch Fabric Workspaces
    fab_data = make_request("https://api.fabric.microsoft.com/v1/workspaces", token_fabric)
    workspaces = fab_data.get("value", []) if fab_data else []
    
    # Fetch Power BI Groups
    pbi_data = make_request("https://api.powerbi.com/v1.0/myorg/groups", token_pbi)
    pbi_groups = pbi_data.get("value", []) if pbi_data else []

    ws_map = {}
    for ws in workspaces:
        ws_id = ws.get("id")
        ws_name = ws.get("displayName", "")
        if ws_name.strip() == EXCLUDED_WORKSPACE_NAME or ws_id == EXCLUDED_WORKSPACE_ID:
            print(f"Skipping excluded workspace: {ws_name}")
            continue
        ws_map[ws_id] = {
            "id": ws_id,
            "name": ws_name,
            "description": ws.get("description", ""),
            "type": ws.get("type", "Fabric Workspace"),
            "capacityId": ws.get("capacityId", ""),
            "fabric_items": [],
            "pbi_datasets": [],
            "pbi_reports": [],
            "pbi_dashboards": [],
            "pbi_dataflows": []
        }

    for grp in pbi_groups:
        grp_id = grp.get("id")
        grp_name = grp.get("name", "")
        if grp_name.strip() == EXCLUDED_WORKSPACE_NAME or grp_id == EXCLUDED_WORKSPACE_ID:
            continue
        if grp_id in ws_map:
            ws_map[grp_id]["type"] = "Fabric / PowerBI Workspace"
        else:
            ws_map[grp_id] = {
                "id": grp_id,
                "name": grp_name,
                "description": grp.get("description", ""),
                "type": "Power BI Workspace",
                "capacityId": grp.get("capacityId", ""),
                "fabric_items": [],
                "pbi_datasets": [],
                "pbi_reports": [],
                "pbi_dashboards": [],
                "pbi_dataflows": []
            }

    print(f"Total Workspaces to document (excluding {EXCLUDED_WORKSPACE_NAME}): {len(ws_map)}")

    all_schedules = []
    all_lineage = []

    count = 0
    total = len(ws_map)
    for ws_id, ws in ws_map.items():
        count += 1
        print(f"[{count}/{total}] Extracting Workspace: {ws['name']} ({ws_id})")
        
        # 1. Native Fabric Items
        items_data = make_request(f"https://api.fabric.microsoft.com/v1/workspaces/{ws_id}/items", token_fabric)
        if items_data and "value" in items_data:
            ws["fabric_items"] = items_data["value"]

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
                    days_list = sched.get("days", [])
                    days_str = ", ".join(days_list) if days_list else "Daily"
                    times_list = sched.get("times", [])
                    times_str = ", ".join(times_list) if times_list else "N/A"
                    all_schedules.append({
                        "workspace": ws['name'],
                        "item_name": ds.get("name", ds_id),
                        "item_type": "Semantic Model / Dataset",
                        "days": days_str,
                        "times": times_str,
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
                        "target_model": ds.get("name", ds_id),
                        "target_type": "Semantic Model"
                    })

            ws["pbi_datasets"] = datasets

        # 3. Power BI Reports
        reports_data = make_request(f"https://api.powerbi.com/v1.0/myorg/groups/{ws_id}/reports", token_pbi)
        if reports_data and "value" in reports_data:
            reports = reports_data["value"]
            ws["pbi_reports"] = reports
            for rpt in reports:
                all_lineage.append({
                    "workspace": ws['name'],
                    "source": rpt.get("datasetId", "Semantic Model"),
                    "connection": "Dataset Link",
                    "target_model": rpt.get("name", rpt.get("id")),
                    "target_type": "Power BI Report"
                })

        # 4. Dataflows & Dashboards
        dataflows_data = make_request(f"https://api.powerbi.com/v1.0/myorg/groups/{ws_id}/dataflows", token_pbi)
        if dataflows_data and "value" in dataflows_data:
            ws["pbi_dataflows"] = dataflows_data["value"]

        dashboards_data = make_request(f"https://api.powerbi.com/v1.0/myorg/groups/{ws_id}/dashboards", token_pbi)
        if dashboards_data and "value" in dashboards_data:
            ws["pbi_dashboards"] = dashboards_data["value"]

    # Generate Markdown documentation
    generate_markdown_docs(ws_map, all_schedules, all_lineage)

def generate_markdown_docs(ws_map, all_schedules, all_lineage):
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
                item_name = item.get('displayName', item.get('itemName', 'Item'))
                content += f"| **{item_name}** | `{item.get('type')}` | `{item.get('id')}` | {desc} |\n"
        else:
            content += "*No native Fabric items (Lakehouses, Warehouses, Pipelines, Notebooks) found in this workspace.*\n"
        content += "\n"

        # Semantic Models / Datasets Table
        content += "## 3. Semantic Models (Datasets) & Refresh Schedules\n\n"
        if ws["pbi_datasets"]:
            for ds in ws["pbi_datasets"]:
                content += f"### Semantic Model: {ds.get('name', ds.get('id'))}\n"
                content += f"- **Dataset ID**: `{ds.get('id')}`\n"
                content += f"- **Target Storage Mode**: `{ds.get('targetStorageMode', 'Import / Default')}`\n"
                content += f"- **Is Refreshable**: `{ds.get('isRefreshable', False)}`\n"
                content += f"- **Configured By**: `{ds.get('configuredBy', 'N/A')}`\n\n"

                sched = ds.get("refreshSchedule")
                if sched:
                    enabled = sched.get("enabled", False)
                    status_str = "ENABLED ✅" if enabled else "DISABLED ❌"
                    days_list = sched.get("days", [])
                    days = ", ".join(days_list) if days_list else "Daily"
                    times_list = sched.get("times", [])
                    times = ", ".join(times_list) if times_list else "N/A"
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

    print("\nSUCCESS: Documentation Extraction and Generation Complete!")
    print(f"Generated documentation saved locally to: {OUTPUT_DIR}")

if __name__ == "__main__":
    extract_and_generate()
