# Workspace Documentation: BI_TMU_Parts Market

**Workspace ID**: `dd2db963-6c36-49ad-a015-9e6d0fa5ee17`  
**Type**: `Fabric / PowerBI Workspace`  
**Capacity ID**: `70650ed2-f7a2-46df-96e8-8089f25db80e`  
**Description**: No description provided.

---

## 1. Executive Summary & Newcomer Overview

> [!IMPORTANT]
> **Ukraine Market & Competitor Intelligence**
> This workspace is used primarily to evaluate the Ukrainian market using external, non-organizational data. The data relates to competitor VAT information retrieved from a governmental portal database, allowing TMU to evaluate its standing among key market players.

### Key Reports at a Glance
| Report Name | What It Shows |
|:---|:---|
| **TMU AfterSales Market (VAT based)** | Evaluates TMU's Aftersales market position against competitors using external VAT data. |
| **TMU Market VAT Report** | General market overview based on governmental VAT database. |
| **TMU Market VAT Report - Export Enabled** | Same as above, but configured to allow data exports for offline analysis. |
| **TMU Sales VAT Report** | Sales-focused market evaluation based on competitor VAT data. |
| **TMU Parts Customs Import MGMNT** | Analyzes imported goods to Ukraine using external customs databases to evaluate competition from an import perspective. |
| **TMU Parts Turn & Budget** | Calculates parts turn metrics using historical and budgeted data; primarily used by the parts purchasing team. |
| **TMU Assortment Budget** | Features writeback functionality to automatically distribute aggregated high-level budgeted amounts down to the branch and parts category level. |

This document contains operational and technical details for the **BI_TMU_Parts Market** workspace. It is designed to give new team members full visibility into key items, data models, report lineage, and refresh schedules.

## 2. Native Fabric Items Inventory

| Item Name | Item Type | Item ID | Description |
| :--- | :--- | :--- | :--- |
| **TMU Parts Customs Import MGMNT** | `Report` | `bf90a17d-111e-4048-b1c4-8cd8c53766ae` | - |
| **TMU Market VAT Report** | `Report` | `ea14cd6e-b07f-4206-ba0d-bdc0261e2d2e` | - |
| **TMU Sales VAT Report** | `Report` | `8e30784e-e2f4-44d9-a3f0-fee141660e3d` | - |
| **TMU Market VAT Report - Export Enabled** | `Report` | `ff05dcbf-d896-4e60-ad8c-0df55b8cd24c` | - |
| **TMU AfterSales Market (VAT based)** | `Report` | `04698596-0194-4528-b413-2ed1b09e5744` | - |
| **Usage Metrics Report** | `Report` | `97e5b06c-b9eb-4c66-8bfb-8072f1153871` | - |
| **TMU Parts Customs Import with Text OneLake** | `Report` | `101910e2-fa34-4235-b7ab-b318a228cc0a` | - |
| **TMU Assortment Budget** | `Report` | `2baed91a-27f6-49ef-a302-61989069a254` | - |
| **TMU Parts Turn & Budget** | `Report` | `16e7d7ff-852f-4830-a877-6bfb56e27160` | - |
| **TMU Parts Customs Import MGMNT** | `SemanticModel` | `43cc0cb0-fbc7-4dd1-aba4-6b42f42c5d40` | - |
| **TMU Market VAT Report** | `SemanticModel` | `d6821a68-887d-4da1-8cb8-a74e81798000` | - |
| **TMU Sales VAT Report** | `SemanticModel` | `bcd6ba6d-fd7b-4ade-a908-c15234b07dc3` | - |
| **TMU Market VAT Report - Export Enabled** | `SemanticModel` | `455390ca-a392-493c-920e-05d60dbc5141` | - |
| **TMU AfterSales Market (VAT based)** | `SemanticModel` | `76d8d8c4-9b2e-4e44-8fe9-6edbbe655605` | - |
| **Usage Metrics Report** | `SemanticModel` | `f24c0fa0-0a81-45f6-b0ab-8a866bf35084` | - |
| **TMU Parts Customs Import with Text OneLake** | `SemanticModel` | `13854906-b695-46e3-a278-86e7497d8bdd` | - |
| **TMU Assortment Budget** | `SemanticModel` | `f82dbbaf-dce5-44d4-b575-6c40c315f60b` | - |
| **TMU Parts Turn & Budget** | `SemanticModel` | `3c4de179-08d3-4730-b02e-a3c31ca96df3` | - |

## 3. Semantic Models (Datasets) & Refresh Schedules

### Semantic Model: TMU Parts Customs Import MGMNT
- **Dataset ID**: `43cc0cb0-fbc7-4dd1-aba4-6b42f42c5d40`
- **Target Storage Mode**: `PremiumFiles`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (DISABLED ❌):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `03:30` (UTC)

**Connected Data Sources (Lineage)**:
- Type: `Sql` | Connection: `{'server': 'cwgz5ola5r6u5e4heu5qw3drgy-zzqhzdizzmcurky2zbgw4gw7la.datawarehouse.fabric.microsoft.com', 'database': 'tmu_bronze_lakehouse'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2026-08-14 09:56:29 | 2026-08-14 10:09:04 | `Completed` | `OnDemand` | - |
| 2026-07-17 08:14:01 | 2026-07-17 08:26:08 | `Completed` | `OnDemand` | - |
| 2026-06-12 11:19:33 | 2026-06-12 11:29:58 | `Completed` | `OnDemand` | - |
| 2026-05-22 15:16:39 | 2026-05-22 15:25:27 | `Completed` | `OnDemand` | - |
| 2026-04-17 08:20:22 | 2026-04-17 08:34:05 | `Completed` | `OnDemand` | - |

### Semantic Model: TMU Market VAT Report
- **Dataset ID**: `d6821a68-887d-4da1-8cb8-a74e81798000`
- **Target Storage Mode**: `PremiumFiles`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (DISABLED ❌):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `12:30` (UTC)

**Connected Data Sources (Lineage)**:
- Type: `Sql` | Connection: `{'server': 'cwgz5ola5r6u5e4heu5qw3drgy-zzqhzdizzmcurky2zbgw4gw7la.datawarehouse.fabric.microsoft.com', 'database': 'tmu_bronze_lakehouse'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2026-08-21 06:15:06 | 2026-08-21 06:24:25 | `Completed` | `OnDemand` | - |
| 2026-08-20 17:26:52 | 2026-08-20 17:36:04 | `Completed` | `OnDemand` | - |
| 2026-07-31 11:10:24 | 2026-07-31 11:21:04 | `Completed` | `OnDemand` | - |
| 2026-06-23 14:32:32 | 2026-06-23 14:44:29 | `Completed` | `OnDemand` | - |
| 2026-05-22 14:05:48 | 2026-05-22 14:20:07 | `Completed` | `OnDemand` | - |

### Semantic Model: TMU Sales VAT Report
- **Dataset ID**: `bcd6ba6d-fd7b-4ade-a908-c15234b07dc3`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (DISABLED ❌):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `02:00` (FLE Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `Sql` | Connection: `{'server': 'cwgz5ola5r6u5e4heu5qw3drgy-zzqhzdizzmcurky2zbgw4gw7la.datawarehouse.fabric.microsoft.com', 'database': 'tmu_bronze_lakehouse'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2026-08-21 06:15:15 | 2026-08-21 06:18:14 | `Completed` | `OnDemand` | - |
| 2026-08-20 17:27:01 | 2026-08-20 17:30:01 | `Completed` | `OnDemand` | - |
| 2026-07-31 11:10:27 | 2026-07-31 11:13:56 | `Completed` | `OnDemand` | - |
| 2026-06-23 14:32:38 | 2026-06-23 14:35:21 | `Completed` | `OnDemand` | - |
| 2026-04-22 11:31:02 | 2026-04-22 11:35:00 | `Completed` | `OnDemand` | - |

### Semantic Model: TMU Market VAT Report - Export Enabled
- **Dataset ID**: `455390ca-a392-493c-920e-05d60dbc5141`
- **Target Storage Mode**: `PremiumFiles`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (DISABLED ❌):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `22:30` (UTC)

**Connected Data Sources (Lineage)**:
- Type: `Sql` | Connection: `{'server': 'cwgz5ola5r6u5e4heu5qw3drgy-zzqhzdizzmcurky2zbgw4gw7la.datawarehouse.fabric.microsoft.com', 'database': 'tmu_bronze_lakehouse'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2026-08-21 06:15:09 | 2026-08-21 06:24:43 | `Completed` | `OnDemand` | - |
| 2026-08-20 17:26:56 | 2026-08-20 17:37:20 | `Completed` | `OnDemand` | - |
| 2026-07-31 11:10:25 | 2026-07-31 11:19:41 | `Completed` | `OnDemand` | - |
| 2026-06-23 14:32:30 | 2026-06-23 14:44:31 | `Completed` | `OnDemand` | - |
| 2026-05-22 14:05:51 | 2026-05-22 14:14:11 | `Completed` | `OnDemand` | - |

### Semantic Model: TMU AfterSales Market (VAT based)
- **Dataset ID**: `76d8d8c4-9b2e-4e44-8fe9-6edbbe655605`
- **Target Storage Mode**: `PremiumFiles`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (DISABLED ❌):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `15:00` (UTC)

**Connected Data Sources (Lineage)**:
- Type: `Sql` | Connection: `{'server': 'cwgz5ola5r6u5e4heu5qw3drgy-zzqhzdizzmcurky2zbgw4gw7la.datawarehouse.fabric.microsoft.com', 'database': 'tmu_bronze_lakehouse'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2026-08-21 06:14:57 | 2026-08-21 06:35:02 | `Completed` | `OnDemand` | - |
| 2026-08-20 17:26:45 | 2026-08-20 17:47:11 | `Completed` | `OnDemand` | - |
| 2026-07-31 11:10:22 | 2026-07-31 11:32:51 | `Completed` | `OnDemand` | - |
| 2026-06-23 14:32:27 | 2026-06-23 14:51:03 | `Completed` | `OnDemand` | - |
| 2026-05-22 14:05:46 | 2026-05-22 14:26:55 | `Completed` | `OnDemand` | - |

### Semantic Model: Usage Metrics Report
- **Dataset ID**: `f24c0fa0-0a81-45f6-b0ab-8a866bf35084`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `16:24` (UTC)

**Connected Data Sources (Lineage)**:
- Type: `Extension` | Connection: `{'path': 'UsageMetricsDataConnector', 'kind': 'UsageMetricsDataConnector'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2025-07-21 16:24:15 | 2025-07-21 16:24:15 | `Disabled` | `Scheduled` | - |
| 2025-07-20 16:24:06 | 2025-07-20 16:24:23 | `Completed` | `Scheduled` | - |
| 2025-07-19 16:24:09 | 2025-07-19 16:24:22 | `Completed` | `Scheduled` | - |
| 2025-07-18 16:24:07 | 2025-07-18 16:24:18 | `Completed` | `Scheduled` | - |
| 2025-07-17 16:24:09 | 2025-07-17 16:24:21 | `Completed` | `Scheduled` | - |

### Semantic Model: TMU Parts Customs Import with Text OneLake
- **Dataset ID**: `13854906-b695-46e3-a278-86e7497d8bdd`
- **Target Storage Mode**: `PremiumFiles`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (DISABLED ❌):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `15:30` (UTC)

**Connected Data Sources (Lineage)**:
- Type: `Sql` | Connection: `{'server': 'cwgz5ola5r6u5e4heu5qw3drgy-zzqhzdizzmcurky2zbgw4gw7la.datawarehouse.fabric.microsoft.com', 'database': 'tmu_bronze_lakehouse'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2026-08-14 09:56:25 | 2026-08-14 10:12:07 | `Completed` | `OnDemand` | - |
| 2026-07-17 08:14:05 | 2026-07-17 08:29:26 | `Completed` | `OnDemand` | - |
| 2026-06-12 11:19:35 | 2026-06-12 11:35:03 | `Completed` | `OnDemand` | - |
| 2026-05-22 15:16:41 | 2026-05-22 15:32:52 | `Completed` | `OnDemand` | - |
| 2026-04-17 08:20:20 | 2026-04-17 08:34:06 | `Completed` | `OnDemand` | - |

### Semantic Model: TMU Assortment Budget
- **Dataset ID**: `f82dbbaf-dce5-44d4-b575-6c40c315f60b`
- **Target Storage Mode**: `PremiumFiles`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `05:00` (UTC)

**Connected Data Sources (Lineage)**:
- Type: `Sql` | Connection: `{'server': 'cwgz5ola5r6u5e4heu5qw3drgy-zzqhzdizzmcurky2zbgw4gw7la.database.fabric.microsoft.com', 'database': 'tmu assortment budget-2ad254ce-44d5-4c67-9aee-a34267f0a56d'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2026-09-15 05:02:12 | 2026-09-15 05:07:00 | `Completed` | `Scheduled` | - |
| 2026-09-14 05:01:11 | 2026-09-14 05:05:12 | `Completed` | `Scheduled` | - |
| 2026-09-13 05:02:13 | 2026-09-13 05:07:13 | `Completed` | `Scheduled` | - |
| 2026-09-12 05:02:16 | 2026-09-12 05:08:26 | `Completed` | `Scheduled` | - |
| 2026-09-11 05:02:17 | 2026-09-11 05:07:18 | `Completed` | `Scheduled` | - |

### Semantic Model: TMU Parts Turn & Budget
- **Dataset ID**: `3c4de179-08d3-4730-b02e-a3c31ca96df3`
- **Target Storage Mode**: `PremiumFiles`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `02:00` (FLE Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `Sql` | Connection: `{'server': 'cwgz5ola5r6u5e4heu5qw3drgy-zzqhzdizzmcurky2zbgw4gw7la.database.fabric.microsoft.com', 'database': 'tmu assortment budget-2ad254ce-44d5-4c67-9aee-a34267f0a56d'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2026-09-14 23:02:06 | 2026-09-14 23:07:25 | `Completed` | `Scheduled` | - |
| 2026-09-13 23:02:17 | 2026-09-13 23:09:03 | `Completed` | `Scheduled` | - |
| 2026-09-12 23:02:11 | 2026-09-12 23:08:14 | `Completed` | `Scheduled` | - |
| 2026-09-11 23:01:08 | 2026-09-11 23:05:25 | `Completed` | `Scheduled` | - |
| 2026-09-10 23:02:19 | 2026-09-10 23:09:06 | `Completed` | `Scheduled` | - |

## 4. Power BI Reports Inventory

| Report Name | Report ID | Dataset ID | Web URL |
| :--- | :--- | :--- | :--- |
| **TMU Parts Customs Import MGMNT** | `bf90a17d-111e-4048-b1c4-8cd8c53766ae` | `43cc0cb0-fbc7-4dd1-aba4-6b42f42c5d40` | [Open Report](https://app.powerbi.com/groups/dd2db963-6c36-49ad-a015-9e6d0fa5ee17/reports/bf90a17d-111e-4048-b1c4-8cd8c53766ae) |
| **TMU Market VAT Report** | `ea14cd6e-b07f-4206-ba0d-bdc0261e2d2e` | `d6821a68-887d-4da1-8cb8-a74e81798000` | [Open Report](https://app.powerbi.com/groups/dd2db963-6c36-49ad-a015-9e6d0fa5ee17/reports/ea14cd6e-b07f-4206-ba0d-bdc0261e2d2e) |
| **TMU Sales VAT Report** | `8e30784e-e2f4-44d9-a3f0-fee141660e3d` | `bcd6ba6d-fd7b-4ade-a908-c15234b07dc3` | [Open Report](https://app.powerbi.com/groups/dd2db963-6c36-49ad-a015-9e6d0fa5ee17/reports/8e30784e-e2f4-44d9-a3f0-fee141660e3d) |
| **TMU Market VAT Report - Export Enabled** | `ff05dcbf-d896-4e60-ad8c-0df55b8cd24c` | `455390ca-a392-493c-920e-05d60dbc5141` | [Open Report](https://app.powerbi.com/groups/dd2db963-6c36-49ad-a015-9e6d0fa5ee17/reports/ff05dcbf-d896-4e60-ad8c-0df55b8cd24c) |
| **TMU AfterSales Market (VAT based)** | `04698596-0194-4528-b413-2ed1b09e5744` | `76d8d8c4-9b2e-4e44-8fe9-6edbbe655605` | [Open Report](https://app.powerbi.com/groups/dd2db963-6c36-49ad-a015-9e6d0fa5ee17/reports/04698596-0194-4528-b413-2ed1b09e5744) |
| **Usage Metrics Report** | `97e5b06c-b9eb-4c66-8bfb-8072f1153871` | `f24c0fa0-0a81-45f6-b0ab-8a866bf35084` | [Open Report](https://app.powerbi.com/groups/dd2db963-6c36-49ad-a015-9e6d0fa5ee17/reports/97e5b06c-b9eb-4c66-8bfb-8072f1153871) |
| **TMU Parts Customs Import with Text OneLake** | `101910e2-fa34-4235-b7ab-b318a228cc0a` | `13854906-b695-46e3-a278-86e7497d8bdd` | [Open Report](https://app.powerbi.com/groups/dd2db963-6c36-49ad-a015-9e6d0fa5ee17/reports/101910e2-fa34-4235-b7ab-b318a228cc0a) |
| **TMU Assortment Budget** | `2baed91a-27f6-49ef-a302-61989069a254` | `f82dbbaf-dce5-44d4-b575-6c40c315f60b` | [Open Report](https://app.powerbi.com/groups/dd2db963-6c36-49ad-a015-9e6d0fa5ee17/reports/2baed91a-27f6-49ef-a302-61989069a254) |
| **TMU Parts Turn & Budget** | `16e7d7ff-852f-4830-a877-6bfb56e27160` | `3c4de179-08d3-4730-b02e-a3c31ca96df3` | [Open Report](https://app.powerbi.com/groups/dd2db963-6c36-49ad-a015-9e6d0fa5ee17/reports/16e7d7ff-852f-4830-a877-6bfb56e27160) |

## 5. Dataflows & Dashboards

*No dataflows or dashboards in this workspace.*

---

## 6. Newcomer Operational Runbook & Notes
- **Primary Contact / Owner**: Refer to workspace access settings in Power BI portal.
- **Troubleshooting**: If a refresh fails in `BI_TMU_Parts Market`, inspect the failure log under section 3 above and check upstream data gateway connectivity.
