# Workspace Documentation: BI_TMB_OPSpackage

**Workspace ID**: `a285e0f3-8eb3-435e-8e1d-0c741d8abeff`  
**Type**: `Fabric / PowerBI Workspace`  
**Capacity ID**: `70650ed2-f7a2-46df-96e8-8089f25db80e`  
**Description**: No description provided.

---

## 1. Executive Summary & Newcomer Overview

> [!IMPORTANT]
> **Core Country Operations Report (Bulgaria)**
> This workspace houses the primary **TMB OPS Package report**, which is the business-critical operations dashboard for Bulgaria. 
> - **Primary Data Source:** Legacy `JetDWH` data warehouse maintained by Arggo.
> - **Manual Adjustments:** Pulls from a dedicated `TMB OPS Package Helpers` dataflow (located in the `DS_TMEU_Datasets and Dataflows` workspace) for manual user overrides.

This document contains operational and technical details for the **BI_TMB_OPSpackage** workspace. It is designed to give new team members full visibility into key items, data models, report lineage, and refresh schedules.

## 2. Native Fabric Items Inventory

| Item Name | Item Type | Item ID | Description |
| :--- | :--- | :--- | :--- |
| **DB_SERVICE_KPI_old_v** | `Dashboard` | `8957a7d6-fd00-4f1c-9299-17cd5315aeb0` | - |
| **TMB OPS Package** | `Report` | `f9470603-2b5f-4e69-b859-4bc9522a0ac7` | - |
| **Report Usage Metrics Report** | `Report` | `53fc9e6d-3feb-4142-ba67-c5d6d0c0054b` | - |
| **TMB OPS Package** | `SemanticModel` | `25029823-27bf-4fbf-ac11-9d0cf33445d0` | - |
| **Report Usage Metrics Model** | `SemanticModel` | `754588d4-8706-4344-bb2c-11e83df40ac8` | - |

## 3. Semantic Models (Datasets) & Refresh Schedules

### Semantic Model: TMB OPS Package
- **Dataset ID**: `25029823-27bf-4fbf-ac11-9d0cf33445d0`
- **Target Storage Mode**: `PremiumFiles`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `01:30` (Romance Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `Sql` | Connection: `{'server': '10.75.1.7', 'database': 'jetnavdwh'}` — *Legacy JetDWH data warehouse (primary ERP source)*
- Type: `Extension` | Connection: `{'path': 'PowerPlatformDataflows', 'kind': 'PowerPlatformDataflows'}` — *TMB OPS Package Helpers dataflow (manual adjustments)*
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/int_orderbook', 'database': 'tmeu order book'}`
- Type: `Sql` | Connection: `{'server': 'cwgz5ola5r6u5e4heu5qw3drgy-zzqhzdizzmcurky2zbgw4gw7la.datawarehouse.fabric.microsoft.com', 'database': 'tmeu_bronze_lakehouse'}`
- Type: `Sql` | Connection: `{'server': 'cwgz5ola5r6u5e4heu5qw3drgy-zzqhzdizzmcurky2zbgw4gw7la.datawarehouse.fabric.microsoft.com', 'database': 'tmeu_erp_raw_lakehouse'}`


### Semantic Model: Report Usage Metrics Model
- **Dataset ID**: `754588d4-8706-4344-bb2c-11e83df40ac8`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `False`
- **Configured By**: `OBaliuta@titanmachinery.ua`

*No refresh schedule configured.*

## 4. Power BI Reports Inventory

| Report Name | Report ID | Dataset ID | Web URL |
| :--- | :--- | :--- | :--- |
| **TMB OPS Package** | `f9470603-2b5f-4e69-b859-4bc9522a0ac7` | `25029823-27bf-4fbf-ac11-9d0cf33445d0` | [Open Report](https://app.powerbi.com/groups/a285e0f3-8eb3-435e-8e1d-0c741d8abeff/reports/f9470603-2b5f-4e69-b859-4bc9522a0ac7) |
| **Report Usage Metrics Report** | `53fc9e6d-3feb-4142-ba67-c5d6d0c0054b` | `754588d4-8706-4344-bb2c-11e83df40ac8` | [Open Report](https://app.powerbi.com/groups/a285e0f3-8eb3-435e-8e1d-0c741d8abeff/reports/53fc9e6d-3feb-4142-ba67-c5d6d0c0054b) |

## 5. Dataflows & Dashboards

**Dashboards**:
- **DB_SERVICE_KPI_old_v** (ID: `8957a7d6-fd00-4f1c-9299-17cd5315aeb0`)

---

## 6. Newcomer Operational Runbook & Notes
- **Primary Contact / Owner**: Refer to workspace access settings in Power BI portal.
- **Troubleshooting (Refresh Failures)**: If a refresh fails in `BI_TMB_OPSpackage`, inspect the failure log under section 3 above and check upstream data gateway connectivity.
- **Troubleshooting (Missing P&L Accounts)**: If the finance team reports that a newly added account is not showing up in the P&L, it most likely needs to be manually added to the Power Query steps within the report, specifically for the **'Finance Transactions'** table.
