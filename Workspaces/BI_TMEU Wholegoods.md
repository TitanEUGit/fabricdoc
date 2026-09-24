# Workspace Documentation: BI_TMEU Wholegoods

**Workspace ID**: `bab7ddd2-e1c2-4ba1-a256-1249369dc086`  
**Type**: `Fabric / PowerBI Workspace`  
**Capacity ID**: `70650ed2-f7a2-46df-96e8-8089f25db80e`  
**Description**: No description provided.

---

## 1. Executive Summary & Newcomer Overview

> [!IMPORTANT]
> **Core European Wholegoods Workspace (TMA HQ)**
> This is a very important TMA workspace that consolidates Wholegoods (WG) data across all European countries. It houses the critical "source of truth" reports for Wholegoods inventory, orders, and forecasting.

### Key Reports at a Glance
| Report Name | What It Shows | Audience |
|:---|:---|:---|
| **TMEU Inventory Book** | **Source of truth.** WG inventory data gets collected from OPS packages reports on the 10th calendar day and persists in the lakehouse. | TMA WG Team / Management |
| **TMEU Order Book** | **Source of truth.** Shows all active and arrived orders. Crucial for WG sales forecasting. | TMA WG Team / Management |
| **TMEU Inventory Forecast** | Forecasts inventory based on the Order Book, Inventory Book, and manual adjustments (Excel files from SharePoint). | TMA Finance / Management |
| **TMEU Inventory Forecast (EDD)** | Same as the standard forecast but includes manual Excel adjustments for the Planned Arrival date. | TMA Finance / Management |
| **TMB KTI Report** | Relies on TMB KTI data (fed by a pipeline in the `Fabric_Prod_Workspace` with a similar name). | Country / TMA |

### Newcomer Tips
- All manual Excel adjustment files used in the Inventory Forecast reports are maintained by the **TMA Finance Manager** on SharePoint.
- **Pending Deletion Review:** All `WG Stock Order Helper (model input)` reports across all countries (TMB, TMR, TMD, TMU) currently have unproven usage. Verify if they are still needed by the business and consider decommissioning them if not.

This document contains operational and technical details for the **BI_TMEU Wholegoods** workspace. It is designed to give new team members full visibility into key items, data models, report lineage, and refresh schedules.

## 2. Native Fabric Items Inventory

| Item Name | Item Type | Item ID | Description |
| :--- | :--- | :--- | :--- |
| **TMR WG Stock Order Helper (model input)** | `Report` | `de8e4ae7-de56-4307-9a31-279b6f8f0f24` | - |
| **TMB WG Stock Order Helper (model input)** | `Report` | `7d03dc6a-37b7-4faf-bbfb-6cb8af89c92a` | - |
| **TMD WG Stock Order Helper (model input)** | `Report` | `bac075d1-6448-4071-963b-0278a73cf2d3` | - |
| **TMEU Inventory Forecast** | `Report` | `c06bc7bc-51cf-402d-9f3c-b677eafa0473` | - |
| **TMU WG Stock Order Helper (model input)** | `Report` | `9ce9d6ad-e98a-4f09-baa5-bbb3a2e62398` | - |
| **Usage Metrics Report** | `Report` | `e397f811-c632-4ef3-8b15-d0387a84f5df` | - |
| **Report Usage Metrics Report** | `Report` | `fa484086-80dc-43ed-8e7c-c4d811cdc27a` | - |
| **TMU Inventory Forecast** | `Report` | `3d006a32-4ea9-40e7-a911-e915cfb2fe97` | - |
| **TMEU Inventory Forecast (EDD)** | `Report` | `40acdbac-1044-4b2a-b952-ee5124267aa2` | - |
| **TMB KTI Report** | `Report` | `e9b89ac7-87e8-40ee-8d70-cd0e60379932` | - |
| **TMR WG Stock Order Helper (model input)** | `SemanticModel` | `6d51da16-27cc-4a09-a7b8-ff1077575cc2` | - |
| **TMB WG Stock Order Helper (model input)** | `SemanticModel` | `b5bfbc6e-574a-478d-bcd9-03a52b2aa70f` | - |
| **TMD WG Stock Order Helper (model input)** | `SemanticModel` | `8da0d574-58ee-431e-b764-65b1cb0ef79c` | - |
| **TMEU Inventory Forecast** | `SemanticModel` | `9f00ef86-146e-45c2-8424-fdb6bbde4626` | - |
| **TMU WG Stock Order Helper (model input)** | `SemanticModel` | `57746fbc-5b9a-44b1-9a9b-45dfdd4c62d1` | - |
| **Usage Metrics Report** | `SemanticModel` | `99cf25b7-e07f-43fa-a0dc-539fdc60dee5` | - |
| **Report Usage Metrics Model** | `SemanticModel` | `cfc5b550-e550-4398-acdd-a0b053816717` | - |
| **TMU Inventory Forecast** | `SemanticModel` | `2327fe6d-8514-4e9a-a591-39a9d308eb3d` | - |
| **TMEU Inventory Forecast (EDD)** | `SemanticModel` | `1af8389e-51c5-45e5-bb2e-cb85cabbec1a` | - |
| **TMB KTI Report** | `SemanticModel` | `cbb167d6-301c-4a54-9bbf-82794c0f09d1` | - |

## 3. Semantic Models (Datasets) & Refresh Schedules

### Semantic Model: TMR WG Stock Order Helper (model input)
- **Dataset ID**: `6d51da16-27cc-4a09-a7b8-ff1077575cc2`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `06:00` (FLE Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/int_orderbook', 'database': 'tmeu order book'}`
- Type: `Sql` | Connection: `{'server': '10.75.1.7', 'database': 'jetnavdwh'}`
- Type: `Extension` | Connection: `{'path': 'titanromania.crm4.dynamics.com', 'kind': 'CommonDataService'}`
- Type: `Web` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/Collaboration/Shared%20Documents/INT_POWERBI_HELPER/TMR/Order%20Helper/Models%20and%20Leadtime.xlsx'}`
- Type: `Web` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/Collaboration/Shared%20Documents/INT_POWERBI_HELPER/TMR/Order%20Helper/Budget%20Units.xlsx'}`


### Semantic Model: TMB WG Stock Order Helper (model input)
- **Dataset ID**: `b5bfbc6e-574a-478d-bcd9-03a52b2aa70f`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `06:00` (FLE Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `Sql` | Connection: `{'server': '10.75.1.7', 'database': 'jetnavdwh'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/int_orderbook', 'database': 'tmeu order book'}`
- Type: `Web` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/Collaboration/Shared%20Documents/INT_POWERBI_HELPER/TMB/Order%20Helper/Budget%20Units.xlsx'}`
- Type: `Web` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/Collaboration/Shared%20Documents/INT_POWERBI_HELPER/TMB/Order%20Helper/Models%20and%20Leadtime.xlsx'}`


### Semantic Model: TMD WG Stock Order Helper (model input)
- **Dataset ID**: `8da0d574-58ee-431e-b764-65b1cb0ef79c`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `06:00` (FLE Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmd_sales', 'database': 'tmd wg sales'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/int_orderbook', 'database': 'tmeu order book'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmeu_inventorybook', 'database': 'tmeu inventory book'}`
- Type: `Web` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/Collaboration/Shared%20Documents/INT_POWERBI_HELPER/TMD/Order%20Helper/Models%20and%20Leadtime.xlsx'}`
- Type: `Web` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/Collaboration/Shared%20Documents/INT_POWERBI_HELPER/TMD/Order%20Helper/Budget%20Units.xlsx'}`
- Type: `Extension` | Connection: `{'path': 'titanmachinery.crm4.dynamics.com', 'kind': 'CommonDataService'}`


### Semantic Model: TMEU Inventory Forecast
- **Dataset ID**: `9f00ef86-146e-45c2-8424-fdb6bbde4626`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `06:00` (FLE Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_eoc_opspackage', 'database': 'tmeu multi-country ops package'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmeu_inventorybook', 'database': 'tmeu inventory book'}`
- Type: `SharePointList` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/collaboration/'}`
- Type: `Web` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/Collaboration/Shared%20Documents/INT_POWERBI_HELPER/WG/Inventory_forecast_report/Inventory%20Forecast%20Helper.xlsx'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/int_orderbook', 'database': 'tmeu order book'}`
- Type: `Extension` | Connection: `{'path': 'PowerPlatformDataflows', 'kind': 'PowerPlatformDataflows'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmr_opspackage', 'database': 'tmr ops package'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmu_opspackage', 'database': 'tmu ops package'}`


### Semantic Model: TMU WG Stock Order Helper (model input)
- **Dataset ID**: `57746fbc-5b9a-44b1-9a9b-45dfdd4c62d1`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `06:00` (FLE Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/int_orderbook', 'database': 'tmeu order book'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmeu_inventorybook', 'database': 'tmeu inventory book'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmu_opspackage', 'database': 'tmu ops package'}`
- Type: `Web` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/Collaboration/Shared%20Documents/INT_POWERBI_HELPER/TMU/Order%20Helper/Models%20and%20Leadtime.xlsx'}`
- Type: `Web` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/Collaboration/Shared%20Documents/INT_POWERBI_HELPER/TMU/Order%20Helper/Budget%20Units.xlsx'}`
- Type: `Extension` | Connection: `{'path': 'PowerPlatformDataflows', 'kind': 'PowerPlatformDataflows'}`


### Semantic Model: Usage Metrics Report
- **Dataset ID**: `99cf25b7-e07f-43fa-a0dc-539fdc60dee5`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `02:42` (UTC)

**Connected Data Sources (Lineage)**:
- Type: `Extension` | Connection: `{'path': 'UsageMetricsDataConnector', 'kind': 'UsageMetricsDataConnector'}`


### Semantic Model: Report Usage Metrics Model
- **Dataset ID**: `cfc5b550-e550-4398-acdd-a0b053816717`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `False`
- **Configured By**: `gandreev@titanmachinery.at`

*No refresh schedule configured.*

### Semantic Model: TMU Inventory Forecast
- **Dataset ID**: `2327fe6d-8514-4e9a-a591-39a9d308eb3d`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `07:00` (FLE Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmeu_inventorybook', 'database': 'tmeu inventory book'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_eoc_opspackage', 'database': 'tmeu multi-country ops package'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmu_opspackage', 'database': 'tmu ops package'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/int_orderbook', 'database': 'tmeu order book'}`
- Type: `Extension` | Connection: `{'path': 'PowerPlatformDataflows', 'kind': 'PowerPlatformDataflows'}`
- Type: `Web` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/Collaboration/Shared%20Documents/INT_POWERBI_HELPER/TMU/Inventory%20Forecast%20Helper/TMU%20Inventory%20Forecast%20Helper.xlsx'}`
- Type: `SharePointList` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/collaboration/'}`


### Semantic Model: TMEU Inventory Forecast (EDD)
- **Dataset ID**: `1af8389e-51c5-45e5-bb2e-cb85cabbec1a`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `07:00` (FLE Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmr_opspackage', 'database': 'tmr ops package'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_eoc_opspackage', 'database': 'tmeu multi-country ops package'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmu_opspackage', 'database': 'tmu ops package'}`
- Type: `Extension` | Connection: `{'path': 'PowerPlatformDataflows', 'kind': 'PowerPlatformDataflows'}`
- Type: `Web` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/Collaboration/Shared%20Documents/INT_POWERBI_HELPER/WG/Inventory_forecast_report/Inventory%20Forecast%20Helper.xlsx'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/int_orderbook', 'database': 'tmeu order book'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmeu_inventorybook', 'database': 'tmeu inventory book'}`
- Type: `SharePointList` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/collaboration/'}`
- Type: `Web` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/Collaboration/Shared%20Documents/INT_POWERBI_HELPER/WG/source%20based%20on%20EDD/Estimated%20delivery%20dates.xlsx'}`
- Type: `Sql` | Connection: `{'server': 'cwgz5ola5r6u5e4heu5qw3drgy-zzqhzdizzmcurky2zbgw4gw7la.datawarehouse.fabric.microsoft.com', 'database': 'tmeu_bronze_lakehouse'}`


### Semantic Model: TMB KTI Report
- **Dataset ID**: `cbb167d6-301c-4a54-9bbf-82794c0f09d1`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (DISABLED ❌):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `05:00` (FLE Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `Sql` | Connection: `{'server': 'cwgz5ola5r6u5e4heu5qw3drgy-zzqhzdizzmcurky2zbgw4gw7la.datawarehouse.fabric.microsoft.com', 'database': 'tmeu_bronze_lakehouse'}`


## 4. Power BI Reports Inventory

| Report Name | Report ID | Dataset ID | Web URL |
| :--- | :--- | :--- | :--- |
| **TMR WG Stock Order Helper (model input)** | `de8e4ae7-de56-4307-9a31-279b6f8f0f24` | `6d51da16-27cc-4a09-a7b8-ff1077575cc2` | [Open Report](https://app.powerbi.com/groups/bab7ddd2-e1c2-4ba1-a256-1249369dc086/reports/de8e4ae7-de56-4307-9a31-279b6f8f0f24) |
| **TMB WG Stock Order Helper (model input)** | `7d03dc6a-37b7-4faf-bbfb-6cb8af89c92a` | `b5bfbc6e-574a-478d-bcd9-03a52b2aa70f` | [Open Report](https://app.powerbi.com/groups/bab7ddd2-e1c2-4ba1-a256-1249369dc086/reports/7d03dc6a-37b7-4faf-bbfb-6cb8af89c92a) |
| **TMD WG Stock Order Helper (model input)** | `bac075d1-6448-4071-963b-0278a73cf2d3` | `8da0d574-58ee-431e-b764-65b1cb0ef79c` | [Open Report](https://app.powerbi.com/groups/bab7ddd2-e1c2-4ba1-a256-1249369dc086/reports/bac075d1-6448-4071-963b-0278a73cf2d3) |
| **TMEU Inventory Forecast** | `c06bc7bc-51cf-402d-9f3c-b677eafa0473` | `9f00ef86-146e-45c2-8424-fdb6bbde4626` | [Open Report](https://app.powerbi.com/groups/bab7ddd2-e1c2-4ba1-a256-1249369dc086/reports/c06bc7bc-51cf-402d-9f3c-b677eafa0473) |
| **TMU WG Stock Order Helper (model input)** | `9ce9d6ad-e98a-4f09-baa5-bbb3a2e62398` | `57746fbc-5b9a-44b1-9a9b-45dfdd4c62d1` | [Open Report](https://app.powerbi.com/groups/bab7ddd2-e1c2-4ba1-a256-1249369dc086/reports/9ce9d6ad-e98a-4f09-baa5-bbb3a2e62398) |
| **Usage Metrics Report** | `e397f811-c632-4ef3-8b15-d0387a84f5df` | `99cf25b7-e07f-43fa-a0dc-539fdc60dee5` | [Open Report](https://app.powerbi.com/groups/bab7ddd2-e1c2-4ba1-a256-1249369dc086/reports/e397f811-c632-4ef3-8b15-d0387a84f5df) |
| **Report Usage Metrics Report** | `fa484086-80dc-43ed-8e7c-c4d811cdc27a` | `cfc5b550-e550-4398-acdd-a0b053816717` | [Open Report](https://app.powerbi.com/groups/bab7ddd2-e1c2-4ba1-a256-1249369dc086/reports/fa484086-80dc-43ed-8e7c-c4d811cdc27a) |
| **TMU Inventory Forecast** | `3d006a32-4ea9-40e7-a911-e915cfb2fe97` | `2327fe6d-8514-4e9a-a591-39a9d308eb3d` | [Open Report](https://app.powerbi.com/groups/bab7ddd2-e1c2-4ba1-a256-1249369dc086/reports/3d006a32-4ea9-40e7-a911-e915cfb2fe97) |
| **TMEU Inventory Forecast (EDD)** | `40acdbac-1044-4b2a-b952-ee5124267aa2` | `1af8389e-51c5-45e5-bb2e-cb85cabbec1a` | [Open Report](https://app.powerbi.com/groups/bab7ddd2-e1c2-4ba1-a256-1249369dc086/reports/40acdbac-1044-4b2a-b952-ee5124267aa2) |
| **TMB KTI Report** | `e9b89ac7-87e8-40ee-8d70-cd0e60379932` | `cbb167d6-301c-4a54-9bbf-82794c0f09d1` | [Open Report](https://app.powerbi.com/groups/bab7ddd2-e1c2-4ba1-a256-1249369dc086/reports/e9b89ac7-87e8-40ee-8d70-cd0e60379932) |

## 5. Dataflows & Dashboards

*No dataflows or dashboards in this workspace.*

---

## 6. Newcomer Operational Runbook & Notes
- **Primary Contact / Owner**: Refer to workspace access settings in Power BI portal.
- **Troubleshooting**: If a refresh fails in `BI_TMEU Wholegoods`, inspect the failure log under section 3 above and check upstream data gateway connectivity.
