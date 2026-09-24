# Workspace Documentation: BI_TMU_CRM

**Workspace ID**: `8bf660b9-c71f-49f6-a59a-af51ba6ea206`  
**Type**: `Fabric / PowerBI Workspace`  
**Capacity ID**: `70650ed2-f7a2-46df-96e8-8089f25db80e`  
**Description**: No description provided.

---

## 1. Executive Summary & Newcomer Overview

> [!NOTE]
> **CRM Reporting (Dynamics 365)**
> This workspace handles CRM reporting sourced from **Dataverse**. 
> **Country Specific Setup (Ukraine):** The TMU sales process exclusively uses the **Opportunity** entity. Sales progression is tracked entirely through the *status* field rather than utilizing separate Quote or Sales Order entities.

This document contains operational and technical details for the **BI_TMU_CRM** workspace. It is designed to give new team members full visibility into key items, data models, report lineage, and refresh schedules.

## 2. Native Fabric Items Inventory

| Item Name | Item Type | Item ID | Description |
| :--- | :--- | :--- | :--- |
| **BI_TMU Customers Interaction Plan (local)** | `Dashboard` | `18fd7ae3-9399-4d90-ba85-b2690f36bb53` | - |
| **BI_TMU_CRM_Activities_Details** | `Dashboard` | `6d76469a-b497-4a6e-ad01-6abb2a440709` | - |
| **TMU CRM** | `Report` | `192c3c0e-38da-4e53-8f97-0373e42bd899` | - |
| **TMU ESC Appointments** | `Report` | `97eafc83-08e4-454f-97be-6e7524a12590` | - |
| **TMU Quoted Offers** | `Report` | `8ef43076-727a-45b7-81d5-f073cc8d9136` | - |
| **TMU CRM Customers and Regions** | `Report` | `11824ad8-a642-482c-8265-470cdf8ce6a1` | - |
| **Usage Metrics Report** | `Report` | `c6a58aa6-bdb6-4c5d-b8ce-37d047ca575f` | - |
| **TMU ESC Interactions & Confirmations** | `Report` | `865b7eaf-8442-4fe8-a735-f78aadf05c8e` | - |
| **TMU CRM** | `SemanticModel` | `65f63afc-a43f-4b5a-9b1d-74bb9d425cc0` | - |
| **TMU ESC Appointments** | `SemanticModel` | `e8cbfe04-219e-414e-867c-dcbb04ba24d3` | - |
| **TMU Quoted Offers** | `SemanticModel` | `fa133345-23e3-49b0-ba68-a104d7fad4a5` | - |
| **TMU CRM Customers and Regions** | `SemanticModel` | `c86883d9-cb1a-47c9-8d1b-d68db7bb2b1b` | - |
| **Usage Metrics Report** | `SemanticModel` | `88ce196a-dac7-4b2d-af0e-6507104bb39f` | - |
| **TMU ESC Interactions & Confirmations** | `SemanticModel` | `6f4ca986-4ab0-4fed-b23b-1b1c57155f6d` | - |

## 3. Semantic Models (Datasets) & Refresh Schedules

### Semantic Model: TMU CRM
- **Dataset ID**: `65f63afc-a43f-4b5a-9b1d-74bb9d425cc0`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `04:00` (GTB Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `Extension` | Connection: `{'path': 'titanukraine.crm4.dynamics.com', 'kind': 'CommonDataService'}`
- Type: `Extension` | Connection: `{'path': 'PowerPlatformDataflows', 'kind': 'PowerPlatformDataflows'}`


### Semantic Model: TMU ESC Appointments
- **Dataset ID**: `e8cbfe04-219e-414e-867c-dcbb04ba24d3`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `05:00` (FLE Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `Extension` | Connection: `{'path': 'titanukraine.crm4.dynamics.com', 'kind': 'CommonDataService'}`
- Type: `Sql` | Connection: `{'server': 'cwgz5ola5r6u5e4heu5qw3drgy-zzqhzdizzmcurky2zbgw4gw7la.datawarehouse.fabric.microsoft.com', 'database': 'tmu_bronze_lakehouse'}`


### Semantic Model: TMU Quoted Offers
- **Dataset ID**: `fa133345-23e3-49b0-ba68-a104d7fad4a5`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `06:00` (FLE Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `Extension` | Connection: `{'path': 'titanukraine.crm4.dynamics.com', 'kind': 'CommonDataService'}`
- Type: `Extension` | Connection: `{'path': 'PowerPlatformDataflows', 'kind': 'PowerPlatformDataflows'}`


### Semantic Model: TMU CRM Customers and Regions
- **Dataset ID**: `c86883d9-cb1a-47c9-8d1b-d68db7bb2b1b`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `08:00` (FLE Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `Extension` | Connection: `{'path': 'titanukraine.crm4.dynamics.com', 'kind': 'CommonDataService'}`


### Semantic Model: Usage Metrics Report
- **Dataset ID**: `88ce196a-dac7-4b2d-af0e-6507104bb39f`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `05:51` (UTC)

**Connected Data Sources (Lineage)**:
- Type: `Extension` | Connection: `{'path': 'UsageMetricsDataConnector', 'kind': 'UsageMetricsDataConnector'}`


### Semantic Model: TMU ESC Interactions & Confirmations
- **Dataset ID**: `6f4ca986-4ab0-4fed-b23b-1b1c57155f6d`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `04:00` (FLE Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `Extension` | Connection: `{'path': 'titanukraine.crm4.dynamics.com', 'kind': 'CommonDataService'}`
- Type: `Sql` | Connection: `{'server': 'cwgz5ola5r6u5e4heu5qw3drgy-zzqhzdizzmcurky2zbgw4gw7la.datawarehouse.fabric.microsoft.com', 'database': 'tmu_bronze_lakehouse'}`


## 4. Power BI Reports Inventory

| Report Name | Report ID | Dataset ID | Web URL |
| :--- | :--- | :--- | :--- |
| **TMU CRM** | `192c3c0e-38da-4e53-8f97-0373e42bd899` | `65f63afc-a43f-4b5a-9b1d-74bb9d425cc0` | [Open Report](https://app.powerbi.com/groups/8bf660b9-c71f-49f6-a59a-af51ba6ea206/reports/192c3c0e-38da-4e53-8f97-0373e42bd899) |
| **TMU ESC Appointments** | `97eafc83-08e4-454f-97be-6e7524a12590` | `e8cbfe04-219e-414e-867c-dcbb04ba24d3` | [Open Report](https://app.powerbi.com/groups/8bf660b9-c71f-49f6-a59a-af51ba6ea206/reports/97eafc83-08e4-454f-97be-6e7524a12590) |
| **TMU Quoted Offers** | `8ef43076-727a-45b7-81d5-f073cc8d9136` | `fa133345-23e3-49b0-ba68-a104d7fad4a5` | [Open Report](https://app.powerbi.com/groups/8bf660b9-c71f-49f6-a59a-af51ba6ea206/reports/8ef43076-727a-45b7-81d5-f073cc8d9136) |
| **TMU CRM Customers and Regions** | `11824ad8-a642-482c-8265-470cdf8ce6a1` | `c86883d9-cb1a-47c9-8d1b-d68db7bb2b1b` | [Open Report](https://app.powerbi.com/groups/8bf660b9-c71f-49f6-a59a-af51ba6ea206/reports/11824ad8-a642-482c-8265-470cdf8ce6a1) |
| **Usage Metrics Report** | `c6a58aa6-bdb6-4c5d-b8ce-37d047ca575f` | `88ce196a-dac7-4b2d-af0e-6507104bb39f` | [Open Report](https://app.powerbi.com/groups/8bf660b9-c71f-49f6-a59a-af51ba6ea206/reports/c6a58aa6-bdb6-4c5d-b8ce-37d047ca575f) |
| **TMU ESC Interactions & Confirmations** | `865b7eaf-8442-4fe8-a735-f78aadf05c8e` | `6f4ca986-4ab0-4fed-b23b-1b1c57155f6d` | [Open Report](https://app.powerbi.com/groups/8bf660b9-c71f-49f6-a59a-af51ba6ea206/reports/865b7eaf-8442-4fe8-a735-f78aadf05c8e) |

## 5. Dataflows & Dashboards

**Dashboards**:
- **BI_TMU Customers Interaction Plan (local)** (ID: `18fd7ae3-9399-4d90-ba85-b2690f36bb53`)
- **BI_TMU_CRM_Activities_Details** (ID: `6d76469a-b497-4a6e-ad01-6abb2a440709`)

---

## 6. Newcomer Operational Runbook & Notes
- **Primary Contact / Owner**: Refer to workspace access settings in Power BI portal.
- **Troubleshooting**: If a refresh fails in `BI_TMU_CRM`, inspect the failure log under section 3 above and check upstream data gateway connectivity.
