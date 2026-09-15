# Workspace Documentation: DS_TMEU_Wholegoods

**Workspace ID**: `3fc5ee8e-273c-40a0-b54a-87077f6b9c43`  
**Type**: `Fabric / PowerBI Workspace`  
**Capacity ID**: `70650ed2-f7a2-46df-96e8-8089f25db80e`  
**Description**: No description provided.

---

## 1. Executive Summary & Newcomer Overview
This document contains operational and technical details for the **DS_TMEU_Wholegoods** workspace. It is designed to give new team members full visibility into key items, data models, report lineage, and refresh schedules.

## 2. Native Fabric Items Inventory

| Item Name | Item Type | Item ID | Description |
| :--- | :--- | :--- | :--- |
| **SQL_WG_Purchases** | `SQLEndpoint` | `c2889c57-1299-47c6-8a94-612502a66aed` | - |
| **SQL_WG_Purchases** | `SQLDatabase` | `697d1333-d3f1-4de2-8763-b9c72df266c0` | - |
| **CJ_TMB_WG_Purchase** | `CopyJob` | `391f1918-b1cd-4f97-bd31-dcd50a952aa2` | - |
| **CJ_TMA_WG_Purchase** | `CopyJob` | `6164ec14-d886-4edf-9a7b-192b0d88be8b` | - |
| **CJ_TMR_WG_Purchase** | `CopyJob` | `7afe716f-0e7b-41b4-bced-16427b82dda2` | - |
| **PPL_WG_Purchases_ERP_to_Silver** | `DataPipeline` | `4669b818-8bee-456e-a605-fdaca45c3a65` | - |
| **CJ_TMA_WG_Test_Purchase** | `CopyJob` | `c0d742a2-bbf1-4b50-9dcc-45e044e3be0a` | - |
| **CJ_TMB_WG_Test_Purchase** | `CopyJob` | `fd4c961a-8a14-4a34-8625-fefbafca3021` | - |
| **CJ_TMR_WG_Test_Purchase** | `CopyJob` | `5ee9a5fc-d1fa-4a19-91b5-66de392c98a6` | - |
| **GraphQL_WG_PurchaseOrder** | `GraphQLApi` | `18a4dc01-c37f-421d-ab22-aea4b1a3728b` | - |
| **NAV_API_Test** | `DataPipeline` | `ba995eae-d468-44ac-b498-cf39c617740c` | - |
| **NAV_API_Landing** | `Notebook` | `09215cb0-147a-474f-87ca-f4285c8bab26` | - |
| **NAV_API_Transformation** | `Notebook` | `a336de70-848a-4403-92be-71ca0075880a` | - |
| **NAV_API_Writeback** | `DataPipeline` | `a2e96f5d-5a6d-48ae-8b2f-99a7bf550fc0` | - |
| **NAV_API_Writeback_Prep** | `Notebook` | `9b453d88-6edd-4295-becf-a56363a4302b` | - |
| **NAV_API_Writeback_Executor_State** | `Notebook` | `63a7dacd-6463-4999-92a4-39cb821ee95e` | Claims, finalizes, and safely reconciles NAV writeback creation steps and verified ERP write requests. |
| **NAV_API_Landing_TM_BG** | `Notebook` | `8063c310-8b63-42a2-aea7-f1f8e341e2ee` | - |
| **NAV_API_Transformation_TM_BG** | `Notebook` | `58169497-94de-47ae-8719-919a1b8a95cf` | - |
| **NAV_API_TM_BG** | `DataPipeline` | `ac4e9ea8-07a5-4c43-b283-d133ef09042f` | - |
| **NAV_API_Landing_TM_AT** | `Notebook` | `2c618da1-3c6c-47b0-88f8-be6ab95b151c` | - |
| **NAV_API_Transformation_TM_AT** | `Notebook` | `b8bcbfd6-f1ef-496d-9577-7e7b2cca5e55` | - |
| **NAV_API_TM_AT** | `DataPipeline` | `9d409b51-d842-459c-a368-8599bd90b431` | - |
| **NAV_API_Writeback_TM_BG** | `DataPipeline` | `0f44b1ff-6e67-4cba-8eae-cdb1ba3d6e36` | - |
| **NAV_API_Writeback_TM_AT** | `DataPipeline` | `48f89c91-984a-4cd7-97c0-adb13497b7bd` | - |
| **NAV_API_Writeback_Executor_TM_BG** | `Notebook` | `88114c45-211b-48e6-9c54-7bfdadfe9b99` | Claims, finalizes, and safely reconciles NAV writeback creation steps and verified ERP write requests. |
| **NAV_API_Writeback_Prep_TM_BG** | `Notebook` | `b63be9a8-5464-47fb-99b0-a4cc93400c12` | - |
| **NAV_API_Writeback_Executor_TM_AT** | `Notebook` | `f51c88c4-0978-4e63-add8-a6d56fbc81db` | Claims, finalizes, and safely reconciles NAV writeback creation steps and verified ERP write requests. |
| **NAV_API_Writeback_Prep_TM_AT** | `Notebook` | `7d731f58-dab8-4d00-813c-2d36f86fa843` | - |
| **NAV_API_Writeback_TM_BG_Worker** | `DataPipeline` | `838c13f4-cd37-469e-8a0f-7112d7a5aced` | Unscheduled Bulgarian ERP writeback worker. Invoked only by the guarded dispatcher. |
| **NAV_API_Writeback_TM_RO_Lines** | `DataPipeline` | `8c195f1b-537f-48aa-ba24-5c9ec3bda63a` | Isolated line-only accelerator. One NAV line per PO at a time; different POs may run concurrently. |
| **NAV_API_Writeback_TM_BG_Lines** | `DataPipeline` | `0e4b53c5-0875-4395-a46d-6e894bd58ba1` | Isolated line-only accelerator. One NAV line per PO at a time; different POs may run concurrently. |
| **NAV_API_Writeback_TM_AT_Lines** | `DataPipeline` | `b0e410d9-de9a-4c70-9f1e-5abaf318e541` | Isolated line-only accelerator. One NAV line per PO at a time; different POs may run concurrently. |
| **NAV_API_Writeback_TM_RO_Lines_Worker** | `DataPipeline` | `30fa26ab-01d3-4fe4-aec0-4e935fb4ab32` | Unsheduled line worker. Claims one line per PO per wave and runs different POs concurrently. |
| **NAV_API_Writeback_TM_BG_Lines_Worker** | `DataPipeline` | `7f56f75d-7cb7-4fa1-b971-25746ddb3b8a` | Unsheduled line worker. Claims one line per PO per wave and runs different POs concurrently. |
| **NAV_API_Writeback_TM_AT_Lines_Worker** | `DataPipeline` | `49262fb9-fd0b-4355-8c42-bcaa2530e01d` | Unsheduled line worker. Claims one line per PO per wave and runs different POs concurrently. |
| **NAV_API_Writeback_TM_AT_Worker** | `DataPipeline` | `706339a2-e568-4741-8ef9-ef4670f95321` | Unscheduled Austria bulk writeback worker cloned from the proven Bulgaria SQL/batch architecture. |
| **NAV_API_Writeback_TM_RO_Worker** | `DataPipeline` | `bf345f3a-9fa0-4008-950c-f93d9e94501b` | Unscheduled Romania bulk writeback worker cloned from the proven Bulgaria SQL/batch architecture. |
| **NAV_API_Landing_References_TM_RO** | `Notebook` | `fb9ffb48-d6f7-4860-bff2-6499f0f7c0d7` | - |
| **NAV_API_Transformation_References_TM_RO** | `Notebook` | `118dfc04-5bfd-4c97-be56-35d8bc26b7a0` | - |
| **NAV_API_References_TM_RO** | `DataPipeline` | `852f8cfd-17a1-43c9-a36f-a40d9b1ce679` | - |
| **NAV_API_Landing_References_TM_AT** | `Notebook` | `a3d0e554-4f69-4b4a-bdb3-dc0e2ec13d19` | - |
| **NAV_API_Transformation_References_TM_AT** | `Notebook` | `ff171c19-88c8-44da-913c-2f4547a77126` | - |
| **NAV_API_References_TM_AT** | `DataPipeline` | `3625daf5-e1c2-4162-8852-31946b6376fc` | - |
| **NAV_API_Landing_References_TM_BG** | `Notebook` | `93282a3d-335a-4791-a3bc-70cf82f116d0` | - |
| **NAV_API_Transformation_References_TM_BG** | `Notebook` | `f979165a-faad-41b2-818a-83659c30bfd0` | - |
| **NAV_API_References_TM_BG** | `DataPipeline` | `51da687b-a1bd-4ac8-b298-28a2d8b75b55` | - |
| **TMEU_Inventory_Impairment_UDF** | `UserDataFunction` | `ac0f49e1-45ac-4f4f-9293-f3b57d43f07b` | - |
| **PHASE A ISOLATED AT paged read 20260914-210303** | `DataPipeline` | `b73da7a7-bc50-4b90-b4b5-5d6b77f79612` | - |
| **PHASE A ISOLATED AT paged read 20260914-210752** | `DataPipeline` | `23bf35fc-76f7-45e3-97e8-da2dbcfb48dc` | - |
| **PHASE A ISOLATED RO paged read 20260914-210758** | `DataPipeline` | `496ea1e3-e6ba-4881-b822-1a0ba2ed9cc9` | - |
| **PHASE A ISOLATED BG paged read 20260914-210804** | `DataPipeline` | `439492c3-a73e-4470-8b8b-16b9021e14e6` | - |
| **PHASE A ISOLATED AT paged read 20260914-210946** | `DataPipeline` | `1c796d19-c550-47b2-9e1b-745807f416ce` | - |
| **PHASE A ISOLATED RO paged read 20260914-211301** | `DataPipeline` | `17a5cf0d-498b-411f-90df-cb1e05fa7b69` | - |
| **ISOLATED AT Web SQL read probe 20260915** | `DataPipeline` | `91ae639a-08a4-4eee-a95b-aa2870ecb90f` | - |

## 3. Semantic Models (Datasets) & Refresh Schedules

*No semantic models/datasets found in this workspace.*

## 4. Power BI Reports Inventory

*No Power BI reports found in this workspace.*

## 5. Dataflows & Dashboards

*No dataflows or dashboards in this workspace.*

---

## 6. Newcomer Operational Runbook & Notes
- **Primary Contact / Owner**: Refer to workspace access settings in Power BI portal.
- **Troubleshooting**: If a refresh fails in `DS_TMEU_Wholegoods`, inspect the failure log under section 3 above and check upstream data gateway connectivity.
