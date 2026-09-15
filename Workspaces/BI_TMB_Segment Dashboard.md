# Workspace Documentation: BI_TMB_Segment Dashboard

**Workspace ID**: `f182fb94-d92f-4073-895a-2ea6aa935182`  
**Type**: `Fabric / PowerBI Workspace`  
**Capacity ID**: `70650ed2-f7a2-46df-96e8-8089f25db80e`  
**Description**: No description provided.

---

## 1. Executive Summary & Newcomer Overview
This document contains operational and technical details for the **BI_TMB_Segment Dashboard** workspace. It is designed to give new team members full visibility into key items, data models, report lineage, and refresh schedules.

## 2. Native Fabric Items Inventory

| Item Name | Item Type | Item ID | Description |
| :--- | :--- | :--- | :--- |
| **TMB Segment Dashboard** | `Report` | `392f4154-863c-4118-9ef3-6336dc3c98ed` | - |
| **Report Usage Metrics Report** | `Report` | `0dc473ef-1e11-4b6a-b0a2-0223a992d1ea` | - |
| **Usage Metrics Report** | `Report` | `9cce3c20-c3ba-4b92-89ec-5a1993b08c09` | - |
| **TMB Segment Dashboard** | `SemanticModel` | `cca1fadf-d996-4c78-82e6-8c2872aadbc6` | - |
| **Report Usage Metrics Model** | `SemanticModel` | `6af76276-4eb9-4a73-941a-b97a1055fe7c` | - |
| **Usage Metrics Report** | `SemanticModel` | `721d2176-5398-4563-a7e1-b2d0ff38dfb4` | - |

## 3. Semantic Models (Datasets) & Refresh Schedules

### Semantic Model: TMB Segment Dashboard
- **Dataset ID**: `cca1fadf-d996-4c78-82e6-8c2872aadbc6`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Monday
- **Scheduled Times**: `23:00` (GTB Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmb_opspackage', 'database': 'tmb ops package'}`
- Type: `Web` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/Collaboration/Shared%20Documents/INT_POWERBI_HELPER/TMB/serv_rec_rate/gross_sal_serv.xlsx'}`
- Type: `Web` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/Collaboration/Shared%20Documents/INT_POWERBI_HELPER/TMB/TIV/TIV%20inputs.xlsx'}`
- Type: `Web` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/Collaboration/Shared%20Documents/INT_POWERBI_HELPER/TMB/headcount_division/headcount_by_division.xlsx'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2025-08-18 20:02:13 | 2025-08-18 20:02:13 | `Disabled` | `Scheduled` | - |
| 2025-08-11 20:03:11 | 2025-08-11 20:11:57 | `Completed` | `Scheduled` | - |
| 2025-08-04 20:01:15 | 2025-08-04 20:04:38 | `Completed` | `Scheduled` | - |
| 2025-07-28 20:01:15 | 2025-07-28 20:09:01 | `Completed` | `Scheduled` | - |
| 2025-07-21 20:01:14 | 2025-07-21 20:09:35 | `Completed` | `Scheduled` | - |

### Semantic Model: Report Usage Metrics Model
- **Dataset ID**: `6af76276-4eb9-4a73-941a-b97a1055fe7c`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `False`
- **Configured By**: `OBaliuta@titanmachinery.ua`

*No refresh schedule configured.*

### Semantic Model: Usage Metrics Report
- **Dataset ID**: `721d2176-5398-4563-a7e1-b2d0ff38dfb4`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `07:35` (UTC)

**Connected Data Sources (Lineage)**:
- Type: `Extension` | Connection: `{'path': 'UsageMetricsDataConnector', 'kind': 'UsageMetricsDataConnector'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2024-05-25 07:35:06 | 2024-05-25 07:35:06 | `Disabled` | `Scheduled` | - |
| 2024-05-24 07:35:06 | 2024-05-24 07:44:10 | `Completed` | `Scheduled` | - |
| 2024-05-23 07:35:01 | 2024-05-23 07:44:10 | `Completed` | `Scheduled` | - |
| 2024-05-22 07:35:00 | 2024-05-22 07:43:48 | `Completed` | `Scheduled` | - |
| 2024-05-21 07:35:05 | 2024-05-21 07:43:58 | `Completed` | `Scheduled` | - |

## 4. Power BI Reports Inventory

| Report Name | Report ID | Dataset ID | Web URL |
| :--- | :--- | :--- | :--- |
| **TMB Segment Dashboard** | `392f4154-863c-4118-9ef3-6336dc3c98ed` | `cca1fadf-d996-4c78-82e6-8c2872aadbc6` | [Open Report](https://app.powerbi.com/groups/f182fb94-d92f-4073-895a-2ea6aa935182/reports/392f4154-863c-4118-9ef3-6336dc3c98ed) |
| **Report Usage Metrics Report** | `0dc473ef-1e11-4b6a-b0a2-0223a992d1ea` | `6af76276-4eb9-4a73-941a-b97a1055fe7c` | [Open Report](https://app.powerbi.com/groups/f182fb94-d92f-4073-895a-2ea6aa935182/reports/0dc473ef-1e11-4b6a-b0a2-0223a992d1ea) |
| **Usage Metrics Report** | `9cce3c20-c3ba-4b92-89ec-5a1993b08c09` | `721d2176-5398-4563-a7e1-b2d0ff38dfb4` | [Open Report](https://app.powerbi.com/groups/f182fb94-d92f-4073-895a-2ea6aa935182/reports/9cce3c20-c3ba-4b92-89ec-5a1993b08c09) |

## 5. Dataflows & Dashboards

*No dataflows or dashboards in this workspace.*

---

## 6. Newcomer Operational Runbook & Notes
- **Primary Contact / Owner**: Refer to workspace access settings in Power BI portal.
- **Troubleshooting**: If a refresh fails in `BI_TMB_Segment Dashboard`, inspect the failure log under section 3 above and check upstream data gateway connectivity.
