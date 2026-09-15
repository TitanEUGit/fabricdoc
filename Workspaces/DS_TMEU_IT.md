# Workspace Documentation: DS_TMEU_IT

**Workspace ID**: `bdc1f104-6296-488d-bfa3-9916fcb023a7`  
**Type**: `Fabric / PowerBI Workspace`  
**Capacity ID**: `70650ed2-f7a2-46df-96e8-8089f25db80e`  
**Description**: No description provided.

---

## 1. Executive Summary & Newcomer Overview
This document contains operational and technical details for the **DS_TMEU_IT** workspace. It is designed to give new team members full visibility into key items, data models, report lineage, and refresh schedules.

## 2. Native Fabric Items Inventory

| Item Name | Item Type | Item ID | Description |
| :--- | :--- | :--- | :--- |
| **IT_Inventory_Management** | `SQLEndpoint` | `d84d6b44-cbe2-49b9-8033-6837c992c141` | - |
| **TitanADSync** | `SQLEndpoint` | `f0859980-4b51-4862-9276-fbbd440a7287` | - |
| **TitanID** | `SQLEndpoint` | `a3909f2e-c658-40ff-beec-ebaed0827a30` | - |
| **New_Employee** | `SQLEndpoint` | `ebbe9190-b7ed-43c4-be68-e19844ce0afc` | - |
| **IT_Inventory_Management** | `SQLDatabase` | `04a7fcbe-59c0-4c18-bf13-f5d273ba2c95` | - |
| **GraphQL_IT_Inventory_Management** | `GraphQLApi` | `c45d1c1c-206b-4192-a839-9277355cfacc` | - |
| **TitanADSync** | `SQLDatabase` | `132a65a4-843a-4f90-8699-e790490ded3d` | - |
| **TitanID** | `SQLDatabase` | `90b97ff8-edab-40c2-ae0b-5c3af7e32cca` | - |
| **GraphQL_IT_Expenses** | `GraphQLApi` | `9aa2cfaa-a424-489d-b692-349e201b459b` | - |
| **New_Employee** | `SQLDatabase` | `30fc4044-734d-4588-9ff3-c9ea55fc935c` | - |

## 3. Semantic Models (Datasets) & Refresh Schedules

*No semantic models/datasets found in this workspace.*

## 4. Power BI Reports Inventory

*No Power BI reports found in this workspace.*

## 5. Dataflows & Dashboards

*No dataflows or dashboards in this workspace.*

---

## 6. Newcomer Operational Runbook & Notes
- **Primary Contact / Owner**: Refer to workspace access settings in Power BI portal.
- **Troubleshooting**: If a refresh fails in `DS_TMEU_IT`, inspect the failure log under section 3 above and check upstream data gateway connectivity.
