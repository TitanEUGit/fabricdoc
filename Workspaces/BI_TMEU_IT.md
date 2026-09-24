# Workspace Documentation: BI_TMEU_IT

**Workspace ID**: `d55dce3c-6837-416c-a503-517366031fdd`  
**Type**: `Fabric / PowerBI Workspace`  
**Capacity ID**: `70650ed2-f7a2-46df-96e8-8089f25db80e`  
**Description**: No description provided.

---

## 1. Executive Summary & Newcomer Overview

> [!IMPORTANT]
> **European IT Department Reporting**
> This workspace is the central hub for the TMA IT Department, encompassing IT reporting for all European countries. 

> [!WARNING]
> **Pending Decommissioning / Usage Review**
> - **IT Infrastructure DevOps**: Deprecated. Consider decommissioning.
> - **TMEU ERP&CRM DevOps**: Usage not proven. Verify if deprecated.
> - **TMEU IT Inventory**: Usage not proven.
> - **TMEU Open Tickets**: Usage not proven.
> - **TMEU Policies Reponses**: Usage not proven.

### Key Reports & Workflows
| Report Name | What It Shows / Context |
|:---|:---|
| **TMEU IT Dashboard** | Fundamental financial IT report tracking budgeting and costs. **Lineage:** Based on the `it` schema in the `TMEU_Bronze_Lakehouse`. It depends on a pipeline in `Fabric_Prod_Workspace` that reprocesses data from the ERP. |
| **TMU Freshservice Tasks Report** | Source of truth for tickets and tasks related to TMU ERP (based on Freshservice). Critical for supervising outsourced tasks while TMU hires an internal ERP developer. |
| **TMB_TMR_CSI_DataIntake** | Automation report that generates service data for CNH. This data is subsequently used by a Power Automate flow to send the payload to an IT support service account for manual submission. |
| **Certificates** | Visualization of SharePoint data for tracking certificates and their expiries. |

This document contains operational and technical details for the **BI_TMEU_IT** workspace. It is designed to give new team members full visibility into key items, data models, report lineage, and refresh schedules.

## 2. Native Fabric Items Inventory

| Item Name | Item Type | Item ID | Description |
| :--- | :--- | :--- | :--- |
| **TMEU Open Tickets** | `Report` | `53fa1a20-2811-4c40-ae17-3af77740e470` | - |
| **Certificates** | `Report` | `335ca64d-1a8d-44d3-9507-136bb7d872ce` | - |
| **TMU ERP DevOps** | `Report` | `a06ce184-8e7f-40e4-bdc6-4c89675d1d59` | - |
| **TMB_TMR_CSI_DataIntake** | `Report` | `6dabb9b5-6208-41ca-af1e-951092a83451` | - |
| **Usage Metrics Report** | `Report` | `7eed87ed-3498-4623-a606-37bb554aa2f4` | - |
| **TMEU IT Dashboard** | `Report` | `7c513ce7-eeef-4f34-800b-59b7593d73c0` | - |
| **TMEU IT Inventory** | `Report` | `40cb0c0e-6288-491f-81ac-d025ce458b19` | - |
| **IT Infrastructure DevOps** | `Report` | `3e57f406-5440-4bf3-a751-02fdeb2d1689` | - |
| **TMEU ERP&CRM DevOps** | `Report` | `b4c43ca6-f056-4bd4-800d-2161d474981a` | - |
| **TMEU_Network Downtime** | `Report` | `a54987bb-1bd9-49f6-8148-69ea76f02806` | - |
| **TMEU Policies Reponses** | `Report` | `a5d83edb-2b62-42ef-b701-85749d8b1903` | - |
| **TMU Freshservice Tasks Report** | `Report` | `2728461e-5745-4fdf-97b6-459e1fd58ffc` | - |
| **TMEU Open Tickets** | `SemanticModel` | `5abbda8f-1bbd-4d87-94cb-e20b32a071d6` | - |
| **Certificates** | `SemanticModel` | `fd38d4a1-802b-4610-9b5f-893a206363c8` | - |
| **TMU ERP DevOps** | `SemanticModel` | `95d870eb-7e3e-43fa-bec3-e110ffdc3397` | - |
| **TMB_TMR_CSI_DataIntake** | `SemanticModel` | `9943353d-effe-4439-a061-5796dfd9f24b` | - |
| **Usage Metrics Report** | `SemanticModel` | `8acb873d-b024-4d83-ae4e-946fd788ce9f` | - |
| **TMEU IT Dashboard** | `SemanticModel` | `2184dd44-c40a-4a05-8e1e-dcddd2b1c11a` | - |
| **TMEU IT Inventory** | `SemanticModel` | `7fefdee6-f845-417e-85a4-c833d3828a80` | - |
| **IT Infrastructure DevOps** | `SemanticModel` | `c17b2735-f4c5-4b91-a7e1-c4a2e932f7d0` | - |
| **TMEU ERP&CRM DevOps** | `SemanticModel` | `c39abe76-3c04-4bbf-8f93-b126b79c9f62` | - |
| **TMEU_Network Downtime** | `SemanticModel` | `3e3bcddc-92c7-47fa-ad39-9337ff5b7aed` | - |
| **TMEU Policies Reponses** | `SemanticModel` | `e4a47798-ba26-4339-9f3d-a11306cafdbc` | - |
| **TMU Freshservice Tasks Report** | `SemanticModel` | `0fbb0b68-28f5-4464-96ce-493a11e8c016` | - |

## 3. Semantic Models (Datasets) & Refresh Schedules

### Semantic Model: TMEU Open Tickets
- **Dataset ID**: `5abbda8f-1bbd-4d87-94cb-e20b32a071d6`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `09:00, 10:00, 11:00, 12:00, 13:00, 14:00, 15:00, 16:00` (W. Europe Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `Web` | Connection: `{'url': 'https://tmitsupport.freshservice.com/'}`


### Semantic Model: Certificates
- **Dataset ID**: `fd38d4a1-802b-4610-9b5f-893a206363c8`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `02:00` (FLE Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `SharePointList` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/it/documentation/'}`


### Semantic Model: TMU ERP DevOps
- **Dataset ID**: `95d870eb-7e3e-43fa-bec3-e110ffdc3397`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `09:30, 10:30, 11:30, 12:30, 13:30, 14:30, 15:30, 16:30` (FLE Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `Extension` | Connection: `{'path': 'tmu-erp', 'kind': 'VSTS'}`
- Type: `Extension` | Connection: `{'path': 'Visual Studio Team Services', 'kind': 'Visual Studio Team Services'}`
- Type: `Web` | Connection: `{'url': 'https://tmitsupport.freshservice.com/'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmeu_it', 'database': 'tmeu open tickets'}`


### Semantic Model: TMB_TMR_CSI_DataIntake
- **Dataset ID**: `9943353d-effe-4439-a061-5796dfd9f24b`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `08:00` (W. Europe Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `Sql` | Connection: `{'server': '10.75.1.7', 'database': 'jetnavdwh'}`


### Semantic Model: Usage Metrics Report
- **Dataset ID**: `8acb873d-b024-4d83-ae4e-946fd788ce9f`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `20:32` (UTC)

**Connected Data Sources (Lineage)**:
- Type: `Extension` | Connection: `{'path': 'UsageMetricsDataConnector', 'kind': 'UsageMetricsDataConnector'}`


### Semantic Model: TMEU IT Dashboard
- **Dataset ID**: `2184dd44-c40a-4a05-8e1e-dcddd2b1c11a`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `08:00, 08:30, 09:00, 09:30, 10:00, 10:30, 11:00, 11:30, 12:00, 12:30, 13:00, 13:30, 14:00, 14:30, 15:00, 15:30, 16:00, 16:30, 17:00, 17:30, 18:00, 18:30, 19:00` (W. Europe Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `Sql` | Connection: `{'server': 'cwgz5ola5r6u5e4heu5qw3drgy-zzqhzdizzmcurky2zbgw4gw7la.datawarehouse.fabric.microsoft.com', 'database': 'tmeu_it_db'}`


### Semantic Model: TMEU IT Inventory
- **Dataset ID**: `7fefdee6-f845-417e-85a4-c833d3828a80`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `08:00, 08:30, 09:00, 09:30, 10:00, 10:30, 11:00, 11:30, 12:00, 12:30, 13:00, 13:30, 14:00, 14:30, 15:00, 15:30, 16:00, 16:30, 17:00, 17:30, 18:00, 18:30, 19:00` (W. Europe Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `SharePointList` | Connection: `{'url': 'https://titanmachinery365europe.sharepoint.com/sites/it-dataset-hardware-inventory/'}`
- Type: `Web` | Connection: `{'url': 'https://accounts.zoho.eu/'}`
- Type: `SharePointList` | Connection: `{'url': 'https://titanmachinery365europe.sharepoint.com/sites/hr-dataset-europe/'}`
- Type: `Web` | Connection: `{'url': 'https://endpointcentral.manageengine.eu/'}`


### Semantic Model: IT Infrastructure DevOps
- **Dataset ID**: `c17b2735-f4c5-4b91-a7e1-c4a2e932f7d0`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `08:00, 08:30, 09:00, 09:30, 10:00, 10:30, 11:00, 11:30, 12:00, 12:30, 13:00, 13:30, 14:00, 14:30, 15:00, 15:30, 16:00, 16:30, 17:00, 17:30, 18:00, 18:30, 19:00` (W. Europe Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `Extension` | Connection: `{'path': 'Visual Studio Team Services', 'kind': 'Visual Studio Team Services'}`
- Type: `Extension` | Connection: `{'path': 'tm-it-infrastructure', 'kind': 'VSTS'}`


### Semantic Model: TMEU ERP&CRM DevOps
- **Dataset ID**: `c39abe76-3c04-4bbf-8f93-b126b79c9f62`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `08:00, 08:30, 09:00, 09:30, 10:00, 10:30, 11:00, 11:30, 12:00, 12:30, 13:00, 13:30, 14:00, 14:30, 15:00, 15:30, 16:00, 16:30, 17:00, 17:30, 18:00, 18:30, 19:00` (W. Europe Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `Extension` | Connection: `{'path': 'tmr-crm', 'kind': 'VSTS'}`
- Type: `Extension` | Connection: `{'path': 'Visual Studio Team Services', 'kind': 'Visual Studio Team Services'}`
- Type: `Extension` | Connection: `{'path': 'tmu-crm', 'kind': 'VSTS'}`
- Type: `Extension` | Connection: `{'path': 'tmb-crm', 'kind': 'VSTS'}`
- Type: `Extension` | Connection: `{'path': 'tmu-erp', 'kind': 'VSTS'}`


### Semantic Model: TMEU_Network Downtime
- **Dataset ID**: `3e3bcddc-92c7-47fa-ad39-9337ff5b7aed`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `01:00` (FLE Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `SharePointList` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/it/operations/'}`


### Semantic Model: TMEU Policies Reponses
- **Dataset ID**: `e4a47798-ba26-4339-9f3d-a11306cafdbc`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `10:00` (FLE Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `SharePointList` | Connection: `{'url': 'https://titanmachinery365europe.sharepoint.com/sites/policycenter/'}`
- Type: `SharePointList` | Connection: `{'url': 'https://titanmachinery365europe.sharepoint.com/sites/hr-dataset-europe/'}`


### Semantic Model: TMU Freshservice Tasks Report
- **Dataset ID**: `0fbb0b68-28f5-4464-96ce-493a11e8c016`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `08:30, 09:30, 10:30, 11:30, 12:30, 13:30, 14:30, 15:30, 16:30, 17:30, 18:30` (FLE Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `Sql` | Connection: `{'server': 'cwgz5ola5r6u5e4heu5qw3drgy-zzqhzdizzmcurky2zbgw4gw7la.datawarehouse.fabric.microsoft.com', 'database': 'tmeu_freshservice_lakehouse'}`
- Type: `SharePointList` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/it/management/'}`


## 4. Power BI Reports Inventory

| Report Name | Report ID | Dataset ID | Web URL |
| :--- | :--- | :--- | :--- |
| **TMEU Open Tickets** | `53fa1a20-2811-4c40-ae17-3af77740e470` | `5abbda8f-1bbd-4d87-94cb-e20b32a071d6` | [Open Report](https://app.powerbi.com/groups/d55dce3c-6837-416c-a503-517366031fdd/reports/53fa1a20-2811-4c40-ae17-3af77740e470) |
| **Certificates** | `335ca64d-1a8d-44d3-9507-136bb7d872ce` | `fd38d4a1-802b-4610-9b5f-893a206363c8` | [Open Report](https://app.powerbi.com/groups/d55dce3c-6837-416c-a503-517366031fdd/reports/335ca64d-1a8d-44d3-9507-136bb7d872ce) |
| **TMU ERP DevOps** | `a06ce184-8e7f-40e4-bdc6-4c89675d1d59` | `95d870eb-7e3e-43fa-bec3-e110ffdc3397` | [Open Report](https://app.powerbi.com/groups/d55dce3c-6837-416c-a503-517366031fdd/reports/a06ce184-8e7f-40e4-bdc6-4c89675d1d59) |
| **TMB_TMR_CSI_DataIntake** | `6dabb9b5-6208-41ca-af1e-951092a83451` | `9943353d-effe-4439-a061-5796dfd9f24b` | [Open Report](https://app.powerbi.com/groups/d55dce3c-6837-416c-a503-517366031fdd/reports/6dabb9b5-6208-41ca-af1e-951092a83451) |
| **Usage Metrics Report** | `7eed87ed-3498-4623-a606-37bb554aa2f4` | `8acb873d-b024-4d83-ae4e-946fd788ce9f` | [Open Report](https://app.powerbi.com/groups/d55dce3c-6837-416c-a503-517366031fdd/reports/7eed87ed-3498-4623-a606-37bb554aa2f4) |
| **TMEU IT Dashboard** | `7c513ce7-eeef-4f34-800b-59b7593d73c0` | `2184dd44-c40a-4a05-8e1e-dcddd2b1c11a` | [Open Report](https://app.powerbi.com/groups/d55dce3c-6837-416c-a503-517366031fdd/reports/7c513ce7-eeef-4f34-800b-59b7593d73c0) |
| **TMEU IT Inventory** | `40cb0c0e-6288-491f-81ac-d025ce458b19` | `7fefdee6-f845-417e-85a4-c833d3828a80` | [Open Report](https://app.powerbi.com/groups/d55dce3c-6837-416c-a503-517366031fdd/reports/40cb0c0e-6288-491f-81ac-d025ce458b19) |
| **IT Infrastructure DevOps** | `3e57f406-5440-4bf3-a751-02fdeb2d1689` | `c17b2735-f4c5-4b91-a7e1-c4a2e932f7d0` | [Open Report](https://app.powerbi.com/groups/d55dce3c-6837-416c-a503-517366031fdd/reports/3e57f406-5440-4bf3-a751-02fdeb2d1689) |
| **TMEU ERP&CRM DevOps** | `b4c43ca6-f056-4bd4-800d-2161d474981a` | `c39abe76-3c04-4bbf-8f93-b126b79c9f62` | [Open Report](https://app.powerbi.com/groups/d55dce3c-6837-416c-a503-517366031fdd/reports/b4c43ca6-f056-4bd4-800d-2161d474981a) |
| **TMEU_Network Downtime** | `a54987bb-1bd9-49f6-8148-69ea76f02806` | `3e3bcddc-92c7-47fa-ad39-9337ff5b7aed` | [Open Report](https://app.powerbi.com/groups/d55dce3c-6837-416c-a503-517366031fdd/reports/a54987bb-1bd9-49f6-8148-69ea76f02806) |
| **TMEU Policies Reponses** | `a5d83edb-2b62-42ef-b701-85749d8b1903` | `e4a47798-ba26-4339-9f3d-a11306cafdbc` | [Open Report](https://app.powerbi.com/groups/d55dce3c-6837-416c-a503-517366031fdd/reports/a5d83edb-2b62-42ef-b701-85749d8b1903) |
| **TMU Freshservice Tasks Report** | `2728461e-5745-4fdf-97b6-459e1fd58ffc` | `0fbb0b68-28f5-4464-96ce-493a11e8c016` | [Open Report](https://app.powerbi.com/groups/d55dce3c-6837-416c-a503-517366031fdd/reports/2728461e-5745-4fdf-97b6-459e1fd58ffc) |

## 5. Dataflows & Dashboards

*No dataflows or dashboards in this workspace.*

---

## 6. Newcomer Operational Runbook & Notes
- **Primary Contact / Owner**: Refer to workspace access settings in Power BI portal.
- **Troubleshooting**: If a refresh fails in `BI_TMEU_IT`, inspect the failure log under section 3 above and check upstream data gateway connectivity.
