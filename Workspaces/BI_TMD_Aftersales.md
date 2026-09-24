# Workspace Documentation: BI_TMD_Aftersales

**Workspace ID**: `6a3df89d-f233-4471-942c-23827cb9ca8b`  
**Type**: `Fabric / PowerBI Workspace`  
**Capacity ID**: `70650ed2-f7a2-46df-96e8-8089f25db80e`  
**Description**: No description provided.

---

## 1. Executive Summary & Newcomer Overview
This document contains operational and technical details for the **BI_TMD_Aftersales** workspace. It is designed to give new team members full visibility into key items, data models, report lineage, and refresh schedules.

## 2. Native Fabric Items Inventory

| Item Name | Item Type | Item ID | Description |
| :--- | :--- | :--- | :--- |
| **DB_TMD Service KPI YTD** | `Dashboard` | `6d928506-04a1-4e04-93a5-5290752c0ced` | - |
| **DB_TMD Service KPI MTD** | `Dashboard` | `20ee8eea-ed88-44b9-931c-c51f6dea57d4` | - |
| **TMD Service KPI NEW** | `Report` | `3df69175-d84a-42d5-b6ff-aa0ec11d2ad4` | - |
| **TMD CRM Contacts** | `Report` | `f33df8aa-4e4c-4490-89f4-66a3c19fccb1` | - |
| **TMD Parts Sales** | `Report` | `121b90cd-a8fe-46a6-8309-3035d8ee18ca` | - |
| **TMD Parts Purchase Orders** | `Report` | `804fc572-b117-4a58-b588-05bb5e4a0ad7` | - |
| **TMD Variable Service Compensation** | `Report` | `8b5a4047-b51e-4b69-911e-3a529b26df14` | - |
| **Usage Metrics Report** | `Report` | `98304028-6852-4ac6-bbb9-b93f09e0c3c8` | - |
| **Report Usage Metrics Report** | `Report` | `eb47805f-017b-4dd9-b6c6-ffa49706b8b7` | - |
| **TMD Service KPI NEW** | `SemanticModel` | `417f4e11-9a70-4eaa-adb3-d5cbef415fc5` | - |
| **TMD CRM Contacts** | `SemanticModel` | `008cd3f2-4e8f-426e-b41f-44deaca0be1a` | - |
| **TMD Parts Sales** | `SemanticModel` | `065ba841-8533-4bab-820c-292021b46135` | - |
| **TMD Parts Purchase Orders** | `SemanticModel` | `3f876c52-b1db-482a-9d0c-f45eb9ba9d44` | - |
| **TMD Variable Service Compensation** | `SemanticModel` | `90240e20-71eb-47b7-891a-8340e4b458bc` | - |
| **Usage Metrics Report** | `SemanticModel` | `bb0c2b75-4a52-4dda-b863-8765aacd779c` | - |
| **Report Usage Metrics Model** | `SemanticModel` | `b3a2c743-21f9-4b7c-b81c-d35b8a1c6f68` | - |

## 3. Semantic Models (Datasets) & Refresh Schedules

### Semantic Model: TMD Service KPI NEW
- **Dataset ID**: `417f4e11-9a70-4eaa-adb3-d5cbef415fc5`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `08:00` (FLE Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `ODBC` | Connection: `{'connectionString': 'dsn=timeline - tmd'}`
- Type: `Extension` | Connection: `{'path': 'PowerPlatformDataflows', 'kind': 'PowerPlatformDataflows'}`


### Semantic Model: TMD CRM Contacts
- **Dataset ID**: `008cd3f2-4e8f-426e-b41f-44deaca0be1a`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `01:00` (FLE Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `Extension` | Connection: `{'path': 'titanmachinery.crm4.dynamics.com', 'kind': 'CommonDataService'}`


### Semantic Model: TMD Parts Sales
- **Dataset ID**: `065ba841-8533-4bab-820c-292021b46135`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `03:00` (FLE Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `ODBC` | Connection: `{'connectionString': 'dsn=timeline - tmd'}`
- Type: `Extension` | Connection: `{'path': 'PowerPlatformDataflows', 'kind': 'PowerPlatformDataflows'}`
- Type: `SharePointList` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/collaboration/'}`
- Type: `Extension` | Connection: `{'path': 'titanmachinery.crm4.dynamics.com', 'kind': 'CommonDataService'}`


### Semantic Model: TMD Parts Purchase Orders
- **Dataset ID**: `3f876c52-b1db-482a-9d0c-f45eb9ba9d44`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `08:00` (FLE Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `ODBC` | Connection: `{'connectionString': 'dsn=timeline - tmd'}`


### Semantic Model: TMD Variable Service Compensation
- **Dataset ID**: `90240e20-71eb-47b7-891a-8340e4b458bc`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Monday
- **Scheduled Times**: `01:00` (FLE Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmd_aftersales', 'database': 'tmd service kpi new'}`
- Type: `SharePointList` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/collaboration/'}`
- Type: `Extension` | Connection: `{'path': 'PowerPlatformDataflows', 'kind': 'PowerPlatformDataflows'}`


### Semantic Model: Usage Metrics Report
- **Dataset ID**: `bb0c2b75-4a52-4dda-b863-8765aacd779c`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `16:14` (UTC)

**Connected Data Sources (Lineage)**:
- Type: `Extension` | Connection: `{'path': 'UsageMetricsDataConnector', 'kind': 'UsageMetricsDataConnector'}`


### Semantic Model: Report Usage Metrics Model
- **Dataset ID**: `b3a2c743-21f9-4b7c-b81c-d35b8a1c6f68`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `False`
- **Configured By**: `OBaliuta@titanmachinery.ua`

*No refresh schedule configured.*

## 4. Power BI Reports Inventory

| Report Name | Report ID | Dataset ID | Web URL |
| :--- | :--- | :--- | :--- |
| **TMD Service KPI NEW** | `3df69175-d84a-42d5-b6ff-aa0ec11d2ad4` | `417f4e11-9a70-4eaa-adb3-d5cbef415fc5` | [Open Report](https://app.powerbi.com/groups/6a3df89d-f233-4471-942c-23827cb9ca8b/reports/3df69175-d84a-42d5-b6ff-aa0ec11d2ad4) |
| **TMD CRM Contacts** | `f33df8aa-4e4c-4490-89f4-66a3c19fccb1` | `008cd3f2-4e8f-426e-b41f-44deaca0be1a` | [Open Report](https://app.powerbi.com/groups/6a3df89d-f233-4471-942c-23827cb9ca8b/reports/f33df8aa-4e4c-4490-89f4-66a3c19fccb1) |
| **TMD Parts Sales** | `121b90cd-a8fe-46a6-8309-3035d8ee18ca` | `065ba841-8533-4bab-820c-292021b46135` | [Open Report](https://app.powerbi.com/groups/6a3df89d-f233-4471-942c-23827cb9ca8b/reports/121b90cd-a8fe-46a6-8309-3035d8ee18ca) |
| **TMD Parts Purchase Orders** | `804fc572-b117-4a58-b588-05bb5e4a0ad7` | `3f876c52-b1db-482a-9d0c-f45eb9ba9d44` | [Open Report](https://app.powerbi.com/groups/6a3df89d-f233-4471-942c-23827cb9ca8b/reports/804fc572-b117-4a58-b588-05bb5e4a0ad7) |
| **TMD Variable Service Compensation** | `8b5a4047-b51e-4b69-911e-3a529b26df14` | `90240e20-71eb-47b7-891a-8340e4b458bc` | [Open Report](https://app.powerbi.com/groups/6a3df89d-f233-4471-942c-23827cb9ca8b/reports/8b5a4047-b51e-4b69-911e-3a529b26df14) |
| **Usage Metrics Report** | `98304028-6852-4ac6-bbb9-b93f09e0c3c8` | `bb0c2b75-4a52-4dda-b863-8765aacd779c` | [Open Report](https://app.powerbi.com/groups/6a3df89d-f233-4471-942c-23827cb9ca8b/reports/98304028-6852-4ac6-bbb9-b93f09e0c3c8) |
| **Report Usage Metrics Report** | `eb47805f-017b-4dd9-b6c6-ffa49706b8b7` | `b3a2c743-21f9-4b7c-b81c-d35b8a1c6f68` | [Open Report](https://app.powerbi.com/groups/6a3df89d-f233-4471-942c-23827cb9ca8b/reports/eb47805f-017b-4dd9-b6c6-ffa49706b8b7) |

## 5. Dataflows & Dashboards

**Dashboards**:
- **DB_TMD Service KPI YTD** (ID: `6d928506-04a1-4e04-93a5-5290752c0ced`)
- **DB_TMD Service KPI MTD** (ID: `20ee8eea-ed88-44b9-931c-c51f6dea57d4`)

---

## 6. Newcomer Operational Runbook & Notes
- **Primary Contact / Owner**: Refer to workspace access settings in Power BI portal.
- **Troubleshooting**: If a refresh fails in `BI_TMD_Aftersales`, inspect the failure log under section 3 above and check upstream data gateway connectivity.
