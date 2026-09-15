# Workspace Documentation: BI_TME_Sales Management

**Workspace ID**: `6c2d6611-73ea-432a-8328-0d4cee3b83ec`  
**Type**: `Fabric / PowerBI Workspace`  
**Capacity ID**: `70650ed2-f7a2-46df-96e8-8089f25db80e`  
**Description**: Multicounty reports related to Sales

---

## 1. Executive Summary & Newcomer Overview
This document contains operational and technical details for the **BI_TME_Sales Management** workspace. It is designed to give new team members full visibility into key items, data models, report lineage, and refresh schedules.

## 2. Native Fabric Items Inventory

| Item Name | Item Type | Item ID | Description |
| :--- | :--- | :--- | :--- |
| **Multicountry CRM Summary Report** | `Report` | `44177fda-9923-45dc-a112-422001fe34cb` | - |
| **TMEU New Equipment - Sales by Top Manufacturers** | `Report` | `f8ab2e11-4ea5-4675-8a74-23e6f8aae062` | - |
| **Usage Metrics Report** | `Report` | `f5878961-5ff5-4fae-9ab9-01c71340c562` | - |
| **Multicountry CRM Summary Report** | `SemanticModel` | `d96ea13a-531d-47f6-a5cd-d07ed45f8b5d` | - |
| **TMEU New Equipment - Sales by Top Manufacturers** | `SemanticModel` | `cfdd5f24-29fd-47d3-bf32-6bc07d0f7347` | - |
| **Usage Metrics Report** | `SemanticModel` | `90b75a6a-50f0-4b41-b5a2-04f2d96dab3c` | - |

## 3. Semantic Models (Datasets) & Refresh Schedules

### Semantic Model: Multicountry CRM Summary Report
- **Dataset ID**: `d96ea13a-531d-47f6-a5cd-d07ed45f8b5d`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `03:00` (FLE Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `Extension` | Connection: `{'path': 'titanukraine.crm4.dynamics.com', 'kind': 'CommonDataService'}`
- Type: `Extension` | Connection: `{'path': 'titanromania.crm4.dynamics.com', 'kind': 'CommonDataService'}`
- Type: `Extension` | Connection: `{'path': 'titanmachinery.crm4.dynamics.com', 'kind': 'CommonDataService'}`
- Type: `Extension` | Connection: `{'path': 'PowerPlatformDataflows', 'kind': 'PowerPlatformDataflows'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2025-05-28 00:01:06 | 2025-05-28 00:01:06 | `Disabled` | `Scheduled` | - |
| 2025-05-27 00:00:05 | 2025-05-27 00:10:55 | `Completed` | `Scheduled` | - |
| 2025-05-26 00:01:05 | 2025-05-26 00:07:44 | `Completed` | `Scheduled` | - |
| 2025-05-25 00:01:06 | 2025-05-25 00:07:47 | `Completed` | `Scheduled` | - |
| 2025-05-24 00:00:08 | 2025-05-24 00:05:51 | `Completed` | `Scheduled` | - |

### Semantic Model: TMEU New Equipment - Sales by Top Manufacturers
- **Dataset ID**: `cfdd5f24-29fd-47d3-bf32-6bc07d0f7347`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `10:00` (FLE Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmr_opspackage', 'database': 'tmr ops package'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmb_opspackage', 'database': 'tmb ops package'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmd_sales', 'database': 'tmd wg sales'}`
- Type: `Extension` | Connection: `{'path': 'PowerPlatformDataflows', 'kind': 'PowerPlatformDataflows'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2026-01-14 08:01:20 | 2026-01-14 08:01:20 | `Disabled` | `Scheduled` | - |
| 2026-01-13 08:01:03 | 2026-01-13 08:03:55 | `Completed` | `Scheduled` | - |
| 2026-01-12 08:01:02 | 2026-01-12 08:04:28 | `Completed` | `Scheduled` | - |
| 2026-01-11 08:01:02 | 2026-01-11 08:04:37 | `Completed` | `Scheduled` | - |
| 2026-01-10 08:01:18 | 2026-01-10 08:07:39 | `Completed` | `Scheduled` | - |

### Semantic Model: Usage Metrics Report
- **Dataset ID**: `90b75a6a-50f0-4b41-b5a2-04f2d96dab3c`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `00:35` (UTC)

**Connected Data Sources (Lineage)**:
- Type: `Extension` | Connection: `{'path': 'UsageMetricsDataConnector', 'kind': 'UsageMetricsDataConnector'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2025-07-21 00:35:13 | 2025-07-21 00:35:13 | `Disabled` | `Scheduled` | - |
| 2025-07-20 00:35:05 | 2025-07-20 00:42:00 | `Completed` | `Scheduled` | - |
| 2025-07-19 00:35:11 | 2025-07-19 00:40:59 | `Completed` | `Scheduled` | - |
| 2025-07-18 00:35:17 | 2025-07-18 00:42:09 | `Completed` | `Scheduled` | - |
| 2025-07-17 00:35:02 | 2025-07-17 00:44:32 | `Completed` | `Scheduled` | - |

## 4. Power BI Reports Inventory

| Report Name | Report ID | Dataset ID | Web URL |
| :--- | :--- | :--- | :--- |
| **Multicountry CRM Summary Report** | `44177fda-9923-45dc-a112-422001fe34cb` | `d96ea13a-531d-47f6-a5cd-d07ed45f8b5d` | [Open Report](https://app.powerbi.com/groups/6c2d6611-73ea-432a-8328-0d4cee3b83ec/reports/44177fda-9923-45dc-a112-422001fe34cb) |
| **TMEU New Equipment - Sales by Top Manufacturers** | `f8ab2e11-4ea5-4675-8a74-23e6f8aae062` | `cfdd5f24-29fd-47d3-bf32-6bc07d0f7347` | [Open Report](https://app.powerbi.com/groups/6c2d6611-73ea-432a-8328-0d4cee3b83ec/reports/f8ab2e11-4ea5-4675-8a74-23e6f8aae062) |
| **Usage Metrics Report** | `f5878961-5ff5-4fae-9ab9-01c71340c562` | `90b75a6a-50f0-4b41-b5a2-04f2d96dab3c` | [Open Report](https://app.powerbi.com/groups/6c2d6611-73ea-432a-8328-0d4cee3b83ec/reports/f5878961-5ff5-4fae-9ab9-01c71340c562) |

## 5. Dataflows & Dashboards

*No dataflows or dashboards in this workspace.*

---

## 6. Newcomer Operational Runbook & Notes
- **Primary Contact / Owner**: Refer to workspace access settings in Power BI portal.
- **Troubleshooting**: If a refresh fails in `BI_TME_Sales Management`, inspect the failure log under section 3 above and check upstream data gateway connectivity.
