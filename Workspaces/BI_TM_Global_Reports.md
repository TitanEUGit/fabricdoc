# Workspace Documentation: BI_TM_Global_Reports

**Workspace ID**: `5c528200-a3b4-491d-9af7-f3cefe028128`  
**Type**: `Fabric / PowerBI Workspace`  
**Capacity ID**: `70650ed2-f7a2-46df-96e8-8089f25db80e`  
**Description**: No description provided.

---

## 1. Executive Summary & Newcomer Overview
This document contains operational and technical details for the **BI_TM_Global_Reports** workspace. It is designed to give new team members full visibility into key items, data models, report lineage, and refresh schedules.

## 2. Native Fabric Items Inventory

| Item Name | Item Type | Item ID | Description |
| :--- | :--- | :--- | :--- |
| **New Equipment - Sales by Top Manufacturers** | `Report` | `28015425-eff1-4ca3-b6b5-e68d4a4aa27d` | - |
| **Usage Metrics Report** | `Report` | `f7cce3c8-44b8-46fe-b858-6599fec673a9` | - |
| **New Equipment - Sales by Top Manufacturers** | `SemanticModel` | `367e9a3f-c9d5-4b6f-82ee-56dfd066bd89` | - |
| **Usage Metrics Report** | `SemanticModel` | `1dce8a70-2dd0-4eb8-9e64-2cd85b938035` | - |

## 3. Semantic Models (Datasets) & Refresh Schedules

### Semantic Model: New Equipment - Sales by Top Manufacturers
- **Dataset ID**: `367e9a3f-c9d5-4b6f-82ee-56dfd066bd89`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (DISABLED ❌):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `N/A` (Romance Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `Web` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/Collaboration/Shared%20Documents/INT_POWERBI_HELPER/Global/Sales_Equipment_New/US%20Manufacturer%20Data%20Calendar%20Year.xlsx'}`
- Type: `Extension` | Connection: `{'path': 'PowerPlatformDataflows', 'kind': 'PowerPlatformDataflows'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmd_sales', 'database': 'tmd wg sales'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmb_opspackage', 'database': 'tmb ops package'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmr_opspackage', 'database': 'tmr ops package'}`
- Type: `Web` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/Collaboration/Shared%20Documents/INT_POWERBI_HELPER/Global/Sales_Equipment_New/Australia%20Wholegoods%20Sales%20data.xlsx'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2024-05-03 08:40:39 | 2024-05-03 08:40:46 | `Completed` | `OnDemand` | - |
| 2024-04-24 16:09:16 | 2024-04-24 16:09:33 | `Completed` | `OnDemand` | - |
| 2024-04-24 13:29:46 | 2024-04-24 13:29:58 | `Completed` | `OnDemand` | - |
| 2024-04-24 06:19:16 | 2024-04-24 06:19:32 | `Completed` | `OnDemand` | - |
| 2024-02-19 15:03:42 | 2024-02-19 15:04:03 | `Completed` | `OnDemand` | - |

### Semantic Model: Usage Metrics Report
- **Dataset ID**: `1dce8a70-2dd0-4eb8-9e64-2cd85b938035`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `01:03` (UTC)

**Connected Data Sources (Lineage)**:
- Type: `Extension` | Connection: `{'path': 'UsageMetricsDataConnector', 'kind': 'UsageMetricsDataConnector'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2025-07-21 01:03:00 | 2025-07-21 01:03:00 | `Disabled` | `Scheduled` | - |
| 2025-07-20 01:03:01 | 2025-07-20 01:17:35 | `Completed` | `Scheduled` | - |
| 2025-07-19 01:03:01 | 2025-07-19 01:17:15 | `Completed` | `Scheduled` | - |
| 2025-07-18 01:03:03 | 2025-07-18 01:17:42 | `Completed` | `Scheduled` | - |
| 2025-07-17 01:03:01 | 2025-07-17 01:17:31 | `Completed` | `Scheduled` | - |

## 4. Power BI Reports Inventory

| Report Name | Report ID | Dataset ID | Web URL |
| :--- | :--- | :--- | :--- |
| **New Equipment - Sales by Top Manufacturers** | `28015425-eff1-4ca3-b6b5-e68d4a4aa27d` | `367e9a3f-c9d5-4b6f-82ee-56dfd066bd89` | [Open Report](https://app.powerbi.com/groups/5c528200-a3b4-491d-9af7-f3cefe028128/reports/28015425-eff1-4ca3-b6b5-e68d4a4aa27d) |
| **Usage Metrics Report** | `f7cce3c8-44b8-46fe-b858-6599fec673a9` | `1dce8a70-2dd0-4eb8-9e64-2cd85b938035` | [Open Report](https://app.powerbi.com/groups/5c528200-a3b4-491d-9af7-f3cefe028128/reports/f7cce3c8-44b8-46fe-b858-6599fec673a9) |

## 5. Dataflows & Dashboards

*No dataflows or dashboards in this workspace.*

---

## 6. Newcomer Operational Runbook & Notes
- **Primary Contact / Owner**: Refer to workspace access settings in Power BI portal.
- **Troubleshooting**: If a refresh fails in `BI_TM_Global_Reports`, inspect the failure log under section 3 above and check upstream data gateway connectivity.
