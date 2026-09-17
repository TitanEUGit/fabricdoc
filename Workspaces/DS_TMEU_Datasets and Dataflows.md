# Workspace Documentation: DS_TMEU_Datasets and Dataflows

**Workspace ID**: `d12f5bb1-de90-4b86-97e9-223086cf4629`  
**Type**: `Fabric / PowerBI Workspace`  
**Capacity ID**: `70650ed2-f7a2-46df-96e8-8089f25db80e`  
**Description**: 🛠️ Space for Lakes/Warehouses 🏠, pipelines 🚀, and other data storage/automation items

---

## 1. Executive Summary & Newcomer Overview

> [!WARNING]
> **Legacy Storage Workspace (Pre-Fabric)**
> This workspace is primarily used for legacy data storage that predates the introduction of Microsoft Fabric and OneLake in our environment.
> **Architectural Goal:** Whenever modifying pipelines or datasets in this workspace, evaluate if the data can be migrated to OneLake (e.g., `Fabric_Prod_Workspace`) — moving from Power BI native items (Dataflows Gen1, standard datasets) to Fabric native items (Notebooks, Pipelines, Lakehouses). New infrastructure should avoid using this workspace as a primary sink.

This document contains operational and technical details for the **DS_TMEU_Datasets and Dataflows** workspace. It is designed to give new team members full visibility into key items, data models, report lineage, and refresh schedules.

## 2. Native Fabric Items Inventory

| Item Name | Item Type | Item ID | Description |
| :--- | :--- | :--- | :--- |
| **alert_ar_sharepoint_file_modified_date** | `Dashboard` | `d1e31b3c-4ef5-4c7d-bbca-28273ffd92c4` | ⚠️ Legacy Power Automate pipeline (monthly CSV copy). Monitor refresh and deprecate in the future |
| **TMEU_HC_Dataset** | `Report` | `b9f8759c-a985-4258-b6c6-5c60900b1aff` | Legacy staging report for EU-wide Headcount data. Driven by the `TMEU_HC_Dataset` semantic model |
| **alert_sharepoint** | `Report` | `6549ea36-f79e-4d59-8cf6-408cfa6ff59a` | ⚠️ Legacy Power Automate pipeline (monthly CSV copy). Monitor refresh and deprecate in the future |
| **TMR Headcount File** | `Report` | `f61c64d0-fc00-4a4a-8df0-fdd2b383de10` | Legacy staging report for Romania (TMR) Headcount data. Driven by the `TMR Headcount File` semantic model |
| **TMR PA History** | `Report` | `08295924-fe94-4f56-a21a-4d8804519ee8` | ⚠️ Legacy Power Automate pipeline (monthly CSV copy). Monitor refresh and deprecate in the future |
| **TMD PA History** | `Report` | `f8eb323b-fb1f-485f-aed9-c7a1e469b046` | ⚠️ **DO NOT DELETE** without management approval. Must verify TMD (Germany) exit deal is 100% closed and data is no longer needed by users |
| **TMU PA History** | `Report` | `514a2155-0dfe-40d0-a744-0330cb35699f` | ⚠️ Legacy Power Automate pipeline (monthly CSV copy). Monitor refresh and deprecate in the future |
| **TMEU TIV and MS** | `Report` | `cbd4b531-6c52-42b1-b5c5-7b2856c3ba0e` | ⚠️ Extremely legacy report for Wholegoods market data (TIV = Total Industry Volume). Candidate for deletion |
| **TMEU Parts Inventory Staging** | `Report` | `6859a591-023a-4a6d-bd93-50af72d69347` | ⚠️ Legacy Power Automate pipeline (monthly CSV copy). Monitor refresh and deprecate in the future |
| **TMD Parts Inventory Staging** | `Report` | `c03f27f1-1e48-4c62-bc2b-0066a38554bd` | ⚠️ **DO NOT DELETE** without management approval. Must verify TMD (Germany) exit deal is 100% closed and data is no longer needed by users |
| **1C SQL Ledger Data** | `Report` | `a7952345-0ef8-4f55-aded-b1669dd7cc5d` | Auto-generated report for the semantic model bridging raw 1C data and the IT costs pipeline |
| **EU IT Expenses Staging** | `Report` | `8bc26454-168d-4db2-80da-bc97aeae63f4` | ⚠️ Legacy report for IT costs calculation |
| **TMU Sales Backlog Staging** | `Report` | `cec2dae3-2f80-4757-b25b-f7987ec635be` | ⚠️ Legacy Power Automate pipeline (monthly CSV copy). Monitor refresh and deprecate in the future |
| **TMEU IT Devices Users** | `Report` | `eeadc0b6-b631-4b72-b4a1-5459decbc155` | ⚠️ Legacy report (now automated elsewhere). Monitor and consider for deletion |
| **Zoho Dataset** | `Report` | `138d117b-a120-4d48-be0b-3d1b9b80f965` | ⚠️ Legacy report (now automated elsewhere). Monitor and consider for deletion |
| **TMEU_HC_Dataset** | `SemanticModel` | `f9a0fe7e-b471-4e05-a381-c953fd1fec24` | Processes manual OPS Package Excels from SharePoint monthly. ⚠️ **Fragile:** Prone to breaking due to manual data entry errors in the source Excels |
| **alert_sharepoint** | `SemanticModel` | `99fc1dac-c34a-453e-ad54-d35434dab6a9` | ⚠️ Legacy Power Automate pipeline (monthly CSV copy). Monitor refresh and deprecate in the future |
| **TMR Headcount File** | `SemanticModel` | `e53c9781-f5f6-462f-8712-4f1d2fd4c0ef` | Processes manual OPS Package Excels from SharePoint monthly. ⚠️ **Fragile:** Prone to breaking due to manual data entry errors in the source Excels |
| **TMR PA History** | `SemanticModel` | `707be0b8-6f26-4354-9bb2-08bf71a155c0` | ⚠️ Legacy Power Automate pipeline (monthly CSV copy). Monitor refresh and deprecate in the future |
| **TMD PA History** | `SemanticModel` | `73b1811a-a5d7-47b5-aaf7-ef28841cbae0` | ⚠️ **DO NOT DELETE** without management approval. Must verify TMD (Germany) exit deal is 100% closed and data is no longer needed by users |
| **TMU PA History** | `SemanticModel` | `b2119e5e-b4ee-46b1-b67b-c943981d46b5` | ⚠️ Legacy Power Automate pipeline (monthly CSV copy). Monitor refresh and deprecate in the future |
| **Staging TMU Inventory** | `SemanticModel` | `abaff326-14a3-4ef9-a000-e36913fa5f4f` | ⚠️ Legacy TMU inventory dataset (bundled with Power Automate in the past). Candidate for deletion |
| **TMEU TIV and MS** | `SemanticModel` | `b5f3ee4d-f7d1-4ae9-a05b-0b36110acd08` | ⚠️ Extremely legacy Wholegoods market data based on manual Excel files from former employees. Candidate for deletion |
| **TMEU Parts Inventory Staging** | `SemanticModel` | `43ac2f83-8541-4894-8a5a-4916eb084327` | ⚠️ Legacy Power Automate pipeline (monthly CSV copy). Monitor refresh and deprecate in the future |
| **TMD Parts Inventory Staging** | `SemanticModel` | `fb8b36d5-bff0-4308-bdba-7b752deaf8a8` | ⚠️ **DO NOT DELETE** without management approval. Must verify TMD (Germany) exit deal is 100% closed and data is no longer needed by users |
| **1C SQL Ledger Data** | `SemanticModel` | `b46cf783-91f2-4da3-9656-ca9a2e4317db` | Acts as a bridge semantic model between the raw 1C (1s) database and the IT costs pipeline |
| **EU IT Expenses Staging** | `SemanticModel` | `644f3fb9-a8ba-4eaf-94d0-cc3e8968577f` | ⚠️ Legacy (pre-Fabric, Power Automate driven) calculation of IT costs. Candidate for deletion if no longer needed by business |
| **TMU Sales Backlog Staging** | `SemanticModel` | `6dbc849f-4f47-4b32-80d0-d0550020c1c5` | ⚠️ Legacy Power Automate pipeline (monthly CSV copy). Monitor refresh and deprecate in the future |
| **TMEU IT Devices Users** | `SemanticModel` | `7d81e1fe-3853-42db-a0a6-59778f12532d` | ⚠️ Legacy dataset (now automated elsewhere). Monitor and consider for deletion |
| **Zoho Dataset** | `SemanticModel` | `4c6de12d-dc63-4152-8c1e-79ed38cc792b` | ⚠️ Legacy dataset (now automated elsewhere). Monitor and consider for deletion |

## 3. Semantic Models (Datasets) & Refresh Schedules

### Semantic Model: TMEU_HC_Dataset
- **Dataset ID**: `f9a0fe7e-b471-4e05-a381-c953fd1fec24`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (DISABLED ❌):
- **Frequency**: Monday
- **Scheduled Times**: `05:00` (GTB Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `SharePointList` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/collaboration/'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2026-09-14 02:00:23 | 2026-09-14 02:36:37 | `Failed` | `Scheduled` | {"errorCode":"ModelRefresh_ShortMessage_Process... |
| 2026-09-07 02:00:14 | 2026-09-07 02:41:12 | `Failed` | `Scheduled` | {"errorCode":"ModelRefresh_ShortMessage_Process... |
| 2026-08-31 02:00:15 | 2026-08-31 02:36:53 | `Failed` | `Scheduled` | {"errorCode":"ModelRefresh_ShortMessage_Process... |
| 2026-08-24 02:00:14 | 2026-08-24 02:38:23 | `Failed` | `Scheduled` | {"errorCode":"ModelRefresh_ShortMessage_Process... |
| 2026-08-19 13:47:45 | 2026-08-19 14:23:34 | `Failed` | `OnDemand` | {"errorCode":"ModelRefresh_ShortMessage_Process... |

### Semantic Model: alert_sharepoint
- **Dataset ID**: `99fc1dac-c34a-453e-ad54-d35434dab6a9`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `01:00` (FLE Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `SharePointList` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/tmua/'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2026-09-14 22:01:09 | 2026-09-14 22:08:14 | `Completed` | `Scheduled` | - |
| 2026-09-13 22:01:17 | 2026-09-13 22:07:13 | `Completed` | `Scheduled` | - |
| 2026-09-12 22:01:17 | 2026-09-12 22:07:35 | `Completed` | `Scheduled` | - |
| 2026-09-11 22:01:18 | 2026-09-11 22:07:36 | `Completed` | `Scheduled` | - |
| 2026-09-10 22:01:21 | 2026-09-10 22:07:02 | `Completed` | `Scheduled` | - |

### Semantic Model: TMR Headcount File
- **Dataset ID**: `e53c9781-f5f6-462f-8712-4f1d2fd4c0ef`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (DISABLED ❌):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `N/A` (FLE Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `Web` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/Collaboration/Shared%20Documents/RO_HR/Reporting/HC%20report/2024/TMR_HC%20report_rev%20as%20per%20service%20dashboard.xlsx'}`
- Type: `SharePointList` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/collaboration/'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2026-09-03 21:01:24 | 2026-09-03 21:57:28 | `Failed` | `Scheduled` | {"errorCode":"ModelRefresh_ShortMessage_Process... |
| 2026-09-03 06:58:31 | 2026-09-03 07:53:47 | `Failed` | `OnDemand` | {"errorCode":"ModelRefresh_ShortMessage_Process... |
| 2026-09-02 21:02:30 | 2026-09-02 22:20:07 | `Failed` | `Scheduled` | {"errorCode":"ModelRefresh_ShortMessage_Process... |
| 2026-09-01 21:01:28 | 2026-09-01 21:15:24 | `Completed` | `Scheduled` | - |
| 2026-08-31 21:01:23 | 2026-08-31 21:15:49 | `Completed` | `Scheduled` | - |

### Semantic Model: TMR PA History
- **Dataset ID**: `707be0b8-6f26-4354-9bb2-08bf71a155c0`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Monday
- **Scheduled Times**: `01:00` (GTB Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `SharePointList` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/collaboration/'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2025-12-28 23:01:11 | 2025-12-28 23:01:11 | `Disabled` | `Scheduled` | - |
| 2025-12-21 23:01:06 | 2025-12-21 23:10:30 | `Completed` | `Scheduled` | - |
| 2025-12-14 23:00:21 | 2025-12-14 23:10:28 | `Completed` | `Scheduled` | - |
| 2025-12-07 23:01:17 | 2025-12-07 23:10:59 | `Completed` | `Scheduled` | - |
| 2025-11-30 23:01:06 | 2025-11-30 23:08:55 | `Completed` | `Scheduled` | - |

### Semantic Model: TMD PA History
- **Dataset ID**: `73b1811a-a5d7-47b5-aaf7-ef28841cbae0`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `01:00` (GTB Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `SharePointList` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/collaboration/'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2026-01-03 23:00:09 | 2026-01-03 23:00:09 | `Disabled` | `Scheduled` | - |
| 2026-01-02 23:01:03 | 2026-01-02 23:07:41 | `Completed` | `Scheduled` | - |
| 2026-01-01 23:01:09 | 2026-01-01 23:09:45 | `Completed` | `Scheduled` | - |
| 2025-12-31 23:00:13 | 2025-12-31 23:06:16 | `Completed` | `Scheduled` | - |
| 2025-12-30 23:01:03 | 2025-12-30 23:06:23 | `Completed` | `Scheduled` | - |

### Semantic Model: TMU PA History
- **Dataset ID**: `b2119e5e-b4ee-46b1-b67b-c943981d46b5`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `01:00` (FLE Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `SharePointList` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/collaboration/'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2026-09-14 22:01:18 | 2026-09-14 22:13:23 | `Completed` | `Scheduled` | - |
| 2026-09-13 22:01:18 | 2026-09-13 22:12:38 | `Completed` | `Scheduled` | - |
| 2026-09-12 22:01:19 | 2026-09-12 22:13:16 | `Completed` | `Scheduled` | - |
| 2026-09-11 22:01:20 | 2026-09-11 22:13:44 | `Completed` | `Scheduled` | - |
| 2026-09-10 22:01:23 | 2026-09-10 22:13:01 | `Completed` | `Scheduled` | - |

### Semantic Model: Staging TMU Inventory
- **Dataset ID**: `abaff326-14a3-4ef9-a000-e36913fa5f4f`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `07:00` (FLE Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `Web` | Connection: `{'url': 'https://parts.titanmachinery.ua/'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2026-05-10 04:01:17 | 2026-05-10 04:01:17 | `Disabled` | `Scheduled` | - |
| 2026-05-09 04:01:07 | 2026-05-09 04:07:09 | `Completed` | `Scheduled` | - |
| 2026-05-08 04:01:18 | 2026-05-08 04:09:16 | `Completed` | `Scheduled` | - |
| 2026-05-07 04:01:07 | 2026-05-07 04:07:23 | `Completed` | `Scheduled` | - |
| 2026-05-06 04:01:07 | 2026-05-06 04:07:34 | `Completed` | `Scheduled` | - |

### Semantic Model: TMEU TIV and MS
- **Dataset ID**: `b5f3ee4d-f7d1-4ae9-a05b-0b36110acd08`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `01:00` (FLE Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `Web` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/Collaboration/Shared%20Documents/INT_Logistics/Marketshare%2012months%20rolling/MS%2012%20months%20rolling.xlsm'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2026-09-14 22:01:02 | 2026-09-14 22:03:18 | `Completed` | `Scheduled` | - |
| 2026-09-13 22:01:21 | 2026-09-13 22:06:57 | `Completed` | `Scheduled` | - |
| 2026-09-12 22:01:21 | 2026-09-12 22:06:05 | `Completed` | `Scheduled` | - |
| 2026-09-11 22:01:23 | 2026-09-11 22:05:47 | `Completed` | `Scheduled` | - |
| 2026-09-10 22:01:26 | 2026-09-10 22:05:41 | `Completed` | `Scheduled` | - |

### Semantic Model: TMEU Parts Inventory Staging
- **Dataset ID**: `43ac2f83-8541-4894-8a5a-4916eb084327`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `08:00` (FLE Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `Extension` | Connection: `{'path': 'PowerPlatformDataflows', 'kind': 'PowerPlatformDataflows'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmr_opspackage', 'database': 'tmr ops package'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmb_opspackage', 'database': 'tmb ops package'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmd_aftersales', 'database': 'tmd parts sales'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2026-09-15 05:01:02 | 2026-09-15 05:06:21 | `Completed` | `Scheduled` | - |
| 2026-09-14 05:00:11 | 2026-09-14 05:03:33 | `Completed` | `Scheduled` | - |
| 2026-09-13 05:01:16 | 2026-09-13 05:06:43 | `Completed` | `Scheduled` | - |
| 2026-09-12 05:01:16 | 2026-09-12 05:08:56 | `Completed` | `Scheduled` | - |
| 2026-09-11 05:01:04 | 2026-09-11 05:04:34 | `Completed` | `Scheduled` | - |

### Semantic Model: TMD Parts Inventory Staging
- **Dataset ID**: `fb8b36d5-bff0-4308-bdba-7b752deaf8a8`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (DISABLED ❌):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `15:00` (UTC)

**Connected Data Sources (Lineage)**:
- Type: `SharePointList` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/collaboration/'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2025-08-18 07:51:16 | 2025-08-18 08:35:04 | `Completed` | `ViaApi` | - |
| 2025-08-13 09:12:56 | 2025-08-13 09:58:20 | `Completed` | `ViaApi` | - |
| 2025-06-19 05:54:14 | 2025-06-19 05:54:20 | `Cancelled` | `OnDemand` | {"errorCode":"ModelRefresh_ShortMessage_Cancell... |
| 2025-06-18 15:32:26 | 2025-06-18 16:38:54 | `Completed` | `ViaApi` | - |
| 2025-06-18 12:21:09 | 2025-06-18 13:18:49 | `Completed` | `ViaApi` | - |

### Semantic Model: 1C SQL Ledger Data
- **Dataset ID**: `b46cf783-91f2-4da3-9656-ca9a2e4317db`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `01:00` (UTC)

**Connected Data Sources (Lineage)**:
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmu_opspackage', 'database': 'tmu ops package'}`
- Type: `Sql` | Connection: `{'server': '10.71.3.14', 'database': 'dailywork'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2026-09-15 11:00:21 | - | `Unknown` | `DataFactory` | - |
| 2026-09-15 01:01:09 | 2026-09-15 01:11:57 | `Completed` | `Scheduled` | - |
| 2026-09-14 11:00:23 | 2026-09-14 11:08:14 | `Completed` | `DataFactory` | - |
| 2026-09-14 01:00:30 | 2026-09-14 01:10:46 | `Completed` | `Scheduled` | - |
| 2026-09-13 11:00:37 | 2026-09-13 11:07:39 | `Completed` | `DataFactory` | - |

### Semantic Model: EU IT Expenses Staging
- **Dataset ID**: `644f3fb9-a8ba-4eaf-94d0-cc3e8968577f`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `09:00` (FLE Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmb_opspackage', 'database': 'tmb ops package'}`
- Type: `SharePointList` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/it/management/'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmr_opspackage', 'database': 'tmr ops package'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmd_finance', 'database': 'tmd p&l'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/ds_tmeu_datasets and dataflows', 'database': '1c sql ledger data'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tma_finance', 'database': 'eoc entity report'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2026-07-18 06:01:30 | 2026-07-18 06:01:30 | `Disabled` | `Scheduled` | - |
| 2026-07-17 06:01:10 | 2026-07-17 06:04:53 | `Completed` | `Scheduled` | - |
| 2026-07-16 06:01:19 | 2026-07-16 06:07:36 | `Completed` | `Scheduled` | - |
| 2026-07-15 06:00:18 | 2026-07-15 06:04:57 | `Completed` | `Scheduled` | - |
| 2026-07-14 06:01:08 | 2026-07-14 06:06:01 | `Completed` | `Scheduled` | - |

### Semantic Model: TMU Sales Backlog Staging
- **Dataset ID**: `6dbc849f-4f47-4b32-80d0-d0550020c1c5`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (DISABLED ❌):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `09:00` (UTC)

**Connected Data Sources (Lineage)**:
- Type: `SharePointList` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/collaboration/'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2026-06-28 16:00:09 | 2026-06-28 16:30:18 | `Failed` | `ViaApi` | {"errorCode":"ModelRefresh_ShortMessage_Process... |
| 2026-05-28 16:00:05 | 2026-05-28 16:05:46 | `Completed` | `ViaApi` | - |
| 2026-04-28 16:00:07 | 2026-04-28 16:05:39 | `Completed` | `ViaApi` | - |
| 2026-03-28 16:00:10 | 2026-03-28 16:22:34 | `Failed` | `ViaApi` | {"errorCode":"ModelRefresh_ShortMessage_Process... |
| 2026-02-28 16:00:10 | 2026-02-28 16:32:31 | `Failed` | `ViaApi` | {"errorCode":"ModelRefresh_ShortMessage_Process... |

### Semantic Model: TMEU IT Devices Users
- **Dataset ID**: `7d81e1fe-3853-42db-a0a6-59778f12532d`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `05:00` (FLE Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `SharePointList` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/it/operations/'}`
- Type: `SharePointList` | Connection: `{'url': 'https://titanmachinery365europe.sharepoint.com/sites/hr-dataset-europe/'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/ds_tmeu_datasets and dataflows', 'database': 'zoho dataset'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2026-01-10 03:01:06 | 2026-01-10 03:01:06 | `Disabled` | `Scheduled` | - |
| 2026-01-09 03:01:05 | 2026-01-09 03:05:20 | `Completed` | `Scheduled` | - |
| 2026-01-08 03:01:02 | 2026-01-08 03:05:01 | `Completed` | `Scheduled` | - |
| 2026-01-07 03:01:02 | 2026-01-07 03:05:40 | `Completed` | `Scheduled` | - |
| 2026-01-06 03:01:07 | 2026-01-06 03:07:04 | `Completed` | `Scheduled` | - |

### Semantic Model: Zoho Dataset
- **Dataset ID**: `4c6de12d-dc63-4152-8c1e-79ed38cc792b`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `03:00` (FLE Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `Web` | Connection: `{'url': 'https://accounts.zoho.eu/'}`
- Type: `Web` | Connection: `{'url': 'https://endpointcentral.manageengine.eu/'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2026-05-11 00:02:09 | 2026-05-11 00:02:09 | `Disabled` | `Scheduled` | - |
| 2026-05-10 00:01:09 | 2026-05-10 00:12:28 | `Completed` | `Scheduled` | - |
| 2026-05-09 00:02:06 | 2026-05-09 00:14:42 | `Completed` | `Scheduled` | - |
| 2026-05-08 00:01:12 | 2026-05-08 00:12:20 | `Completed` | `Scheduled` | - |
| 2026-05-07 00:02:13 | 2026-05-07 00:15:05 | `Completed` | `Scheduled` | - |

## 4. Power BI Reports Inventory

| Report Name | Report ID | Dataset ID | Web URL |
| :--- | :--- | :--- | :--- |
| **TMEU_HC_Dataset** | `b9f8759c-a985-4258-b6c6-5c60900b1aff` | `f9a0fe7e-b471-4e05-a381-c953fd1fec24` | [Open Report](https://app.powerbi.com/groups/d12f5bb1-de90-4b86-97e9-223086cf4629/reports/b9f8759c-a985-4258-b6c6-5c60900b1aff) |
| **alert_sharepoint** | `6549ea36-f79e-4d59-8cf6-408cfa6ff59a` | `99fc1dac-c34a-453e-ad54-d35434dab6a9` | [Open Report](https://app.powerbi.com/groups/d12f5bb1-de90-4b86-97e9-223086cf4629/reports/6549ea36-f79e-4d59-8cf6-408cfa6ff59a) |
| **TMR Headcount File** | `f61c64d0-fc00-4a4a-8df0-fdd2b383de10` | `e53c9781-f5f6-462f-8712-4f1d2fd4c0ef` | [Open Report](https://app.powerbi.com/groups/d12f5bb1-de90-4b86-97e9-223086cf4629/reports/f61c64d0-fc00-4a4a-8df0-fdd2b383de10) |
| **TMR PA History** | `08295924-fe94-4f56-a21a-4d8804519ee8` | `707be0b8-6f26-4354-9bb2-08bf71a155c0` | [Open Report](https://app.powerbi.com/groups/d12f5bb1-de90-4b86-97e9-223086cf4629/reports/08295924-fe94-4f56-a21a-4d8804519ee8) |
| **TMD PA History** | `f8eb323b-fb1f-485f-aed9-c7a1e469b046` | `73b1811a-a5d7-47b5-aaf7-ef28841cbae0` | [Open Report](https://app.powerbi.com/groups/d12f5bb1-de90-4b86-97e9-223086cf4629/reports/f8eb323b-fb1f-485f-aed9-c7a1e469b046) |
| **TMU PA History** | `514a2155-0dfe-40d0-a744-0330cb35699f` | `b2119e5e-b4ee-46b1-b67b-c943981d46b5` | [Open Report](https://app.powerbi.com/groups/d12f5bb1-de90-4b86-97e9-223086cf4629/reports/514a2155-0dfe-40d0-a744-0330cb35699f) |
| **TMEU TIV and MS** | `cbd4b531-6c52-42b1-b5c5-7b2856c3ba0e` | `b5f3ee4d-f7d1-4ae9-a05b-0b36110acd08` | [Open Report](https://app.powerbi.com/groups/d12f5bb1-de90-4b86-97e9-223086cf4629/reports/cbd4b531-6c52-42b1-b5c5-7b2856c3ba0e) |
| **TMEU Parts Inventory Staging** | `6859a591-023a-4a6d-bd93-50af72d69347` | `43ac2f83-8541-4894-8a5a-4916eb084327` | [Open Report](https://app.powerbi.com/groups/d12f5bb1-de90-4b86-97e9-223086cf4629/reports/6859a591-023a-4a6d-bd93-50af72d69347) |
| **TMD Parts Inventory Staging** | `c03f27f1-1e48-4c62-bc2b-0066a38554bd` | `fb8b36d5-bff0-4308-bdba-7b752deaf8a8` | [Open Report](https://app.powerbi.com/groups/d12f5bb1-de90-4b86-97e9-223086cf4629/reports/c03f27f1-1e48-4c62-bc2b-0066a38554bd) |
| **1C SQL Ledger Data** | `a7952345-0ef8-4f55-aded-b1669dd7cc5d` | `b46cf783-91f2-4da3-9656-ca9a2e4317db` | [Open Report](https://app.powerbi.com/groups/d12f5bb1-de90-4b86-97e9-223086cf4629/reports/a7952345-0ef8-4f55-aded-b1669dd7cc5d) |
| **EU IT Expenses Staging** | `8bc26454-168d-4db2-80da-bc97aeae63f4` | `644f3fb9-a8ba-4eaf-94d0-cc3e8968577f` | [Open Report](https://app.powerbi.com/groups/d12f5bb1-de90-4b86-97e9-223086cf4629/reports/8bc26454-168d-4db2-80da-bc97aeae63f4) |
| **TMU Sales Backlog Staging** | `cec2dae3-2f80-4757-b25b-f7987ec635be` | `6dbc849f-4f47-4b32-80d0-d0550020c1c5` | [Open Report](https://app.powerbi.com/groups/d12f5bb1-de90-4b86-97e9-223086cf4629/reports/cec2dae3-2f80-4757-b25b-f7987ec635be) |
| **TMEU IT Devices Users** | `eeadc0b6-b631-4b72-b4a1-5459decbc155` | `7d81e1fe-3853-42db-a0a6-59778f12532d` | [Open Report](https://app.powerbi.com/groups/d12f5bb1-de90-4b86-97e9-223086cf4629/reports/eeadc0b6-b631-4b72-b4a1-5459decbc155) |
| **Zoho Dataset** | `138d117b-a120-4d48-be0b-3d1b9b80f965` | `4c6de12d-dc63-4152-8c1e-79ed38cc792b` | [Open Report](https://app.powerbi.com/groups/d12f5bb1-de90-4b86-97e9-223086cf4629/reports/138d117b-a120-4d48-be0b-3d1b9b80f965) |

## 5. Dataflows & Dashboards

**Dataflows**:
- **TMU Service HR Tables** (ID: `13f50965-b993-41a5-80b4-b9ac793c8b63`)
- **TMB OPS Package Helpers** (ID: `85fdccde-c127-47f6-abca-20372d36c64d`)
- **TMR OPS Package Helpers** (ID: `8da432b8-78ee-4821-bd58-8da64ae8e734`)
- **TMD HR Tables** (ID: `15d26653-4f86-4420-be69-5f32a2ea0124`)
- **TMEU Mappings** (ID: `f4703fc2-e426-4d6b-a394-24aa3d433ca9`)
- **TMR SP Stock History** (ID: `3cf66791-50d0-4468-846a-1a54e9635fec`)
- **TMU SP Stock History** (ID: `6830a477-3276-4927-8c93-efc2ba845bf6`)
- **TMU SP Turn Ratio** (ID: `8a7a1800-b289-4364-9622-e2fe8b113158`)
- **TMU Actual WG Stock** (ID: `ec24c4cc-f0a3-46b6-9de2-9ab30b9f18ea`)
- **TMEU Parts Supplier Category** (ID: `94a3e9e8-2f55-4efc-b484-f9bf5b9f931a`)
- **TMD Parts Inventory Dataflow** (ID: `e4b02254-a584-4078-9154-e9d5f633a37f`)
- **TMEU SP Item ENG Description** (ID: `7590ec83-bbb9-45bb-ba23-b91943449d2d`)
- **TMU PIH Excel Data** (ID: `733f9633-c636-4be6-bbc2-aa05390fd661`)
- **HR Database DF** (ID: `f449640a-15cb-45b1-a943-3a7c4aff2a06`)
- **TMR OPS Package helpers P2** (ID: `f0acb7ee-7e3d-4db5-9510-74f0743e09cf`)
- **TMU Sales Backlog (Forecast)** (ID: `51bfac21-2e3d-4ea3-a3f8-ca6e1ec49ec3`)
- **TMUS Service SRT** (ID: `7b46ff70-3892-440e-ade0-5338a1b3b435`)
- **TMU Active ESCs** (ID: `cbe781c0-61f1-46b6-80d3-adefb7b09b10`)
- **TMEU WG Inventory Hardcopy** (ID: `31ee2eee-4880-46e9-8e80-d97ab5347550`)
- **TMEU HR Temp Data** (ID: `eef5623f-5daf-4e61-9f5c-5c9e07b9003a`)
**Dashboards**:
- **alert_ar_sharepoint_file_modified_date** (ID: `d1e31b3c-4ef5-4c7d-bbca-28273ffd92c4`)

---

## 6. Newcomer Operational Runbook & Notes
- **Primary Contact / Owner**: Refer to workspace access settings in Power BI portal.
- **Troubleshooting**: If a refresh fails in `DS_TMEU_Datasets and Dataflows`, inspect the failure log under section 3 above and check upstream data gateway connectivity.
