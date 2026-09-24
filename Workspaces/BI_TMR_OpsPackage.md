# Workspace Documentation: BI_TMR_OpsPackage

**Workspace ID**: `a64c7035-492e-478a-87ef-6ebf6030e151`  
**Type**: `Fabric / PowerBI Workspace`  
**Capacity ID**: `70650ed2-f7a2-46df-96e8-8089f25db80e`  
**Description**: No description provided.

---

## 1. Executive Summary & Newcomer Overview

> [!IMPORTANT]
> **Core Country Operations Report (Romania)**
> This workspace houses the primary **TMR OPS Package report**, which is the business-critical operations dashboard for Romania. 
> - **Primary Data Source:** Legacy `JetDWH` data warehouse maintained by Arggo.
> - **Manual Adjustments:** Pulls from dedicated `TMR OPS Package Helpers` dataflows (Parts 1 & 2, located in the `DS_TMEU_Datasets and Dataflows` workspace) for manual user overrides.

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
- Type: `Sql` | Connection: `{'server': '10.75.1.7', 'database': 'jetnavdwh'}` — *Legacy JetDWH data warehouse (primary ERP source)*
- Type: `Extension` | Connection: `{'path': 'titanromania.crm4.dynamics.com', 'kind': 'CommonDataService'}`
- Type: `Extension` | Connection: `{'path': 'PowerPlatformDataflows', 'kind': 'PowerPlatformDataflows'}` — *TMR OPS Package Helpers dataflows Part 1 & 2 (manual adjustments)*
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/int_orderbook', 'database': 'tmeu order book'}`
- Type: `Sql` | Connection: `{'server': 'cwgz5ola5r6u5e4heu5qw3drgy-zzqhzdizzmcurky2zbgw4gw7la.datawarehouse.fabric.microsoft.com', 'database': 'tmeu_bronze_lakehouse'}`
- Type: `Sql` | Connection: `{'server': 'cwgz5ola5r6u5e4heu5qw3drgy-zzqhzdizzmcurky2zbgw4gw7la.datawarehouse.fabric.microsoft.com', 'database': 'tmeu_erp_raw_lakehouse'}`


## 4. Power BI Reports Inventory

| Report Name | Report ID | Dataset ID | Web URL |
| :--- | :--- | :--- | :--- |
| **TMR OPS Package** | `fe403e56-3512-4ecc-b674-eefbe3f9908a` | `84c66778-4a62-413e-bc56-cefbaeddb68e` | [Open Report](https://app.powerbi.com/groups/a64c7035-492e-478a-87ef-6ebf6030e151/reports/fe403e56-3512-4ecc-b674-eefbe3f9908a) |

## 5. Dataflows & Dashboards

*No dataflows or dashboards in this workspace.*

---

## 6. Newcomer Operational Runbook & Notes
- **Primary Contact / Owner**: Refer to workspace access settings in Power BI portal.
- **Troubleshooting (Refresh Failures)**: If a refresh fails in `BI_TMR_OpsPackage`, inspect the failure log under section 3 above and check upstream data gateway connectivity.
- **Troubleshooting (Missing P&L Accounts)**: If the finance team reports that a newly added account is not showing up in the P&L, it most likely needs to be manually added to the Power Query steps within the report, specifically for the **'Finance Transactions'** table.
