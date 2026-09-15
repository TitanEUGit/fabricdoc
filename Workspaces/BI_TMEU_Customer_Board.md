# Workspace Documentation: BI_TMEU_Customer_Board

**Workspace ID**: `f8b208b3-5e8a-4610-8f20-c30759eb3fd7`  
**Type**: `Fabric / PowerBI Workspace`  
**Capacity ID**: `70650ed2-f7a2-46df-96e8-8089f25db80e`  
**Description**: No description provided.

---

## 1. Executive Summary & Newcomer Overview
This document contains operational and technical details for the **BI_TMEU_Customer_Board** workspace. It is designed to give new team members full visibility into key items, data models, report lineage, and refresh schedules.

## 2. Native Fabric Items Inventory

| Item Name | Item Type | Item ID | Description |
| :--- | :--- | :--- | :--- |
| **TMR Customer Penetration Board** | `Report` | `e89a78f7-1a11-46e2-b963-ead6bf8898be` | - |
| **TMB Customer Penetration Board** | `Report` | `092675bd-fbb6-4160-84ba-10be85d6b1fd` | - |
| **TMU Customer Penetration Board** | `Report` | `ac14520d-8dec-418b-9982-f42624ae27ad` | - |
| **TMR Customer Penetration Board** | `SemanticModel` | `cc966151-7fc2-4241-8550-c4406676d4d7` | - |
| **TMB Customer Penetration Board** | `SemanticModel` | `04ee2469-c9c8-4f94-83c9-b3dcbef43aa2` | - |
| **TMU Customer Penetration Board** | `SemanticModel` | `bc3953ee-b242-417a-885f-a8b824494619` | - |

## 3. Semantic Models (Datasets) & Refresh Schedules

### Semantic Model: TMR Customer Penetration Board
- **Dataset ID**: `cc966151-7fc2-4241-8550-c4406676d4d7`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `09:00` (FLE Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `Extension` | Connection: `{'path': 'titanromania.crm4.dynamics.com', 'kind': 'CommonDataService'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmr_opspackage', 'database': 'tmr ops package'}`
- Type: `Sql` | Connection: `{'server': '10.75.1.7', 'database': 'jetnavdwh'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2026-09-15 06:02:16 | 2026-09-15 06:11:40 | `Completed` | `Scheduled` | - |
| 2026-09-14 06:01:15 | 2026-09-14 06:09:35 | `Completed` | `Scheduled` | - |
| 2026-09-13 06:02:09 | 2026-09-13 06:11:44 | `Completed` | `Scheduled` | - |
| 2026-09-12 06:02:18 | 2026-09-12 06:11:37 | `Completed` | `Scheduled` | - |
| 2026-09-11 06:02:18 | 2026-09-11 06:11:08 | `Completed` | `Scheduled` | - |

### Semantic Model: TMB Customer Penetration Board
- **Dataset ID**: `04ee2469-c9c8-4f94-83c9-b3dcbef43aa2`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `09:00` (FLE Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `Extension` | Connection: `{'path': 'titanbulgaria.crm4.dynamics.com', 'kind': 'CommonDataService'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmb_opspackage', 'database': 'tmb ops package'}`
- Type: `Sql` | Connection: `{'server': '10.75.1.7', 'database': 'jetnavdwh'}`
- Type: `Sql` | Connection: `{'server': 'titaneu.database.windows.net', 'database': 'titanbg'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2026-09-15 06:02:14 | 2026-09-15 06:08:10 | `Completed` | `Scheduled` | - |
| 2026-09-14 06:01:14 | 2026-09-14 06:06:06 | `Completed` | `Scheduled` | - |
| 2026-09-13 06:02:09 | 2026-09-13 06:08:15 | `Completed` | `Scheduled` | - |
| 2026-09-12 06:02:16 | 2026-09-12 06:09:32 | `Completed` | `Scheduled` | - |
| 2026-09-11 06:02:16 | 2026-09-11 06:07:53 | `Completed` | `Scheduled` | - |

### Semantic Model: TMU Customer Penetration Board
- **Dataset ID**: `bc3953ee-b242-417a-885f-a8b824494619`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `09:00` (FLE Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `Extension` | Connection: `{'path': 'titanukraine.crm4.dynamics.com', 'kind': 'CommonDataService'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmu_opspackage', 'database': 'tmu ops package'}`
- Type: `Sql` | Connection: `{'server': 'cwgz5ola5r6u5e4heu5qw3drgy-zzqhzdizzmcurky2zbgw4gw7la.datawarehouse.fabric.microsoft.com', 'database': 'tmu_bronze_lakehouse'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2026-09-15 06:02:08 | 2026-09-15 06:07:03 | `Completed` | `Scheduled` | - |
| 2026-09-14 06:01:06 | 2026-09-14 06:04:59 | `Completed` | `Scheduled` | - |
| 2026-09-13 06:02:10 | 2026-09-13 06:07:50 | `Completed` | `Scheduled` | - |
| 2026-09-12 06:02:08 | 2026-09-12 06:08:04 | `Completed` | `Scheduled` | - |
| 2026-09-11 06:02:08 | 2026-09-11 06:06:19 | `Completed` | `Scheduled` | - |

## 4. Power BI Reports Inventory

| Report Name | Report ID | Dataset ID | Web URL |
| :--- | :--- | :--- | :--- |
| **TMR Customer Penetration Board** | `e89a78f7-1a11-46e2-b963-ead6bf8898be` | `cc966151-7fc2-4241-8550-c4406676d4d7` | [Open Report](https://app.powerbi.com/groups/f8b208b3-5e8a-4610-8f20-c30759eb3fd7/reports/e89a78f7-1a11-46e2-b963-ead6bf8898be) |
| **TMB Customer Penetration Board** | `092675bd-fbb6-4160-84ba-10be85d6b1fd` | `04ee2469-c9c8-4f94-83c9-b3dcbef43aa2` | [Open Report](https://app.powerbi.com/groups/f8b208b3-5e8a-4610-8f20-c30759eb3fd7/reports/092675bd-fbb6-4160-84ba-10be85d6b1fd) |
| **TMU Customer Penetration Board** | `ac14520d-8dec-418b-9982-f42624ae27ad` | `bc3953ee-b242-417a-885f-a8b824494619` | [Open Report](https://app.powerbi.com/groups/f8b208b3-5e8a-4610-8f20-c30759eb3fd7/reports/ac14520d-8dec-418b-9982-f42624ae27ad) |

## 5. Dataflows & Dashboards

*No dataflows or dashboards in this workspace.*

---

## 6. Newcomer Operational Runbook & Notes
- **Primary Contact / Owner**: Refer to workspace access settings in Power BI portal.
- **Troubleshooting**: If a refresh fails in `BI_TMEU_Customer_Board`, inspect the failure log under section 3 above and check upstream data gateway connectivity.
