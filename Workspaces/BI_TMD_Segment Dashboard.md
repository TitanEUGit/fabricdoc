# Workspace Documentation: BI_TMD_Segment Dashboard

**Workspace ID**: `95e08ec5-34db-4804-9d3e-43d0b741b8c0`  
**Type**: `Fabric / PowerBI Workspace`  
**Capacity ID**: `70650ed2-f7a2-46df-96e8-8089f25db80e`  
**Description**: No description provided.

---

## 1. Executive Summary & Newcomer Overview
This document contains operational and technical details for the **BI_TMD_Segment Dashboard** workspace. It is designed to give new team members full visibility into key items, data models, report lineage, and refresh schedules.

## 2. Native Fabric Items Inventory

| Item Name | Item Type | Item ID | Description |
| :--- | :--- | :--- | :--- |
| **TMD Segment Dashboard** | `Report` | `ac4f0391-4035-4750-b294-92f8fb11428a` | - |
| **Report Usage Metrics Report** | `Report` | `b8d680cb-5c0c-4152-a5a8-90b80ed93c11` | - |
| **Usage Metrics Report** | `Report` | `ad8e3a04-ac20-45b6-a710-8d606a636774` | - |
| **TMD Segment Dashboard** | `SemanticModel` | `452d098d-ada9-43d1-8940-c7306ee3d3c3` | - |
| **Report Usage Metrics Model** | `SemanticModel` | `53d7aade-856d-44d2-a88a-4f643890371e` | - |
| **Usage Metrics Report** | `SemanticModel` | `a2ee7a50-5598-4fd5-8244-a407ba7adcca` | - |

## 3. Semantic Models (Datasets) & Refresh Schedules

### Semantic Model: TMD Segment Dashboard
- **Dataset ID**: `452d098d-ada9-43d1-8940-c7306ee3d3c3`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Monday
- **Scheduled Times**: `23:00` (FLE Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `Web` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/Collaboration/Shared%20Documents/INT_POWERBI_HELPER/TMD/serv_rec_rate/gross_sal_serv.xlsx'}`
- Type: `Web` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/Collaboration/Shared%20Documents/INT_POWERBI_HELPER/TMD/TIV/TIV%20inputs.xlsx'}`
- Type: `Web` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/Collaboration/Shared%20Documents/INT_POWERBI_HELPER/TMD/headcount_division/headcount_by_division.xlsx'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmd_finance', 'database': 'tmd p&l'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmd_crm', 'database': 'tmd crm'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmd_aftersales', 'database': 'tmd service kpi new'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2025-12-08 21:00:04 | 2025-12-08 21:00:04 | `Disabled` | `Scheduled` | - |
| 2025-12-01 21:00:27 | 2025-12-01 21:03:49 | `Completed` | `Scheduled` | - |
| 2025-11-24 21:00:14 | 2025-11-24 21:02:55 | `Completed` | `Scheduled` | - |
| 2025-11-17 21:01:20 | 2025-11-17 21:04:41 | `Completed` | `Scheduled` | - |
| 2025-11-10 21:01:32 | 2025-11-10 21:09:32 | `Completed` | `Scheduled` | - |

### Semantic Model: Report Usage Metrics Model
- **Dataset ID**: `53d7aade-856d-44d2-a88a-4f643890371e`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `False`
- **Configured By**: `OBaliuta@titanmachinery.ua`

*No refresh schedule configured.*

### Semantic Model: Usage Metrics Report
- **Dataset ID**: `a2ee7a50-5598-4fd5-8244-a407ba7adcca`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `03:30` (UTC)

**Connected Data Sources (Lineage)**:
- Type: `Extension` | Connection: `{'path': 'UsageMetricsDataConnector', 'kind': 'UsageMetricsDataConnector'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2024-05-26 03:30:24 | 2024-05-26 03:30:24 | `Disabled` | `Scheduled` | - |
| 2024-05-25 03:30:38 | 2024-05-25 03:38:51 | `Completed` | `Scheduled` | - |
| 2024-05-24 03:30:33 | 2024-05-24 03:38:20 | `Completed` | `Scheduled` | - |
| 2024-05-23 03:30:35 | 2024-05-23 03:37:26 | `Completed` | `Scheduled` | - |
| 2024-05-22 03:30:12 | 2024-05-22 03:31:20 | `Completed` | `Scheduled` | - |

## 4. Power BI Reports Inventory

| Report Name | Report ID | Dataset ID | Web URL |
| :--- | :--- | :--- | :--- |
| **TMD Segment Dashboard** | `ac4f0391-4035-4750-b294-92f8fb11428a` | `452d098d-ada9-43d1-8940-c7306ee3d3c3` | [Open Report](https://app.powerbi.com/groups/95e08ec5-34db-4804-9d3e-43d0b741b8c0/reports/ac4f0391-4035-4750-b294-92f8fb11428a) |
| **Report Usage Metrics Report** | `b8d680cb-5c0c-4152-a5a8-90b80ed93c11` | `53d7aade-856d-44d2-a88a-4f643890371e` | [Open Report](https://app.powerbi.com/groups/95e08ec5-34db-4804-9d3e-43d0b741b8c0/reports/b8d680cb-5c0c-4152-a5a8-90b80ed93c11) |
| **Usage Metrics Report** | `ad8e3a04-ac20-45b6-a710-8d606a636774` | `a2ee7a50-5598-4fd5-8244-a407ba7adcca` | [Open Report](https://app.powerbi.com/groups/95e08ec5-34db-4804-9d3e-43d0b741b8c0/reports/ad8e3a04-ac20-45b6-a710-8d606a636774) |

## 5. Dataflows & Dashboards

*No dataflows or dashboards in this workspace.*

---

## 6. Newcomer Operational Runbook & Notes
- **Primary Contact / Owner**: Refer to workspace access settings in Power BI portal.
- **Troubleshooting**: If a refresh fails in `BI_TMD_Segment Dashboard`, inspect the failure log under section 3 above and check upstream data gateway connectivity.
