# Workspace Documentation: Microsoft Fabric Capacity Metrics - US

**Workspace ID**: `b7d1c3c9-8783-472f-8e10-169ca04eb413`  
**Type**: `Fabric / PowerBI Workspace`  
**Capacity ID**: `Shared / Pro`  
**Description**: No description provided.

---

## 1. Executive Summary & Newcomer Overview
This document contains operational and technical details for the **Microsoft Fabric Capacity Metrics - US** workspace. It is designed to give new team members full visibility into key items, data models, report lineage, and refresh schedules.

## 2. Native Fabric Items Inventory

| Item Name | Item Type | Item ID | Description |
| :--- | :--- | :--- | :--- |
| **Fabric Capacity Metrics** | `Report` | `2f6cec62-ab70-4dbb-b46d-0064e38744b9` | - |
| **Fabric Capacity Metrics** | `SemanticModel` | `f7d4bb50-7bae-4e50-b89e-90e01c770d9f` | - |

## 3. Semantic Models (Datasets) & Refresh Schedules

### Semantic Model: Fabric Capacity Metrics
- **Dataset ID**: `f7d4bb50-7bae-4e50-b89e-90e01c770d9f`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `avollen@titanmachinery.com`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `02:00, 08:00, 09:00, 10:00, 13:00, 14:00, 15:00, 17:00` (Central Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `Extension` | Connection: `{'path': 'CapacityMetricsCES', 'kind': 'CapacityMetricsCES'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2026-09-15 07:02:06 | 2026-09-15 07:12:50 | `Completed` | `Scheduled` | - |
| 2026-09-14 22:02:16 | 2026-09-14 22:16:36 | `Completed` | `Scheduled` | - |
| 2026-09-14 20:02:06 | 2026-09-14 20:13:09 | `Completed` | `Scheduled` | - |
| 2026-09-14 19:02:03 | 2026-09-14 19:12:04 | `Completed` | `Scheduled` | - |
| 2026-09-14 18:03:05 | 2026-09-14 18:16:35 | `Completed` | `Scheduled` | - |

## 4. Power BI Reports Inventory

| Report Name | Report ID | Dataset ID | Web URL |
| :--- | :--- | :--- | :--- |
| **Fabric Capacity Metrics** | `2f6cec62-ab70-4dbb-b46d-0064e38744b9` | `f7d4bb50-7bae-4e50-b89e-90e01c770d9f` | [Open Report](https://app.powerbi.com/groups/b7d1c3c9-8783-472f-8e10-169ca04eb413/reports/2f6cec62-ab70-4dbb-b46d-0064e38744b9) |
| **Fabric Capacity Metrics** | `2f6cec62-ab70-4dbb-b46d-0064e38744b9` | `f7d4bb50-7bae-4e50-b89e-90e01c770d9f` | [Open Report](https://app.powerbi.com/groups/b7d1c3c9-8783-472f-8e10-169ca04eb413/reports/2f6cec62-ab70-4dbb-b46d-0064e38744b9) |

## 5. Dataflows & Dashboards

*No dataflows or dashboards in this workspace.*

---

## 6. Newcomer Operational Runbook & Notes
- **Primary Contact / Owner**: Refer to workspace access settings in Power BI portal.
- **Troubleshooting**: If a refresh fails in `Microsoft Fabric Capacity Metrics - US`, inspect the failure log under section 3 above and check upstream data gateway connectivity.
