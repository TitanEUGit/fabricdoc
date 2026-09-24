# Workspace Documentation: BI_TMEU_Aftersales

**Workspace ID**: `2c05a4e4-4d2d-483e-be6c-2d0ecdd9f902`  
**Type**: `Fabric / PowerBI Workspace`  
**Capacity ID**: `70650ed2-f7a2-46df-96e8-8089f25db80e`  
**Description**: Workspace for Multi-Country reports related to AfterSales Segment

---

## 1. Executive Summary & Newcomer Overview

> [!IMPORTANT]
> **European Aftersales Reporting**
> This workspace consolidates Aftersales reports for the European scope. 
> **Primary Data Sources:** Data is mainly sourced from the core **ERP systems** and **Frontu** (the CRM used for service workshops).
> **Data Ownership:** The key data owner is the **TMA Aftersales Manager**, who is responsible for deciding all business logic adjustments and approving viewer access.

> [!WARNING]
> **Decommissioning Review**
> All reports in this workspace that currently have an inactive refresh schedule should be considered for decommissioning.

This document contains operational and technical details for the **BI_TMEU_Aftersales** workspace. It is designed to give new team members full visibility into key items, data models, report lineage, and refresh schedules.

## 2. Native Fabric Items Inventory

| Item Name | Item Type | Item ID | Description |
| :--- | :--- | :--- | :--- |
| **SP Supplier Matrix** | `Report` | `0071d275-ff03-4571-acc1-baba66378905` | - |
| **TMEU Open Service Jobcards** | `Report` | `03a3b768-5773-4472-a5e1-f7b8bbaa976f` | - |
| **TMEU Overstocked Parts** | `Report` | `48a67a3d-6318-4069-9a26-9f994bdcebb1` | - |
| **Usage Metrics Report** | `Report` | `78471d8d-6eb4-4541-b8d9-06321355208e` | - |
| **TMEU Parts Item List** | `Report` | `e2d112a1-3a44-4ce5-9bc9-2fe0496e859a` | ⚠️ **Pending Usage Review:** Verify if this report is still actively used (fed by Power Automate `parts_items_translation` flow). |
| **TMEU Warranty Dashboard** | `Report` | `cfdf3f50-f10a-4000-bcbe-cec05722d0d6` | - |
| **SP Supplier Matrix** | `SemanticModel` | `0fc31860-861c-4131-8b73-f785f161b94a` | - |
| **TMEU Open Service Jobcards** | `SemanticModel` | `005f67d8-0096-4be7-85bd-2330fd6648a7` | - |
| **TMEU Overstocked Parts** | `SemanticModel` | `1a51c1d3-0d58-431f-88ec-8006cfe3513e` | - |
| **Usage Metrics Report** | `SemanticModel` | `6b1d9649-7e95-4d0b-ae3e-c97e0a8cf48e` | - |
| **TMEU Parts Item List** | `SemanticModel` | `5faeb973-dc3e-4165-b824-3e0f6abbd850` | ⚠️ **Pending Usage Review** |
| **TMEU Warranty Dashboard** | `SemanticModel` | `b3c3f284-7d05-44c5-89ee-22c1f3a36250` | - |

## 3. Semantic Models (Datasets) & Refresh Schedules

### Semantic Model: SP Supplier Matrix
- **Dataset ID**: `0fc31860-861c-4131-8b73-f785f161b94a`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `07:00` (FLE Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmr_opspackage', 'database': 'tmr ops package'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmb_opspackage', 'database': 'tmb ops package'}`
- Type: `Extension` | Connection: `{'path': 'PowerPlatformDataflows', 'kind': 'PowerPlatformDataflows'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmu_opspackage', 'database': 'tmu ops package'}`


### Semantic Model: TMEU Open Service Jobcards
- **Dataset ID**: `005f67d8-0096-4be7-85bd-2330fd6648a7`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `08:30` (FLE Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `Sql` | Connection: `{'server': '10.75.1.7', 'database': 'jetnavdwh'}`
- Type: `ODBC` | Connection: `{'connectionString': 'dsn=timeline - tmd'}`
- Type: `Web` | Connection: `{'url': 'https://titanmachineryro.frontu.com/'}`
- Type: `Web` | Connection: `{'url': 'https://titanmachinerybg.frontu.com/'}`
- Type: `Sql` | Connection: `{'server': 'cwgz5ola5r6u5e4heu5qw3drgy-zzqhzdizzmcurky2zbgw4gw7la.datawarehouse.fabric.microsoft.com', 'database': 'tmu_bronze_lakehouse'}`


### Semantic Model: TMEU Overstocked Parts
- **Dataset ID**: `1a51c1d3-0d58-431f-88ec-8006cfe3513e`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday
- **Scheduled Times**: `09:00` (FLE Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `Extension` | Connection: `{'path': 'PowerPlatformDataflows', 'kind': 'PowerPlatformDataflows'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmr_opspackage', 'database': 'tmr ops package'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmd_aftersales', 'database': 'tmd parts sales'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmb_opspackage', 'database': 'tmb ops package'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmu_opspackage', 'database': 'tmu ops package'}`


### Semantic Model: Usage Metrics Report
- **Dataset ID**: `6b1d9649-7e95-4d0b-ae3e-c97e0a8cf48e`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `06:25` (UTC)

**Connected Data Sources (Lineage)**:
- Type: `Extension` | Connection: `{'path': 'UsageMetricsDataConnector', 'kind': 'UsageMetricsDataConnector'}`


### Semantic Model: TMEU Parts Item List
- **Dataset ID**: `5faeb973-dc3e-4165-b824-3e0f6abbd850`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Monday
- **Scheduled Times**: `08:00` (UTC)

**Connected Data Sources (Lineage)**:
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmd_aftersales', 'database': 'tmd parts sales'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmr_opspackage', 'database': 'tmr ops package'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmu_opspackage', 'database': 'tmu ops package'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmb_opspackage', 'database': 'tmb ops package'}`


### Semantic Model: TMEU Warranty Dashboard
- **Dataset ID**: `b3c3f284-7d05-44c5-89ee-22c1f3a36250`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `06:00` (FLE Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `Sql` | Connection: `{'server': '10.75.1.7', 'database': 'jetnavdwh'}`


## 4. Power BI Reports Inventory

| Report Name | Report ID | Dataset ID | Web URL |
| :--- | :--- | :--- | :--- |
| **SP Supplier Matrix** | `0071d275-ff03-4571-acc1-baba66378905` | `0fc31860-861c-4131-8b73-f785f161b94a` | [Open Report](https://app.powerbi.com/groups/2c05a4e4-4d2d-483e-be6c-2d0ecdd9f902/reports/0071d275-ff03-4571-acc1-baba66378905) |
| **TMEU Open Service Jobcards** | `03a3b768-5773-4472-a5e1-f7b8bbaa976f` | `005f67d8-0096-4be7-85bd-2330fd6648a7` | [Open Report](https://app.powerbi.com/groups/2c05a4e4-4d2d-483e-be6c-2d0ecdd9f902/reports/03a3b768-5773-4472-a5e1-f7b8bbaa976f) |
| **TMEU Overstocked Parts** | `48a67a3d-6318-4069-9a26-9f994bdcebb1` | `1a51c1d3-0d58-431f-88ec-8006cfe3513e` | [Open Report](https://app.powerbi.com/groups/2c05a4e4-4d2d-483e-be6c-2d0ecdd9f902/reports/48a67a3d-6318-4069-9a26-9f994bdcebb1) |
| **Usage Metrics Report** | `78471d8d-6eb4-4541-b8d9-06321355208e` | `6b1d9649-7e95-4d0b-ae3e-c97e0a8cf48e` | [Open Report](https://app.powerbi.com/groups/2c05a4e4-4d2d-483e-be6c-2d0ecdd9f902/reports/78471d8d-6eb4-4541-b8d9-06321355208e) |
| **TMEU Parts Item List** | `e2d112a1-3a44-4ce5-9bc9-2fe0496e859a` | `5faeb973-dc3e-4165-b824-3e0f6abbd850` | [Open Report](https://app.powerbi.com/groups/2c05a4e4-4d2d-483e-be6c-2d0ecdd9f902/reports/e2d112a1-3a44-4ce5-9bc9-2fe0496e859a) |
| **TMEU Warranty Dashboard** | `cfdf3f50-f10a-4000-bcbe-cec05722d0d6` | `b3c3f284-7d05-44c5-89ee-22c1f3a36250` | [Open Report](https://app.powerbi.com/groups/2c05a4e4-4d2d-483e-be6c-2d0ecdd9f902/reports/cfdf3f50-f10a-4000-bcbe-cec05722d0d6) |

## 5. Dataflows & Dashboards

*No dataflows or dashboards in this workspace.*

---

## 6. Newcomer Operational Runbook & Notes
- **Primary Contact / Owner**: Refer to workspace access settings in Power BI portal.
- **Troubleshooting**: If a refresh fails in `BI_TMEU_Aftersales`, inspect the failure log under section 3 above and check upstream data gateway connectivity.
