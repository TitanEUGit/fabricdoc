# Workspace Documentation: BI_EOC_Parts_Dashboard

**Workspace ID**: `0276ac15-c83c-4db6-a4b7-cfc272559958`  
**Type**: `Fabric / PowerBI Workspace`  
**Capacity ID**: `70650ed2-f7a2-46df-96e8-8089f25db80e`  
**Description**: No description provided.

---

## 1. Executive Summary & Newcomer Overview
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

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2026-09-15 05:30:26 | 2026-09-15 05:42:51 | `Completed` | `Scheduled` | - |
| 2026-09-14 05:31:21 | 2026-09-14 05:43:52 | `Completed` | `Scheduled` | - |
| 2026-09-13 05:31:10 | 2026-09-13 05:38:59 | `Completed` | `Scheduled` | - |
| 2026-09-12 05:31:21 | 2026-09-12 05:43:47 | `Completed` | `Scheduled` | - |
| 2026-09-11 05:31:19 | 2026-09-11 05:43:10 | `Completed` | `Scheduled` | - |

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

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2026-09-15 06:01:01 | 2026-09-15 06:03:57 | `Completed` | `Scheduled` | - |
| 2026-09-14 06:00:27 | 2026-09-14 06:06:24 | `Completed` | `Scheduled` | - |
| 2026-09-13 06:01:08 | 2026-09-13 06:06:13 | `Completed` | `Scheduled` | - |
| 2026-09-12 06:01:08 | 2026-09-12 06:07:03 | `Completed` | `Scheduled` | - |
| 2026-09-11 06:01:02 | 2026-09-11 06:04:12 | `Completed` | `Scheduled` | - |

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

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2026-09-15 06:01:05 | 2026-09-15 06:03:15 | `Completed` | `Scheduled` | - |
| 2026-09-14 06:00:12 | 2026-09-14 06:01:53 | `Completed` | `Scheduled` | - |
| 2026-09-13 06:01:13 | 2026-09-13 06:05:01 | `Completed` | `Scheduled` | - |
| 2026-09-12 06:01:15 | 2026-09-12 06:05:45 | `Completed` | `Scheduled` | - |
| 2026-09-11 06:01:08 | 2026-09-11 06:03:10 | `Completed` | `Scheduled` | - |

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

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2026-09-15 06:01:09 | 2026-09-15 06:06:35 | `Completed` | `Scheduled` | - |
| 2026-09-14 06:00:30 | 2026-09-14 06:05:13 | `Completed` | `Scheduled` | - |
| 2026-09-13 06:01:06 | 2026-09-13 06:04:49 | `Completed` | `Scheduled` | - |
| 2026-09-12 06:01:06 | 2026-09-12 06:05:43 | `Completed` | `Scheduled` | - |
| 2026-09-11 06:01:13 | 2026-09-11 06:05:04 | `Completed` | `Scheduled` | - |

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

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2026-09-15 06:30:25 | 2026-09-15 06:37:17 | `Completed` | `Scheduled` | - |
| 2026-09-14 06:31:17 | 2026-09-14 06:38:20 | `Completed` | `Scheduled` | - |
| 2026-09-13 06:31:15 | 2026-09-13 06:38:37 | `Completed` | `Scheduled` | - |
| 2026-09-12 06:31:19 | 2026-09-12 06:38:32 | `Completed` | `Scheduled` | - |
| 2026-09-11 06:31:12 | 2026-09-11 06:35:23 | `Completed` | `Scheduled` | - |

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

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2025-07-21 08:32:13 | 2025-07-21 08:32:13 | `Disabled` | `Scheduled` | - |
| 2025-07-20 08:32:13 | 2025-07-20 08:45:08 | `Completed` | `Scheduled` | - |
| 2025-07-19 08:32:20 | 2025-07-19 08:45:35 | `Completed` | `Scheduled` | - |
| 2025-07-18 08:32:10 | 2025-07-18 08:45:41 | `Completed` | `Scheduled` | - |
| 2025-07-17 08:32:14 | 2025-07-17 08:44:51 | `Completed` | `Scheduled` | - |

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
