# Workspace Documentation: BI_TMU_OPSpackage

**Workspace ID**: `bd89fb03-9bee-4b40-9e53-13f841bf0dee`  
**Type**: `Fabric / PowerBI Workspace`  
**Capacity ID**: `70650ed2-f7a2-46df-96e8-8089f25db80e`  
**Description**: No description provided.

---

## 1. Executive Summary & Newcomer Overview

> [!IMPORTANT]
> **Core Country Operations Report (Ukraine)**
> This workspace houses the primary **TMU OPS Package report**, which is the business-critical operations dashboard for Ukraine. 
> - **Primary Data Source:** `TMU_Bronze_Lakehouse`, which stores ERP data received via endpoints overnight.
> - **Headcount Data:** Manually populated by the HR department in a SharePoint location every month during the first calendar days.

This document contains operational and technical details for the **BI_TMU_OPSpackage** workspace. It is designed to give new team members full visibility into key items, data models, report lineage, and refresh schedules.

## 2. Native Fabric Items Inventory

| Item Name | Item Type | Item ID | Description |
| :--- | :--- | :--- | :--- |
| **TMU_SP_Inventory_Surplus** | `Dashboard` | `7449e7c2-6800-49fb-8058-fcab0cbe5732` | - |
| **TMU OPS Package** | `Report` | `28004ae3-0c14-4ee4-bca3-331ec5015b2f` | - |
| **Usage Metrics Report** | `Report` | `ff2712c2-13cd-4b63-bb7e-f06fe65192a0` | - |
| **TMU OPS Package** | `SemanticModel` | `bb98a0ec-c342-404c-b267-983ec8a7821b` | - |
| **Usage Metrics Report** | `SemanticModel` | `a17cf531-be9f-4681-9a6e-f54c37a5a990` | - |

## 3. Semantic Models (Datasets) & Refresh Schedules

### Semantic Model: TMU OPS Package
- **Dataset ID**: `bb98a0ec-c342-404c-b267-983ec8a7821b`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `07:00` (FLE Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `Extension` | Connection: `{'path': 'PowerPlatformDataflows', 'kind': 'PowerPlatformDataflows'}`
- Type: `Web` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/Collaboration/Shared%20Documents/INT_POWERBI_HELPER/TMU/OPSPackage/AR_adjustments/ar_adjustments.xlsx'}`
- Type: `Web` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/Collaboration/Shared%20Documents/INT_POWERBI_HELPER/TMU/OPSPackage/Budget/SP_Budget.xlsx'}`
- Type: `Web` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/Collaboration/Shared%20Documents/INT_POWERBI_HELPER/TMU/OPSPackage/Budget/PNL%20Budget%20Division.xlsx'}`
- Type: `SharePointList` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/collaboration/'}`
- Type: `Sql` | Connection: `{'server': '10.75.1.7', 'database': 'jetnavdwh'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/int_orderbook', 'database': 'tmeu order book'}`
- Type: `Extension` | Connection: `{'path': 'titanukraine.crm4.dynamics.com', 'kind': 'CommonDataService'}`
- Type: `Sql` | Connection: `{'server': 'cwgz5ola5r6u5e4heu5qw3drgy-zzqhzdizzmcurky2zbgw4gw7la.datawarehouse.fabric.microsoft.com', 'database': 'tmu_bronze_lakehouse'}` — *Primary ERP source (stores data received via endpoints overnight)*
- Type: `Sql` | Connection: `{'server': 'cwgz5ola5r6u5e4heu5qw3drgy-zzqhzdizzmcurky2zbgw4gw7la.database.fabric.microsoft.com', 'database': 'tmu assortment budget-2ad254ce-44d5-4c67-9aee-a34267f0a56d'}`
- Type: `Sql` | Connection: `{'server': 'cwgz5ola5r6u5e4heu5qw3drgy-zzqhzdizzmcurky2zbgw4gw7la.datawarehouse.fabric.microsoft.com', 'database': 'tmeu_erp_raw_lakehouse'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2026-09-15 04:00:27 | 2026-09-15 04:11:56 | `Completed` | `Scheduled` | - |
| 2026-09-14 04:00:27 | 2026-09-14 04:10:50 | `Completed` | `Scheduled` | - |
| 2026-09-13 04:01:14 | 2026-09-13 04:13:28 | `Completed` | `Scheduled` | - |
| 2026-09-12 04:00:33 | 2026-09-12 04:14:27 | `Completed` | `Scheduled` | - |
| 2026-09-11 04:01:24 | 2026-09-11 04:13:39 | `Completed` | `Scheduled` | - |

### Semantic Model: Usage Metrics Report
- **Dataset ID**: `a17cf531-be9f-4681-9a6e-f54c37a5a990`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `19:52` (UTC)

**Connected Data Sources (Lineage)**:
- Type: `Extension` | Connection: `{'path': 'UsageMetricsDataConnector', 'kind': 'UsageMetricsDataConnector'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2025-07-20 19:52:17 | 2025-07-20 19:52:17 | `Disabled` | `Scheduled` | - |
| 2025-07-19 19:52:04 | 2025-07-19 19:53:44 | `Completed` | `Scheduled` | - |
| 2025-07-18 19:52:24 | 2025-07-18 19:53:50 | `Completed` | `Scheduled` | - |
| 2025-07-17 19:52:16 | 2025-07-17 19:52:47 | `Completed` | `Scheduled` | - |
| 2025-07-16 19:52:15 | 2025-07-16 19:53:26 | `Completed` | `Scheduled` | - |

## 4. Power BI Reports Inventory

| Report Name | Report ID | Dataset ID | Web URL |
| :--- | :--- | :--- | :--- |
| **TMU OPS Package** | `28004ae3-0c14-4ee4-bca3-331ec5015b2f` | `bb98a0ec-c342-404c-b267-983ec8a7821b` | [Open Report](https://app.powerbi.com/groups/bd89fb03-9bee-4b40-9e53-13f841bf0dee/reports/28004ae3-0c14-4ee4-bca3-331ec5015b2f) |
| **Usage Metrics Report** | `ff2712c2-13cd-4b63-bb7e-f06fe65192a0` | `a17cf531-be9f-4681-9a6e-f54c37a5a990` | [Open Report](https://app.powerbi.com/groups/bd89fb03-9bee-4b40-9e53-13f841bf0dee/reports/ff2712c2-13cd-4b63-bb7e-f06fe65192a0) |

## 5. Dataflows & Dashboards

**Dashboards**:
- **TMU_SP_Inventory_Surplus** (ID: `7449e7c2-6800-49fb-8058-fcab0cbe5732`)

---

## 6. Newcomer Operational Runbook & Notes
- **Primary Contact / Owner**: Refer to workspace access settings in Power BI portal.
- **Troubleshooting (Refresh Failures)**: If a refresh fails in `BI_TMU_OPSpackage`, inspect the failure log under section 3 above and check upstream data gateway connectivity.
- **Troubleshooting (Missing P&L Accounts)**: If the finance team reports that a newly added account is not showing up in the P&L, you need to maintain/add it within the **`TMU_Bronze_Lakehouse`** in the **`dbo.uausmapping`** table.
