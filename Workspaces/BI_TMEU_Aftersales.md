# Workspace Documentation: BI_TMEU_Aftersales

**Workspace ID**: `2c05a4e4-4d2d-483e-be6c-2d0ecdd9f902`  
**Type**: `Fabric / PowerBI Workspace`  
**Capacity ID**: `70650ed2-f7a2-46df-96e8-8089f25db80e`  
**Description**: Workspace for Multi-Country reports related to AfterSales Segment

---

## 1. Executive Summary & Newcomer Overview
This document contains operational and technical details for the **BI_TMEU_Aftersales** workspace. It is designed to give new team members full visibility into key items, data models, report lineage, and refresh schedules.

## 2. Native Fabric Items Inventory

| Item Name | Item Type | Item ID | Description |
| :--- | :--- | :--- | :--- |
| **SP Supplier Matrix** | `Report` | `0071d275-ff03-4571-acc1-baba66378905` | - |
| **TMEU Open Service Jobcards** | `Report` | `03a3b768-5773-4472-a5e1-f7b8bbaa976f` | - |
| **TMEU Overstocked Parts** | `Report` | `48a67a3d-6318-4069-9a26-9f994bdcebb1` | - |
| **Usage Metrics Report** | `Report` | `78471d8d-6eb4-4541-b8d9-06321355208e` | - |
| **TMEU Parts Item List** | `Report` | `e2d112a1-3a44-4ce5-9bc9-2fe0496e859a` | - |
| **TMEU Warranty Dashboard** | `Report` | `cfdf3f50-f10a-4000-bcbe-cec05722d0d6` | - |
| **SP Supplier Matrix** | `SemanticModel` | `0fc31860-861c-4131-8b73-f785f161b94a` | - |
| **TMEU Open Service Jobcards** | `SemanticModel` | `005f67d8-0096-4be7-85bd-2330fd6648a7` | - |
| **TMEU Overstocked Parts** | `SemanticModel` | `1a51c1d3-0d58-431f-88ec-8006cfe3513e` | - |
| **Usage Metrics Report** | `SemanticModel` | `6b1d9649-7e95-4d0b-ae3e-c97e0a8cf48e` | - |
| **TMEU Parts Item List** | `SemanticModel` | `5faeb973-dc3e-4165-b824-3e0f6abbd850` | - |
| **TMEU Warranty Dashboard** | `SemanticModel` | `b3c3f284-7d05-44c5-89ee-22c1f3a36250` | - |

## 3. Semantic Models (Datasets) & Refresh Schedules

### Semantic Model: SP Supplier Matrix
- **Dataset ID**: `0fc31860-861c-4131-8b73-f785f161b94a`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `07:00` (FLE Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmr_opspackage', 'database': 'tmr ops package'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmb_opspackage', 'database': 'tmb ops package'}`
- Type: `Extension` | Connection: `{'path': 'PowerPlatformDataflows', 'kind': 'PowerPlatformDataflows'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmu_opspackage', 'database': 'tmu ops package'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2026-03-23 05:01:05 | 2026-03-23 05:01:05 | `Disabled` | `Scheduled` | - |
| 2026-03-22 05:01:07 | 2026-03-22 05:03:12 | `Completed` | `Scheduled` | - |
| 2026-03-21 05:01:10 | 2026-03-21 05:03:51 | `Completed` | `Scheduled` | - |
| 2026-03-20 05:01:05 | 2026-03-20 05:03:18 | `Completed` | `Scheduled` | - |
| 2026-03-19 05:01:06 | 2026-03-19 05:03:07 | `Completed` | `Scheduled` | - |

### Semantic Model: TMEU Open Service Jobcards
- **Dataset ID**: `005f67d8-0096-4be7-85bd-2330fd6648a7`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `08:30` (FLE Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `Sql` | Connection: `{'server': '10.75.1.7', 'database': 'jetnavdwh'}`
- Type: `ODBC` | Connection: `{'connectionString': 'dsn=timeline - tmd'}`
- Type: `Web` | Connection: `{'url': 'https://titanmachineryro.frontu.com/'}`
- Type: `Web` | Connection: `{'url': 'https://titanmachinerybg.frontu.com/'}`
- Type: `Sql` | Connection: `{'server': 'cwgz5ola5r6u5e4heu5qw3drgy-zzqhzdizzmcurky2zbgw4gw7la.datawarehouse.fabric.microsoft.com', 'database': 'tmu_bronze_lakehouse'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2026-09-15 05:30:23 | 2026-09-15 05:39:55 | `Completed` | `Scheduled` | - |
| 2026-09-14 05:31:15 | 2026-09-14 05:41:44 | `Completed` | `Scheduled` | - |
| 2026-09-13 05:31:17 | 2026-09-13 05:46:50 | `Completed` | `Scheduled` | - |
| 2026-09-12 05:31:12 | 2026-09-12 05:42:03 | `Completed` | `Scheduled` | - |
| 2026-09-11 05:31:14 | 2026-09-11 05:41:12 | `Completed` | `Scheduled` | - |

### Semantic Model: TMEU Overstocked Parts
- **Dataset ID**: `1a51c1d3-0d58-431f-88ec-8006cfe3513e`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday
- **Scheduled Times**: `09:00` (FLE Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `Extension` | Connection: `{'path': 'PowerPlatformDataflows', 'kind': 'PowerPlatformDataflows'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmr_opspackage', 'database': 'tmr ops package'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmd_aftersales', 'database': 'tmd parts sales'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmb_opspackage', 'database': 'tmb ops package'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmu_opspackage', 'database': 'tmu ops package'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2026-09-13 06:01:15 | 2026-09-13 06:05:50 | `Completed` | `Scheduled` | - |
| 2026-09-06 06:01:12 | 2026-09-06 06:05:33 | `Completed` | `Scheduled` | - |
| 2026-08-30 06:01:18 | 2026-08-30 06:06:34 | `Completed` | `Scheduled` | - |
| 2026-08-23 06:00:27 | 2026-08-23 06:05:05 | `Completed` | `Scheduled` | - |
| 2026-08-16 06:00:33 | 2026-08-16 06:05:03 | `Completed` | `Scheduled` | - |

### Semantic Model: Usage Metrics Report
- **Dataset ID**: `6b1d9649-7e95-4d0b-ae3e-c97e0a8cf48e`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `06:25` (UTC)

**Connected Data Sources (Lineage)**:
- Type: `Extension` | Connection: `{'path': 'UsageMetricsDataConnector', 'kind': 'UsageMetricsDataConnector'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2025-07-21 06:26:32 | 2025-07-21 06:26:32 | `Disabled` | `Scheduled` | - |
| 2025-07-20 06:25:02 | 2025-07-20 06:25:19 | `Completed` | `Scheduled` | - |
| 2025-07-19 06:25:10 | 2025-07-19 06:25:43 | `Completed` | `Scheduled` | - |
| 2025-07-18 06:25:01 | 2025-07-18 06:25:26 | `Completed` | `Scheduled` | - |
| 2025-07-17 06:25:11 | 2025-07-17 06:25:31 | `Completed` | `Scheduled` | - |

### Semantic Model: TMEU Parts Item List
- **Dataset ID**: `5faeb973-dc3e-4165-b824-3e0f6abbd850`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Monday
- **Scheduled Times**: `08:00` (UTC)

**Connected Data Sources (Lineage)**:
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmd_aftersales', 'database': 'tmd parts sales'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmr_opspackage', 'database': 'tmr ops package'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmu_opspackage', 'database': 'tmu ops package'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmb_opspackage', 'database': 'tmb ops package'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2026-09-14 08:01:02 | 2026-09-14 08:02:58 | `Completed` | `Scheduled` | - |
| 2026-09-07 08:02:07 | 2026-09-07 08:05:55 | `Completed` | `Scheduled` | - |
| 2026-08-31 08:02:06 | 2026-08-31 08:05:51 | `Completed` | `Scheduled` | - |
| 2026-08-24 08:02:07 | 2026-08-24 08:06:03 | `Completed` | `Scheduled` | - |
| 2026-08-17 08:02:03 | 2026-08-17 08:05:15 | `Completed` | `Scheduled` | - |

### Semantic Model: TMEU Warranty Dashboard
- **Dataset ID**: `b3c3f284-7d05-44c5-89ee-22c1f3a36250`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `06:00` (FLE Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `Sql` | Connection: `{'server': '10.75.1.7', 'database': 'jetnavdwh'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2026-09-15 03:00:28 | 2026-09-15 03:13:51 | `Completed` | `Scheduled` | - |
| 2026-09-14 03:01:04 | 2026-09-14 03:10:46 | `Completed` | `Scheduled` | - |
| 2026-09-13 03:01:20 | 2026-09-13 03:13:19 | `Completed` | `Scheduled` | - |
| 2026-09-12 03:01:15 | 2026-09-12 03:12:01 | `Completed` | `Scheduled` | - |
| 2026-09-11 03:01:17 | 2026-09-11 03:10:24 | `Completed` | `Scheduled` | - |

## 4. Power BI Reports Inventory

| Report Name | Report ID | Dataset ID | Web URL |
| :--- | :--- | :--- | :--- |
| **SP Supplier Matrix** | `0071d275-ff03-4571-acc1-baba66378905` | `0fc31860-861c-4131-8b73-f785f161b94a` | [Open Report](https://app.powerbi.com/groups/2c05a4e4-4d2d-483e-be6c-2d0ecdd9f902/reports/0071d275-ff03-4571-acc1-baba66378905) |
| **TMEU Open Service Jobcards** | `03a3b768-5773-4472-a5e1-f7b8bbaa976f` | `005f67d8-0096-4be7-85bd-2330fd6648a7` | [Open Report](https://app.powerbi.com/groups/2c05a4e4-4d2d-483e-be6c-2d0ecdd9f902/reports/03a3b768-5773-4472-a5e1-f7b8bbaa976f) |
| **TMEU Overstocked Parts** | `48a67a3d-6318-4069-9a26-9f994bdcebb1` | `1a51c1d3-0d58-431f-88ec-8006cfe3513e` | [Open Report](https://app.powerbi.com/groups/2c05a4e4-4d2d-483e-be6c-2d0ecdd9f902/reports/48a67a3d-6318-4069-9a26-9f994bdcebb1) |
| **Usage Metrics Report** | `78471d8d-6eb4-4541-b8d9-06321355208e` | `6b1d9649-7e95-4d0b-ae3e-c97e0a8cf48e` | [Open Report](https://app.powerbi.com/groups/2c05a4e4-4d2d-483e-be6c-2d0ecdd9f902/reports/78471d8d-6eb4-4541-b8d9-06321355208e) |
| **TMEU Parts Item List** | `e2d112a1-3a44-4ce5-9bc9-2fe0496e859a` | `5faeb973-dc3e-4165-b824-3e0f6abbd850` | [Open Report](https://app.powerbi.com/groups/2c05a4e4-4d2d-483e-be6c-2d0ecdd9f902/reports/e2d112a1-3a44-4ce5-9bc9-2fe0496e859a) |
| **TMEU Warranty Dashboard** | `cfdf3f50-f10a-4000-bcbe-cec05722d0d6` | `b3c3f284-7d05-44c5-89ee-22c1f3a36250` | [Open Report](https://app.powerbi.com/groups/2c05a4e4-4d2d-483e-be6c-2d0ecdd9f902/reports/cfdf3f50-f10a-4000-bcbe-cec05722d0d6) |

## 5. Dataflows & Dashboards

*No dataflows or dashboards in this workspace.*

---

## 6. Newcomer Operational Runbook & Notes
- **Primary Contact / Owner**: Refer to workspace access settings in Power BI portal.
- **Troubleshooting**: If a refresh fails in `BI_TMEU_Aftersales`, inspect the failure log under section 3 above and check upstream data gateway connectivity.
