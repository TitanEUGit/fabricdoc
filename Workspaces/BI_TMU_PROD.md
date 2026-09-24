# Workspace Documentation: BI_TMU_PROD

**Workspace ID**: `49226436-1f31-4889-a274-968ed5954d4c`  
**Type**: `Fabric / PowerBI Workspace`  
**Capacity ID**: `70650ed2-f7a2-46df-96e8-8089f25db80e`  
**Description**: No description provided.

---

## 1. Executive Summary & Newcomer Overview

> [!IMPORTANT]
> **TMU Production Operations & Supply Chain**
> This workspace houses a variety of operational reports, dashboards, and critical dataflows for Ukraine (TMU). Notably, it contains cross-country legacy dataflows that are still heavily relied upon.

> [!WARNING]
> **Deprecated Items (Pending Decommissioning)**
> - **TMU Returns**: Deprecated.
> - **TMU WG Sales Forecast**: Forecast based on old Excel flows. Deprecated.

### Key Dataflows & Reports
| Item Name | Type | What It Shows / Context |
|:---|:---|:---|
| **TMEU_FX_Rates** | `Dataflow` | Contains EU USD/EUR FX rates depending on the official TMA finance file. **Warning:** Although located in TMU, it is used across *many* countries and reports. As a legacy dataflow, it should ideally be migrated to a Delta table, but this will be time-consuming due to heavy downstream dependencies. |
| **TMU 1C AR Dataflow E** | `Dataflow` | Accounts receivable dataflow. It depends on Excel because the standard API cannot handle the compute required for this report. |
| **TMU AfterSales Credit Limits Report** | `Report` | Tracks customer credit limits and their review in a dedicated workflow. **Features writeback functionality.** |
| **TMU Parts Transport Cost Awareness** | `Report` | Calculates the transport share of delivered Aftersales goods. |
| **TMU PIH** | `Report` | Detailed inventory report developed specifically for the purchase/supply department. *(Note: Most of this data can also be found in the standard OPS package).* |
| **TMU SC Dashboard** | `Report` | Supply Chain dashboard for the TMU purchase/supply chain department. |
| **TMU WG Forecast Accuracy** | `Report` | WG sales budget report. **Features writeback functionality.** |

This document contains operational and technical details for the **BI_TMU_PROD** workspace. It is designed to give new team members full visibility into key items, data models, report lineage, and refresh schedules.

## 2. Native Fabric Items Inventory

| Item Name | Item Type | Item ID | Description |
| :--- | :--- | :--- | :--- |
| **TMU Returns** | `Report` | `28cdcda3-cc3c-494f-8f35-198bd319296e` | - |
| **TMU Service Mileage & Hours** | `Report` | `e3b094ea-dc2b-4fb4-aa2c-7dc0bf440989` | - |
| **TMU Service Sales & Working Hours** | `Report` | `fa0f15fa-ede4-4cbc-a756-1b421aa6416d` | - |
| **TMU PIH** | `Report` | `cc2d6e74-bdae-42f6-881c-803dc65a2a78` | - |
| **TMU SC Dashboard** | `Report` | `1f671065-1a5d-416a-b58d-80fd087d0a13` | - |
| **TMU SC Dashboard 2024** | `Report` | `bc5d2a3e-b9bc-421f-a3ac-9d4e3f584962` | - |
| **Usage Metrics Report** | `Report` | `8fcb6096-ecb9-436e-81d4-62098b9f93e0` | - |
| **TMU WG Forecast Accuracy** | `Report` | `c524a7b2-4ece-4920-b102-d0b6f12ed09a` | - |
| **TMU Parts Transport Cost Awareness** | `Report` | `cf4e107e-1ff0-43fc-bc80-d002685ce036` | - |
| **TMU SC Dashboard 2025** | `Report` | `cca5cf91-96fd-4822-974a-7f4d58a10ded` | - |
| **TMU WG Sales Forecast** | `Report` | `e3e3f374-a9e7-4387-b218-8c83c4ed088f` | - |
| **TMU AfterSales Credit Limits Report** | `Report` | `6ea8f577-ebe1-48da-82dd-c974d89f3240` | - |
| **TMU Returns** | `SemanticModel` | `e8d58fd3-687f-4e40-8a7e-1e2d8fe4b1fc` | - |
| **TMU Service Mileage & Hours** | `SemanticModel` | `0aa29cbe-c6ec-4533-8d63-76422659d1ac` | - |
| **TMU Service Sales & Working Hours** | `SemanticModel` | `93ea0d0e-8fe0-4b6a-8050-7076e94c528c` | - |
| **TMU PIH** | `SemanticModel` | `49074992-c1ff-4f5c-a7d1-0fc8e61b7a8c` | - |
| **TMU SC Dashboard** | `SemanticModel` | `33d8e090-1d24-47fd-be45-d6ed2ee5cfdb` | - |
| **TMU SC Dashboard 2024** | `SemanticModel` | `adea2dd9-db57-4e79-9b64-405c7183e085` | - |
| **Usage Metrics Report** | `SemanticModel` | `3c187fc2-b12f-4ba7-ad0b-fa10fdeb4b5f` | - |
| **TMU WG Forecast Accuracy** | `SemanticModel` | `5eb681ae-11b2-4c8a-a71b-2f58374b05c8` | - |
| **TMU Parts Transport Cost Awareness** | `SemanticModel` | `2ec90fe7-61b9-4b0a-9f24-46d0230c2265` | - |
| **TMU SC Dashboard 2025** | `SemanticModel` | `811e22b8-ec21-4330-ad4f-10e3f45f05a0` | - |
| **TMU WG Sales Forecast** | `SemanticModel` | `c9a81717-a93b-4d19-9855-8e2a1b8bb05b` | - |
| **TMU AfterSales Credit Limits Report** | `SemanticModel` | `fa85ef02-d7db-436a-9df6-eec70bedb2d7` | - |

## 3. Semantic Models (Datasets) & Refresh Schedules

### Semantic Model: TMU Returns
- **Dataset ID**: `e8d58fd3-687f-4e40-8a7e-1e2d8fe4b1fc`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `07:00` (GTB Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `Sql` | Connection: `{'server': 'cwgz5ola5r6u5e4heu5qw3drgy-zzqhzdizzmcurky2zbgw4gw7la.datawarehouse.fabric.microsoft.com', 'database': 'tmu_bronze_lakehouse'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2026-02-01 05:01:12 | 2026-02-01 05:01:12 | `Disabled` | `Scheduled` | - |
| 2026-01-31 05:00:07 | 2026-01-31 05:01:50 | `Completed` | `Scheduled` | - |
| 2026-01-30 05:00:23 | 2026-01-30 05:03:30 | `Completed` | `Scheduled` | - |
| 2026-01-29 05:00:25 | 2026-01-29 05:03:21 | `Completed` | `Scheduled` | - |
| 2026-01-28 05:00:17 | 2026-01-28 05:02:39 | `Completed` | `Scheduled` | - |

### Semantic Model: TMU Service Mileage & Hours
- **Dataset ID**: `0aa29cbe-c6ec-4533-8d63-76422659d1ac`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `07:00` (GTB Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `Sql` | Connection: `{'server': 'cwgz5ola5r6u5e4heu5qw3drgy-zzqhzdizzmcurky2zbgw4gw7la.datawarehouse.fabric.microsoft.com', 'database': 'tmu_bronze_lakehouse'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2026-03-22 05:01:09 | 2026-03-22 05:01:09 | `Disabled` | `Scheduled` | - |
| 2026-03-21 05:01:12 | 2026-03-21 05:03:58 | `Completed` | `Scheduled` | - |
| 2026-03-20 05:01:06 | 2026-03-20 05:02:37 | `Completed` | `Scheduled` | - |
| 2026-03-19 05:01:08 | 2026-03-19 05:02:35 | `Completed` | `Scheduled` | - |
| 2026-03-18 05:00:15 | 2026-03-18 05:03:16 | `Completed` | `Scheduled` | - |

### Semantic Model: TMU Service Sales & Working Hours
- **Dataset ID**: `93ea0d0e-8fe0-4b6a-8050-7076e94c528c`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `07:00` (GTB Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `Sql` | Connection: `{'server': 'cwgz5ola5r6u5e4heu5qw3drgy-zzqhzdizzmcurky2zbgw4gw7la.datawarehouse.fabric.microsoft.com', 'database': 'tmu_bronze_lakehouse'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2026-02-01 05:01:06 | 2026-02-01 05:01:06 | `Disabled` | `Scheduled` | - |
| 2026-01-31 05:00:13 | 2026-01-31 05:02:21 | `Completed` | `Scheduled` | - |
| 2026-01-30 05:00:25 | 2026-01-30 05:03:22 | `Completed` | `Scheduled` | - |
| 2026-01-29 05:00:27 | 2026-01-29 05:03:10 | `Completed` | `Scheduled` | - |
| 2026-01-28 05:00:09 | 2026-01-28 05:01:48 | `Completed` | `Scheduled` | - |

### Semantic Model: TMU PIH
- **Dataset ID**: `49074992-c1ff-4f5c-a7d1-0fc8e61b7a8c`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `08:00` (FLE Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `Extension` | Connection: `{'path': 'PowerPlatformDataflows', 'kind': 'PowerPlatformDataflows'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmeu_inventorybook', 'database': 'tmeu inventory book'}`
- Type: `Sql` | Connection: `{'server': 'cwgz5ola5r6u5e4heu5qw3drgy-zzqhzdizzmcurky2zbgw4gw7la.datawarehouse.fabric.microsoft.com', 'database': 'tmu_bronze_lakehouse'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2026-09-15 05:01:12 | 2026-09-15 05:03:55 | `Completed` | `Scheduled` | - |
| 2026-09-14 05:00:21 | 2026-09-14 05:02:43 | `Completed` | `Scheduled` | - |
| 2026-09-13 05:01:09 | 2026-09-13 05:03:11 | `Completed` | `Scheduled` | - |
| 2026-09-12 05:00:19 | 2026-09-12 05:02:01 | `Completed` | `Scheduled` | - |
| 2026-09-11 05:01:11 | 2026-09-11 05:03:54 | `Completed` | `Scheduled` | - |

### Semantic Model: TMU SC Dashboard
- **Dataset ID**: `33d8e090-1d24-47fd-be45-d6ed2ee5cfdb`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `09:00` (GTB Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmu_prod', 'database': 'tmu pih'}`
- Type: `Web` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/Collaboration/Shared%20Documents/INT_POWERBI_HELPER/TMU/suply_chain_db/sc_dashboard_budget_title.xlsx'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_eoc_sales_dashboard', 'database': 'tmu sales dashboard'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2026-09-15 06:01:09 | 2026-09-15 06:03:53 | `Completed` | `Scheduled` | - |
| 2026-09-14 06:00:29 | 2026-09-14 06:03:17 | `Completed` | `Scheduled` | - |
| 2026-09-13 06:01:06 | 2026-09-13 06:02:37 | `Completed` | `Scheduled` | - |
| 2026-09-12 06:00:28 | 2026-09-12 06:02:45 | `Completed` | `Scheduled` | - |
| 2026-09-11 06:01:14 | 2026-09-11 06:03:34 | `Completed` | `Scheduled` | - |

### Semantic Model: TMU SC Dashboard 2024
- **Dataset ID**: `adea2dd9-db57-4e79-9b64-405c7183e085`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (DISABLED ❌):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `22:00` (UTC)

**Connected Data Sources (Lineage)**:
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmu_prod', 'database': 'tmu pih'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_eoc_sales_dashboard', 'database': 'tmu sales dashboard'}`
- Type: `Web` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/Collaboration/Shared%20Documents/INT_POWERBI_HELPER/TMU/suply_chain_db/sc_dashboard_budget_title.xlsx'}`

### Semantic Model: Usage Metrics Report
- **Dataset ID**: `3c187fc2-b12f-4ba7-ad0b-fa10fdeb4b5f`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `08:25` (UTC)

**Connected Data Sources (Lineage)**:
- Type: `Extension` | Connection: `{'path': 'UsageMetricsDataConnector', 'kind': 'UsageMetricsDataConnector'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2025-07-21 08:25:14 | 2025-07-21 08:25:14 | `Disabled` | `Scheduled` | - |
| 2025-07-20 08:25:14 | 2025-07-20 08:25:45 | `Completed` | `Scheduled` | - |
| 2025-07-19 08:25:15 | 2025-07-19 08:25:29 | `Completed` | `Scheduled` | - |
| 2025-07-18 08:25:19 | 2025-07-18 08:25:33 | `Completed` | `Scheduled` | - |
| 2025-07-17 08:25:18 | 2025-07-17 08:25:46 | `Completed` | `Scheduled` | - |

### Semantic Model: TMU WG Forecast Accuracy
- **Dataset ID**: `5eb681ae-11b2-4c8a-a71b-2f58374b05c8`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `10:00` (UTC)

**Connected Data Sources (Lineage)**:
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/int_orderbook', 'database': 'tmeu order book'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmeu_inventorybook', 'database': 'tmeu inventory book'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmu_opspackage', 'database': 'tmu ops package'}`
- Type: `Extension` | Connection: `{'path': 'PowerPlatformDataflows', 'kind': 'PowerPlatformDataflows'}`
- Type: `Web` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/Collaboration/Shared%20Documents/INT_POWERBI_HELPER/TMU/Order%20Helper/Models%20and%20Leadtime.xlsx'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2026-09-15 10:02:06 | 2026-09-15 10:05:51 | `Completed` | `Scheduled` | - |
| 2026-09-14 10:02:12 | 2026-09-14 10:06:58 | `Completed` | `Scheduled` | - |
| 2026-09-13 10:02:08 | 2026-09-13 10:06:50 | `Completed` | `Scheduled` | - |
| 2026-09-12 10:02:10 | 2026-09-12 10:06:40 | `Completed` | `Scheduled` | - |
| 2026-09-11 10:02:06 | 2026-09-11 10:05:50 | `Completed` | `Scheduled` | - |

### Semantic Model: TMU Parts Transport Cost Awareness
- **Dataset ID**: `2ec90fe7-61b9-4b0a-9f24-46d0230c2265`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `08:00` (FLE Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `Sql` | Connection: `{'server': 'cwgz5ola5r6u5e4heu5qw3drgy-zzqhzdizzmcurky2zbgw4gw7la.datawarehouse.fabric.microsoft.com', 'database': 'tmu_bronze_lakehouse'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2026-03-24 06:02:13 | 2026-03-24 06:02:13 | `Disabled` | `Scheduled` | - |
| 2026-03-23 06:02:13 | 2026-03-23 06:07:44 | `Completed` | `Scheduled` | - |
| 2026-03-22 06:02:08 | 2026-03-22 06:06:37 | `Completed` | `Scheduled` | - |
| 2026-03-21 06:01:15 | 2026-03-21 06:06:03 | `Completed` | `Scheduled` | - |
| 2026-03-20 06:01:14 | 2026-03-20 06:05:55 | `Completed` | `Scheduled` | - |

### Semantic Model: TMU SC Dashboard 2025
- **Dataset ID**: `811e22b8-ec21-4330-ad4f-10e3f45f05a0`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (DISABLED ❌):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `10:30` (UTC)

**Connected Data Sources (Lineage)**:
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmu_prod', 'database': 'tmu pih'}`
- Type: `Web` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/Collaboration/Shared%20Documents/INT_POWERBI_HELPER/TMU/suply_chain_db/sc_dashboard_budget_title.xlsx'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmeu_testspace', 'database': 'tmu sales dashboard'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2026-04-24 13:32:48 | 2026-04-24 13:32:51 | `Failed` | `OnDemand` | {"errorCode":"ModelRefresh_ShortMessage_Process... |

### Semantic Model: TMU WG Sales Forecast
- **Dataset ID**: `c9a81717-a93b-4d19-9855-8e2a1b8bb05b`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (DISABLED ❌):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `04:00` (UTC)

**Connected Data Sources (Lineage)**:
- Type: `Sql` | Connection: `{'server': 'cwgz5ola5r6u5e4heu5qw3drgy-zzqhzdizzmcurky2zbgw4gw7la.datawarehouse.fabric.microsoft.com', 'database': 'tmeu_bronze_lakehouse'}`
- Type: `Sql` | Connection: `{'server': 'cwgz5ola5r6u5e4heu5qw3drgy-zzqhzdizzmcurky2zbgw4gw7la.database.fabric.microsoft.com', 'database': 'tmu assortment budget-2ad254ce-44d5-4c67-9aee-a34267f0a56d'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2026-08-13 12:58:20 | 2026-08-13 12:58:24 | `Completed` | `ViaApi` | - |
| 2026-08-13 12:53:25 | 2026-08-13 12:53:29 | `Completed` | `ViaApi` | - |
| 2026-08-13 12:53:17 | 2026-08-13 12:53:20 | `Completed` | `ViaApi` | - |
| 2026-08-13 12:50:45 | 2026-08-13 12:50:48 | `Completed` | `ViaApi` | - |
| 2026-08-13 12:47:27 | 2026-08-13 12:47:32 | `Completed` | `ViaApi` | - |

### Semantic Model: TMU AfterSales Credit Limits Report
- **Dataset ID**: `fa85ef02-d7db-436a-9df6-eec70bedb2d7`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Monday
- **Scheduled Times**: `04:00` (UTC)

**Connected Data Sources (Lineage)**:
- Type: `Sql` | Connection: `{'server': 'cwgz5ola5r6u5e4heu5qw3drgy-zzqhzdizzmcurky2zbgw4gw7la.datawarehouse.fabric.microsoft.com', 'database': 'tmu_bronze_lakehouse'}`
- Type: `Extension` | Connection: `{'path': 'PowerPlatformDataflows', 'kind': 'PowerPlatformDataflows'}`
- Type: `Sql` | Connection: `{'server': 'cwgz5ola5r6u5e4heu5qw3drgy-zzqhzdizzmcurky2zbgw4gw7la.database.fabric.microsoft.com', 'database': 'credit_limit_leger_db-63c686ae-3399-4ce0-bc13-5ce0336cab9e'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2026-09-14 04:02:17 | 2026-09-14 04:10:34 | `Completed` | `Scheduled` | - |
| 2026-09-07 04:03:03 | 2026-09-07 04:10:24 | `Completed` | `Scheduled` | - |
| 2026-08-31 13:16:02 | 2026-08-31 13:17:44 | `Completed` | `OnDemandTraining` | - |
| 2026-08-31 13:04:40 | 2026-08-31 13:06:35 | `Completed` | `OnDemand` | - |

## 4. Power BI Reports Inventory

| Report Name | Report ID | Dataset ID | Web URL |
| :--- | :--- | :--- | :--- |
| **TMU Returns** | `28cdcda3-cc3c-494f-8f35-198bd319296e` | `e8d58fd3-687f-4e40-8a7e-1e2d8fe4b1fc` | [Open Report](https://app.powerbi.com/groups/49226436-1f31-4889-a274-968ed5954d4c/reports/28cdcda3-cc3c-494f-8f35-198bd319296e) |
| **TMU Service Mileage & Hours** | `e3b094ea-dc2b-4fb4-aa2c-7dc0bf440989` | `0aa29cbe-c6ec-4533-8d63-76422659d1ac` | [Open Report](https://app.powerbi.com/groups/49226436-1f31-4889-a274-968ed5954d4c/reports/e3b094ea-dc2b-4fb4-aa2c-7dc0bf440989) |
| **TMU Service Sales & Working Hours** | `fa0f15fa-ede4-4cbc-a756-1b421aa6416d` | `93ea0d0e-8fe0-4b6a-8050-7076e94c528c` | [Open Report](https://app.powerbi.com/groups/49226436-1f31-4889-a274-968ed5954d4c/reports/fa0f15fa-ede4-4cbc-a756-1b421aa6416d) |
| **TMU PIH** | `cc2d6e74-bdae-42f6-881c-803dc65a2a78` | `49074992-c1ff-4f5c-a7d1-0fc8e61b7a8c` | [Open Report](https://app.powerbi.com/groups/49226436-1f31-4889-a274-968ed5954d4c/reports/cc2d6e74-bdae-42f6-881c-803dc65a2a78) |
| **TMU SC Dashboard** | `1f671065-1a5d-416a-b58d-80fd087d0a13` | `33d8e090-1d24-47fd-be45-d6ed2ee5cfdb` | [Open Report](https://app.powerbi.com/groups/49226436-1f31-4889-a274-968ed5954d4c/reports/1f671065-1a5d-416a-b58d-80fd087d0a13) |
| **TMU SC Dashboard 2024** | `bc5d2a3e-b9bc-421f-a3ac-9d4e3f584962` | `adea2dd9-db57-4e79-9b64-405c7183e085` | [Open Report](https://app.powerbi.com/groups/49226436-1f31-4889-a274-968ed5954d4c/reports/bc5d2a3e-b9bc-421f-a3ac-9d4e3f584962) |
| **Usage Metrics Report** | `8fcb6096-ecb9-436e-81d4-62098b9f93e0` | `3c187fc2-b12f-4ba7-ad0b-fa10fdeb4b5f` | [Open Report](https://app.powerbi.com/groups/49226436-1f31-4889-a274-968ed5954d4c/reports/8fcb6096-ecb9-436e-81d4-62098b9f93e0) |
| **TMU WG Forecast Accuracy** | `c524a7b2-4ece-4920-b102-d0b6f12ed09a` | `5eb681ae-11b2-4c8a-a71b-2f58374b05c8` | [Open Report](https://app.powerbi.com/groups/49226436-1f31-4889-a274-968ed5954d4c/reports/c524a7b2-4ece-4920-b102-d0b6f12ed09a) |
| **TMU Parts Transport Cost Awareness** | `cf4e107e-1ff0-43fc-bc80-d002685ce036` | `2ec90fe7-61b9-4b0a-9f24-46d0230c2265` | [Open Report](https://app.powerbi.com/groups/49226436-1f31-4889-a274-968ed5954d4c/reports/cf4e107e-1ff0-43fc-bc80-d002685ce036) |
| **TMU SC Dashboard 2025** | `cca5cf91-96fd-4822-974a-7f4d58a10ded` | `811e22b8-ec21-4330-ad4f-10e3f45f05a0` | [Open Report](https://app.powerbi.com/groups/49226436-1f31-4889-a274-968ed5954d4c/reports/cca5cf91-96fd-4822-974a-7f4d58a10ded) |
| **TMU WG Sales Forecast** | `e3e3f374-a9e7-4387-b218-8c83c4ed088f` | `c9a81717-a93b-4d19-9855-8e2a1b8bb05b` | [Open Report](https://app.powerbi.com/groups/49226436-1f31-4889-a274-968ed5954d4c/reports/e3e3f374-a9e7-4387-b218-8c83c4ed088f) |
| **TMU AfterSales Credit Limits Report** | `6ea8f577-ebe1-48da-82dd-c974d89f3240` | `fa85ef02-d7db-436a-9df6-eec70bedb2d7` | [Open Report](https://app.powerbi.com/groups/49226436-1f31-4889-a274-968ed5954d4c/reports/6ea8f577-ebe1-48da-82dd-c974d89f3240) |

## 5. Dataflows & Dashboards

**Dataflows**:
- **TMU 1C Dataflow** (ID: `97f70344-7b0e-417c-8c98-221d679977fc`)
- **TMU 1C P&L Dataflow #** (ID: `9f3092f5-ea3a-47fa-a4e5-edd8cfcf2c06`)
- **TMU 1C Spare Parts Sales #** (ID: `58dab748-de79-447c-b33d-b63d6c3dcca9`)
- **TMU 1C Service Dataflow #** (ID: `e4be8360-f6f4-4a20-bb36-e577e9c06618`)
- **TMU 1C PIH Dataflow #** (ID: `99c97743-8249-4777-8d63-56c4ab90bf53`)
- **TMU 1C AR Dataflow E** (ID: `084099e9-234a-4864-966c-1cc12ba5073c`)
- **TMU 1C WG Listing #** (ID: `ed2424a2-59a1-4363-bc74-1b6dd6e8ecb3`)
- **TMEU_FX_Rates** (ID: `58c81585-1ee0-46f2-94f8-173690fb4af1`)
- **TMU 1C Dataflow P2** (ID: `367ddbea-30ba-4cdf-9df8-50aae54553ee`)
- **TMU 1C SPSALESFIN** (ID: `f2509040-9e19-473e-a6a7-b85b4e2d719c`)
- **TMU 1C BalanceSheet** (ID: `33e085e0-af26-4da3-a324-7debb79b6257`)

---

## 6. Newcomer Operational Runbook & Notes
- **Primary Contact / Owner**: Refer to workspace access settings in Power BI portal.
- **Troubleshooting**: If a refresh fails in `BI_TMU_PROD`, inspect the failure log under section 3 above and check upstream data gateway connectivity.
