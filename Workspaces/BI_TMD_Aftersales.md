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

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2026-09-15 05:01:10 | 2026-09-15 05:09:21 | `Completed` | `Scheduled` | - |
| 2026-09-14 05:00:19 | 2026-09-14 05:04:25 | `Completed` | `Scheduled` | - |
| 2026-09-13 05:01:17 | 2026-09-13 05:09:10 | `Completed` | `Scheduled` | - |
| 2026-09-12 05:01:17 | 2026-09-12 05:14:06 | `Completed` | `Scheduled` | - |
| 2026-09-11 05:01:10 | 2026-09-11 05:06:25 | `Completed` | `Scheduled` | - |

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

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2025-10-04 22:01:02 | 2025-10-04 22:01:02 | `Disabled` | `Scheduled` | - |
| 2025-10-03 22:01:07 | 2025-10-03 22:06:00 | `Completed` | `Scheduled` | - |
| 2025-10-02 22:01:03 | 2025-10-02 22:04:24 | `Completed` | `Scheduled` | - |
| 2025-10-01 22:01:03 | 2025-10-01 22:04:46 | `Completed` | `Scheduled` | - |
| 2025-09-30 22:01:03 | 2025-09-30 22:04:03 | `Completed` | `Scheduled` | - |

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

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2026-09-15 00:00:14 | 2026-09-15 00:08:31 | `Completed` | `Scheduled` | - |
| 2026-09-14 00:00:16 | 2026-09-14 00:07:56 | `Completed` | `Scheduled` | - |
| 2026-09-13 00:01:04 | 2026-09-13 00:10:23 | `Completed` | `Scheduled` | - |
| 2026-09-12 00:00:17 | 2026-09-12 00:08:18 | `Completed` | `Scheduled` | - |
| 2026-09-11 00:01:06 | 2026-09-11 00:09:13 | `Completed` | `Scheduled` | - |

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

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2026-03-11 06:00:07 | 2026-03-11 06:00:07 | `Disabled` | `Scheduled` | - |
| 2026-03-10 06:01:05 | 2026-03-10 06:03:14 | `Completed` | `Scheduled` | - |
| 2026-03-09 06:01:05 | 2026-03-09 06:04:09 | `Completed` | `Scheduled` | - |
| 2026-03-08 06:01:16 | 2026-03-08 06:05:33 | `Completed` | `Scheduled` | - |
| 2026-03-07 06:01:05 | 2026-03-07 06:05:03 | `Completed` | `Scheduled` | - |

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

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2026-04-19 22:01:10 | 2026-04-19 22:01:10 | `Disabled` | `Scheduled` | - |
| 2026-04-12 22:01:22 | 2026-04-12 22:10:23 | `Completed` | `Scheduled` | - |
| 2026-04-05 22:01:21 | 2026-04-05 22:09:51 | `Completed` | `Scheduled` | - |
| 2026-03-29 22:01:15 | 2026-03-29 22:11:19 | `Completed` | `Scheduled` | - |
| 2026-03-22 23:01:16 | 2026-03-22 23:10:57 | `Completed` | `Scheduled` | - |

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

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2025-08-18 16:16:14 | 2025-08-18 16:16:14 | `Disabled` | `Scheduled` | - |
| 2025-08-17 16:16:10 | 2025-08-17 16:20:10 | `Completed` | `Scheduled` | - |
| 2025-08-16 16:16:05 | 2025-08-16 16:20:33 | `Completed` | `Scheduled` | - |
| 2025-08-15 16:17:11 | 2025-08-15 16:22:23 | `Completed` | `Scheduled` | - |
| 2025-08-14 16:18:05 | 2025-08-14 16:22:40 | `Completed` | `Scheduled` | - |

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
