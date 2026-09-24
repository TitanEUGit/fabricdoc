# Workspace Documentation: BI_TMA_NAV_Data

**Workspace ID**: `a63d5741-75c7-498a-b264-bef89e34099e`  
**Type**: `Fabric / PowerBI Workspace`  
**Capacity ID**: `70650ed2-f7a2-46df-96e8-8089f25db80e`  
**Description**: No description provided.

---

## 1. Executive Summary & Newcomer Overview

> [!NOTE]
> **EOC Finance & NAV Data Source**
> This workspace is primarily designed for the **EOC Finance team**. All reports in this workspace are based on TMA NAV database tables sourced from the [TMA_NAV_Lakehouse](https://app.powerbi.com/groups/8d7c60ce-cb19-4805-ab1a-c84d6e1adf58/lakehouses/560be169-9531-4fc2-8c36-4bb173fc1240?experience=fabric-developer&subfolderId=136973).

This document contains operational and technical details for the **BI_TMA_NAV_Data** workspace. It is designed to give new team members full visibility into key items, data models, report lineage, and refresh schedules.

## 2. Native Fabric Items Inventory

| Item Name | Item Type | Item ID | Description |
| :--- | :--- | :--- | :--- |
| **TMA NAV Reporting** | `Report` | `ef023446-922a-4e38-971c-29e95b053e67` | Based on TMA NAV database tables from [TMA_NAV_Lakehouse](https://app.powerbi.com/groups/8d7c60ce-cb19-4805-ab1a-c84d6e1adf58/lakehouses/560be169-9531-4fc2-8c36-4bb173fc1240?experience=fabric-developer&subfolderId=136973) |
| **TMA NAV Data** | `Report` | `b2ad0ca2-61cc-405d-936d-f439b238973f` | Based on TMA NAV database tables from [TMA_NAV_Lakehouse](https://app.powerbi.com/groups/8d7c60ce-cb19-4805-ab1a-c84d6e1adf58/lakehouses/560be169-9531-4fc2-8c36-4bb173fc1240?experience=fabric-developer&subfolderId=136973) |
| **TMA NAV Data Full Refresh** | `Report` | `9cff7aa3-5b26-437f-aa2a-386c5540889a` | Based on TMA NAV database tables from [TMA_NAV_Lakehouse](https://app.powerbi.com/groups/8d7c60ce-cb19-4805-ab1a-c84d6e1adf58/lakehouses/560be169-9531-4fc2-8c36-4bb173fc1240?experience=fabric-developer&subfolderId=136973) |
| **TMA Accounts Receivable_Payable** | `Report` | `5b6eeaa8-daa0-4e11-9d3e-3299906a96b3` | Based on TMA NAV database tables from [TMA_NAV_Lakehouse](https://app.powerbi.com/groups/8d7c60ce-cb19-4805-ab1a-c84d6e1adf58/lakehouses/560be169-9531-4fc2-8c36-4bb173fc1240?experience=fabric-developer&subfolderId=136973) |
| **TMA Revenue Report (Direct Lake)** | `Report` | `794c1d5d-43e8-452e-a208-1317523f0f67` | Based on TMA NAV database tables from [TMA_NAV_Lakehouse](https://app.powerbi.com/groups/8d7c60ce-cb19-4805-ab1a-c84d6e1adf58/lakehouses/560be169-9531-4fc2-8c36-4bb173fc1240?experience=fabric-developer&subfolderId=136973) |
| **TMA Shipped Not Invoiced WG Items** | `Report` | `4f1f3c3e-4d37-41f0-96f8-506b02103af4` | Based on TMA NAV database tables from [TMA_NAV_Lakehouse](https://app.powerbi.com/groups/8d7c60ce-cb19-4805-ab1a-c84d6e1adf58/lakehouses/560be169-9531-4fc2-8c36-4bb173fc1240?experience=fabric-developer&subfolderId=136973) |
| **TMA NAV Reporting** | `SemanticModel` | `d25843b4-18e0-4711-a40f-0cc0b685757f` | - |
| **TMA NAV Data** | `SemanticModel` | `736a59a6-7fa8-45da-a0fa-3bc4bb07c0c6` | - |
| **TMA NAV Data Full Refresh** | `SemanticModel` | `2c7570c7-d984-4897-9581-c82f9840a245` | - |
| **TMA Accounts Receivable_Payable** | `SemanticModel` | `f047b72f-5d9e-40b6-a5da-27b4ababc7a7` | - |
| **TMA Shipped Not Invoiced WG Items** | `SemanticModel` | `00a016cf-0e3c-45a3-8720-50c3e773cbd9` | - |

## 3. Semantic Models (Datasets) & Refresh Schedules

### Semantic Model: TMA NAV Reporting
- **Dataset ID**: `d25843b4-18e0-4711-a40f-0cc0b685757f`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `07:00` (W. Europe Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `Sql` | Connection: `{'server': 'titaneu.database.windows.net', 'database': 'titanat_prod'}`


### Semantic Model: TMA NAV Data
- **Dataset ID**: `736a59a6-7fa8-45da-a0fa-3bc4bb07c0c6`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `07:00` (W. Europe Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `Sql` | Connection: `{'server': 'titaneu.database.windows.net', 'database': 'titanat_prod'}`


### Semantic Model: TMA NAV Data Full Refresh
- **Dataset ID**: `2c7570c7-d984-4897-9581-c82f9840a245`
- **Target Storage Mode**: `PremiumFiles`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `06:00` (W. Europe Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `Sql` | Connection: `{'server': 'titaneu.database.windows.net', 'database': 'titanat_prod'}`


### Semantic Model: TMA Accounts Receivable_Payable
- **Dataset ID**: `f047b72f-5d9e-40b6-a5da-27b4ababc7a7`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `05:00` (FLE Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `Sql` | Connection: `{'server': 'cwgz5ola5r6u5e4heu5qw3drgy-zzqhzdizzmcurky2zbgw4gw7la.datawarehouse.fabric.microsoft.com', 'database': 'tma_nav_lakehouse'}`


### Semantic Model: TMA Shipped Not Invoiced WG Items
- **Dataset ID**: `00a016cf-0e3c-45a3-8720-50c3e773cbd9`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `09:00, 12:00, 16:00` (FLE Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `Sql` | Connection: `{'server': 'cwgz5ola5r6u5e4heu5qw3drgy-zzqhzdizzmcurky2zbgw4gw7la.datawarehouse.fabric.microsoft.com', 'database': 'tma_nav_lakehouse'}`


## 4. Power BI Reports Inventory

| Report Name | Report ID | Dataset ID | Web URL |
| :--- | :--- | :--- | :--- |
| **TMA NAV Reporting** | `ef023446-922a-4e38-971c-29e95b053e67` | `d25843b4-18e0-4711-a40f-0cc0b685757f` | [Open Report](https://app.powerbi.com/groups/a63d5741-75c7-498a-b264-bef89e34099e/reports/ef023446-922a-4e38-971c-29e95b053e67) |
| **TMA NAV Data** | `b2ad0ca2-61cc-405d-936d-f439b238973f` | `736a59a6-7fa8-45da-a0fa-3bc4bb07c0c6` | [Open Report](https://app.powerbi.com/groups/a63d5741-75c7-498a-b264-bef89e34099e/reports/b2ad0ca2-61cc-405d-936d-f439b238973f) |
| **TMA NAV Data Full Refresh** | `9cff7aa3-5b26-437f-aa2a-386c5540889a` | `2c7570c7-d984-4897-9581-c82f9840a245` | [Open Report](https://app.powerbi.com/groups/a63d5741-75c7-498a-b264-bef89e34099e/reports/9cff7aa3-5b26-437f-aa2a-386c5540889a) |
| **TMA Accounts Receivable_Payable** | `5b6eeaa8-daa0-4e11-9d3e-3299906a96b3` | `f047b72f-5d9e-40b6-a5da-27b4ababc7a7` | [Open Report](https://app.powerbi.com/groups/a63d5741-75c7-498a-b264-bef89e34099e/reports/5b6eeaa8-daa0-4e11-9d3e-3299906a96b3) |
| **TMA Revenue Report (Direct Lake)** | `794c1d5d-43e8-452e-a208-1317523f0f67` | `9b32e872-baeb-42f6-9af4-fbdf159b4e84` | [Open Report](https://app.powerbi.com/groups/a63d5741-75c7-498a-b264-bef89e34099e/reports/794c1d5d-43e8-452e-a208-1317523f0f67) |
| **TMA Shipped Not Invoiced WG Items** | `4f1f3c3e-4d37-41f0-96f8-506b02103af4` | `00a016cf-0e3c-45a3-8720-50c3e773cbd9` | [Open Report](https://app.powerbi.com/groups/a63d5741-75c7-498a-b264-bef89e34099e/reports/4f1f3c3e-4d37-41f0-96f8-506b02103af4) |

## 5. Dataflows & Dashboards

*No dataflows or dashboards in this workspace.*

---

## 6. Newcomer Operational Runbook & Notes
- **Primary Contact / Owner**: Refer to workspace access settings in Power BI portal.
- **Troubleshooting**: If a refresh fails in `BI_TMA_NAV_Data`, inspect the failure log under section 3 above and check upstream data gateway connectivity.
