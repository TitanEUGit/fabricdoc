# Workspace Documentation: BI_EOC_Sales_Dashboard

**Workspace ID**: `e726a8ce-cda6-4df9-b5ed-eb36db3571e5`  
**Type**: `Fabric / PowerBI Workspace`  
**Capacity ID**: `70650ed2-f7a2-46df-96e8-8089f25db80e`  
**Description**: No description provided.

---

## 1. Executive Summary & Newcomer Overview

> [!IMPORTANT]
> **Core Domain Dashboard (Sales)**
> This workspace houses one of the most critical domain-specific dashboards in the environment. It contains highly summarized Sales data that is heavily utilized by both **country-level management** and **TMA (Austria HQ) domain managers** for strategic oversight and decision-making.

This document contains operational and technical details for the **BI_EOC_Sales_Dashboard** workspace. It is designed to give new team members full visibility into key items, data models, report lineage, and refresh schedules.

## 2. Native Fabric Items Inventory

| Item Name | Item Type | Item ID | Description |
| :--- | :--- | :--- | :--- |
| **TMB Sales Dashboard** | `Report` | `fbb332fe-fa0f-49ad-9544-30279cd91422` | - |
| **TMD Sales Dashboard** | `Report` | `0a257575-b366-4db0-b0fc-8c4fc14bc909` | - |
| **TMR Sales Dashboard** | `Report` | `926fb5ba-4c05-4e29-973b-33eac9dd176e` | - |
| **TMU Sales Dashboard** | `Report` | `dec0c9db-c528-46a9-99f3-98a9b4f40bc9` | - |
| **Usage Metrics Report** | `Report` | `b322f3cc-e051-4135-8cc6-4b47ad445795` | - |
| **TMB Sales Dashboard** | `SemanticModel` | `61b0271c-fddf-4d37-bfe5-1296117a26a1` | - |
| **TMD Sales Dashboard** | `SemanticModel` | `b38619ee-4e3e-40f1-9c50-142eb78e297e` | - |
| **TMR Sales Dashboard** | `SemanticModel` | `93f283a6-44d5-4b26-9187-109886419f3a` | - |
| **TMU Sales Dashboard** | `SemanticModel` | `790817e9-b7d1-4d74-a7a4-7e75b0cb0b72` | - |
| **Usage Metrics Report** | `SemanticModel` | `a6c9e921-4a74-4ed0-80c4-60a8b90d5416` | - |

## 3. Semantic Models (Datasets) & Refresh Schedules

### Semantic Model: TMB Sales Dashboard
- **Dataset ID**: `61b0271c-fddf-4d37-bfe5-1296117a26a1`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `07:00` (FLE Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/ds_tmeu_datasets and dataflows', 'database': 'tmeu tiv and ms'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmeu_inventorybook', 'database': 'tmeu inventory book'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmb_opspackage', 'database': 'tmb ops package'}`
- Type: `Web` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/Collaboration/Shared%20Documents/INT_POWERBI_HELPER/TMR/Sales_dashboard/sales_dashboard_budget_title.xlsx'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/ds_tmeu_datasets and dataflows', 'database': 'tmeu_hc_dataset'}`
- Type: `Web` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/Collaboration/Shared%20Documents/INT_POWERBI_HELPER/TMB/Sales_dashboard/sales_dashboard_budget_title.xlsx'}`
- Type: `Web` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/Collaboration/Shared%20Documents/INT_POWERBI_HELPER/EOC/TMEU_Sales_dashboard_fin_inputs.xlsx'}`


### Semantic Model: TMD Sales Dashboard
- **Dataset ID**: `b38619ee-4e3e-40f1-9c50-142eb78e297e`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `07:00` (FLE Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmd_crm', 'database': 'tmd crm'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmeu_inventorybook', 'database': 'tmeu inventory book'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/ds_tmeu_datasets and dataflows', 'database': 'tmd pa history'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmd_sales', 'database': 'tmd wg sales'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/ds_tmeu_datasets and dataflows', 'database': 'tmeu_hc_dataset'}`
- Type: `Web` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/Collaboration/Shared%20Documents/INT_POWERBI_HELPER/TMD/Sales_dashboard/sales_dashboard_budget_title.xlsx'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/ds_tmeu_datasets and dataflows', 'database': 'tmeu tiv and ms'}`
- Type: `Web` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/Collaboration/Shared%20Documents/INT_POWERBI_HELPER/EOC/TMEU_Sales_dashboard_fin_inputs.xlsx'}`


### Semantic Model: TMR Sales Dashboard
- **Dataset ID**: `93f283a6-44d5-4b26-9187-109886419f3a`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `07:00` (GTB Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmr_crm', 'database': 'tmr crm'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/ds_tmeu_datasets and dataflows', 'database': 'tmeu tiv and ms'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmr_opspackage', 'database': 'tmr ops package'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/ds_tmeu_datasets and dataflows', 'database': 'tmeu_hc_dataset'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/ds_tmeu_datasets and dataflows', 'database': 'tmr pa history'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmeu_inventorybook', 'database': 'tmeu inventory book'}`
- Type: `Web` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/Collaboration/Shared%20Documents/INT_POWERBI_HELPER/TMR/Sales_dashboard/sales_dashboard_budget_title.xlsx'}`
- Type: `Web` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/Collaboration/Shared%20Documents/INT_POWERBI_HELPER/EOC/TMEU_Sales_dashboard_fin_inputs.xlsx'}`


### Semantic Model: TMU Sales Dashboard
- **Dataset ID**: `790817e9-b7d1-4d74-a7a4-7e75b0cb0b72`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `07:00` (GTB Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmu_crm', 'database': 'tmu crm'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmeu_inventorybook', 'database': 'tmeu inventory book'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmu_opspackage', 'database': 'tmu ops package'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/ds_tmeu_datasets and dataflows', 'database': 'tmu pa history'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/ds_tmeu_datasets and dataflows', 'database': 'tmeu tiv and ms'}`
- Type: `Web` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/Collaboration/Shared%20Documents/INT_POWERBI_HELPER/TMU/Sales_dashboard/sales_dashboard_budget_title.xlsx'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/ds_tmeu_datasets and dataflows', 'database': 'tmeu_hc_dataset'}`
- Type: `Web` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/Collaboration/Shared%20Documents/INT_POWERBI_HELPER/EOC/TMEU_Sales_dashboard_fin_inputs.xlsx'}`


### Semantic Model: Usage Metrics Report
- **Dataset ID**: `a6c9e921-4a74-4ed0-80c4-60a8b90d5416`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `00:45` (UTC)

**Connected Data Sources (Lineage)**:
- Type: `Extension` | Connection: `{'path': 'UsageMetricsDataConnector', 'kind': 'UsageMetricsDataConnector'}`


## 4. Power BI Reports Inventory

| Report Name | Report ID | Dataset ID | Web URL |
| :--- | :--- | :--- | :--- |
| **TMB Sales Dashboard** | `fbb332fe-fa0f-49ad-9544-30279cd91422` | `61b0271c-fddf-4d37-bfe5-1296117a26a1` | [Open Report](https://app.powerbi.com/groups/e726a8ce-cda6-4df9-b5ed-eb36db3571e5/reports/fbb332fe-fa0f-49ad-9544-30279cd91422) |
| **TMD Sales Dashboard** | `0a257575-b366-4db0-b0fc-8c4fc14bc909` | `b38619ee-4e3e-40f1-9c50-142eb78e297e` | [Open Report](https://app.powerbi.com/groups/e726a8ce-cda6-4df9-b5ed-eb36db3571e5/reports/0a257575-b366-4db0-b0fc-8c4fc14bc909) |
| **TMR Sales Dashboard** | `926fb5ba-4c05-4e29-973b-33eac9dd176e` | `93f283a6-44d5-4b26-9187-109886419f3a` | [Open Report](https://app.powerbi.com/groups/e726a8ce-cda6-4df9-b5ed-eb36db3571e5/reports/926fb5ba-4c05-4e29-973b-33eac9dd176e) |
| **TMU Sales Dashboard** | `dec0c9db-c528-46a9-99f3-98a9b4f40bc9` | `790817e9-b7d1-4d74-a7a4-7e75b0cb0b72` | [Open Report](https://app.powerbi.com/groups/e726a8ce-cda6-4df9-b5ed-eb36db3571e5/reports/dec0c9db-c528-46a9-99f3-98a9b4f40bc9) |
| **Usage Metrics Report** | `b322f3cc-e051-4135-8cc6-4b47ad445795` | `a6c9e921-4a74-4ed0-80c4-60a8b90d5416` | [Open Report](https://app.powerbi.com/groups/e726a8ce-cda6-4df9-b5ed-eb36db3571e5/reports/b322f3cc-e051-4135-8cc6-4b47ad445795) |

## 5. Dataflows & Dashboards

*No dataflows or dashboards in this workspace.*

---

## 6. Newcomer Operational Runbook & Notes
- **Primary Contact / Owner**: Refer to workspace access settings in Power BI portal.
- **Troubleshooting**: If a refresh fails in `BI_EOC_Sales_Dashboard`, inspect the failure log under section 3 above and check upstream data gateway connectivity.
