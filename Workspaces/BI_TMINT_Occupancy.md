# Workspace Documentation: BI_TMINT_Occupancy

**Workspace ID**: `cf7e934b-a3de-47cb-8657-8919fa76a863`  
**Type**: `Fabric / PowerBI Workspace`  
**Capacity ID**: `70650ed2-f7a2-46df-96e8-8089f25db80e`  
**Description**: No description provided.

---

## 1. Executive Summary & Newcomer Overview
This document contains operational and technical details for the **BI_TMINT_Occupancy** workspace. It is designed to give new team members full visibility into key items, data models, report lineage, and refresh schedules.

## 2. Native Fabric Items Inventory

| Item Name | Item Type | Item ID | Description |
| :--- | :--- | :--- | :--- |
| **Occupancy** | `Report` | `8a509468-84df-43eb-abd2-a10b50436192` | - |
| **TMU Occupancy Report** | `Report` | `33821549-95f5-46a4-ab31-b9aaba12c721` | - |
| **Usage Metrics Report** | `Report` | `c2bd96e0-fe16-4e9a-bd3a-850d122f27b4` | - |
| **Occupancy** | `SemanticModel` | `436ed979-95d0-453a-95ed-a67c5ca1500f` | - |
| **Usage Metrics Report** | `SemanticModel` | `837d9537-cd25-41d6-acb6-909ee92508d1` | - |

## 3. Semantic Models (Datasets) & Refresh Schedules

### Semantic Model: Occupancy
- **Dataset ID**: `436ed979-95d0-453a-95ed-a67c5ca1500f`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `08:00` (Romance Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `SharePointList` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/occupancycenter/'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2025-08-26 06:01:09 | 2025-08-26 06:01:09 | `Disabled` | `Scheduled` | - |
| 2025-08-25 06:01:09 | 2025-08-25 06:06:40 | `Completed` | `Scheduled` | - |
| 2025-08-24 06:04:01 | 2025-08-24 06:05:31 | `Completed` | `Scheduled` | - |
| 2025-08-23 06:01:01 | 2025-08-23 06:01:49 | `Completed` | `Scheduled` | - |
| 2025-08-22 06:02:09 | 2025-08-22 06:05:15 | `Completed` | `Scheduled` | - |

### Semantic Model: Usage Metrics Report
- **Dataset ID**: `837d9537-cd25-41d6-acb6-909ee92508d1`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `21:44` (UTC)

**Connected Data Sources (Lineage)**:
- Type: `Extension` | Connection: `{'path': 'UsageMetricsDataConnector', 'kind': 'UsageMetricsDataConnector'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2025-07-20 21:44:04 | 2025-07-20 21:44:04 | `Disabled` | `Scheduled` | - |
| 2025-07-19 21:44:07 | 2025-07-19 21:45:21 | `Completed` | `Scheduled` | - |
| 2025-07-18 21:45:03 | 2025-07-18 21:45:43 | `Completed` | `Scheduled` | - |
| 2025-07-17 21:45:07 | 2025-07-17 21:45:48 | `Completed` | `Scheduled` | - |
| 2025-07-16 21:44:09 | 2025-07-16 21:44:54 | `Completed` | `Scheduled` | - |

## 4. Power BI Reports Inventory

| Report Name | Report ID | Dataset ID | Web URL |
| :--- | :--- | :--- | :--- |
| **Occupancy** | `8a509468-84df-43eb-abd2-a10b50436192` | `436ed979-95d0-453a-95ed-a67c5ca1500f` | [Open Report](https://app.powerbi.com/groups/cf7e934b-a3de-47cb-8657-8919fa76a863/reports/8a509468-84df-43eb-abd2-a10b50436192) |
| **TMU Occupancy Report** | `33821549-95f5-46a4-ab31-b9aaba12c721` | `436ed979-95d0-453a-95ed-a67c5ca1500f` | [Open Report](https://app.powerbi.com/groups/cf7e934b-a3de-47cb-8657-8919fa76a863/reports/33821549-95f5-46a4-ab31-b9aaba12c721) |
| **Usage Metrics Report** | `c2bd96e0-fe16-4e9a-bd3a-850d122f27b4` | `837d9537-cd25-41d6-acb6-909ee92508d1` | [Open Report](https://app.powerbi.com/groups/cf7e934b-a3de-47cb-8657-8919fa76a863/reports/c2bd96e0-fe16-4e9a-bd3a-850d122f27b4) |

## 5. Dataflows & Dashboards

*No dataflows or dashboards in this workspace.*

---

## 6. Newcomer Operational Runbook & Notes
- **Primary Contact / Owner**: Refer to workspace access settings in Power BI portal.
- **Troubleshooting**: If a refresh fails in `BI_TMINT_Occupancy`, inspect the failure log under section 3 above and check upstream data gateway connectivity.
