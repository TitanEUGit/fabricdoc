# Workspace Documentation: BI_TMU_Segment Dashboard

**Workspace ID**: `c254f0bb-8e00-4ef8-a56f-6643eb9f08ec`  
**Type**: `Fabric / PowerBI Workspace`  
**Capacity ID**: `70650ed2-f7a2-46df-96e8-8089f25db80e`  
**Description**: No description provided.

---

## 1. Executive Summary & Newcomer Overview

> [!WARNING]
> **Legacy Workspace (Pending Deletion Review)**
> This workspace contains legacy reports built in 2024. Their ongoing usage hasn't been proven. TMA Management Team should be involved in evaluating this priority upon request, as they were the initial requesters. Clarify the necessity of these reports and decommission/delete them if confirmed as unused.

This document contains operational and technical details for the **BI_TMU_Segment Dashboard** workspace. It is designed to give new team members full visibility into key items, data models, report lineage, and refresh schedules.

## 2. Native Fabric Items Inventory

| Item Name | Item Type | Item ID | Description |
| :--- | :--- | :--- | :--- |
| **TMU Segment Dashboard** | `Report` | `99526aae-a7c7-461d-9615-5f0cba761d1c` | - |
| **Report Usage Metrics Report** | `Report` | `7b518733-6f3d-4646-940b-ab17f3d164bb` | - |
| **Usage Metrics Report** | `Report` | `6c1d00ea-1e57-4083-8da0-82a6c5579fa8` | - |
| **TMU Segment Dashboard** | `SemanticModel` | `7fd02f96-d861-4b1b-9d9c-bb6b553b5717` | - |
| **Report Usage Metrics Model** | `SemanticModel` | `ff311e11-0fdb-49cd-ac88-5c0d7c25d0d4` | - |
| **Usage Metrics Report** | `SemanticModel` | `c81b876d-8f1e-46ab-a607-f270ad328d6d` | - |

## 3. Semantic Models (Datasets) & Refresh Schedules

### Semantic Model: TMU Segment Dashboard
- **Dataset ID**: `7fd02f96-d861-4b1b-9d9c-bb6b553b5717`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (DISABLED ❌):
- **Frequency**: Monday
- **Scheduled Times**: `23:00` (GTB Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmu_opspackage_reports', 'database': 'p&l tmu'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmu_opspackage_reports', 'database': 'service kpi'}`
- Type: `Web` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/Collaboration/Shared%20Documents/INT_POWERBI_HELPER/TMU/TIV/TIV%20inputs.xlsx'}`
- Type: `Web` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/Collaboration/Shared%20Documents/INT_POWERBI_HELPER/TMU/headcount_division/headcount_by_division.xlsx'}`
- Type: `Web` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/Collaboration/Shared%20Documents/INT_POWERBI_HELPER/TMU/serv_rec_rate/gross_sal_serv.xlsx'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmu_crm', 'database': 'tmu crm'}`


### Semantic Model: Report Usage Metrics Model
- **Dataset ID**: `ff311e11-0fdb-49cd-ac88-5c0d7c25d0d4`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `False`
- **Configured By**: `OBaliuta@titanmachinery.ua`

*No refresh schedule configured.*

### Semantic Model: Usage Metrics Report
- **Dataset ID**: `c81b876d-8f1e-46ab-a607-f270ad328d6d`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `03:09` (UTC)

**Connected Data Sources (Lineage)**:
- Type: `Extension` | Connection: `{'path': 'UsageMetricsDataConnector', 'kind': 'UsageMetricsDataConnector'}`


## 4. Power BI Reports Inventory

| Report Name | Report ID | Dataset ID | Web URL |
| :--- | :--- | :--- | :--- |
| **TMU Segment Dashboard** | `99526aae-a7c7-461d-9615-5f0cba761d1c` | `7fd02f96-d861-4b1b-9d9c-bb6b553b5717` | [Open Report](https://app.powerbi.com/groups/c254f0bb-8e00-4ef8-a56f-6643eb9f08ec/reports/99526aae-a7c7-461d-9615-5f0cba761d1c) |
| **Report Usage Metrics Report** | `7b518733-6f3d-4646-940b-ab17f3d164bb` | `ff311e11-0fdb-49cd-ac88-5c0d7c25d0d4` | [Open Report](https://app.powerbi.com/groups/c254f0bb-8e00-4ef8-a56f-6643eb9f08ec/reports/7b518733-6f3d-4646-940b-ab17f3d164bb) |
| **Usage Metrics Report** | `6c1d00ea-1e57-4083-8da0-82a6c5579fa8` | `c81b876d-8f1e-46ab-a607-f270ad328d6d` | [Open Report](https://app.powerbi.com/groups/c254f0bb-8e00-4ef8-a56f-6643eb9f08ec/reports/6c1d00ea-1e57-4083-8da0-82a6c5579fa8) |

## 5. Dataflows & Dashboards

*No dataflows or dashboards in this workspace.*

---

## 6. Newcomer Operational Runbook & Notes
- **Primary Contact / Owner**: Refer to workspace access settings in Power BI portal.
- **Troubleshooting**: If a refresh fails in `BI_TMU_Segment Dashboard`, inspect the failure log under section 3 above and check upstream data gateway connectivity.
