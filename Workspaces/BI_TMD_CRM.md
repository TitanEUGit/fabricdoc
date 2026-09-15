# Workspace Documentation: BI_TMD_CRM

**Workspace ID**: `1492a811-679b-4107-9e63-f2135a718de7`  
**Type**: `Fabric / PowerBI Workspace`  
**Capacity ID**: `70650ed2-f7a2-46df-96e8-8089f25db80e`  
**Description**: No description provided.

---

## 1. Executive Summary & Newcomer Overview
This document contains operational and technical details for the **BI_TMD_CRM** workspace. It is designed to give new team members full visibility into key items, data models, report lineage, and refresh schedules.

## 2. Native Fabric Items Inventory

| Item Name | Item Type | Item ID | Description |
| :--- | :--- | :--- | :--- |
| **TMD CRM Activities** | `Dashboard` | `00a4c1de-265d-43f3-ac4c-1c4bec79313c` | - |
| **TMD CRM Leads** | `Dashboard` | `b93f3e64-aa63-401c-897a-13fbdaed7cfe` | - |
| **TMD CRM Opportunities** | `Dashboard` | `b96599d1-3f09-49a5-8135-e68f1067c646` | - |
| **TMD CRM Quotes** | `Dashboard` | `8e8b3a6e-298b-4b2d-9d45-9ef82c1ceddc` | - |
| **TMD CRM Sales Orders** | `Dashboard` | `e2fdc086-6178-463c-8277-9abeb540560e` | - |
| **TMD CRM Accounts** | `Dashboard` | `10fff59c-cf0c-4a68-a4a9-e8344b6703f6` | - |
| **TMD CRM Accounts Interaction** | `Dashboard` | `bfe1ea1a-d454-44d1-970c-03fd4b05a8d5` | - |
| **TMD CRM Accounts Update** | `Dashboard` | `210daf5d-6d9d-4b1f-8d0b-87e429ef4f71` | - |
| **TMD CRM Conversion Summary** | `Dashboard` | `33a26b94-1b76-40c6-bddc-1dbe4b62ec48` | - |
| **TMD CRM** | `Report` | `4b2049ba-12ab-43e9-90c8-294c7b8166df` | - |
| **Usage Metrics Report** | `Report` | `e78b4fe0-3c9f-469e-9320-fe30da457acb` | - |
| **TMD CRM** | `SemanticModel` | `ad1ee965-87d2-4d82-812f-6c6504a9d1be` | - |
| **Usage Metrics Report** | `SemanticModel` | `4de1bb70-4ae2-4c26-bb59-a496fbcb16f9` | - |

## 3. Semantic Models (Datasets) & Refresh Schedules

### Semantic Model: TMD CRM
- **Dataset ID**: `ad1ee965-87d2-4d82-812f-6c6504a9d1be`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `02:00` (FLE Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `Extension` | Connection: `{'path': 'titanmachinery.crm4.dynamics.com', 'kind': 'CommonDataService'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2026-05-14 23:00:25 | 2026-05-14 23:00:25 | `Disabled` | `Scheduled` | - |
| 2026-05-13 23:01:15 | 2026-05-13 23:18:24 | `Completed` | `Scheduled` | - |
| 2026-05-12 23:00:25 | 2026-05-12 23:07:47 | `Completed` | `Scheduled` | - |
| 2026-05-11 23:00:27 | 2026-05-11 23:13:43 | `Completed` | `Scheduled` | - |
| 2026-05-10 23:00:18 | 2026-05-10 23:07:46 | `Completed` | `Scheduled` | - |

### Semantic Model: Usage Metrics Report
- **Dataset ID**: `4de1bb70-4ae2-4c26-bb59-a496fbcb16f9`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `07:10` (UTC)

**Connected Data Sources (Lineage)**:
- Type: `Extension` | Connection: `{'path': 'UsageMetricsDataConnector', 'kind': 'UsageMetricsDataConnector'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2025-07-21 07:10:12 | 2025-07-21 07:10:12 | `Disabled` | `Scheduled` | - |
| 2025-07-20 07:10:11 | 2025-07-20 07:18:11 | `Completed` | `Scheduled` | - |
| 2025-07-19 07:10:11 | 2025-07-19 07:17:49 | `Completed` | `Scheduled` | - |
| 2025-07-18 07:10:05 | 2025-07-18 07:18:17 | `Completed` | `Scheduled` | - |
| 2025-07-17 07:10:11 | 2025-07-17 07:17:38 | `Completed` | `Scheduled` | - |

## 4. Power BI Reports Inventory

| Report Name | Report ID | Dataset ID | Web URL |
| :--- | :--- | :--- | :--- |
| **TMD CRM** | `4b2049ba-12ab-43e9-90c8-294c7b8166df` | `ad1ee965-87d2-4d82-812f-6c6504a9d1be` | [Open Report](https://app.powerbi.com/groups/1492a811-679b-4107-9e63-f2135a718de7/reports/4b2049ba-12ab-43e9-90c8-294c7b8166df) |
| **Usage Metrics Report** | `e78b4fe0-3c9f-469e-9320-fe30da457acb` | `4de1bb70-4ae2-4c26-bb59-a496fbcb16f9` | [Open Report](https://app.powerbi.com/groups/1492a811-679b-4107-9e63-f2135a718de7/reports/e78b4fe0-3c9f-469e-9320-fe30da457acb) |

## 5. Dataflows & Dashboards

**Dashboards**:
- **TMD CRM Activities** (ID: `00a4c1de-265d-43f3-ac4c-1c4bec79313c`)
- **TMD CRM Leads** (ID: `b93f3e64-aa63-401c-897a-13fbdaed7cfe`)
- **TMD CRM Opportunities** (ID: `b96599d1-3f09-49a5-8135-e68f1067c646`)
- **TMD CRM Quotes** (ID: `8e8b3a6e-298b-4b2d-9d45-9ef82c1ceddc`)
- **TMD CRM Sales Orders** (ID: `e2fdc086-6178-463c-8277-9abeb540560e`)
- **TMD CRM Accounts** (ID: `10fff59c-cf0c-4a68-a4a9-e8344b6703f6`)
- **TMD CRM Accounts Interaction** (ID: `bfe1ea1a-d454-44d1-970c-03fd4b05a8d5`)
- **TMD CRM Accounts Update** (ID: `210daf5d-6d9d-4b1f-8d0b-87e429ef4f71`)
- **TMD CRM Conversion Summary** (ID: `33a26b94-1b76-40c6-bddc-1dbe4b62ec48`)

---

## 6. Newcomer Operational Runbook & Notes
- **Primary Contact / Owner**: Refer to workspace access settings in Power BI portal.
- **Troubleshooting**: If a refresh fails in `BI_TMD_CRM`, inspect the failure log under section 3 above and check upstream data gateway connectivity.
