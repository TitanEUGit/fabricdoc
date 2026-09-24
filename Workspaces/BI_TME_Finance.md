# Workspace Documentation: BI_TME_Finance

**Workspace ID**: `d20374f2-6d2a-498d-a425-ccba79bf8500`  
**Type**: `Fabric / PowerBI Workspace`  
**Capacity ID**: `70650ed2-f7a2-46df-96e8-8089f25db80e`  
**Description**: A workspace for FMs of TME

---

## 1. Executive Summary & Newcomer Overview

> [!NOTE]
> **Cross-Country Finance Reporting**
> The reports within this workspace are developed primarily for the **Finance Manager of TMA (Austria HQ)** and include consolidated financial and operational data spanning **all countries** across the European division.

This document contains operational and technical details for the **BI_TME_Finance** workspace. It is designed to give new team members full visibility into key items, data models, report lineage, and refresh schedules.

## 2. Native Fabric Items Inventory

| Item Name | Item Type | Item ID | Description |
| :--- | :--- | :--- | :--- |
| **TMB_TMR Credit Limit Change Tracking** | `Report` | `f1e2c088-02b1-4cfc-aadd-426634f4c08e` | - |
| **CarFleet Report** | `Report` | `404682a0-1e0b-40b8-8b1e-451ee612b9af` | - |
| **Usage Metrics Report** | `Report` | `c5dfe2cf-097a-42b9-8fc4-944fce775664` | - |
| **TMEU Agriculture Commodities Prices** | `Report` | `8e242298-a491-4698-9428-71a38579c944` | - |
| **TMB_TMR Credit Limit Change Tracking** | `SemanticModel` | `8524fbcb-83e2-426e-9dcb-518f1b65f51f` | - |
| **CarFleet Report** | `SemanticModel` | `c404b2cd-de68-4b23-946e-4118d40731fd` | - |
| **Usage Metrics Report** | `SemanticModel` | `6a19e86d-da68-492b-beef-3af72830bfcb` | - |
| **TMEU Agriculture Commodities Prices** | `SemanticModel` | `96b33a20-df2b-4b96-b650-8ab114282924` | - |

## 3. Semantic Models (Datasets) & Refresh Schedules

### Semantic Model: TMB_TMR Credit Limit Change Tracking
- **Dataset ID**: `8524fbcb-83e2-426e-9dcb-518f1b65f51f`
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
| 2026-09-15 00:00:24 | 2026-09-15 00:02:43 | `Completed` | `Scheduled` | - |
| 2026-09-14 00:00:25 | 2026-09-14 00:02:48 | `Completed` | `Scheduled` | - |
| 2026-09-13 00:00:24 | 2026-09-13 00:00:45 | `Completed` | `Scheduled` | - |
| 2026-09-12 00:00:25 | 2026-09-12 00:02:42 | `Completed` | `Scheduled` | - |
| 2026-09-11 00:00:26 | 2026-09-11 00:01:52 | `Completed` | `Scheduled` | - |

### Semantic Model: CarFleet Report
- **Dataset ID**: `c404b2cd-de68-4b23-946e-4118d40731fd`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `23:00` (FLE Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `SharePointList` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/collaboration/'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2026-07-25 20:00:24 | 2026-07-25 20:00:24 | `Disabled` | `Scheduled` | - |
| 2026-07-24 20:01:14 | 2026-07-24 20:14:27 | `Completed` | `Scheduled` | - |
| 2026-07-23 20:00:22 | 2026-07-23 20:14:29 | `Completed` | `Scheduled` | - |
| 2026-07-22 20:01:09 | 2026-07-22 20:13:41 | `Completed` | `Scheduled` | - |
| 2026-07-21 20:00:26 | 2026-07-21 20:12:21 | `Completed` | `Scheduled` | - |

### Semantic Model: Usage Metrics Report
- **Dataset ID**: `6a19e86d-da68-492b-beef-3af72830bfcb`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `14:08` (UTC)

**Connected Data Sources (Lineage)**:
- Type: `Extension` | Connection: `{'path': 'UsageMetricsDataConnector', 'kind': 'UsageMetricsDataConnector'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2025-07-21 14:08:05 | 2025-07-21 14:08:05 | `Disabled` | `Scheduled` | - |
| 2025-07-20 14:08:06 | 2025-07-20 14:18:59 | `Completed` | `Scheduled` | - |
| 2025-07-19 14:08:11 | 2025-07-19 14:19:11 | `Completed` | `Scheduled` | - |
| 2025-07-18 14:08:08 | 2025-07-18 14:19:22 | `Completed` | `Scheduled` | - |
| 2025-07-17 14:08:05 | 2025-07-17 14:20:17 | `Completed` | `Scheduled` | - |

### Semantic Model: TMEU Agriculture Commodities Prices
- **Dataset ID**: `96b33a20-df2b-4b96-b650-8ab114282924`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `10:00` (FLE Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `Sql` | Connection: `{'server': 'cwgz5ola5r6u5e4heu5qw3drgy-zzqhzdizzmcurky2zbgw4gw7la.datawarehouse.fabric.microsoft.com', 'database': 'tmu_bronze_lakehouse'}`
- Type: `Sql` | Connection: `{'server': 'cwgz5ola5r6u5e4heu5qw3drgy-zzqhzdizzmcurky2zbgw4gw7la.datawarehouse.fabric.microsoft.com', 'database': 'tmeu_bronze_lakehouse'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2026-09-15 07:02:01 | 2026-09-15 07:05:42 | `Completed` | `Scheduled` | - |
| 2026-09-14 07:02:01 | 2026-09-14 07:06:57 | `Completed` | `Scheduled` | - |
| 2026-09-13 07:02:11 | 2026-09-13 07:07:38 | `Completed` | `Scheduled` | - |
| 2026-09-12 07:02:18 | 2026-09-12 07:08:03 | `Completed` | `Scheduled` | - |
| 2026-09-11 07:02:15 | 2026-09-11 07:07:33 | `Completed` | `Scheduled` | - |

## 4. Power BI Reports Inventory

| Report Name | Report ID | Dataset ID | Web URL |
| :--- | :--- | :--- | :--- |
| **TMB_TMR Credit Limit Change Tracking** | `f1e2c088-02b1-4cfc-aadd-426634f4c08e` | `8524fbcb-83e2-426e-9dcb-518f1b65f51f` | [Open Report](https://app.powerbi.com/groups/d20374f2-6d2a-498d-a425-ccba79bf8500/reports/f1e2c088-02b1-4cfc-aadd-426634f4c08e) |
| **CarFleet Report** | `404682a0-1e0b-40b8-8b1e-451ee612b9af` | `c404b2cd-de68-4b23-946e-4118d40731fd` | [Open Report](https://app.powerbi.com/groups/d20374f2-6d2a-498d-a425-ccba79bf8500/reports/404682a0-1e0b-40b8-8b1e-451ee612b9af) |
| **Usage Metrics Report** | `c5dfe2cf-097a-42b9-8fc4-944fce775664` | `6a19e86d-da68-492b-beef-3af72830bfcb` | [Open Report](https://app.powerbi.com/groups/d20374f2-6d2a-498d-a425-ccba79bf8500/reports/c5dfe2cf-097a-42b9-8fc4-944fce775664) |
| **TMEU Agriculture Commodities Prices** | `8e242298-a491-4698-9428-71a38579c944` | `96b33a20-df2b-4b96-b650-8ab114282924` | [Open Report](https://app.powerbi.com/groups/d20374f2-6d2a-498d-a425-ccba79bf8500/reports/8e242298-a491-4698-9428-71a38579c944) |

## 5. Dataflows & Dashboards

*No dataflows or dashboards in this workspace.*

---

## 6. Newcomer Operational Runbook & Notes
- **Primary Contact / Owner**: Refer to workspace access settings in Power BI portal.
- **Troubleshooting**: If a refresh fails in `BI_TME_Finance`, inspect the failure log under section 3 above and check upstream data gateway connectivity.
