# Workspace Documentation: BI_TMR_CRM

**Workspace ID**: `f0143435-d097-4e8d-8577-5d89773161e1`  
**Type**: `Fabric / PowerBI Workspace`  
**Capacity ID**: `70650ed2-f7a2-46df-96e8-8089f25db80e`  
**Description**: No description provided.

---

## 1. Executive Summary & Newcomer Overview
This document contains operational and technical details for the **BI_TMR_CRM** workspace. It is designed to give new team members full visibility into key items, data models, report lineage, and refresh schedules.

## 2. Native Fabric Items Inventory

| Item Name | Item Type | Item ID | Description |
| :--- | :--- | :--- | :--- |
| **BI_Activities (by Owner)** | `Dashboard` | `40c3f0f5-f4d9-4505-ad85-62cc81c24fbe` | - |
| **BI_Activities (by Creator)** | `Dashboard` | `c187f245-2a07-4b07-8215-df41d59c7d82` | - |
| **BI_Leads** | `Dashboard` | `ada6602f-11da-4e93-8e14-37105b42cf86` | - |
| **BI_Opportunities** | `Dashboard` | `2876aa0d-52cb-4e9a-a1a7-307c318373b6` | - |
| **BI_Quotes** | `Dashboard` | `8f0e60b8-267d-4593-b92c-b8c6eeccff9f` | - |
| **BI_Quote & Products** | `Dashboard` | `55732b90-f31c-45a4-965f-7ca5011f4880` | - |
| **BI_Sales Orders** | `Dashboard` | `804f560f-ea24-42b6-aad1-28c8371d3803` | - |
| **BI_Accounts** | `Dashboard` | `b9d287e9-99dc-4b3a-bc3e-406ab115489b` | - |
| **BI_Accounts Geographics** | `Dashboard` | `00acb344-8168-408f-9aa7-410ff56c2788` | - |
| **BI_Accounts Update** | `Dashboard` | `ba668f7f-2ad4-4a0a-860c-02b960ab0fcf` | - |
| **BI_Activities_Detailed_Table** | `Dashboard` | `ad263429-93ae-48cb-b9a0-762332d0545c` | - |
| **BI_Product KPI** | `Dashboard` | `724a5f77-2da4-446d-ba64-7fa8b2d5e9f2` | - |
| **BI_Quoted Products KPI** | `Dashboard` | `d192335f-7534-4c93-ba52-65425350d147` | - |
| **TMR CRM** | `Report` | `128fbd64-22dc-45f7-ba3b-47d80d5bdfc2` | - |
| **Dashboard Usage Metrics Report** | `Report` | `2ba3a71c-3d0c-477d-afd7-a1008ea97ab7` | - |
| **TMR Quoted Products** | `Report` | `ecff3ffc-3417-4ac2-8c6a-9af756e7bb9f` | - |
| **TMR Product KPI** | `Report` | `1fff6025-c9e9-41bb-b17d-3d21386314d6` | - |
| **Usage Metrics Report** | `Report` | `2384d31a-3419-4469-a9fb-35669ecc0400` | - |
| **TMR CRM** | `SemanticModel` | `d6aeaca3-5200-4200-9d45-9b78b34d8587` | - |
| **Dashboard Usage Metrics Model** | `SemanticModel` | `cbaa7c70-12f0-4e6e-bf6e-fcccc1d6d90c` | - |
| **TMR Quoted Products** | `SemanticModel` | `a4bca9c1-8eec-48bb-b0f9-042ca9fd950a` | - |
| **TMR Product KPI** | `SemanticModel` | `5a0e9736-ca81-4ccf-8dff-86580e0cb2bf` | - |
| **Usage Metrics Report** | `SemanticModel` | `5dccfe3e-9fb3-4146-9928-0de00691dcf7` | - |

## 3. Semantic Models (Datasets) & Refresh Schedules

### Semantic Model: TMR CRM
- **Dataset ID**: `d6aeaca3-5200-4200-9d45-9b78b34d8587`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `08:00` (FLE Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `Extension` | Connection: `{'path': 'titanromania.crm4.dynamics.com', 'kind': 'CommonDataService'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2026-05-12 05:00:18 | 2026-05-12 05:00:18 | `Disabled` | `Scheduled` | - |
| 2026-05-11 05:01:07 | 2026-05-11 05:07:51 | `Completed` | `Scheduled` | - |
| 2026-05-10 05:01:06 | 2026-05-10 05:06:21 | `Completed` | `Scheduled` | - |
| 2026-05-09 05:01:07 | 2026-05-09 05:08:53 | `Completed` | `Scheduled` | - |
| 2026-05-08 05:01:06 | 2026-05-08 05:07:24 | `Completed` | `Scheduled` | - |

### Semantic Model: Dashboard Usage Metrics Model
- **Dataset ID**: `cbaa7c70-12f0-4e6e-bf6e-fcccc1d6d90c`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `False`
- **Configured By**: `MaGheorghe@titanmachinery.ro`

*No refresh schedule configured.*

### Semantic Model: TMR Quoted Products
- **Dataset ID**: `a4bca9c1-8eec-48bb-b0f9-042ca9fd950a`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `05:00` (FLE Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `Extension` | Connection: `{'path': 'titanromania.crm4.dynamics.com', 'kind': 'CommonDataService'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2025-10-06 02:01:10 | 2025-10-06 02:01:10 | `Disabled` | `Scheduled` | - |
| 2025-10-05 02:01:10 | 2025-10-05 02:12:17 | `Completed` | `Scheduled` | - |
| 2025-10-04 02:01:09 | 2025-10-04 02:11:14 | `Completed` | `Scheduled` | - |
| 2025-10-03 02:01:09 | 2025-10-03 02:11:46 | `Completed` | `Scheduled` | - |
| 2025-10-02 02:01:10 | 2025-10-02 02:11:59 | `Completed` | `Scheduled` | - |

### Semantic Model: TMR Product KPI
- **Dataset ID**: `5a0e9736-ca81-4ccf-8dff-86580e0cb2bf`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `01:00` (FLE Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `Extension` | Connection: `{'path': 'titanromania.crm4.dynamics.com', 'kind': 'CommonDataService'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2026-01-12 23:00:27 | 2026-01-12 23:00:27 | `Disabled` | `Scheduled` | - |
| 2026-01-11 23:00:27 | 2026-01-11 23:07:33 | `Completed` | `Scheduled` | - |
| 2026-01-10 23:00:26 | 2026-01-10 23:08:10 | `Completed` | `Scheduled` | - |
| 2026-01-09 23:00:24 | 2026-01-09 23:07:55 | `Completed` | `Scheduled` | - |
| 2026-01-08 23:00:12 | 2026-01-08 23:05:58 | `Completed` | `Scheduled` | - |

### Semantic Model: Usage Metrics Report
- **Dataset ID**: `5dccfe3e-9fb3-4146-9928-0de00691dcf7`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `09:02` (UTC)

**Connected Data Sources (Lineage)**:
- Type: `Extension` | Connection: `{'path': 'UsageMetricsDataConnector', 'kind': 'UsageMetricsDataConnector'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2025-07-23 09:04:15 | 2025-07-23 09:04:15 | `Disabled` | `Scheduled` | - |
| 2025-07-22 09:03:23 | 2025-07-22 09:17:48 | `Completed` | `Scheduled` | - |
| 2025-07-21 09:04:19 | 2025-07-21 09:18:40 | `Completed` | `Scheduled` | - |
| 2025-07-20 09:03:18 | 2025-07-20 09:17:58 | `Completed` | `Scheduled` | - |
| 2025-07-19 09:04:16 | 2025-07-19 09:18:36 | `Completed` | `Scheduled` | - |

## 4. Power BI Reports Inventory

| Report Name | Report ID | Dataset ID | Web URL |
| :--- | :--- | :--- | :--- |
| **TMR CRM** | `128fbd64-22dc-45f7-ba3b-47d80d5bdfc2` | `d6aeaca3-5200-4200-9d45-9b78b34d8587` | [Open Report](https://app.powerbi.com/groups/f0143435-d097-4e8d-8577-5d89773161e1/reports/128fbd64-22dc-45f7-ba3b-47d80d5bdfc2) |
| **Dashboard Usage Metrics Report** | `2ba3a71c-3d0c-477d-afd7-a1008ea97ab7` | `cbaa7c70-12f0-4e6e-bf6e-fcccc1d6d90c` | [Open Report](https://app.powerbi.com/groups/f0143435-d097-4e8d-8577-5d89773161e1/reports/2ba3a71c-3d0c-477d-afd7-a1008ea97ab7) |
| **TMR Quoted Products** | `ecff3ffc-3417-4ac2-8c6a-9af756e7bb9f` | `a4bca9c1-8eec-48bb-b0f9-042ca9fd950a` | [Open Report](https://app.powerbi.com/groups/f0143435-d097-4e8d-8577-5d89773161e1/reports/ecff3ffc-3417-4ac2-8c6a-9af756e7bb9f) |
| **TMR Product KPI** | `1fff6025-c9e9-41bb-b17d-3d21386314d6` | `5a0e9736-ca81-4ccf-8dff-86580e0cb2bf` | [Open Report](https://app.powerbi.com/groups/f0143435-d097-4e8d-8577-5d89773161e1/reports/1fff6025-c9e9-41bb-b17d-3d21386314d6) |
| **Usage Metrics Report** | `2384d31a-3419-4469-a9fb-35669ecc0400` | `5dccfe3e-9fb3-4146-9928-0de00691dcf7` | [Open Report](https://app.powerbi.com/groups/f0143435-d097-4e8d-8577-5d89773161e1/reports/2384d31a-3419-4469-a9fb-35669ecc0400) |

## 5. Dataflows & Dashboards

**Dashboards**:
- **BI_Activities (by Owner)** (ID: `40c3f0f5-f4d9-4505-ad85-62cc81c24fbe`)
- **BI_Activities (by Creator)** (ID: `c187f245-2a07-4b07-8215-df41d59c7d82`)
- **BI_Leads** (ID: `ada6602f-11da-4e93-8e14-37105b42cf86`)
- **BI_Opportunities** (ID: `2876aa0d-52cb-4e9a-a1a7-307c318373b6`)
- **BI_Quotes** (ID: `8f0e60b8-267d-4593-b92c-b8c6eeccff9f`)
- **BI_Quote & Products** (ID: `55732b90-f31c-45a4-965f-7ca5011f4880`)
- **BI_Sales Orders** (ID: `804f560f-ea24-42b6-aad1-28c8371d3803`)
- **BI_Accounts** (ID: `b9d287e9-99dc-4b3a-bc3e-406ab115489b`)
- **BI_Accounts Geographics** (ID: `00acb344-8168-408f-9aa7-410ff56c2788`)
- **BI_Accounts Update** (ID: `ba668f7f-2ad4-4a0a-860c-02b960ab0fcf`)
- **BI_Activities_Detailed_Table** (ID: `ad263429-93ae-48cb-b9a0-762332d0545c`)
- **BI_Product KPI** (ID: `724a5f77-2da4-446d-ba64-7fa8b2d5e9f2`)
- **BI_Quoted Products KPI** (ID: `d192335f-7534-4c93-ba52-65425350d147`)

---

## 6. Newcomer Operational Runbook & Notes
- **Primary Contact / Owner**: Refer to workspace access settings in Power BI portal.
- **Troubleshooting**: If a refresh fails in `BI_TMR_CRM`, inspect the failure log under section 3 above and check upstream data gateway connectivity.
