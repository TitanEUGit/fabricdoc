# Workspace Documentation: BI_EOC_Parts_Dashboard

**Workspace ID**: `0276ac15-c83c-4db6-a4b7-cfc272559958`  
**Type**: `Fabric / PowerBI Workspace`  
**Capacity ID**: `70650ed2-f7a2-46df-96e8-8089f25db80e`  
**Description**: No description provided.

---

## 1. Executive Summary & Newcomer Overview

> [!IMPORTANT]
> **Core Domain Dashboard (Parts)**
> This workspace houses one of the most critical domain-specific dashboards in the environment. It contains highly summarized Parts data that is heavily utilized by both **country-level management** and **TMA (Austria HQ) domain managers** for strategic oversight and decision-making.

This document contains operational and technical details for the **BI_EOC_Parts_Dashboard** workspace. It is designed to give new team members full visibility into key items, data models, report lineage, and refresh schedules.

## 2. Native Fabric Items Inventory

| Item Name | Item Type | Item ID | Description |
| :--- | :--- | :--- | :--- |
| **TMR Parts Dashboard** | `Report` | `0cc3d10a-cff3-405c-83c9-a8adfc78ff6d` | - |
| **TMB Parts Dashboard** | `Report` | `8e13a54b-0896-4bc3-aa55-c4dbceb60376` | - |
| **TMD Parts Dashboard** | `Report` | `1588bb59-0075-4957-b3fa-2d369a258c57` | - |
| **TMU Parts Dashboard** | `Report` | `ba56cf26-603c-4e36-9b8a-e36477fe70ed` | - |
| **TMEU Summary Parts Dashboard** | `Report` | `4c128de1-4e8d-4356-8d39-7d550f85321d` | - |
| **Usage Metrics Report** | `Report` | `d1f9f608-cd4e-4bbc-9ed1-778986435282` | - |
| **TMR Parts Dashboard** | `SemanticModel` | `a2dee8dd-a060-4289-a75f-3a49de2f6127` | - |
| **TMB Parts Dashboard** | `SemanticModel` | `9a90fe75-6c0b-4390-b39a-7ef6135a7bcf` | - |
| **TMD Parts Dashboard** | `SemanticModel` | `95925f55-ef55-4919-977b-48741d236856` | - |
| **TMU Parts Dashboard** | `SemanticModel` | `cf6c9900-8f7d-4086-b0aa-3aadf193527c` | - |
| **TMEU Summary Parts Dashboard** | `SemanticModel` | `e9dc8b7f-ca7f-42eb-beab-d93ea8b1adba` | - |
| **Usage Metrics Report** | `SemanticModel` | `6412b717-c799-432c-b745-9ea5b75dacc6` | - |

## 3. Semantic Models (Datasets) & Refresh Schedules

### Semantic Model: TMR Parts Dashboard
- **Dataset ID**: `a2dee8dd-a060-4289-a75f-3a49de2f6127`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `08:30` (FLE Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/ds_tmeu_datasets and dataflows', 'database': 'tmeu_hc_dataset'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/ds_tmeu_datasets and dataflows', 'database': 'tmeu parts inventory staging'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmr_opspackage', 'database': 'tmr ops package'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/ds_tmeu_datasets and dataflows', 'database': 'tmr headcount file'}`
- Type: `Web` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/Collaboration/Shared%20Documents/INT_POWERBI_HELPER/TMR/Parts_dashboard/parts_dashboard_budget_title.xlsx'}`
- Type: `Web` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/Collaboration/Shared%20Documents/INT_POWERBI_HELPER/EOC/TMEU_Parts_dashboard_turnrates.xlsx'}`
- Type: `Extension` | Connection: `{'path': 'PowerPlatformDataflows', 'kind': 'PowerPlatformDataflows'}`


### Semantic Model: TMB Parts Dashboard
- **Dataset ID**: `9a90fe75-6c0b-4390-b39a-7ef6135a7bcf`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `09:00` (FLE Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/ds_tmeu_datasets and dataflows', 'database': 'tmr headcount file'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/ds_tmeu_datasets and dataflows', 'database': 'tmeu_hc_dataset'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmb_opspackage', 'database': 'tmb ops package'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/ds_tmeu_datasets and dataflows', 'database': 'tmeu parts inventory staging'}`
- Type: `Web` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/Collaboration/Shared%20Documents/INT_POWERBI_HELPER/TMB/Parts_dashboard/parts_dashboard_budget_title.xlsx'}`
- Type: `Web` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/Collaboration/Shared%20Documents/INT_POWERBI_HELPER/EOC/TMEU_Parts_dashboard_turnrates.xlsx'}`
- Type: `Extension` | Connection: `{'path': 'PowerPlatformDataflows', 'kind': 'PowerPlatformDataflows'}`


### Semantic Model: TMD Parts Dashboard
- **Dataset ID**: `95925f55-ef55-4919-977b-48741d236856`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `09:00` (FLE Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/ds_tmeu_datasets and dataflows', 'database': 'tmeu parts inventory staging'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/ds_tmeu_datasets and dataflows', 'database': 'tmeu_hc_dataset'}`
- Type: `Web` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/Collaboration/Shared%20Documents/INT_POWERBI_HELPER/TMD/Parts_dashboard/parts_dashboard_budget_title.xlsx'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmd_aftersales', 'database': 'tmd parts sales'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmd_aftersales', 'database': 'tmd service kpi new'}`
- Type: `Web` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/Collaboration/Shared%20Documents/INT_POWERBI_HELPER/EOC/TMEU_Parts_dashboard_turnrates.xlsx'}`
- Type: `Extension` | Connection: `{'path': 'PowerPlatformDataflows', 'kind': 'PowerPlatformDataflows'}`


### Semantic Model: TMU Parts Dashboard
- **Dataset ID**: `cf6c9900-8f7d-4086-b0aa-3aadf193527c`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `09:00` (FLE Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/ds_tmeu_datasets and dataflows', 'database': 'tmeu_hc_dataset'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmu_opspackage', 'database': 'tmu ops package'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/ds_tmeu_datasets and dataflows', 'database': 'tmeu parts inventory staging'}`
- Type: `Web` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/Collaboration/Shared%20Documents/INT_POWERBI_HELPER/TMU/Parts_dashboard/parts_dashboard_budget_title.xlsx'}`
- Type: `Web` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/Collaboration/Shared%20Documents/INT_POWERBI_HELPER/EOC/TMEU_Parts_dashboard_turnrates.xlsx'}`
- Type: `Extension` | Connection: `{'path': 'PowerPlatformDataflows', 'kind': 'PowerPlatformDataflows'}`


### Semantic Model: TMEU Summary Parts Dashboard
- **Dataset ID**: `e9dc8b7f-ca7f-42eb-beab-d93ea8b1adba`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `09:30` (FLE Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_eoc_parts_dashboard', 'database': 'tmb parts dashboard'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_eoc_parts_dashboard', 'database': 'tmd parts dashboard'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_eoc_parts_dashboard', 'database': 'tmr parts dashboard'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_eoc_parts_dashboard', 'database': 'tmu parts dashboard'}`


### Semantic Model: Usage Metrics Report
- **Dataset ID**: `6412b717-c799-432c-b745-9ea5b75dacc6`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `08:32` (UTC)

**Connected Data Sources (Lineage)**:
- Type: `Extension` | Connection: `{'path': 'UsageMetricsDataConnector', 'kind': 'UsageMetricsDataConnector'}`


## 4. Power BI Reports Inventory

| Report Name | Report ID | Dataset ID | Web URL |
| :--- | :--- | :--- | :--- |
| **TMR Parts Dashboard** | `0cc3d10a-cff3-405c-83c9-a8adfc78ff6d` | `a2dee8dd-a060-4289-a75f-3a49de2f6127` | [Open Report](https://app.powerbi.com/groups/0276ac15-c83c-4db6-a4b7-cfc272559958/reports/0cc3d10a-cff3-405c-83c9-a8adfc78ff6d) |
| **TMB Parts Dashboard** | `8e13a54b-0896-4bc3-aa55-c4dbceb60376` | `9a90fe75-6c0b-4390-b39a-7ef6135a7bcf` | [Open Report](https://app.powerbi.com/groups/0276ac15-c83c-4db6-a4b7-cfc272559958/reports/8e13a54b-0896-4bc3-aa55-c4dbceb60376) |
| **TMD Parts Dashboard** | `1588bb59-0075-4957-b3fa-2d369a258c57` | `95925f55-ef55-4919-977b-48741d236856` | [Open Report](https://app.powerbi.com/groups/0276ac15-c83c-4db6-a4b7-cfc272559958/reports/1588bb59-0075-4957-b3fa-2d369a258c57) |
| **TMU Parts Dashboard** | `ba56cf26-603c-4e36-9b8a-e36477fe70ed` | `cf6c9900-8f7d-4086-b0aa-3aadf193527c` | [Open Report](https://app.powerbi.com/groups/0276ac15-c83c-4db6-a4b7-cfc272559958/reports/ba56cf26-603c-4e36-9b8a-e36477fe70ed) |
| **TMEU Summary Parts Dashboard** | `4c128de1-4e8d-4356-8d39-7d550f85321d` | `e9dc8b7f-ca7f-42eb-beab-d93ea8b1adba` | [Open Report](https://app.powerbi.com/groups/0276ac15-c83c-4db6-a4b7-cfc272559958/reports/4c128de1-4e8d-4356-8d39-7d550f85321d) |
| **Usage Metrics Report** | `d1f9f608-cd4e-4bbc-9ed1-778986435282` | `6412b717-c799-432c-b745-9ea5b75dacc6` | [Open Report](https://app.powerbi.com/groups/0276ac15-c83c-4db6-a4b7-cfc272559958/reports/d1f9f608-cd4e-4bbc-9ed1-778986435282) |

## 5. Dataflows & Dashboards

*No dataflows or dashboards in this workspace.*

---

## 6. Newcomer Operational Runbook & Notes
- **Primary Contact / Owner**: Refer to workspace access settings in Power BI portal.
- **Troubleshooting**: If a refresh fails in `BI_EOC_Parts_Dashboard`, inspect the failure log under section 3 above and check upstream data gateway connectivity.
