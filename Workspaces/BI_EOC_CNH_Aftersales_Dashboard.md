# Workspace Documentation: BI_EOC_CNH_Aftersales_Dashboard

**Workspace ID**: `34d5c982-28ca-4327-9f8f-6f772371c92e`  
**Type**: `Fabric / PowerBI Workspace`  
**Capacity ID**: `70650ed2-f7a2-46df-96e8-8089f25db80e`  
**Description**: No description provided.

---

## 1. Executive Summary & Newcomer Overview

This workspace (**BI_EOC_CNH_Aftersales_Dashboard**) is dedicated to housing the dashboards and metrics for **Aftersales KPIs for CNH** (Case IH / CASE), Titan Machinery's primary manufacturer and key strategic partner.

This document contains operational and technical details for the workspace, designed to give new team members full visibility into key items, data models, report lineage, and refresh schedules.

## 2. Native Fabric Items Inventory

| Item Name | Item Type | Item ID | Description |
| :--- | :--- | :--- | :--- |
| **TMU AfterSales Dashboard CNH** | `Report` | `e16ebdaf-f854-46fd-be92-4f24fcbe0455` | - |
| **TMR AfterSales Dashboard CNH** | `Report` | `0c730ae7-7d03-4850-8215-2a7a33ea0731` | - |
| **TMD AfterSales Dashboard CNH** | `Report` | `054b9963-5884-406d-92d2-7fcdfcbb6cba` | - |
| **TMB AfterSales Dashboard CNH** | `Report` | `6a5ec8c2-5f46-4fbc-85f8-e1b6b3793c7c` | - |
| **Usage Metrics Report** | `Report` | `0da63d81-ed84-4c8b-bd7b-9cc1d1260c4a` | - |
| **TMU AfterSales Dashboard CNH** | `SemanticModel` | `f8fe3984-f0c9-4d36-9bde-65086c97ccf2` | - |
| **TMR AfterSales Dashboard CNH** | `SemanticModel` | `f642835b-2152-4e83-9026-d90a42843d6d` | - |
| **TMD AfterSales Dashboard CNH** | `SemanticModel` | `5c9f43a2-6d77-45bb-af8a-5f3bcd84441a` | - |
| **TMB AfterSales Dashboard CNH** | `SemanticModel` | `898b1ad4-a7ee-4d2e-a63f-f28615978997` | - |
| **Usage Metrics Report** | `SemanticModel` | `5796aec8-b049-43e4-a99c-23094b93fecb` | - |

## 3. Semantic Models (Datasets) & Refresh Schedules

### Semantic Model: TMU AfterSales Dashboard CNH
- **Dataset ID**: `f8fe3984-f0c9-4d36-9bde-65086c97ccf2`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `09:00` (FLE Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/ds_tmeu_datasets and dataflows', 'database': 'tmeu parts inventory staging'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmu_opspackage', 'database': 'tmu ops package'}`


### Semantic Model: TMR AfterSales Dashboard CNH
- **Dataset ID**: `f642835b-2152-4e83-9026-d90a42843d6d`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `09:00` (FLE Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/ds_tmeu_datasets and dataflows', 'database': 'tmeu parts inventory staging'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmr_opspackage', 'database': 'tmr ops package'}`


### Semantic Model: TMD AfterSales Dashboard CNH
- **Dataset ID**: `5c9f43a2-6d77-45bb-af8a-5f3bcd84441a`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `09:00` (FLE Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmd_aftersales', 'database': 'tmd parts sales'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmd_aftersales', 'database': 'tmd service kpi new'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/ds_tmeu_datasets and dataflows', 'database': 'tmeu parts inventory staging'}`


### Semantic Model: TMB AfterSales Dashboard CNH
- **Dataset ID**: `898b1ad4-a7ee-4d2e-a63f-f28615978997`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `09:00` (FLE Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmb_opspackage', 'database': 'tmb ops package'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/ds_tmeu_datasets and dataflows', 'database': 'tmeu parts inventory staging'}`


### Semantic Model: Usage Metrics Report
- **Dataset ID**: `5796aec8-b049-43e4-a99c-23094b93fecb`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `19:04` (UTC)

**Connected Data Sources (Lineage)**:
- Type: `Extension` | Connection: `{'path': 'UsageMetricsDataConnector', 'kind': 'UsageMetricsDataConnector'}`


## 4. Power BI Reports Inventory

| Report Name | Report ID | Dataset ID | Web URL |
| :--- | :--- | :--- | :--- |
| **TMU AfterSales Dashboard CNH** | `e16ebdaf-f854-46fd-be92-4f24fcbe0455` | `f8fe3984-f0c9-4d36-9bde-65086c97ccf2` | [Open Report](https://app.powerbi.com/groups/34d5c982-28ca-4327-9f8f-6f772371c92e/reports/e16ebdaf-f854-46fd-be92-4f24fcbe0455) |
| **TMR AfterSales Dashboard CNH** | `0c730ae7-7d03-4850-8215-2a7a33ea0731` | `f642835b-2152-4e83-9026-d90a42843d6d` | [Open Report](https://app.powerbi.com/groups/34d5c982-28ca-4327-9f8f-6f772371c92e/reports/0c730ae7-7d03-4850-8215-2a7a33ea0731) |
| **TMD AfterSales Dashboard CNH** | `054b9963-5884-406d-92d2-7fcdfcbb6cba` | `5c9f43a2-6d77-45bb-af8a-5f3bcd84441a` | [Open Report](https://app.powerbi.com/groups/34d5c982-28ca-4327-9f8f-6f772371c92e/reports/054b9963-5884-406d-92d2-7fcdfcbb6cba) |
| **TMB AfterSales Dashboard CNH** | `6a5ec8c2-5f46-4fbc-85f8-e1b6b3793c7c` | `898b1ad4-a7ee-4d2e-a63f-f28615978997` | [Open Report](https://app.powerbi.com/groups/34d5c982-28ca-4327-9f8f-6f772371c92e/reports/6a5ec8c2-5f46-4fbc-85f8-e1b6b3793c7c) |
| **Usage Metrics Report** | `0da63d81-ed84-4c8b-bd7b-9cc1d1260c4a` | `5796aec8-b049-43e4-a99c-23094b93fecb` | [Open Report](https://app.powerbi.com/groups/34d5c982-28ca-4327-9f8f-6f772371c92e/reports/0da63d81-ed84-4c8b-bd7b-9cc1d1260c4a) |

## 5. Dataflows & Dashboards

*No dataflows or dashboards in this workspace.*

---

## 6. Newcomer Operational Runbook & Notes
- **Primary Contact / Owner**: Refer to workspace access settings in Power BI portal.
- **Troubleshooting**: If a refresh fails in `BI_EOC_CNH_Aftersales_Dashboard`, inspect the failure log under section 3 above and check upstream data gateway connectivity.
