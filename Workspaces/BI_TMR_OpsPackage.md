# Workspace Documentation: BI_TMR_OpsPackage

**Workspace ID**: `a64c7035-492e-478a-87ef-6ebf6030e151`  
**Type**: `Fabric / PowerBI Workspace`  
**Capacity ID**: `70650ed2-f7a2-46df-96e8-8089f25db80e`  
**Description**: No description provided.

---

## 1. Executive Summary & Newcomer Overview
This document contains operational and technical details for the **BI_TMR_OpsPackage** workspace. It is designed to give new team members full visibility into key items, data models, report lineage, and refresh schedules.

## 2. Native Fabric Items Inventory

| Item Name | Item Type | Item ID | Description |
| :--- | :--- | :--- | :--- |
| **TMR OPS Package** | `Report` | `fe403e56-3512-4ecc-b674-eefbe3f9908a` | - |
| **TMR OPS Package** | `SemanticModel` | `84c66778-4a62-413e-bc56-cefbaeddb68e` | - |

## 3. Semantic Models (Datasets) & Refresh Schedules

### Semantic Model: TMR OPS Package
- **Dataset ID**: `84c66778-4a62-413e-bc56-cefbaeddb68e`
- **Target Storage Mode**: `PremiumFiles`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `08:00` (FLE Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `Sql` | Connection: `{'server': '10.75.1.7', 'database': 'jetnavdwh'}`
- Type: `Extension` | Connection: `{'path': 'titanromania.crm4.dynamics.com', 'kind': 'CommonDataService'}`
- Type: `Extension` | Connection: `{'path': 'PowerPlatformDataflows', 'kind': 'PowerPlatformDataflows'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/int_orderbook', 'database': 'tmeu order book'}`
- Type: `Sql` | Connection: `{'server': 'cwgz5ola5r6u5e4heu5qw3drgy-zzqhzdizzmcurky2zbgw4gw7la.datawarehouse.fabric.microsoft.com', 'database': 'tmeu_bronze_lakehouse'}`
- Type: `Sql` | Connection: `{'server': 'cwgz5ola5r6u5e4heu5qw3drgy-zzqhzdizzmcurky2zbgw4gw7la.datawarehouse.fabric.microsoft.com', 'database': 'tmeu_erp_raw_lakehouse'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2026-09-15 05:00:27 | 2026-09-15 05:28:03 | `Completed` | `Scheduled` | - |
| 2026-09-14 05:00:26 | 2026-09-14 05:28:10 | `Completed` | `Scheduled` | - |
| 2026-09-13 05:01:02 | 2026-09-13 05:57:41 | `Completed` | `Scheduled` | - |
| 2026-09-12 05:00:10 | 2026-09-12 05:25:27 | `Completed` | `Scheduled` | - |
| 2026-09-11 05:01:15 | 2026-09-11 05:25:54 | `Completed` | `Scheduled` | - |

## 4. Power BI Reports Inventory

| Report Name | Report ID | Dataset ID | Web URL |
| :--- | :--- | :--- | :--- |
| **TMR OPS Package** | `fe403e56-3512-4ecc-b674-eefbe3f9908a` | `84c66778-4a62-413e-bc56-cefbaeddb68e` | [Open Report](https://app.powerbi.com/groups/a64c7035-492e-478a-87ef-6ebf6030e151/reports/fe403e56-3512-4ecc-b674-eefbe3f9908a) |

## 5. Dataflows & Dashboards

*No dataflows or dashboards in this workspace.*

---

## 6. Newcomer Operational Runbook & Notes
- **Primary Contact / Owner**: Refer to workspace access settings in Power BI portal.
- **Troubleshooting**: If a refresh fails in `BI_TMR_OpsPackage`, inspect the failure log under section 3 above and check upstream data gateway connectivity.
