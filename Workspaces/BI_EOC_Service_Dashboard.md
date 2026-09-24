# Workspace Documentation: BI_EOC_Service_Dashboard

**Workspace ID**: `39febb80-095b-45f7-9902-b53b1718f1f1`  
**Type**: `Fabric / PowerBI Workspace`  
**Capacity ID**: `70650ed2-f7a2-46df-96e8-8089f25db80e`  
**Description**: No description provided.

---

## 1. Executive Summary & Newcomer Overview

> [!IMPORTANT]
> **Core Domain Dashboard (Service)**
> This workspace houses one of the most critical domain-specific dashboards in the environment. It contains highly summarized Service data that is heavily utilized by both **country-level management** and **TMA (Austria HQ) domain managers** for strategic oversight and decision-making.

This document contains operational and technical details for the **BI_EOC_Service_Dashboard** workspace. It is designed to give new team members full visibility into key items, data models, report lineage, and refresh schedules.

## 2. Native Fabric Items Inventory

| Item Name | Item Type | Item ID | Description |
| :--- | :--- | :--- | :--- |
| **TMB Service Dashboard** | `Report` | `d56f0fe0-f49f-4e2b-ac23-8c4833785cc6` | - |
| **TMD Service Dashboard** | `Report` | `dfe5edef-923c-44eb-8e6f-9a86c05c687e` | - |
| **TMR Service Dashboard** | `Report` | `df009c42-d1f6-41dc-9983-7f0d96fe57a9` | - |
| **TMU Service Dashboard** | `Report` | `8a223695-c326-4a9f-be88-928a436fc151` | - |
| **Report Usage Metrics Report** | `Report` | `4879d7d3-e7ca-4f88-8fdd-4be665ed014a` | - |
| **Usage Metrics Report** | `Report` | `64578c78-e834-4480-adb1-bd229d3ab70a` | - |
| **TMEU Summary Service Dashboard** | `Report` | `25c1c339-2a80-40e4-8332-a298d0560a10` | - |
| **TMB Service Dashboard** | `SemanticModel` | `5873cd03-368b-4914-b4d3-17814326433d` | - |
| **TMD Service Dashboard** | `SemanticModel` | `9881dc85-86e2-4e89-b3a5-d517a3df3d1f` | - |
| **TMR Service Dashboard** | `SemanticModel` | `69fc80c3-0b92-47c4-8cda-2a46efd0e8cc` | - |
| **TMU Service Dashboard** | `SemanticModel` | `c5b76d01-1ccd-4b97-9222-1b3cc6bce725` | - |
| **Report Usage Metrics Model** | `SemanticModel` | `ab195926-4696-458d-90a4-fcbffdc339c0` | - |
| **Usage Metrics Report** | `SemanticModel` | `16126703-abc9-4f31-b06a-03bcc46c291e` | - |
| **TMEU Summary Service Dashboard** | `SemanticModel` | `8aa29f08-ee09-4ba0-8908-ff33ecd65cb2` | - |

## 3. Semantic Models (Datasets) & Refresh Schedules

### Semantic Model: TMB Service Dashboard
- **Dataset ID**: `5873cd03-368b-4914-b4d3-17814326433d`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `10:00` (FLE Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmb_opspackage', 'database': 'tmb ops package'}`
- Type: `Web` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/Collaboration/Shared%20Documents/INT_POWERBI_HELPER/TMB/Service_dashboard/service_dashboard_budget_title.xlsx'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmeu_aftersales', 'database': 'tmeu open service jobcards'}`


### Semantic Model: TMD Service Dashboard
- **Dataset ID**: `9881dc85-86e2-4e89-b3a5-d517a3df3d1f`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `10:00` (FLE Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmd_aftersales', 'database': 'tmd service kpi new'}`
- Type: `Web` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/Collaboration/Shared%20Documents/INT_POWERBI_HELPER/TMD/Service_dashboard/service_dashboard_budget_title.xlsx'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmeu_aftersales', 'database': 'tmeu open service jobcards'}`


### Semantic Model: TMR Service Dashboard
- **Dataset ID**: `69fc80c3-0b92-47c4-8cda-2a46efd0e8cc`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `10:00` (FLE Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmr_opspackage', 'database': 'tmr ops package'}`
- Type: `Web` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/Collaboration/Shared%20Documents/INT_POWERBI_HELPER/TMR/Service_dashboard/service_dashboard_budget_title.xlsx'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmeu_aftersales', 'database': 'tmeu open service jobcards'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/ds_tmeu_datasets and dataflows', 'database': 'tmeu_hc_dataset'}`


### Semantic Model: TMU Service Dashboard
- **Dataset ID**: `c5b76d01-1ccd-4b97-9222-1b3cc6bce725`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `10:00` (FLE Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmu_opspackage', 'database': 'tmu ops package'}`
- Type: `Web` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/Collaboration/Shared%20Documents/INT_POWERBI_HELPER/TMU/Service_dashboard/service_dashboard_budget_title.xlsx'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmeu_aftersales', 'database': 'tmeu open service jobcards'}`


### Semantic Model: Report Usage Metrics Model
- **Dataset ID**: `ab195926-4696-458d-90a4-fcbffdc339c0`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `False`
- **Configured By**: `OBaliuta@titanmachinery.ua`

*No refresh schedule configured.*

### Semantic Model: Usage Metrics Report
- **Dataset ID**: `16126703-abc9-4f31-b06a-03bcc46c291e`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `14:11` (UTC)

**Connected Data Sources (Lineage)**:
- Type: `Extension` | Connection: `{'path': 'UsageMetricsDataConnector', 'kind': 'UsageMetricsDataConnector'}`


### Semantic Model: TMEU Summary Service Dashboard
- **Dataset ID**: `8aa29f08-ee09-4ba0-8908-ff33ecd65cb2`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `10:30` (FLE Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_eoc_service_dashboard', 'database': 'tmd service dashboard'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_eoc_service_dashboard', 'database': 'tmr service dashboard'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_eoc_service_dashboard', 'database': 'tmu service dashboard'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_eoc_service_dashboard', 'database': 'tmb service dashboard'}`


## 4. Power BI Reports Inventory

| Report Name | Report ID | Dataset ID | Web URL |
| :--- | :--- | :--- | :--- |
| **TMB Service Dashboard** | `d56f0fe0-f49f-4e2b-ac23-8c4833785cc6` | `5873cd03-368b-4914-b4d3-17814326433d` | [Open Report](https://app.powerbi.com/groups/39febb80-095b-45f7-9902-b53b1718f1f1/reports/d56f0fe0-f49f-4e2b-ac23-8c4833785cc6) |
| **TMD Service Dashboard** | `dfe5edef-923c-44eb-8e6f-9a86c05c687e` | `9881dc85-86e2-4e89-b3a5-d517a3df3d1f` | [Open Report](https://app.powerbi.com/groups/39febb80-095b-45f7-9902-b53b1718f1f1/reports/dfe5edef-923c-44eb-8e6f-9a86c05c687e) |
| **TMR Service Dashboard** | `df009c42-d1f6-41dc-9983-7f0d96fe57a9` | `69fc80c3-0b92-47c4-8cda-2a46efd0e8cc` | [Open Report](https://app.powerbi.com/groups/39febb80-095b-45f7-9902-b53b1718f1f1/reports/df009c42-d1f6-41dc-9983-7f0d96fe57a9) |
| **TMU Service Dashboard** | `8a223695-c326-4a9f-be88-928a436fc151` | `c5b76d01-1ccd-4b97-9222-1b3cc6bce725` | [Open Report](https://app.powerbi.com/groups/39febb80-095b-45f7-9902-b53b1718f1f1/reports/8a223695-c326-4a9f-be88-928a436fc151) |
| **Report Usage Metrics Report** | `4879d7d3-e7ca-4f88-8fdd-4be665ed014a` | `ab195926-4696-458d-90a4-fcbffdc339c0` | [Open Report](https://app.powerbi.com/groups/39febb80-095b-45f7-9902-b53b1718f1f1/reports/4879d7d3-e7ca-4f88-8fdd-4be665ed014a) |
| **Usage Metrics Report** | `64578c78-e834-4480-adb1-bd229d3ab70a` | `16126703-abc9-4f31-b06a-03bcc46c291e` | [Open Report](https://app.powerbi.com/groups/39febb80-095b-45f7-9902-b53b1718f1f1/reports/64578c78-e834-4480-adb1-bd229d3ab70a) |
| **TMEU Summary Service Dashboard** | `25c1c339-2a80-40e4-8332-a298d0560a10` | `8aa29f08-ee09-4ba0-8908-ff33ecd65cb2` | [Open Report](https://app.powerbi.com/groups/39febb80-095b-45f7-9902-b53b1718f1f1/reports/25c1c339-2a80-40e4-8332-a298d0560a10) |

## 5. Dataflows & Dashboards

*No dataflows or dashboards in this workspace.*

---

## 6. Newcomer Operational Runbook & Notes
- **Primary Contact / Owner**: Refer to workspace access settings in Power BI portal.
- **Troubleshooting**: If a refresh fails in `BI_EOC_Service_Dashboard`, inspect the failure log under section 3 above and check upstream data gateway connectivity.
