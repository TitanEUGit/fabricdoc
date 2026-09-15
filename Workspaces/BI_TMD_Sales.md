# Workspace Documentation: BI_TMD_Sales

**Workspace ID**: `b693209b-438d-440b-bb1e-d12da52820a2`  
**Type**: `Fabric / PowerBI Workspace`  
**Capacity ID**: `70650ed2-f7a2-46df-96e8-8089f25db80e`  
**Description**: No description provided.

---

## 1. Executive Summary & Newcomer Overview
This document contains operational and technical details for the **BI_TMD_Sales** workspace. It is designed to give new team members full visibility into key items, data models, report lineage, and refresh schedules.

## 2. Native Fabric Items Inventory

| Item Name | Item Type | Item ID | Description |
| :--- | :--- | :--- | :--- |
| **TMD WG Sales** | `Report` | `3d6a6c39-5124-4b35-9960-75eb93a41832` | - |
| **Usage Metrics Report** | `Report` | `4ce17e8e-45b4-472d-9ce2-0ed29b4701c2` | - |
| **TMD WG Sales** | `SemanticModel` | `637988c7-075b-4caf-9a4e-bf71df272f9f` | - |
| **Usage Metrics Report** | `SemanticModel` | `c775c54f-65a4-4235-85b6-2aa97ba2b57a` | - |

## 3. Semantic Models (Datasets) & Refresh Schedules

### Semantic Model: TMD WG Sales
- **Dataset ID**: `637988c7-075b-4caf-9a4e-bf71df272f9f`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `05:00` (FLE Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `ODBC` | Connection: `{'connectionString': 'dsn=timeline - tmd'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/int_orderbook', 'database': 'tmeu order book'}`
- Type: `Extension` | Connection: `{'path': 'PowerPlatformDataflows', 'kind': 'PowerPlatformDataflows'}`
- Type: `SharePointList` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/collaboration/'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2026-09-15 02:00:12 | 2026-09-15 02:12:21 | `Completed` | `Scheduled` | - |
| 2026-09-14 02:00:11 | 2026-09-14 02:10:39 | `Completed` | `Scheduled` | - |
| 2026-09-13 02:01:12 | 2026-09-13 02:12:25 | `Completed` | `Scheduled` | - |
| 2026-09-12 02:00:09 | 2026-09-12 02:09:06 | `Completed` | `Scheduled` | - |
| 2026-09-11 02:01:14 | 2026-09-11 02:11:38 | `Completed` | `Scheduled` | - |

### Semantic Model: Usage Metrics Report
- **Dataset ID**: `c775c54f-65a4-4235-85b6-2aa97ba2b57a`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `17:17` (UTC)

**Connected Data Sources (Lineage)**:
- Type: `Extension` | Connection: `{'path': 'UsageMetricsDataConnector', 'kind': 'UsageMetricsDataConnector'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2025-07-21 17:18:09 | 2025-07-21 17:18:09 | `Disabled` | `Scheduled` | - |
| 2025-07-20 17:17:03 | 2025-07-20 17:18:03 | `Completed` | `Scheduled` | - |
| 2025-07-19 17:18:06 | 2025-07-19 17:18:24 | `Completed` | `Scheduled` | - |
| 2025-07-18 17:17:07 | 2025-07-18 17:18:28 | `Completed` | `Scheduled` | - |
| 2025-07-17 17:17:06 | 2025-07-17 17:18:22 | `Completed` | `Scheduled` | - |

## 4. Power BI Reports Inventory

| Report Name | Report ID | Dataset ID | Web URL |
| :--- | :--- | :--- | :--- |
| **TMD WG Sales** | `3d6a6c39-5124-4b35-9960-75eb93a41832` | `637988c7-075b-4caf-9a4e-bf71df272f9f` | [Open Report](https://app.powerbi.com/groups/b693209b-438d-440b-bb1e-d12da52820a2/reports/3d6a6c39-5124-4b35-9960-75eb93a41832) |
| **Usage Metrics Report** | `4ce17e8e-45b4-472d-9ce2-0ed29b4701c2` | `c775c54f-65a4-4235-85b6-2aa97ba2b57a` | [Open Report](https://app.powerbi.com/groups/b693209b-438d-440b-bb1e-d12da52820a2/reports/4ce17e8e-45b4-472d-9ce2-0ed29b4701c2) |

## 5. Dataflows & Dashboards

*No dataflows or dashboards in this workspace.*

---

## 6. Newcomer Operational Runbook & Notes
- **Primary Contact / Owner**: Refer to workspace access settings in Power BI portal.
- **Troubleshooting**: If a refresh fails in `BI_TMD_Sales`, inspect the failure log under section 3 above and check upstream data gateway connectivity.
