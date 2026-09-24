# Workspace Documentation: BI_TMU_OPSPackage_reports

**Workspace ID**: `2d6a2d00-8f0b-429a-ad52-fcd56c4c4f55`  
**Type**: `Fabric / PowerBI Workspace`  
**Capacity ID**: `70650ed2-f7a2-46df-96e8-8089f25db80e`  
**Description**: No description provided.

---

## 1. Executive Summary & Newcomer Overview

> [!IMPORTANT]
> **TMU Advanced Operations & Aftersales Reports**
> This workspace contains advanced analytical and operational reports for Ukraine (TMU) that provide deeper drill-downs than the standard core OPS Package.

### Key Reports at a Glance
| Report Name | What It Shows |
|:---|:---|
| **AfterSales & PrecisionFarming Sales** | Comprehensive report on TMU aftersales sales activity. |
| **P&L TMU** | Advanced analytical PnL report for TMU. Provides much more financial detail than the standard PnL found in the core OPS package. |
| **P&L AfterSales** | PnL limited exclusively to the Aftersales department. It depends directly on the `P&L TMU` data. |
| **Service KPI** | Internal service KPIs measuring time occupation, efficiency, and revenue-related metrics. |
| **TMU AfterSales RedExcellence KPI** | Specific reports evaluating if TMU will pass the Red Excellence program (CNH's strategic partnering and encouragement initiative). |

This document contains operational and technical details for the **BI_TMU_OPSPackage_reports** workspace. It is designed to give new team members full visibility into key items, data models, report lineage, and refresh schedules.

## 2. Native Fabric Items Inventory

| Item Name | Item Type | Item ID | Description |
| :--- | :--- | :--- | :--- |
| **Service KPI** | `Report` | `a025f836-dbd0-45ce-b170-e6eaf59a20dd` | - |
| **P&L TMU** | `Report` | `075d992d-6c96-425a-8b0d-d8fd0bf4524c` | - |
| **Service Sales** | `Report` | `e64b4582-f90a-42a8-b9de-e382fbd12168` | - |
| **AfterSales & PrecisionFarming Sales** | `Report` | `195e9cb5-5bf7-4450-9e81-675de18cca83` | - |
| **TMU AfterSales RedExcellence KPI** | `Report` | `54d923fa-645f-4cf2-aa04-3e45d82c12c5` | - |
| **Usage Metrics Report** | `Report` | `05d7554a-a21b-4745-980c-fb51f2461dc3` | - |
| **Report Usage Metrics Report** | `Report` | `e95a1f4f-47d6-427c-ae19-0d6b3d13a8ff` | - |
| **P&L AfterSales** | `Report` | `e25c9cc2-35c8-475c-a9d1-24cd08584e6e` | - |
| **Service KPI** | `SemanticModel` | `94cd6e8f-ad0e-407f-bfdc-39ee850717fd` | - |
| **P&L TMU** | `SemanticModel` | `e9574ace-ce2e-42b6-b7b8-05df02acd535` | - |
| **Service Sales** | `SemanticModel` | `099d4b59-0d30-4f4a-9214-493cfcdcb78f` | - |
| **AfterSales & PrecisionFarming Sales** | `SemanticModel` | `b96dc8a7-c059-42f9-b1d8-c7c561768eba` | - |
| **TMU AfterSales RedExcellence KPI** | `SemanticModel` | `afe9f942-1558-408f-af12-89e85bf6fe21` | - |
| **Usage Metrics Report** | `SemanticModel` | `fd8e4334-3286-4313-934b-33d38a1b346a` | - |
| **Report Usage Metrics Model** | `SemanticModel` | `47f72313-b9e5-470d-b32a-dc372055e879` | - |

## 3. Semantic Models (Datasets) & Refresh Schedules

### Semantic Model: Service KPI
- **Dataset ID**: `94cd6e8f-ad0e-407f-bfdc-39ee850717fd`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `08:00` (FLE Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `Web` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/Collaboration/Shared%20Documents/INT_POWERBI_HELPER/TMU/OPSPackage/Service%20Coordinators.xlsx'}`
- Type: `Extension` | Connection: `{'path': 'PowerPlatformDataflows', 'kind': 'PowerPlatformDataflows'}`
- Type: `Sql` | Connection: `{'server': 'cwgz5ola5r6u5e4heu5qw3drgy-zzqhzdizzmcurky2zbgw4gw7la.datawarehouse.fabric.microsoft.com', 'database': 'tmu_bronze_lakehouse'}`


### Semantic Model: P&L TMU
- **Dataset ID**: `e9574ace-ce2e-42b6-b7b8-05df02acd535`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `07:00` (FLE Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `Web` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/Collaboration/Shared%20Documents/INT_POWERBI_HELPER/TMU/OPSPackage/Budget/PNL%20Budget%20Division.xlsx'}`
- Type: `SharePointList` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/collaboration/'}`
- Type: `Sql` | Connection: `{'server': 'cwgz5ola5r6u5e4heu5qw3drgy-zzqhzdizzmcurky2zbgw4gw7la.datawarehouse.fabric.microsoft.com', 'database': 'tmu_bronze_lakehouse'}`


### Semantic Model: Service Sales
- **Dataset ID**: `099d4b59-0d30-4f4a-9214-493cfcdcb78f`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `06:00` (FLE Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `Sql` | Connection: `{'server': 'cwgz5ola5r6u5e4heu5qw3drgy-zzqhzdizzmcurky2zbgw4gw7la.datawarehouse.fabric.microsoft.com', 'database': 'tmu_bronze_lakehouse'}`


### Semantic Model: AfterSales & PrecisionFarming Sales
- **Dataset ID**: `b96dc8a7-c059-42f9-b1d8-c7c561768eba`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `07:00` (FLE Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmu_opspackage_reports', 'database': 'service sales'}`
- Type: `Web` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/Collaboration/Shared%20Documents/INT_POWERBI_HELPER/TMU/OPSPackage/Budget/SP_Budget.xlsx'}`
- Type: `Sql` | Connection: `{'server': 'cwgz5ola5r6u5e4heu5qw3drgy-zzqhzdizzmcurky2zbgw4gw7la.datawarehouse.fabric.microsoft.com', 'database': 'tmu_bronze_lakehouse'}`
- Type: `Sql` | Connection: `{'server': 'cwgz5ola5r6u5e4heu5qw3drgy-zzqhzdizzmcurky2zbgw4gw7la.database.fabric.microsoft.com', 'database': 'tmu assortment budget-2ad254ce-44d5-4c67-9aee-a34267f0a56d'}`


### Semantic Model: TMU AfterSales RedExcellence KPI
- **Dataset ID**: `afe9f942-1558-408f-af12-89e85bf6fe21`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `08:00` (FLE Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmu_opspackage_reports', 'database': 'service sales'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmu_opspackage_reports', 'database': 'service kpi'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmu_opspackage_reports', 'database': 'p&l tmu'}`
- Type: `Sql` | Connection: `{'server': 'cwgz5ola5r6u5e4heu5qw3drgy-zzqhzdizzmcurky2zbgw4gw7la.datawarehouse.fabric.microsoft.com', 'database': 'tmu_bronze_lakehouse'}`


### Semantic Model: Usage Metrics Report
- **Dataset ID**: `fd8e4334-3286-4313-934b-33d38a1b346a`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `04:22` (UTC)

**Connected Data Sources (Lineage)**:
- Type: `Extension` | Connection: `{'path': 'UsageMetricsDataConnector', 'kind': 'UsageMetricsDataConnector'}`


### Semantic Model: Report Usage Metrics Model
- **Dataset ID**: `47f72313-b9e5-470d-b32a-dc372055e879`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `False`
- **Configured By**: `OBaliuta@titanmachinery.ua`

*No refresh schedule configured.*

## 4. Power BI Reports Inventory

| Report Name | Report ID | Dataset ID | Web URL |
| :--- | :--- | :--- | :--- |
| **Service KPI** | `a025f836-dbd0-45ce-b170-e6eaf59a20dd` | `94cd6e8f-ad0e-407f-bfdc-39ee850717fd` | [Open Report](https://app.powerbi.com/groups/2d6a2d00-8f0b-429a-ad52-fcd56c4c4f55/reports/a025f836-dbd0-45ce-b170-e6eaf59a20dd) |
| **P&L TMU** | `075d992d-6c96-425a-8b0d-d8fd0bf4524c` | `e9574ace-ce2e-42b6-b7b8-05df02acd535` | [Open Report](https://app.powerbi.com/groups/2d6a2d00-8f0b-429a-ad52-fcd56c4c4f55/reports/075d992d-6c96-425a-8b0d-d8fd0bf4524c) |
| **Service Sales** | `e64b4582-f90a-42a8-b9de-e382fbd12168` | `099d4b59-0d30-4f4a-9214-493cfcdcb78f` | [Open Report](https://app.powerbi.com/groups/2d6a2d00-8f0b-429a-ad52-fcd56c4c4f55/reports/e64b4582-f90a-42a8-b9de-e382fbd12168) |
| **AfterSales & PrecisionFarming Sales** | `195e9cb5-5bf7-4450-9e81-675de18cca83` | `b96dc8a7-c059-42f9-b1d8-c7c561768eba` | [Open Report](https://app.powerbi.com/groups/2d6a2d00-8f0b-429a-ad52-fcd56c4c4f55/reports/195e9cb5-5bf7-4450-9e81-675de18cca83) |
| **TMU AfterSales RedExcellence KPI** | `54d923fa-645f-4cf2-aa04-3e45d82c12c5` | `afe9f942-1558-408f-af12-89e85bf6fe21` | [Open Report](https://app.powerbi.com/groups/2d6a2d00-8f0b-429a-ad52-fcd56c4c4f55/reports/54d923fa-645f-4cf2-aa04-3e45d82c12c5) |
| **Usage Metrics Report** | `05d7554a-a21b-4745-980c-fb51f2461dc3` | `fd8e4334-3286-4313-934b-33d38a1b346a` | [Open Report](https://app.powerbi.com/groups/2d6a2d00-8f0b-429a-ad52-fcd56c4c4f55/reports/05d7554a-a21b-4745-980c-fb51f2461dc3) |
| **Report Usage Metrics Report** | `e95a1f4f-47d6-427c-ae19-0d6b3d13a8ff` | `47f72313-b9e5-470d-b32a-dc372055e879` | [Open Report](https://app.powerbi.com/groups/2d6a2d00-8f0b-429a-ad52-fcd56c4c4f55/reports/e95a1f4f-47d6-427c-ae19-0d6b3d13a8ff) |
| **P&L AfterSales** | `e25c9cc2-35c8-475c-a9d1-24cd08584e6e` | `e9574ace-ce2e-42b6-b7b8-05df02acd535` | [Open Report](https://app.powerbi.com/groups/2d6a2d00-8f0b-429a-ad52-fcd56c4c4f55/reports/e25c9cc2-35c8-475c-a9d1-24cd08584e6e) |

## 5. Dataflows & Dashboards

*No dataflows or dashboards in this workspace.*

---

## 6. Newcomer Operational Runbook & Notes
- **Primary Contact / Owner**: Refer to workspace access settings in Power BI portal.
- **Troubleshooting**: If a refresh fails in `BI_TMU_OPSPackage_reports`, inspect the failure log under section 3 above and check upstream data gateway connectivity.
