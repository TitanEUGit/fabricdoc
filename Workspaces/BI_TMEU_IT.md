# Workspace Documentation: BI_TMEU_IT

**Workspace ID**: `d55dce3c-6837-416c-a503-517366031fdd`  
**Type**: `Fabric / PowerBI Workspace`  
**Capacity ID**: `70650ed2-f7a2-46df-96e8-8089f25db80e`  
**Description**: No description provided.

---

## 1. Executive Summary & Newcomer Overview
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

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2026-09-08 13:03:26 | 2026-09-08 13:03:26 | `Disabled` | `Scheduled` | - |
| 2026-09-08 12:03:27 | 2026-09-08 12:15:22 | `Completed` | `Scheduled` | - |
| 2026-09-08 11:03:03 | 2026-09-08 11:14:19 | `Completed` | `Scheduled` | - |
| 2026-09-08 10:02:25 | 2026-09-08 10:14:09 | `Completed` | `Scheduled` | - |
| 2026-09-08 09:02:19 | 2026-09-08 09:14:41 | `Completed` | `Scheduled` | - |

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

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2026-07-20 23:01:19 | 2026-07-20 23:01:19 | `Disabled` | `Scheduled` | - |
| 2026-07-19 23:01:13 | 2026-07-19 23:05:28 | `Completed` | `Scheduled` | - |
| 2026-07-18 23:01:11 | 2026-07-18 23:06:24 | `Completed` | `Scheduled` | - |
| 2026-07-17 23:01:15 | 2026-07-17 23:05:18 | `Completed` | `Scheduled` | - |
| 2026-07-16 23:01:10 | 2026-07-16 23:05:55 | `Completed` | `Scheduled` | - |

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

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2026-07-10 13:31:09 | 2026-07-10 13:31:09 | `Disabled` | `Scheduled` | - |
| 2026-07-10 12:32:03 | 2026-07-10 12:34:55 | `Completed` | `Scheduled` | - |
| 2026-07-10 11:31:14 | 2026-07-10 11:34:54 | `Completed` | `Scheduled` | - |
| 2026-07-10 10:32:14 | 2026-07-10 10:38:18 | `Completed` | `Scheduled` | - |
| 2026-07-10 09:31:13 | 2026-07-10 09:37:23 | `Completed` | `Scheduled` | - |

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

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2026-09-15 06:01:09 | 2026-09-15 06:04:26 | `Completed` | `Scheduled` | - |
| 2026-09-14 06:01:11 | 2026-09-14 06:07:05 | `Completed` | `Scheduled` | - |
| 2026-09-13 06:01:14 | 2026-09-13 06:06:41 | `Completed` | `Scheduled` | - |
| 2026-09-12 06:01:16 | 2026-09-12 06:07:48 | `Completed` | `Scheduled` | - |
| 2026-09-11 06:01:14 | 2026-09-11 06:04:51 | `Completed` | `Scheduled` | - |

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

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2026-09-14 20:32:06 | 2026-09-14 20:38:51 | `Completed` | `Scheduled` | - |
| 2026-09-13 20:32:00 | 2026-09-13 20:38:29 | `Completed` | `Scheduled` | - |
| 2026-09-12 20:32:12 | 2026-09-12 20:38:23 | `Completed` | `Scheduled` | - |
| 2026-09-11 20:33:22 | 2026-09-11 20:39:06 | `Completed` | `Scheduled` | - |
| 2026-09-10 20:32:06 | 2026-09-10 20:38:47 | `Completed` | `Scheduled` | - |

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

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2026-09-15 11:04:11 | - | `Unknown` | `Scheduled` | - |
| 2026-09-15 10:32:08 | 2026-09-15 10:37:31 | `Completed` | `Scheduled` | - |
| 2026-09-15 10:03:10 | 2026-09-15 10:07:34 | `Completed` | `Scheduled` | - |
| 2026-09-15 09:31:08 | 2026-09-15 09:34:38 | `Completed` | `Scheduled` | - |
| 2026-09-15 09:02:09 | 2026-09-15 09:05:23 | `Completed` | `Scheduled` | - |

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

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2026-02-02 14:04:16 | 2026-02-02 14:04:16 | `Disabled` | `Scheduled` | - |
| 2026-02-02 13:32:10 | 2026-02-02 13:47:09 | `Completed` | `Scheduled` | - |
| 2026-02-02 13:04:15 | 2026-02-02 13:18:20 | `Completed` | `Scheduled` | - |
| 2026-02-02 12:31:19 | 2026-02-02 12:46:46 | `Completed` | `Scheduled` | - |
| 2026-02-02 12:04:13 | 2026-02-02 12:18:29 | `Completed` | `Scheduled` | - |

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

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2026-09-15 11:04:17 | - | `Unknown` | `Scheduled` | - |
| 2026-09-15 10:32:07 | 2026-09-15 10:38:53 | `Completed` | `Scheduled` | - |
| 2026-09-15 10:03:09 | 2026-09-15 10:09:00 | `Completed` | `Scheduled` | - |
| 2026-09-15 09:31:12 | 2026-09-15 09:36:56 | `Completed` | `Scheduled` | - |
| 2026-09-15 09:02:14 | 2026-09-15 09:08:06 | `Completed` | `Scheduled` | - |

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

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2026-01-26 15:31:06 | 2026-01-26 15:31:06 | `Disabled` | `Scheduled` | - |
| 2026-01-26 15:03:22 | 2026-01-26 15:10:42 | `Completed` | `Scheduled` | - |
| 2026-01-26 14:32:02 | 2026-01-26 14:38:57 | `Completed` | `Scheduled` | - |
| 2026-01-26 14:04:05 | 2026-01-26 14:10:31 | `Completed` | `Scheduled` | - |
| 2026-01-26 13:31:18 | 2026-01-26 13:38:38 | `Completed` | `Scheduled` | - |

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

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2026-03-28 23:02:15 | 2026-03-28 23:02:15 | `Disabled` | `Scheduled` | - |
| 2026-03-27 23:02:15 | 2026-03-27 23:08:15 | `Completed` | `Scheduled` | - |
| 2026-03-26 23:02:15 | 2026-03-26 23:08:03 | `Completed` | `Scheduled` | - |
| 2026-03-25 23:02:11 | 2026-03-25 23:07:53 | `Completed` | `Scheduled` | - |
| 2026-03-24 23:02:14 | 2026-03-24 23:07:49 | `Completed` | `Scheduled` | - |

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

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2026-08-18 07:02:18 | 2026-08-18 07:02:18 | `Disabled` | `Scheduled` | - |
| 2026-08-17 07:02:21 | 2026-08-17 07:13:48 | `Completed` | `Scheduled` | - |
| 2026-08-16 07:02:12 | 2026-08-16 07:13:14 | `Completed` | `Scheduled` | - |
| 2026-08-15 07:02:16 | 2026-08-15 07:13:18 | `Completed` | `Scheduled` | - |
| 2026-08-14 07:02:15 | 2026-08-14 07:13:24 | `Completed` | `Scheduled` | - |

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

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2026-09-15 10:32:04 | 2026-09-15 10:37:30 | `Completed` | `Scheduled` | - |
| 2026-09-15 09:32:05 | 2026-09-15 09:38:41 | `Completed` | `Scheduled` | - |
| 2026-09-15 08:31:08 | 2026-09-15 08:34:46 | `Completed` | `Scheduled` | - |
| 2026-09-15 07:31:08 | 2026-09-15 07:35:34 | `Completed` | `Scheduled` | - |
| 2026-09-15 06:30:18 | 2026-09-15 06:32:53 | `Completed` | `Scheduled` | - |

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
