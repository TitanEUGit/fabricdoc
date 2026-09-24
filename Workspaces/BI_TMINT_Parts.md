# Workspace Documentation: BI_TMINT_Parts

**Workspace ID**: `0f9ead1f-a393-49b0-b9ae-854cce19c159`  
**Type**: `Fabric / PowerBI Workspace`  
**Capacity ID**: `70650ed2-f7a2-46df-96e8-8089f25db80e`  
**Description**: No description provided.

---

## 1. Executive Summary & Newcomer Overview

> [!NOTE]
> **TMR Aftersales Reporting (On-Demand)**
> Despite the legacy `TMINT` (International) prefix, this workspace actually contains Aftersales/Parts reports built specifically for **TMR (Romania)**. These function primarily as on-demand reports rather than scheduled operational dashboards.

This document contains operational and technical details for the **BI_TMINT_Parts** workspace. It is designed to give new team members full visibility into key items, data models, report lineage, and refresh schedules.

## 2. Native Fabric Items Inventory

| Item Name | Item Type | Item ID | Description |
| :--- | :--- | :--- | :--- |
| **TMINT_BI_Inventory_Aging_Report** | `Report` | `daad0a4f-fb2e-4499-9fae-63be99e7c060` | - |
| **TMINT_BI_Preventive_Aging_Report** | `Report` | `46e62fc4-0be9-4579-82e7-b994e15a9e01` | - |
| **Parts - Aging** | `Report` | `152656ef-ec32-47c0-ac60-28990d9b372c` | - |
| **Parts - Aging - EndOfMonth** | `Report` | `3a4ef89b-b517-4fbb-afa9-9ef4ac6fc479` | - |
| **Usage Metrics Report** | `Report` | `38298a16-af11-4103-914f-7c04687894a9` | - |
| **TMR Stock Order Report** | `Report` | `375e34c3-d5ad-4631-9e1d-7a1c41a5d102` | - |
| **Parts - Aging (old)** | `SemanticModel` | `dbb06129-4ab0-4988-b739-49e29b3d040b` | - |
| **TMINT_BI_Inventory_Aging_Report** | `SemanticModel` | `5df8ba3b-557c-4409-ad17-a528d8024276` | - |
| **TMINT_BI_Preventive_Aging_Report** | `SemanticModel` | `b93d3337-f9a4-427e-a9cd-d49e02274930` | - |
| **Parts - Aging** | `SemanticModel` | `05a71bc2-cd63-4fa2-8911-a1df65335625` | - |
| **Parts - Aging - EndOfMonth** | `SemanticModel` | `ff2706e7-600c-4c95-b327-a11fd5c1a342` | - |
| **Usage Metrics Report** | `SemanticModel` | `e3e38f8b-bed7-4248-bd79-2716063255dd` | - |
| **TMR Stock Order Report** | `SemanticModel` | `593e97f2-ab3e-46e4-95f5-ffa12ce25963` | - |

## 3. Semantic Models (Datasets) & Refresh Schedules

### Semantic Model: Parts - Aging (old)
- **Dataset ID**: `dbb06129-4ab0-4988-b739-49e29b3d040b`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `rb.admin@titanmachinery.com`

**Configured Refresh Schedule** (DISABLED ❌):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `N/A` (Romance Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `Sql` | Connection: `{'server': '10.75.1.7', 'database': 'jetnavdwh'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2020-08-16 22:01:34 | 2020-08-16 22:27:40 | `Failed` | `Scheduled` | {"errorCode":"ModelRefresh_ShortMessage_Process... |
| 2020-08-15 22:02:24 | 2020-08-15 22:26:21 | `Failed` | `Scheduled` | {"errorCode":"ModelRefresh_ShortMessage_Process... |
| 2020-08-14 22:02:28 | 2020-08-14 22:24:34 | `Failed` | `Scheduled` | {"errorCode":"ModelRefresh_ShortMessage_Process... |
| 2020-08-13 22:03:28 | 2020-08-13 22:27:37 | `Failed` | `Scheduled` | {"errorCode":"ModelRefresh_ShortMessage_Process... |
| 2020-08-12 22:01:40 | 2020-08-12 22:25:16 | `Completed` | `Scheduled` | - |

### Semantic Model: TMINT_BI_Inventory_Aging_Report
- **Dataset ID**: `5df8ba3b-557c-4409-ad17-a528d8024276`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `N/A`

**Configured Refresh Schedule** (DISABLED ❌):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `09:00, 11:00, 13:00, 15:00, 17:00` (GTB Standard Time)

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2025-04-22 05:43:31 | 2025-04-22 05:47:52 | `Failed` | `OnDemand` | {"errorCode":"ModelRefresh_ShortMessage_Process... |
| 2023-03-23 10:17:25 | 2023-03-23 10:17:26 | `Failed` | `OnDemand` | {"errorCode":"ModelRefreshDisabled_CredentialNo... |
| 2022-10-04 08:31:10 | 2022-10-04 08:38:56 | `Failed` | `OnDemand` | {"errorCode":"ModelRefresh_ShortMessage_Process... |
| 2022-06-10 06:00:45 | 2022-06-10 06:15:14 | `Failed` | `Scheduled` | {"errorCode":"ModelRefresh_ShortMessage_Process... |
| 2022-06-09 14:02:02 | 2022-06-09 14:15:28 | `Failed` | `Scheduled` | {"errorCode":"ModelRefresh_ShortMessage_Process... |

### Semantic Model: TMINT_BI_Preventive_Aging_Report
- **Dataset ID**: `b93d3337-f9a4-427e-a9cd-d49e02274930`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `N/A`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `09:00, 12:00, 15:00` (GTB Standard Time)

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2023-03-23 10:17:30 | 2023-03-23 10:17:30 | `Failed` | `OnDemand` | {"errorCode":"ModelRefreshDisabled_CredentialNo... |
| 2021-10-05 09:01:12 | 2021-10-05 09:01:12 | `Disabled` | `Scheduled` | - |
| 2021-10-05 06:00:21 | 2021-10-05 06:15:35 | `Completed` | `Scheduled` | - |
| 2021-10-04 12:02:16 | 2021-10-04 12:25:29 | `Completed` | `Scheduled` | - |
| 2021-10-04 09:01:12 | 2021-10-04 09:24:22 | `Completed` | `Scheduled` | - |

### Semantic Model: Parts - Aging
- **Dataset ID**: `05a71bc2-cd63-4fa2-8911-a1df65335625`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `07:00, 15:00` (GTB Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `Sql` | Connection: `{'server': '10.75.1.7', 'database': 'jetnavdwh'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2026-09-15 04:00:26 | 2026-09-15 04:11:43 | `Completed` | `Scheduled` | - |
| 2026-09-14 12:01:19 | 2026-09-14 12:12:24 | `Completed` | `Scheduled` | - |
| 2026-09-14 04:00:25 | 2026-09-14 04:10:24 | `Completed` | `Scheduled` | - |
| 2026-09-13 12:01:15 | 2026-09-13 12:13:12 | `Completed` | `Scheduled` | - |
| 2026-09-13 04:01:12 | 2026-09-13 04:11:31 | `Completed` | `Scheduled` | - |

### Semantic Model: Parts - Aging - EndOfMonth
- **Dataset ID**: `ff2706e7-600c-4c95-b327-a11fd5c1a342`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `03:00` (FLE Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `Sql` | Connection: `{'server': '10.75.1.7', 'database': 'jetnavdwh'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2026-09-15 06:00:08 | 2026-09-15 06:08:49 | `Completed` | `ViaApi` | - |
| 2026-09-15 00:01:08 | 2026-09-15 00:13:01 | `Completed` | `Scheduled` | - |
| 2026-09-14 00:01:08 | 2026-09-14 00:12:02 | `Completed` | `Scheduled` | - |
| 2026-09-13 00:01:17 | 2026-09-13 00:13:02 | `Completed` | `Scheduled` | - |
| 2026-09-12 00:01:10 | 2026-09-12 00:12:28 | `Completed` | `Scheduled` | - |

### Semantic Model: Usage Metrics Report
- **Dataset ID**: `e3e38f8b-bed7-4248-bd79-2716063255dd`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `07:35` (UTC)

**Connected Data Sources (Lineage)**:
- Type: `Extension` | Connection: `{'path': 'UsageMetricsDataConnector', 'kind': 'UsageMetricsDataConnector'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2025-07-21 07:35:02 | 2025-07-21 07:35:02 | `Disabled` | `Scheduled` | - |
| 2025-07-20 07:35:05 | 2025-07-20 07:45:21 | `Completed` | `Scheduled` | - |
| 2025-07-19 07:35:11 | 2025-07-19 07:44:43 | `Completed` | `Scheduled` | - |
| 2025-07-18 07:35:07 | 2025-07-18 07:45:12 | `Completed` | `Scheduled` | - |
| 2025-07-17 07:35:06 | 2025-07-17 07:44:30 | `Completed` | `Scheduled` | - |

### Semantic Model: TMR Stock Order Report
- **Dataset ID**: `593e97f2-ab3e-46e4-95f5-ffa12ce25963`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `05:00` (FLE Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `Sql` | Connection: `{'server': '10.75.1.7', 'database': 'jetnavdwh'}`
- Type: `Sql` | Connection: `{'server': 'titaneu.database.windows.net', 'database': 'titanro'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2026-09-15 02:01:13 | 2026-09-15 02:14:46 | `Completed` | `Scheduled` | - |
| 2026-09-14 02:01:07 | 2026-09-14 02:12:38 | `Completed` | `Scheduled` | - |
| 2026-09-13 02:01:08 | 2026-09-13 02:11:23 | `Completed` | `Scheduled` | - |
| 2026-09-12 02:01:06 | 2026-09-12 02:13:15 | `Completed` | `Scheduled` | - |
| 2026-09-11 02:01:09 | 2026-09-11 02:10:18 | `Completed` | `Scheduled` | - |

## 4. Power BI Reports Inventory

| Report Name | Report ID | Dataset ID | Web URL |
| :--- | :--- | :--- | :--- |
| **TMINT_BI_Inventory_Aging_Report** | `daad0a4f-fb2e-4499-9fae-63be99e7c060` | `5df8ba3b-557c-4409-ad17-a528d8024276` | [Open Report](https://app.powerbi.com/groups/0f9ead1f-a393-49b0-b9ae-854cce19c159/reports/daad0a4f-fb2e-4499-9fae-63be99e7c060) |
| **TMINT_BI_Preventive_Aging_Report** | `46e62fc4-0be9-4579-82e7-b994e15a9e01` | `b93d3337-f9a4-427e-a9cd-d49e02274930` | [Open Report](https://app.powerbi.com/groups/0f9ead1f-a393-49b0-b9ae-854cce19c159/reports/46e62fc4-0be9-4579-82e7-b994e15a9e01) |
| **Parts - Aging** | `152656ef-ec32-47c0-ac60-28990d9b372c` | `05a71bc2-cd63-4fa2-8911-a1df65335625` | [Open Report](https://app.powerbi.com/groups/0f9ead1f-a393-49b0-b9ae-854cce19c159/reports/152656ef-ec32-47c0-ac60-28990d9b372c) |
| **Parts - Aging - EndOfMonth** | `3a4ef89b-b517-4fbb-afa9-9ef4ac6fc479` | `ff2706e7-600c-4c95-b327-a11fd5c1a342` | [Open Report](https://app.powerbi.com/groups/0f9ead1f-a393-49b0-b9ae-854cce19c159/reports/3a4ef89b-b517-4fbb-afa9-9ef4ac6fc479) |
| **Usage Metrics Report** | `38298a16-af11-4103-914f-7c04687894a9` | `e3e38f8b-bed7-4248-bd79-2716063255dd` | [Open Report](https://app.powerbi.com/groups/0f9ead1f-a393-49b0-b9ae-854cce19c159/reports/38298a16-af11-4103-914f-7c04687894a9) |
| **TMR Stock Order Report** | `375e34c3-d5ad-4631-9e1d-7a1c41a5d102` | `593e97f2-ab3e-46e4-95f5-ffa12ce25963` | [Open Report](https://app.powerbi.com/groups/0f9ead1f-a393-49b0-b9ae-854cce19c159/reports/375e34c3-d5ad-4631-9e1d-7a1c41a5d102) |

## 5. Dataflows & Dashboards

*No dataflows or dashboards in this workspace.*

---

## 6. Newcomer Operational Runbook & Notes
- **Primary Contact / Owner**: Refer to workspace access settings in Power BI portal.
- **Troubleshooting**: If a refresh fails in `BI_TMINT_Parts`, inspect the failure log under section 3 above and check upstream data gateway connectivity.
