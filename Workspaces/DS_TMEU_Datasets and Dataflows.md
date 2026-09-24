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
| **TMEU IT Devices Users** | `Report` | `eeadc0b6-b631-4b72-b4a1-5459decbc155` | Active datasource for user-related Power Automate flow |
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
| **TMEU IT Devices Users** | `SemanticModel` | `7d81e1fe-3853-42db-a0a6-59778f12532d` | Active datasource for user-related Power Automate flow |
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
- **TMB OPS Package Helpers** (ID: `85fdccde-c127-47f6-abca-20372d36c64d`) — *Legacy storage for manual Excel adjustments for the Bulgaria (TMB) OPS Package*
- **TMR OPS Package Helpers** (ID: `8da432b8-78ee-4821-bd58-8da64ae8e734`) — *Legacy storage for manual Excel adjustments for the Romania (TMR) OPS Package*
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
- **TMR OPS Package helpers P2** (ID: `f0acb7ee-7e3d-4db5-9510-74f0743e09cf`) — *Legacy storage for manual Excel adjustments for the Romania (TMR) OPS Package (Part 2)*
- **TMU Sales Backlog (Forecast)** (ID: `51bfac21-2e3d-4ea3-a3f8-ca6e1ec49ec3`)
- **TMUS Service SRT** (ID: `7b46ff70-3892-440e-ade0-5338a1b3b435`)
- **TMU Active ESCs** (ID: `cbe781c0-61f1-46b6-80d3-adefb7b09b10`) — *Manual configuration table of TMU ESCs. Controls the Monday Power Automate customer interaction emails. Update this when ESCs join or leave in Ukraine.*
- **TMEU WG Inventory Hardcopy** (ID: `31ee2eee-4880-46e9-8e80-d97ab5347550`)
- **TMEU HR Temp Data** (ID: `eef5623f-5daf-4e61-9f5c-5c9e07b9003a`)
**Dashboards**:
- **alert_ar_sharepoint_file_modified_date** (ID: `d1e31b3c-4ef5-4c7d-bbca-28273ffd92c4`)

---

## 6. Newcomer Operational Runbook & Notes
- **Primary Contact / Owner**: Refer to workspace access settings in Power BI portal.
- **Troubleshooting**: If a refresh fails in `DS_TMEU_Datasets and Dataflows`, inspect the failure log under section 3 above and check upstream data gateway connectivity.
