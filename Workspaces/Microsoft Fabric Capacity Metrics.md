# Workspace Documentation: Microsoft Fabric Capacity Metrics

**Workspace ID**: `68fedd5b-d4e9-401d-8b16-1bb723a9de7a`  
**Type**: `Fabric / PowerBI Workspace`  
**Capacity ID**: `Shared / Pro`  
**Description**: No description provided.

---

## 1. Executive Summary & Newcomer Overview
This document contains operational and technical details for the **Microsoft Fabric Capacity Metrics** workspace. It is designed to give new team members full visibility into key items, data models, report lineage, and refresh schedules.

## 2. Native Fabric Items Inventory

| Item Name | Item Type | Item ID | Description |
| :--- | :--- | :--- | :--- |
| **Fabric Capacity Metrics** | `Report` | `21c49f1c-3d6f-4c1f-bc65-d81f3ba1b887` | - |
| **Fabric Capacity Metrics** | `SemanticModel` | `faee8ac6-e147-4b95-a3be-befa6135ff3c` | - |

## 3. Semantic Models (Datasets) & Refresh Schedules

### Semantic Model: Fabric Capacity Metrics
- **Dataset ID**: `faee8ac6-e147-4b95-a3be-befa6135ff3c`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `07:00` (GTB Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `Extension` | Connection: `{'path': 'CapacityMetricsCES', 'kind': 'CapacityMetricsCES'}`


## 4. Power BI Reports Inventory

| Report Name | Report ID | Dataset ID | Web URL |
| :--- | :--- | :--- | :--- |
| **Fabric Capacity Metrics** | `21c49f1c-3d6f-4c1f-bc65-d81f3ba1b887` | `faee8ac6-e147-4b95-a3be-befa6135ff3c` | [Open Report](https://app.powerbi.com/groups/68fedd5b-d4e9-401d-8b16-1bb723a9de7a/reports/21c49f1c-3d6f-4c1f-bc65-d81f3ba1b887) |

## 5. Dataflows & Dashboards

*No dataflows or dashboards in this workspace.*

---

## 6. Newcomer Operational Runbook & Notes
- **Primary Contact / Owner**: Refer to workspace access settings in Power BI portal.
- **Troubleshooting**: If a refresh fails in `Microsoft Fabric Capacity Metrics`, inspect the failure log under section 3 above and check upstream data gateway connectivity.
