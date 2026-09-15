# Workspace Documentation: BI_TMINT_PST

**Workspace ID**: `4c7ee85b-6a87-4cf8-b216-0f511ebf31fa`  
**Type**: `Fabric / PowerBI Workspace`  
**Capacity ID**: `70650ed2-f7a2-46df-96e8-8089f25db80e`  
**Description**: No description provided.

---

## 1. Executive Summary & Newcomer Overview
This document contains operational and technical details for the **BI_TMINT_PST** workspace. It is designed to give new team members full visibility into key items, data models, report lineage, and refresh schedules.

## 2. Native Fabric Items Inventory

| Item Name | Item Type | Item ID | Description |
| :--- | :--- | :--- | :--- |
| **TMINT_PST** | `Report` | `3d554e33-7c8e-49d7-9865-52e570b00da5` | - |
| **Usage Metrics Report** | `Report` | `b625c30b-345a-40b4-9ff3-7d6f5fb1e9b1` | - |
| **TMINT_PST** | `SemanticModel` | `561bbce5-3376-490c-94b5-14cf91476f1b` | - |
| **Usage Metrics Report** | `SemanticModel` | `c369142c-2a06-4782-91ec-05d950c60fac` | - |

## 3. Semantic Models (Datasets) & Refresh Schedules

### Semantic Model: TMINT_PST
- **Dataset ID**: `561bbce5-3376-490c-94b5-14cf91476f1b`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `N/A` (Romance Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `SharePointList` | Connection: `{'url': 'https://titanmachinery365europe.sharepoint.com/sites/hr-dataset-europe/'}`
- Type: `SharePointList` | Connection: `{'url': 'https://titanmachinery365europe.sharepoint.com/sites/hr-dataset-pst/'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2026-06-06 22:00:16 | 2026-06-06 22:00:16 | `Disabled` | `Scheduled` | - |
| 2026-06-05 22:00:19 | 2026-06-05 22:02:19 | `Completed` | `Scheduled` | - |
| 2026-06-04 22:01:18 | 2026-06-04 22:04:27 | `Completed` | `Scheduled` | - |
| 2026-06-03 22:00:19 | 2026-06-03 22:02:35 | `Completed` | `Scheduled` | - |
| 2026-06-02 22:00:17 | 2026-06-02 22:02:04 | `Completed` | `Scheduled` | - |

### Semantic Model: Usage Metrics Report
- **Dataset ID**: `c369142c-2a06-4782-91ec-05d950c60fac`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `19:56` (UTC)

**Connected Data Sources (Lineage)**:
- Type: `Extension` | Connection: `{'path': 'UsageMetricsDataConnector', 'kind': 'UsageMetricsDataConnector'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2025-07-20 19:56:01 | 2025-07-20 19:56:01 | `Disabled` | `Scheduled` | - |
| 2025-07-19 19:56:06 | 2025-07-19 19:56:42 | `Completed` | `Scheduled` | - |
| 2025-07-18 19:56:13 | 2025-07-18 19:56:36 | `Completed` | `Scheduled` | - |
| 2025-07-17 19:56:00 | 2025-07-17 19:57:16 | `Completed` | `Scheduled` | - |
| 2025-07-16 19:56:03 | 2025-07-16 19:57:16 | `Completed` | `Scheduled` | - |

## 4. Power BI Reports Inventory

| Report Name | Report ID | Dataset ID | Web URL |
| :--- | :--- | :--- | :--- |
| **TMINT_PST** | `3d554e33-7c8e-49d7-9865-52e570b00da5` | `561bbce5-3376-490c-94b5-14cf91476f1b` | [Open Report](https://app.powerbi.com/groups/4c7ee85b-6a87-4cf8-b216-0f511ebf31fa/reports/3d554e33-7c8e-49d7-9865-52e570b00da5) |
| **Usage Metrics Report** | `b625c30b-345a-40b4-9ff3-7d6f5fb1e9b1` | `c369142c-2a06-4782-91ec-05d950c60fac` | [Open Report](https://app.powerbi.com/groups/4c7ee85b-6a87-4cf8-b216-0f511ebf31fa/reports/b625c30b-345a-40b4-9ff3-7d6f5fb1e9b1) |

## 5. Dataflows & Dashboards

*No dataflows or dashboards in this workspace.*

---

## 6. Newcomer Operational Runbook & Notes
- **Primary Contact / Owner**: Refer to workspace access settings in Power BI portal.
- **Troubleshooting**: If a refresh fails in `BI_TMINT_PST`, inspect the failure log under section 3 above and check upstream data gateway connectivity.
