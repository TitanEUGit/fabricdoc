# Workspace Documentation: Fabric_Prod_Workspace

**Workspace ID**: `8d7c60ce-cb19-4805-ab1a-c84d6e1adf58`  
**Type**: `Fabric / PowerBI Workspace`  
**Capacity ID**: `70650ed2-f7a2-46df-96e8-8089f25db80e`  
**Description**: Production workspace for Lakes 🌊, DWHs🏠, and pipelines🚀.

---

## 1. Executive Summary & Newcomer Overview
This document contains operational and technical details for the **Fabric_Prod_Workspace** workspace. It is designed to give new team members full visibility into key items, data models, report lineage, and refresh schedules.

## 2. Native Fabric Items Inventory

| Item Name | Item Type | Item ID | Description |
| :--- | :--- | :--- | :--- |
| **TMA_NAV_Silver_Dataset** | `SemanticModel` | `9b32e872-baeb-42f6-9af4-fbdf159b4e84` | - |
| **TMU Assortment Budget** | `SQLEndpoint` | `e09f5a5f-a58a-4aa4-ac3a-139912749507` | - |
| **TMU_Bronze_Lakehouse** | `SQLEndpoint` | `17d5461e-20bc-45c6-9eb1-6afa91eb065e` | - |
| **TMR_Bronze_Warehouse** | `Warehouse` | `6077f433-81c5-44be-a453-f06b5ff07c6d` | - |
| **TMU_Competition_Lakehouse** | `SQLEndpoint` | `dc7f9374-fe89-4315-b44d-58291b5efe1d` | - |
| **TMEU_Bronze_Lakehouse** | `SQLEndpoint` | `6a19f597-3ff7-408f-b103-d3517ad6ab9b` | - |
| **TMA_NAV_Lakehouse** | `SQLEndpoint` | `629832e7-3d1f-4f61-bbbf-eb7575152505` | - |
| **TMEU_IT_DB** | `SQLEndpoint` | `d90fd9ee-ed89-46e3-9c74-1b6a55812d8b` | - |
| **TMEU_Freshservice_Lakehouse** | `SQLEndpoint` | `3843e184-792a-4561-bc60-315707dbccb0` | - |
| **StagingLakehouseForDataflows_20260408083147** | `SQLEndpoint` | `36e18822-b61d-4df2-81ed-26f3c5e71ac3` | - |
| **StagingWarehouseForDataflows_20260408083200** | `Warehouse` | `412b7a71-c497-445f-a7db-a270769a926d` | - |
| **TMEU_ERP_RAW_Lakehouse** | `SQLEndpoint` | `97f232ba-88fc-42b4-8c02-ed8464174ff8` | - |
| **Credit_Limit_Leger_DB** | `SQLEndpoint` | `be997c00-c623-4179-94a9-4847daf7edba` | - |
| **TMU Assortment Budget** | `SQLDatabase` | `2ad254ce-44d5-4c67-9aee-a34267f0a56d` | - |
| **TMUBudgetAssortmentUDFv2** | `UserDataFunction` | `6e202183-01cf-4c57-9f67-1001135035b4` | - |
| **TMU_Bronze_Lakehouse** | `Lakehouse` | `4b774a06-6665-49a6-9c84-c8168f27c717` | - |
| **TMU 1C Requests Pipeline** | `DataPipeline` | `8a316947-bcd9-48b8-afe6-744a59313ac4` | - |
| **TMU Customs Shipper Aliases Processor** | `Notebook` | `da6c7f8b-42f1-4a70-bcd9-019402283dd3` | New notebook |
| **TMU Customs Excel2Bronze** | `Notebook` | `10727727-3496-46ef-b8b0-5ed0b161aae5` | New notebook |
| **TMU VATTaxes Excel2Bronze** | `Notebook` | `8f159519-0fa2-49b8-b215-aa77e214d94e` | - |
| **TMU 1C Transformation Notebook** | `Notebook` | `ac2116bb-6eb3-42ab-a152-959fc8aee76f` | - |
| **TMR SQL Copy Job Incremental** | `CopyJob` | `ee89c9b8-d25a-424a-8d89-4159ee280984` | - |
| **TMR SQL Copy Job Full** | `CopyJob` | `e9721975-1592-408f-a9e1-a9d8dae64a55` | - |
| **TMR SQL to Bronze Pipeline** | `DataPipeline` | `7f16fbc8-3703-4f7a-86cd-95667d022cc8` | - |
| **TMU 1C to Bronze** | `DataPipeline` | `0c22052a-134e-4e94-b9ff-fd3ef0af90f0` | - |
| **Data preparation - nulls handle** | `Notebook` | `43e63511-f24f-4c54-8f94-593b303e629c` | - |
| **TMU_Competition_Lakehouse** | `Lakehouse` | `cf0ab37f-3a6c-4c8d-b7df-c2b03b148bc4` | - |
| **Full Overwrite table** | `Notebook` | `07f55e97-20da-4889-aa3e-57be2d59c104` | - |
| **Actuals2AssortmentSQL** | `DataPipeline` | `7e394073-a85b-444e-8a25-388b3ea5470a` | - |
| **TMEU_Bronze_Lakehouse** | `Lakehouse` | `fe08dba7-b330-4acf-90a7-94bd2c053ff5` | - |
| **Jochens part categories excel transformer** | `Notebook` | `4a7298ee-3d44-4afc-a249-9f59bfec3e50` | New notebook |
| **TMB Sold WG Items Email distribution** | `DataPipeline` | `fd6da78d-4171-4e88-9706-269fa0c37259` | - |
| **TMB WG Sold Items Processing** | `Notebook` | `33490a33-8f92-433c-b022-10d726866443` | - |
| **TMU Open Data Bot Scraper** | `Notebook` | `7389339b-92d9-495a-832a-4aef22177755` | - |
| **TMU VAT AI prompting** | `Notebook` | `377f533e-da9e-4d84-ab95-1d0b3fadb3ff` | - |
| **TMA_NAV_Lakehouse** | `Lakehouse` | `560be169-9531-4fc2-8c36-4bb173fc1240` | - |
| **TMA_Full_Replace_NAV_Job** | `CopyJob` | `30cb2ba6-1f61-46dc-9b29-f678fd581dfa` | - |
| **TMA_NAV_Bronze_to_Silver** | `Notebook` | `38af5547-6a3e-4ba5-a5ae-56825089e904` | - |
| **TMA_NAV_Pipeline** | `DataPipeline` | `a3e7a702-bc78-45b5-bfa6-b8b5204b0a89` | - |
| **TMEU_IT_DB** | `SQLDatabase` | `e3a2cf7a-e2bf-4055-9c0f-ddf847ae5b1e` | - |
| **#Workspace maintenance job** | `Notebook` | `8b4e3f67-6760-4499-bd61-e25017afcf48` | - |
| **Azure_IT_Notebook** | `Notebook` | `52721df1-e83e-4dfe-9244-8aa7fe81209b` | - |
| **KTI_TMB_Files_Download** | `Notebook` | `21de76c6-1903-409a-83ac-b68863f2c3a1` | - |
| **TMB_KTI_to Bronze Pipeline** | `DataPipeline` | `306548b7-2964-41a7-8990-31eb31e8fe7f` | - |
| **TMU VAT AI prompting desc** | `Notebook` | `7b91ebeb-8ad2-4e16-a8a9-59192d46ce6e` | New notebook |
| **Europe_AG_Commodity_Prices** | `Notebook` | `5f16e44b-91e7-467d-8345-ddfc5e4eff31` | - |
| **KTI_TMB_Files_Download Specific File** | `Notebook` | `e63d2d4f-2e31-4abc-9305-a45f17f52b2e` | New notebook |
| **TMEU_Freshservice_Lakehouse** | `Lakehouse` | `b280f320-69ea-4b16-9e87-d032d87e6037` | - |
| **TMU_Freshservice_To_Bronze** | `Notebook` | `6f3bedf7-0c63-46a4-bdc0-5819e83d5ef5` | - |
| **TMU_Dozor_to_Bronze** | `Notebook` | `2c5193cd-e295-4cf5-a95e-8cd85c512f0f` | - |
| **zz_TMU VAT AI Data Merge** | `Notebook` | `1e5481d5-f3c4-4fbd-9014-0daeb18f5249` | - |
| **IT Costs to SQL** | `Notebook` | `75ab6eb2-9163-4c93-a76a-b847f0e2b26c` | - |
| **zz_TMU VAT AI Silver** | `Notebook` | `a4a0ba23-126d-4a7d-812c-45a79b59a9e4` | - |
| **TMU PNL Manual Adjustments** | `Dataflow` | `4dbbf1bb-b68b-4ec9-9e1a-46ccf45807df` | - |
| **StagingLakehouseForDataflows_20260408083147** | `Lakehouse` | `2854ef78-7194-42d5-8ede-6ab7ca0c9268` | - |
| **zz_TMU VAT AI Brands** | `Notebook` | `cacec74f-75a6-4d7c-9aad-59b0104b257b` | - |
| **ZohoManageEngine to SQL** | `Notebook` | `5a0e83fe-256f-4c3a-b351-cda71785c71d` | - |
| **PPL_TMEU_IT_Costs** | `DataPipeline` | `ac4b077d-e649-4f1a-8fa4-4feac994fd9a` | - |
| **TMEU Dataflow** | `Dataflow` | `e3315e67-9dbb-4ac1-8fd1-fb09b2129be3` | - |
| **TMU_CRM_Activities_Dozor_Confirmation** | `Notebook` | `0b143a7f-9ec1-4e9c-aebf-d86cc014b624` | - |
| **PPL_CRM_Bronze** | `DataPipeline` | `b560cbdd-3e7b-46eb-a854-0c20bae26069` | - |
| **TMU_Manual Update Dozor** | `Notebook` | `2f178095-b28a-425d-a570-db9f803a07d4` | New notebook |
| **Ukraine_AG_Commodity_Prices** | `Notebook` | `721d0261-72ae-4d21-8b83-a77861e8121b` | - |
| **Wholegoods_History_Processing** | `Notebook` | `2a42642f-089d-4a55-8a4d-014c08d2b1b9` | - |
| **TMUWGBudgetUDF** | `UserDataFunction` | `8df0e91a-f15c-41cf-84ca-31b6999edeaa` | - |
| **TMU 1C Credit Limit Transformation** | `Notebook` | `ca9a7594-e8be-4c39-9c48-3acdfcfbbbb6` | - |
| **TMEU_ERP_RAW_Lakehouse** | `Lakehouse` | `c35e1bc9-5fd2-4a86-9a2f-7f890b990c65` | - |
| **TMA_ERP_RAW_Lakehouse** | `CopyJob` | `0bc54a7c-208a-4e41-b765-8b3ea3fc9ce0` | - |
| **TMR_ERP_RAW_Lakehouse** | `CopyJob` | `02ce21fd-54c4-4a6b-8519-67e2bc06b4b6` | - |
| **TMB_ERP_RAW_Lakehouse** | `CopyJob` | `cb776ed0-9b7e-4c13-b4bc-2288c176d12b` | - |
| **TMB_LEVA_ERP_RAW_Lakehouse** | `CopyJob` | `3d72b4f2-a1d5-4c13-9e60-d8656c894141` | - |
| **PPL_TMEU_RAW_ERP** | `DataPipeline` | `273feb71-33f2-4167-8adf-b92416654ee5` | - |
| **TMEU_OrderBook_Transformation** | `Notebook` | `aa3c4bdc-a54d-4abf-93af-0d9e5ebbbb65` | - |
| **HR_from summary file** | `Notebook` | `99f40a93-eb90-4412-bc2f-721a4b9a173a` | - |
| **TMU_ERP_RAW_Lakehouse** | `CopyJob` | `8d50f17d-1c25-4600-a3af-96f8c9eb5873` | - |
| **TMU VAT AI Final Validation** | `Notebook` | `7852cdf6-893c-409c-ab27-86dc46b85e9c` | - |
| **fabric_usage_quering** | `Notebook` | `b37c0f5d-7bfc-4642-ae76-854f754251f7` | - |
| **Credit_Limit_Leger_DB** | `SQLDatabase` | `63c686ae-3399-4ce0-bc13-5ce0336cab9e` | - |
| **TMUCreditLimitUDF** | `UserDataFunction` | `1d9954d2-9f17-46b8-aca5-6d4290951513` | - |
| **TMUCreditLimitAdminUDF** | `UserDataFunction` | `3693a3a0-7cc5-4271-9a8d-8c2c97e102af` | - |
| **PartsForecastingDataSet** | `Notebook` | `d916492a-9583-4a5f-906f-141c6c8a4649` | - |
| **TMEU_Inventory_Book_Collection** | `Notebook` | `7dacc3cd-23fa-48fe-90d0-1e97d25de3b8` | - |
| **_TMEU_Lakehouse_MVs** | `Notebook` | `a586a9e1-859d-440c-bfdc-2b28f86cd083` | New notebook |
| **TMU_Market_dbt** | `DataBuildToolJob` | `2a78878a-d719-44de-aae4-15923114eedf` | - |
| **PPL_TMU_Silver_Gold** | `DataPipeline` | `b94b6cec-1d11-4f29-b449-9d36be9b152c` | - |
| **TMU_1C_dbt** | `DataBuildToolJob` | `6c3d5111-83b0-461d-9b92-b9cd8df308cc` | - |
| **TMU 1C Credit Limit Transformation_testdb** | `Notebook` | `63ceac08-4db3-4ca4-a1eb-14da6baf4248` | New notebook |
| **CNH FTP Items** | `Notebook` | `84f35b8d-cd84-48df-9dea-913e39c93f17` | New notebook |
| **Lectura Manual Request** | `Notebook` | `fb280954-989c-4ec7-bcff-6daa8fa31f0a` | - |
| **documentation** | `Notebook` | `666c4d7d-0a6e-4a41-9401-9f0eb61ad1b5` | - |

## 3. Semantic Models (Datasets) & Refresh Schedules

### Semantic Model: TMA_NAV_Silver_Dataset
- **Dataset ID**: `9b32e872-baeb-42f6-9af4-fbdf159b4e84`
- **Target Storage Mode**: `PremiumFiles`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (DISABLED ❌):
- **Frequency**: Daily
- **Scheduled Times**: `N/A` (UTC)

**Connected Data Sources (Lineage)**:
- Type: `AzureDataLakeStorage` | Connection: `{'server': 'onelake.dfs.fabric.microsoft.com', 'path': '/8d7c60ce-cb19-4805-ab1a-c84d6e1adf58/560be169-9531-4fc2-8c36-4bb173fc1240/'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2026-07-27 07:40:30 | 2026-07-27 07:40:41 | `Completed` | `DirectLakeFraming` | - |
| 2026-07-18 03:09:46 | 2026-07-18 03:09:55 | `Failed` | `DirectLakeFraming` | {"errorCode":"Premium_ASWL_Error","errorDescrip... |
| 2026-06-30 19:09:17 | 2026-06-30 19:09:19 | `Completed` | `DirectLakeFraming` | - |
| 2026-06-30 19:07:36 | 2026-06-30 19:09:17 | `Failed` | `DirectLakeFraming` | {"errorCode":"Premium_ASWL_Error","errorDescrip... |
| 2026-04-02 08:52:46 | 2026-04-02 08:52:49 | `Completed` | `WebModeling` | - |

## 4. Power BI Reports Inventory

*No Power BI reports found in this workspace.*

## 5. Dataflows & Dashboards

*No dataflows or dashboards in this workspace.*

---

## 6. Newcomer Operational Runbook & Notes
- **Primary Contact / Owner**: Refer to workspace access settings in Power BI portal.
- **Troubleshooting**: If a refresh fails in `Fabric_Prod_Workspace`, inspect the failure log under section 3 above and check upstream data gateway connectivity.
