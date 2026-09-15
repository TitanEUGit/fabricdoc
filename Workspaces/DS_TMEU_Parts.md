# Workspace Documentation: DS_TMEU_Parts

**Workspace ID**: `4da8ce61-48e7-4c86-a009-dee26bfa8be9`  
**Type**: `Fabric / PowerBI Workspace`  
**Capacity ID**: `70650ed2-f7a2-46df-96e8-8089f25db80e`  
**Description**: No description provided.

---

## 1. Executive Summary & Newcomer Overview
This document contains operational and technical details for the **DS_TMEU_Parts** workspace. It is designed to give new team members full visibility into key items, data models, report lineage, and refresh schedules.

## 2. Native Fabric Items Inventory

| Item Name | Item Type | Item ID | Description |
| :--- | :--- | :--- | :--- |
| **SQL_TMEU_Supplier_Database** | `SQLEndpoint` | `d8b503b7-97ba-4835-a038-a98a8f2bf2d4` | - |
| **SQL_Backend_TMEU_Customer_Categorization** | `SQLEndpoint` | `531ea7ef-9de3-4437-b27f-e6234e6b2851` | - |
| **SQL_TMEU_Parts** | `SQLEndpoint` | `fdfc19a5-0201-4c8f-9392-5a96d446384d` | - |
| **StagingLakehouseForDataflows_20260406164303** | `SQLEndpoint` | `1fa2677e-4568-46ee-a150-27f886720197` | - |
| **StagingWarehouseForDataflows_20260406164317** | `Warehouse` | `6fad3a29-99e9-4338-aac8-55a0f29b0c80` | - |
| **SQL_TMEU_Supplier_Database** | `SQLDatabase` | `77a12241-dbf5-45fb-8b86-50a9aaf2db30` | - |
| **PPL_Bronze_to_SQLTMEUSuppliers** | `DataPipeline` | `15b25b99-6652-4a87-9230-abf0485f45c7` | - |
| **CJ_TMR_Bronze_to_SQLTMEUSuppliers** | `CopyJob` | `1561bcb3-33af-479b-8250-071a799e5f18` | - |
| **CJ_TMU_Bronze_to_SQLTMEUSuppliers** | `CopyJob` | `5c7e1468-a3ab-424b-a3f3-439cb5e479d0` | - |
| **SQL_Backend_TMEU_Customer_Categorization** | `SQLDatabase` | `10f96edb-05e2-433e-827a-42220c130ddf` | - |
| **API_Customer_Categorization** | `GraphQLApi` | `f8f883e0-68f0-45f1-a7cc-078e20ca8263` | - |
| **CJ_TMB_Bronze_to_SQLTMEUSuppliers** | `CopyJob` | `421d9162-ab8f-4a76-8306-f87a5e53f88b` | - |
| **Lovable_Supplier_Management** | `GraphQLApi` | `919e0235-ccfd-4f70-8019-22c486af63b1` | - |
| **SQL_TMEU_Parts** | `SQLDatabase` | `9b498fe6-eac3-4288-a4dd-d5a92315ce4c` | - |
| **PPL_Bronze_SQLTMEUParts** | `DataPipeline` | `f93f3a50-2d8f-4a91-b7ff-6a2addc5fbf5` | - |
| **DF_Bronze_SQLTMEUParts** | `Dataflow` | `010074bb-6e5f-4474-b47f-9c378b27f7c1` | - |
| **StagingLakehouseForDataflows_20260406164303** | `Lakehouse` | `ba57fc84-51b4-44ef-9672-c76879f183bd` | - |
| **CNH_Parts_Substitutions_from_FTP** | `Notebook` | `35f4de18-7bcf-4738-9922-fe5d898a5cdd` | - |
| **GraphQL_Parts_Avaialbility_Substitutes** | `GraphQLApi` | `04b1a7b9-6de3-4149-9a4b-8643189ede33` | - |
| **x_OnDemand_CJ_TMB_Bronze_to_SQLTMEUSuppliers_LEVA** | `CopyJob` | `654381c1-6f4d-4caf-a712-8fe2d9c17abf` | - |
| **CNH_Parts_Prices_from_FTP** | `Notebook` | `e82ba6dd-ffac-4eb2-97a0-cf368c63f56e` | New notebook |

## 3. Semantic Models (Datasets) & Refresh Schedules

*No semantic models/datasets found in this workspace.*

## 4. Power BI Reports Inventory

*No Power BI reports found in this workspace.*

## 5. Dataflows & Dashboards

*No dataflows or dashboards in this workspace.*

---

## 6. Newcomer Operational Runbook & Notes
- **Primary Contact / Owner**: Refer to workspace access settings in Power BI portal.
- **Troubleshooting**: If a refresh fails in `DS_TMEU_Parts`, inspect the failure log under section 3 above and check upstream data gateway connectivity.
