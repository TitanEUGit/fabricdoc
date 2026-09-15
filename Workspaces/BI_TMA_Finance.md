# Workspace Documentation: BI_TMA_Finance

**Workspace ID**: `cdfb246e-047b-4e6f-8f72-7422da8f1894`  
**Type**: `Fabric / PowerBI Workspace`  
**Capacity ID**: `70650ed2-f7a2-46df-96e8-8089f25db80e`  
**Description**: No description provided.

---

## 1. Executive Summary & Newcomer Overview
This document contains operational and technical details for the **BI_TMA_Finance** workspace. It is designed to give new team members full visibility into key items, data models, report lineage, and refresh schedules.

## 2. Native Fabric Items Inventory

| Item Name | Item Type | Item ID | Description |
| :--- | :--- | :--- | :--- |
| **EOC Entity Report** | `Report` | `a59d9fdf-3532-421f-8a88-0ec6f28a7d3b` | - |
| **Report Usage Metrics Report** | `Report` | `6187f350-3392-4b3d-972c-662c4a753422` | - |
| **Usage Metrics Report** | `Report` | `cc9b4fdf-b909-40a4-8319-a45d8279ef54` | - |
| **EOC Entity Report** | `SemanticModel` | `377ea29c-e012-425b-a016-87be61c54cec` | - |
| **Report Usage Metrics Model** | `SemanticModel` | `0c3d19f1-72e4-4176-88e2-779fe814a50c` | - |
| **Usage Metrics Report** | `SemanticModel` | `bdea1283-f935-4356-91a3-05e8983f6a0e` | - |

## 3. Semantic Models (Datasets) & Refresh Schedules

### Semantic Model: EOC Entity Report
- **Dataset ID**: `377ea29c-e012-425b-a016-87be61c54cec`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `04:00` (Romance Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `Sql` | Connection: `{'server': '10.75.1.7', 'database': 'jetnavdwh'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2026-09-15 11:00:22 | - | `Unknown` | `DataFactory` | - |
| 2026-09-15 02:00:26 | 2026-09-15 02:04:07 | `Completed` | `Scheduled` | - |
| 2026-09-14 11:00:23 | 2026-09-14 11:01:49 | `Completed` | `DataFactory` | - |
| 2026-09-14 02:00:26 | 2026-09-14 02:03:33 | `Completed` | `Scheduled` | - |
| 2026-09-13 11:00:37 | 2026-09-13 11:01:58 | `Completed` | `DataFactory` | - |

### Semantic Model: Report Usage Metrics Model
- **Dataset ID**: `0c3d19f1-72e4-4176-88e2-779fe814a50c`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `False`
- **Configured By**: `OBaliuta@titanmachinery.ua`

*No refresh schedule configured.*

### Semantic Model: Usage Metrics Report
- **Dataset ID**: `bdea1283-f935-4356-91a3-05e8983f6a0e`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `03:24` (UTC)

**Connected Data Sources (Lineage)**:
- Type: `Extension` | Connection: `{'path': 'UsageMetricsDataConnector', 'kind': 'UsageMetricsDataConnector'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2024-05-26 03:24:09 | 2024-05-26 03:24:09 | `Disabled` | `Scheduled` | - |
| 2024-05-25 03:24:08 | 2024-05-25 03:25:06 | `Completed` | `Scheduled` | - |
| 2024-05-24 03:24:12 | 2024-05-24 03:24:56 | `Completed` | `Scheduled` | - |
| 2024-05-23 03:24:01 | 2024-05-23 03:24:51 | `Completed` | `Scheduled` | - |
| 2024-05-22 03:24:02 | 2024-05-22 03:24:25 | `Completed` | `Scheduled` | - |

## 4. Power BI Reports Inventory

| Report Name | Report ID | Dataset ID | Web URL |
| :--- | :--- | :--- | :--- |
| **EOC Entity Report** | `a59d9fdf-3532-421f-8a88-0ec6f28a7d3b` | `377ea29c-e012-425b-a016-87be61c54cec` | [Open Report](https://app.powerbi.com/groups/cdfb246e-047b-4e6f-8f72-7422da8f1894/reports/a59d9fdf-3532-421f-8a88-0ec6f28a7d3b) |
| **Report Usage Metrics Report** | `6187f350-3392-4b3d-972c-662c4a753422` | `0c3d19f1-72e4-4176-88e2-779fe814a50c` | [Open Report](https://app.powerbi.com/groups/cdfb246e-047b-4e6f-8f72-7422da8f1894/reports/6187f350-3392-4b3d-972c-662c4a753422) |
| **Usage Metrics Report** | `cc9b4fdf-b909-40a4-8319-a45d8279ef54` | `bdea1283-f935-4356-91a3-05e8983f6a0e` | [Open Report](https://app.powerbi.com/groups/cdfb246e-047b-4e6f-8f72-7422da8f1894/reports/cc9b4fdf-b909-40a4-8319-a45d8279ef54) |

## 5. Dataflows & Dashboards

*No dataflows or dashboards in this workspace.*

---

## 6. Newcomer Operational Runbook & Notes
- **Primary Contact / Owner**: Refer to workspace access settings in Power BI portal.
- **Troubleshooting**: If a refresh fails in `BI_TMA_Finance`, inspect the failure log under section 3 above and check upstream data gateway connectivity.
