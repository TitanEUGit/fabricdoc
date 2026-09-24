# Workspace Documentation: BI_TMEU_Human Resources

**Workspace ID**: `143ba3f6-bcf7-475b-af21-a75e9d8faccc`  
**Type**: `Fabric / PowerBI Workspace`  
**Capacity ID**: `70650ed2-f7a2-46df-96e8-8089f25db80e`  
**Description**: No description provided.

---

## 1. Executive Summary & Newcomer Overview

> [!NOTE]
> **Human Resources Reporting**
> This workspace houses the **TMA HR dashboard**. It is managed by the TMA HR Manager, who oversees HR operations in TMA and sets the HR strategy for all EU countries.

This document contains operational and technical details for the **BI_TMEU_Human Resources** workspace. It is designed to give new team members full visibility into key items, data models, report lineage, and refresh schedules.

## 2. Native Fabric Items Inventory

| Item Name | Item Type | Item ID | Description |
| :--- | :--- | :--- | :--- |
| **TMEU HR Dashboard** | `Report` | `2c253fa6-180f-4185-9869-83fcbe0261b0` | - |
| **TMEU HR Dashboard** | `SemanticModel` | `a2a607a4-1c45-4fe3-a867-ab69e53ba06c` | - |

## 3. Semantic Models (Datasets) & Refresh Schedules

### Semantic Model: TMEU HR Dashboard
- **Dataset ID**: `a2a607a4-1c45-4fe3-a867-ab69e53ba06c`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `06:00` (FLE Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `SharePointList` | Connection: `{'url': 'https://titanmachinery365europe.sharepoint.com/sites/hr-dataset-europe/'}`
- Type: `Sql` | Connection: `{'server': 'cwgz5ola5r6u5e4heu5qw3drgy-zzqhzdizzmcurky2zbgw4gw7la.datawarehouse.fabric.microsoft.com', 'database': 'tmeu_bronze_lakehouse'}`
- Type: `Sql` | Connection: `{'server': 'cwgz5ola5r6u5e4heu5qw3drgy-6yrznhjyk4mejouruyrqklpc7m.datawarehouse.fabric.microsoft.com', 'database': 'hr management'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2026-09-15 09:33:16 | 2026-09-15 09:33:48 | `Completed` | `OnDemand` | - |
| 2026-09-15 03:00:15 | 2026-09-15 03:02:36 | `Completed` | `Scheduled` | - |
| 2026-09-14 03:00:15 | 2026-09-14 03:02:31 | `Completed` | `Scheduled` | - |
| 2026-09-13 03:01:08 | 2026-09-13 03:03:47 | `Completed` | `Scheduled` | - |
| 2026-09-12 03:01:10 | 2026-09-12 03:05:48 | `Completed` | `Scheduled` | - |

## 4. Power BI Reports Inventory

| Report Name | Report ID | Dataset ID | Web URL |
| :--- | :--- | :--- | :--- |
| **TMEU HR Dashboard** | `2c253fa6-180f-4185-9869-83fcbe0261b0` | `a2a607a4-1c45-4fe3-a867-ab69e53ba06c` | [Open Report](https://app.powerbi.com/groups/143ba3f6-bcf7-475b-af21-a75e9d8faccc/reports/2c253fa6-180f-4185-9869-83fcbe0261b0) |

## 5. Dataflows & Dashboards

*No dataflows or dashboards in this workspace.*

---

## 6. Newcomer Operational Runbook & Notes
- **Primary Contact / Owner**: Refer to workspace access settings in Power BI portal.
- **Troubleshooting**: If a refresh fails in `BI_TMEU_Human Resources`, inspect the failure log under section 3 above and check upstream data gateway connectivity.
