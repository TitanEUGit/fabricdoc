# Workspace Documentation: BI_TMB_CRM

**Workspace ID**: `c6774234-117c-4379-acca-b8b77c7a7295`  
**Type**: `Fabric / PowerBI Workspace`  
**Capacity ID**: `70650ed2-f7a2-46df-96e8-8089f25db80e`  
**Description**: No description provided.

---

## 1. Executive Summary & Newcomer Overview
This document contains operational and technical details for the **BI_TMB_CRM** workspace. It is designed to give new team members full visibility into key items, data models, report lineage, and refresh schedules.

## 2. Native Fabric Items Inventory

| Item Name | Item Type | Item ID | Description |
| :--- | :--- | :--- | :--- |
| **TMB SPL Report** | `Report` | `8b9acebe-66bf-4e95-8f4b-c7a549eb14e4` | - |
| **TMB CRM** | `Report` | `7cf1549a-87ff-4324-9a3f-80cd54f3fb50` | - |
| **TMB SPL Report** | `SemanticModel` | `c78c7dd8-6abe-4759-99a9-027211bcb09b` | - |
| **TMB CRM** | `SemanticModel` | `c2269cfc-78f8-47a0-97fd-8759d0ca5a8a` | - |

## 3. Semantic Models (Datasets) & Refresh Schedules

### Semantic Model: TMB SPL Report
- **Dataset ID**: `c78c7dd8-6abe-4759-99a9-027211bcb09b`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `03:30` (FLE Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `Extension` | Connection: `{'path': 'titanbulgaria.crm4.dynamics.com', 'kind': 'CommonDataService'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2026-09-06 00:31:15 | 2026-09-06 00:31:15 | `Disabled` | `Scheduled` | - |
| 2026-09-05 00:31:14 | 2026-09-05 00:39:08 | `Completed` | `Scheduled` | - |
| 2026-09-04 00:30:19 | 2026-09-04 00:35:47 | `Completed` | `Scheduled` | - |
| 2026-09-03 00:31:10 | 2026-09-03 00:38:26 | `Completed` | `Scheduled` | - |
| 2026-09-02 00:31:12 | 2026-09-02 00:39:28 | `Completed` | `Scheduled` | - |

### Semantic Model: TMB CRM
- **Dataset ID**: `c2269cfc-78f8-47a0-97fd-8759d0ca5a8a`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `03:00` (FLE Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `Extension` | Connection: `{'path': 'titanbulgaria.crm4.dynamics.com', 'kind': 'CommonDataService'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2026-09-05 00:03:15 | 2026-09-05 00:03:15 | `Disabled` | `Scheduled` | - |
| 2026-09-04 00:03:15 | 2026-09-04 00:10:28 | `Completed` | `Scheduled` | - |
| 2026-09-03 00:03:14 | 2026-09-03 00:10:32 | `Completed` | `Scheduled` | - |
| 2026-09-02 00:03:13 | 2026-09-02 00:10:37 | `Completed` | `Scheduled` | - |
| 2026-09-01 00:03:14 | 2026-09-01 00:10:10 | `Completed` | `Scheduled` | - |

## 4. Power BI Reports Inventory

| Report Name | Report ID | Dataset ID | Web URL |
| :--- | :--- | :--- | :--- |
| **TMB SPL Report** | `8b9acebe-66bf-4e95-8f4b-c7a549eb14e4` | `c78c7dd8-6abe-4759-99a9-027211bcb09b` | [Open Report](https://app.powerbi.com/groups/c6774234-117c-4379-acca-b8b77c7a7295/reports/8b9acebe-66bf-4e95-8f4b-c7a549eb14e4) |
| **TMB CRM** | `7cf1549a-87ff-4324-9a3f-80cd54f3fb50` | `c2269cfc-78f8-47a0-97fd-8759d0ca5a8a` | [Open Report](https://app.powerbi.com/groups/c6774234-117c-4379-acca-b8b77c7a7295/reports/7cf1549a-87ff-4324-9a3f-80cd54f3fb50) |

## 5. Dataflows & Dashboards

*No dataflows or dashboards in this workspace.*

---

## 6. Newcomer Operational Runbook & Notes
- **Primary Contact / Owner**: Refer to workspace access settings in Power BI portal.
- **Troubleshooting**: If a refresh fails in `BI_TMB_CRM`, inspect the failure log under section 3 above and check upstream data gateway connectivity.
