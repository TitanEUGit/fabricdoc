# Workspace Documentation: BI_TMEU_InventoryBook

**Workspace ID**: `6ed1481d-5b50-4e9e-a5f0-6c1868960eee`  
**Type**: `Fabric / PowerBI Workspace`  
**Capacity ID**: `70650ed2-f7a2-46df-96e8-8089f25db80e`  
**Description**: Workspace for our Inventory tracking accross Europe.

---

## 1. Executive Summary & Newcomer Overview

> [!WARNING]
> **Deprecated Workspace (Pending Decommissioning)**
> This workspace contains the legacy report on Wholegoods (WG) inventory, which was previously manually maintained by the TMA WG team. 
> - **TMA WG team was disbanded in Aug 2026**, and the teams tasks were partially handed over to country managers and/or automated.
> - **As of Sep 2026**, direct ERP-based successors to these reports are in the final stages of evaluation.
> - **Recommendation:** This workspace is deprecated. Consider decommissioning and deleting it once the successors are fully approved.

This document contains operational and technical details for the **BI_TMEU_InventoryBook** workspace. It is designed to give new team members full visibility into key items, data models, report lineage, and refresh schedules.

## 2. Native Fabric Items Inventory

| Item Name | Item Type | Item ID | Description |
| :--- | :--- | :--- | :--- |
| **TMEU Inventory Book** | `Report` | `bcdb20df-1c35-44a1-be48-8009d68239e6` | - |
| **Report Usage Metrics Report** | `Report` | `0c9c1ab0-b7e8-4b29-9cd7-9ec727b6f904` | - |
| **Usage Metrics Report** | `Report` | `1c79cf26-c409-417d-bf03-257256ae1a07` | - |
| **Inventory Book Value on Aged** | `Report` | `2ca98cab-3965-4ed1-8a6b-bc8695785110` | - |
| **TMEU Inventory Book** | `SemanticModel` | `efdfa2d7-db45-41fc-b60f-4af20f293e5f` | - |
| **Report Usage Metrics Model** | `SemanticModel` | `11b91048-04e6-48fe-bc7b-30bb30c9dd62` | - |
| **Usage Metrics Report** | `SemanticModel` | `ecb50ee4-c1bc-48a1-b62f-d5030e5bc1d2` | - |

## 3. Semantic Models (Datasets) & Refresh Schedules

### Semantic Model: TMEU Inventory Book
- **Dataset ID**: `efdfa2d7-db45-41fc-b60f-4af20f293e5f`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `!TMATVDOB@titanmachinery.net`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `01:00` (W. Europe Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `Sql` | Connection: `{'server': 'tmweupautosql01.database.windows.net', 'database': 'tmweu_reporting_db'}`


### Semantic Model: Report Usage Metrics Model
- **Dataset ID**: `11b91048-04e6-48fe-bc7b-30bb30c9dd62`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `False`
- **Configured By**: `N/A`

*No refresh schedule configured.*

### Semantic Model: Usage Metrics Report
- **Dataset ID**: `ecb50ee4-c1bc-48a1-b62f-d5030e5bc1d2`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `11:54` (UTC)

**Connected Data Sources (Lineage)**:
- Type: `Extension` | Connection: `{'path': 'UsageMetricsDataConnector', 'kind': 'UsageMetricsDataConnector'}`


## 4. Power BI Reports Inventory

| Report Name | Report ID | Dataset ID | Web URL |
| :--- | :--- | :--- | :--- |
| **TMEU Inventory Book** | `bcdb20df-1c35-44a1-be48-8009d68239e6` | `efdfa2d7-db45-41fc-b60f-4af20f293e5f` | [Open Report](https://app.powerbi.com/groups/6ed1481d-5b50-4e9e-a5f0-6c1868960eee/reports/bcdb20df-1c35-44a1-be48-8009d68239e6) |
| **Report Usage Metrics Report** | `0c9c1ab0-b7e8-4b29-9cd7-9ec727b6f904` | `11b91048-04e6-48fe-bc7b-30bb30c9dd62` | [Open Report](https://app.powerbi.com/groups/6ed1481d-5b50-4e9e-a5f0-6c1868960eee/reports/0c9c1ab0-b7e8-4b29-9cd7-9ec727b6f904) |
| **Usage Metrics Report** | `1c79cf26-c409-417d-bf03-257256ae1a07` | `ecb50ee4-c1bc-48a1-b62f-d5030e5bc1d2` | [Open Report](https://app.powerbi.com/groups/6ed1481d-5b50-4e9e-a5f0-6c1868960eee/reports/1c79cf26-c409-417d-bf03-257256ae1a07) |
| **Inventory Book Value on Aged** | `2ca98cab-3965-4ed1-8a6b-bc8695785110` | `efdfa2d7-db45-41fc-b60f-4af20f293e5f` | [Open Report](https://app.powerbi.com/groups/6ed1481d-5b50-4e9e-a5f0-6c1868960eee/reports/2ca98cab-3965-4ed1-8a6b-bc8695785110) |

## 5. Dataflows & Dashboards

*No dataflows or dashboards in this workspace.*

---

## 6. Newcomer Operational Runbook & Notes
- **Primary Contact / Owner**: Refer to workspace access settings in Power BI portal.
- **Troubleshooting**: If a refresh fails in `BI_TMEU_InventoryBook`, inspect the failure log under section 3 above and check upstream data gateway connectivity.
