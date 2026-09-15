# Workspace Documentation: BI_TMB_Aftersales

**Workspace ID**: `c8927ad9-aed7-4e00-baf5-ef98180fd537`  
**Type**: `Fabric / PowerBI Workspace`  
**Capacity ID**: `70650ed2-f7a2-46df-96e8-8089f25db80e`  
**Description**: No description provided.

---

## 1. Executive Summary & Newcomer Overview
This document contains operational and technical details for the **BI_TMB_Aftersales** workspace. It is designed to give new team members full visibility into key items, data models, report lineage, and refresh schedules.

## 2. Native Fabric Items Inventory

| Item Name | Item Type | Item ID | Description |
| :--- | :--- | :--- | :--- |
| **TMB SP Stock_Sales Overview** | `Report` | `da43ad07-ae0a-4205-8a96-56604304a869` | - |
| **TMB SP Turn per Vendor** | `Report` | `68793424-d59d-4299-ab1c-b5d657bc6cf3` | - |
| **TMB Open Service Orders** | `Report` | `20dda511-d28a-4c29-b593-cd40073faff0` | - |
| **Report Usage Metrics Report** | `Report` | `6fa938f6-8b67-41a9-8b1d-a7e07dcdca1d` | - |
| **TMB Parts Fill Rate** | `Report` | `1d55023d-128f-467a-b801-1f581764b05b` | - |
| **TMB Parts Sales (OPS_limit)** | `Report` | `f74912a4-11a9-459f-b613-0d3da193a38f` | - |
| **Usage Metrics Report** | `Report` | `bbf327d1-8fab-451a-89ea-9eda17cfb219` | - |
| **TMB SP Stock_Sales Overview** | `SemanticModel` | `863f3203-8f44-405b-8dbc-73fe1a8d2023` | - |
| **TMB SP Turn per Vendor** | `SemanticModel` | `38f04f35-176b-45e1-85f6-6e24dca0f612` | - |
| **TMB Open Service Orders** | `SemanticModel` | `2363bdcc-7277-47d5-9948-2ee49f360901` | - |
| **Report Usage Metrics Model** | `SemanticModel` | `fffd053c-9ed3-4492-b4ec-10a6d6dbc8af` | - |
| **TMB Parts Fill Rate** | `SemanticModel` | `0683f015-c865-428c-a94f-35d532a41e84` | - |
| **TMB Parts Sales (OPS_limit)** | `SemanticModel` | `bf978c4e-4111-4f35-a321-d0b6cba8ffe8` | - |
| **Usage Metrics Report** | `SemanticModel` | `e9105555-df07-421a-93c4-b0ce050b34ea` | - |

## 3. Semantic Models (Datasets) & Refresh Schedules

### Semantic Model: TMB SP Stock_Sales Overview
- **Dataset ID**: `863f3203-8f44-405b-8dbc-73fe1a8d2023`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `01:00` (Romance Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `Sql` | Connection: `{'server': '10.75.1.7', 'database': 'jetnavdwh'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2026-09-14 23:00:13 | 2026-09-14 23:07:46 | `Completed` | `Scheduled` | - |
| 2026-09-13 23:00:11 | 2026-09-13 23:08:07 | `Completed` | `Scheduled` | - |
| 2026-09-12 23:00:16 | 2026-09-12 23:15:21 | `Completed` | `Scheduled` | - |
| 2026-09-11 23:00:19 | 2026-09-11 23:08:21 | `Completed` | `Scheduled` | - |
| 2026-09-10 23:00:19 | 2026-09-10 23:08:01 | `Completed` | `Scheduled` | - |

### Semantic Model: TMB SP Turn per Vendor
- **Dataset ID**: `38f04f35-176b-45e1-85f6-6e24dca0f612`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `N/A`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `05:00` (Romance Standard Time)

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2025-08-25 03:01:03 | 2025-08-25 03:01:03 | `Disabled` | `Scheduled` | - |
| 2025-08-24 03:01:11 | 2025-08-24 03:14:12 | `Completed` | `Scheduled` | - |
| 2025-08-23 03:01:04 | 2025-08-23 03:05:50 | `Completed` | `Scheduled` | - |
| 2025-08-22 03:01:14 | 2025-08-22 03:09:15 | `Completed` | `Scheduled` | - |
| 2025-08-21 03:01:09 | 2025-08-21 03:10:02 | `Completed` | `Scheduled` | - |

### Semantic Model: TMB Open Service Orders
- **Dataset ID**: `2363bdcc-7277-47d5-9948-2ee49f360901`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `N/A`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `01:00` (Romance Standard Time)

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2025-08-17 23:01:15 | 2025-08-17 23:01:15 | `Disabled` | `Scheduled` | - |
| 2025-08-16 23:01:16 | 2025-08-16 23:09:13 | `Completed` | `Scheduled` | - |
| 2025-08-15 23:01:16 | 2025-08-15 23:10:01 | `Completed` | `Scheduled` | - |
| 2025-08-14 23:01:17 | 2025-08-14 23:11:19 | `Completed` | `Scheduled` | - |
| 2025-08-13 23:01:16 | 2025-08-13 23:11:19 | `Completed` | `Scheduled` | - |

### Semantic Model: Report Usage Metrics Model
- **Dataset ID**: `fffd053c-9ed3-4492-b4ec-10a6d6dbc8af`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `False`
- **Configured By**: `OBaliuta@titanmachinery.ua`

*No refresh schedule configured.*

### Semantic Model: TMB Parts Fill Rate
- **Dataset ID**: `0683f015-c865-428c-a94f-35d532a41e84`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `05:00` (FLE Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `Sql` | Connection: `{'server': '10.75.1.7', 'database': 'jetnavdwh'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2025-08-25 02:01:06 | 2025-08-25 02:01:06 | `Disabled` | `Scheduled` | - |
| 2025-08-24 02:01:01 | 2025-08-24 02:03:34 | `Completed` | `Scheduled` | - |
| 2025-08-23 02:01:06 | 2025-08-23 02:07:44 | `Completed` | `Scheduled` | - |
| 2025-08-22 02:01:05 | 2025-08-22 02:04:57 | `Completed` | `Scheduled` | - |
| 2025-08-21 02:02:01 | 2025-08-21 02:04:46 | `Completed` | `Scheduled` | - |

### Semantic Model: TMB Parts Sales (OPS_limit)
- **Dataset ID**: `bf978c4e-4111-4f35-a321-d0b6cba8ffe8`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `08:00` (FLE Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `Extension` | Connection: `{'path': 'PowerPlatformDataflows', 'kind': 'PowerPlatformDataflows'}`
- Type: `Sql` | Connection: `{'server': '10.75.1.7', 'database': 'jetnavdwh'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/int_orderbook', 'database': 'tmeu order book'}`
- Type: `Sql` | Connection: `{'server': 'cwgz5ola5r6u5e4heu5qw3drgy-zzqhzdizzmcurky2zbgw4gw7la.datawarehouse.fabric.microsoft.com', 'database': 'tmeu_bronze_lakehouse'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2026-09-15 05:01:13 | 2026-09-15 05:23:17 | `Completed` | `Scheduled` | - |
| 2026-09-14 05:01:11 | 2026-09-14 05:24:44 | `Completed` | `Scheduled` | - |
| 2026-09-13 05:02:11 | 2026-09-13 05:54:20 | `Completed` | `Scheduled` | - |
| 2026-09-12 05:01:16 | 2026-09-12 05:24:14 | `Completed` | `Scheduled` | - |
| 2026-09-11 05:02:15 | 2026-09-11 05:24:21 | `Completed` | `Scheduled` | - |

### Semantic Model: Usage Metrics Report
- **Dataset ID**: `e9105555-df07-421a-93c4-b0ce050b34ea`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `13:46` (UTC)

**Connected Data Sources (Lineage)**:
- Type: `Extension` | Connection: `{'path': 'UsageMetricsDataConnector', 'kind': 'UsageMetricsDataConnector'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2025-12-15 13:46:00 | 2025-12-15 13:46:00 | `Disabled` | `Scheduled` | - |
| 2025-12-14 13:46:00 | 2025-12-14 13:46:38 | `Completed` | `Scheduled` | - |
| 2025-12-13 13:46:01 | 2025-12-13 13:46:54 | `Completed` | `Scheduled` | - |
| 2025-12-12 13:46:02 | 2025-12-12 13:46:14 | `Completed` | `Scheduled` | - |
| 2025-12-11 13:46:16 | 2025-12-11 13:46:58 | `Completed` | `Scheduled` | - |

## 4. Power BI Reports Inventory

| Report Name | Report ID | Dataset ID | Web URL |
| :--- | :--- | :--- | :--- |
| **TMB SP Stock_Sales Overview** | `da43ad07-ae0a-4205-8a96-56604304a869` | `863f3203-8f44-405b-8dbc-73fe1a8d2023` | [Open Report](https://app.powerbi.com/groups/c8927ad9-aed7-4e00-baf5-ef98180fd537/reports/da43ad07-ae0a-4205-8a96-56604304a869) |
| **TMB SP Turn per Vendor** | `68793424-d59d-4299-ab1c-b5d657bc6cf3` | `38f04f35-176b-45e1-85f6-6e24dca0f612` | [Open Report](https://app.powerbi.com/groups/c8927ad9-aed7-4e00-baf5-ef98180fd537/reports/68793424-d59d-4299-ab1c-b5d657bc6cf3) |
| **TMB Open Service Orders** | `20dda511-d28a-4c29-b593-cd40073faff0` | `2363bdcc-7277-47d5-9948-2ee49f360901` | [Open Report](https://app.powerbi.com/groups/c8927ad9-aed7-4e00-baf5-ef98180fd537/reports/20dda511-d28a-4c29-b593-cd40073faff0) |
| **Report Usage Metrics Report** | `6fa938f6-8b67-41a9-8b1d-a7e07dcdca1d` | `fffd053c-9ed3-4492-b4ec-10a6d6dbc8af` | [Open Report](https://app.powerbi.com/groups/c8927ad9-aed7-4e00-baf5-ef98180fd537/reports/6fa938f6-8b67-41a9-8b1d-a7e07dcdca1d) |
| **TMB Parts Fill Rate** | `1d55023d-128f-467a-b801-1f581764b05b` | `0683f015-c865-428c-a94f-35d532a41e84` | [Open Report](https://app.powerbi.com/groups/c8927ad9-aed7-4e00-baf5-ef98180fd537/reports/1d55023d-128f-467a-b801-1f581764b05b) |
| **TMB Parts Sales (OPS_limit)** | `f74912a4-11a9-459f-b613-0d3da193a38f` | `bf978c4e-4111-4f35-a321-d0b6cba8ffe8` | [Open Report](https://app.powerbi.com/groups/c8927ad9-aed7-4e00-baf5-ef98180fd537/reports/f74912a4-11a9-459f-b613-0d3da193a38f) |
| **Usage Metrics Report** | `bbf327d1-8fab-451a-89ea-9eda17cfb219` | `e9105555-df07-421a-93c4-b0ce050b34ea` | [Open Report](https://app.powerbi.com/groups/c8927ad9-aed7-4e00-baf5-ef98180fd537/reports/bbf327d1-8fab-451a-89ea-9eda17cfb219) |

## 5. Dataflows & Dashboards

*No dataflows or dashboards in this workspace.*

---

## 6. Newcomer Operational Runbook & Notes
- **Primary Contact / Owner**: Refer to workspace access settings in Power BI portal.
- **Troubleshooting**: If a refresh fails in `BI_TMB_Aftersales`, inspect the failure log under section 3 above and check upstream data gateway connectivity.
