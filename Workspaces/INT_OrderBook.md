# Workspace Documentation: INT_OrderBook

**Workspace ID**: `8bfed8bd-eeac-4f98-a57a-44ca24a055a8`  
**Type**: `Fabric / PowerBI Workspace`  
**Capacity ID**: `70650ed2-f7a2-46df-96e8-8089f25db80e`  
**Description**: No description provided.

---

## 1. Executive Summary & Newcomer Overview
This document contains operational and technical details for the **INT_OrderBook** workspace. It is designed to give new team members full visibility into key items, data models, report lineage, and refresh schedules.

## 2. Native Fabric Items Inventory

| Item Name | Item Type | Item ID | Description |
| :--- | :--- | :--- | :--- |
| **Order Book Dashboard** | `Dashboard` | `6479822d-c36f-4ba7-81b7-52c7644f3877` | - |
| **Report Usage Metrics Report** | `Report` | `2a6b0a74-8fa6-49ea-85a3-62c5598efef0` | - |
| **Dashboard Usage Metrics Report** | `Report` | `4e04efca-e56c-4648-b473-2ab8590cf628` | - |
| **TMEU Order Book** | `Report` | `ab6ad5b1-5c93-46b5-85f6-ebb1af70bc5b` | - |
| **Usage Metrics Report** | `Report` | `37a4689e-e588-4c3e-87b3-ffadfa406679` | - |
| **Report Usage Metrics Model** | `SemanticModel` | `676d038b-1e37-490f-afea-46da8c26ef54` | - |
| **Dashboard Usage Metrics Model** | `SemanticModel` | `07024adf-0fbc-4c8f-848e-fb8464baa1e2` | - |
| **TMEU Order Book** | `SemanticModel` | `ececf465-b70c-4c6d-a5c9-f2d30cd5a0a2` | - |
| **Usage Metrics Report** | `SemanticModel` | `8a47e46b-0bdb-4fc8-b855-275ceeb3dde5` | - |

## 3. Semantic Models (Datasets) & Refresh Schedules

### Semantic Model: Report Usage Metrics Model
- **Dataset ID**: `676d038b-1e37-490f-afea-46da8c26ef54`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `False`
- **Configured By**: `N/A`

*No refresh schedule configured.*

### Semantic Model: Dashboard Usage Metrics Model
- **Dataset ID**: `07024adf-0fbc-4c8f-848e-fb8464baa1e2`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `False`
- **Configured By**: `gandreev@titanmachinery.at`

*No refresh schedule configured.*

### Semantic Model: TMEU Order Book
- **Dataset ID**: `ececf465-b70c-4c6d-a5c9-f2d30cd5a0a2`
- **Target Storage Mode**: `PremiumFiles`
- **Is Refreshable**: `True`
- **Configured By**: `!TMATVDOB@titanmachinery.net`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `23:30` (Romance Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `Sql` | Connection: `{'server': 'tmweupautosql01.database.windows.net', 'database': 'tmweu_reporting_db'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2026-09-14 21:30:16 | 2026-09-14 21:37:16 | `Completed` | `Scheduled` | - |
| 2026-09-13 21:30:14 | 2026-09-13 21:37:17 | `Completed` | `Scheduled` | - |
| 2026-09-12 21:30:17 | 2026-09-12 21:36:50 | `Completed` | `Scheduled` | - |
| 2026-09-11 21:30:15 | 2026-09-11 21:35:07 | `Completed` | `Scheduled` | - |
| 2026-09-10 21:30:18 | 2026-09-10 21:37:26 | `Completed` | `Scheduled` | - |

### Semantic Model: Usage Metrics Report
- **Dataset ID**: `8a47e46b-0bdb-4fc8-b855-275ceeb3dde5`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `00:31` (UTC)

**Connected Data Sources (Lineage)**:
- Type: `Extension` | Connection: `{'path': 'UsageMetricsDataConnector', 'kind': 'UsageMetricsDataConnector'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2025-07-21 00:32:06 | 2025-07-21 00:32:06 | `Disabled` | `Scheduled` | - |
| 2025-07-20 00:31:12 | 2025-07-20 00:41:38 | `Completed` | `Scheduled` | - |
| 2025-07-19 00:31:09 | 2025-07-19 00:40:54 | `Completed` | `Scheduled` | - |
| 2025-07-18 00:31:06 | 2025-07-18 00:41:01 | `Completed` | `Scheduled` | - |
| 2025-07-17 00:31:05 | 2025-07-17 00:37:39 | `Completed` | `Scheduled` | - |

## 4. Power BI Reports Inventory

| Report Name | Report ID | Dataset ID | Web URL |
| :--- | :--- | :--- | :--- |
| **Report Usage Metrics Report** | `2a6b0a74-8fa6-49ea-85a3-62c5598efef0` | `676d038b-1e37-490f-afea-46da8c26ef54` | [Open Report](https://app.powerbi.com/groups/8bfed8bd-eeac-4f98-a57a-44ca24a055a8/reports/2a6b0a74-8fa6-49ea-85a3-62c5598efef0) |
| **Dashboard Usage Metrics Report** | `4e04efca-e56c-4648-b473-2ab8590cf628` | `07024adf-0fbc-4c8f-848e-fb8464baa1e2` | [Open Report](https://app.powerbi.com/groups/8bfed8bd-eeac-4f98-a57a-44ca24a055a8/reports/4e04efca-e56c-4648-b473-2ab8590cf628) |
| **TMEU Order Book** | `ab6ad5b1-5c93-46b5-85f6-ebb1af70bc5b` | `ececf465-b70c-4c6d-a5c9-f2d30cd5a0a2` | [Open Report](https://app.powerbi.com/groups/8bfed8bd-eeac-4f98-a57a-44ca24a055a8/reports/ab6ad5b1-5c93-46b5-85f6-ebb1af70bc5b) |
| **Usage Metrics Report** | `37a4689e-e588-4c3e-87b3-ffadfa406679` | `8a47e46b-0bdb-4fc8-b855-275ceeb3dde5` | [Open Report](https://app.powerbi.com/groups/8bfed8bd-eeac-4f98-a57a-44ca24a055a8/reports/37a4689e-e588-4c3e-87b3-ffadfa406679) |

## 5. Dataflows & Dashboards

**Dashboards**:
- **Order Book Dashboard** (ID: `6479822d-c36f-4ba7-81b7-52c7644f3877`)

---

## 6. Newcomer Operational Runbook & Notes
- **Primary Contact / Owner**: Refer to workspace access settings in Power BI portal.
- **Troubleshooting**: If a refresh fails in `INT_OrderBook`, inspect the failure log under section 3 above and check upstream data gateway connectivity.
