# Workspace Documentation: BI_EOC_OPSPackage

**Workspace ID**: `458b4817-c2e7-4897-9775-47faa2a5a065`  
**Type**: `Fabric / PowerBI Workspace`  
**Capacity ID**: `70650ed2-f7a2-46df-96e8-8089f25db80e`  
**Description**: No description provided.

---

## 1. Executive Summary & Newcomer Overview
This document contains operational and technical details for the **BI_EOC_OPSPackage** workspace. It is designed to give new team members full visibility into key items, data models, report lineage, and refresh schedules.

## 2. Native Fabric Items Inventory

| Item Name | Item Type | Item ID | Description |
| :--- | :--- | :--- | :--- |
| **TMEU Multi-Country OPS Package** | `Report` | `471de82c-9421-44e6-8a48-b7cc89421dcc` | - |
| **Usage Metrics Report** | `Report` | `f19d20a5-14e7-4b5b-b6dd-cb66be0c2579` | - |
| **Report Usage Metrics Report** | `Report` | `f4bcac61-286e-46a2-a5c8-65dd1c3e7836` | - |
| **TMEU Multi-Country OPS Package** | `SemanticModel` | `f3a3451c-616c-4c84-9455-403e1a3c50a4` | - |
| **Usage Metrics Report** | `SemanticModel` | `d73cc21f-1a8e-481b-b023-326d966313e3` | - |
| **Report Usage Metrics Model** | `SemanticModel` | `170d6635-faf9-4caa-a052-9dfb4136f797` | - |

## 3. Semantic Models (Datasets) & Refresh Schedules

### Semantic Model: TMEU Multi-Country OPS Package
- **Dataset ID**: `f3a3451c-616c-4c84-9455-403e1a3c50a4`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `10:00` (FLE Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmr_opspackage', 'database': 'tmr ops package'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmd_sales', 'database': 'tmd wg sales'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmb_opspackage', 'database': 'tmb ops package'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmd_finance', 'database': 'tmd p&l'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmu_opspackage', 'database': 'tmu ops package'}`
- Type: `Extension` | Connection: `{'path': 'PowerPlatformDataflows', 'kind': 'PowerPlatformDataflows'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmu_opspackage_reports', 'database': 'p&l tmu'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmd_aftersales', 'database': 'tmd parts sales'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2026-09-15 07:01:08 | 2026-09-15 07:07:44 | `Completed` | `Scheduled` | - |
| 2026-09-14 07:00:12 | 2026-09-14 07:06:52 | `Completed` | `Scheduled` | - |
| 2026-09-13 07:01:09 | 2026-09-13 07:08:37 | `Completed` | `Scheduled` | - |
| 2026-09-12 07:00:25 | 2026-09-12 07:07:01 | `Completed` | `Scheduled` | - |
| 2026-09-11 07:01:04 | 2026-09-11 07:06:55 | `Completed` | `Scheduled` | - |

### Semantic Model: Usage Metrics Report
- **Dataset ID**: `d73cc21f-1a8e-481b-b023-326d966313e3`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `08:59` (UTC)

**Connected Data Sources (Lineage)**:
- Type: `Extension` | Connection: `{'path': 'UsageMetricsDataConnector', 'kind': 'UsageMetricsDataConnector'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2025-07-19 08:59:14 | 2025-07-19 08:59:14 | `Disabled` | `Scheduled` | - |
| 2025-07-18 08:59:06 | 2025-07-18 09:00:36 | `Completed` | `Scheduled` | - |
| 2025-07-17 09:00:16 | 2025-07-17 09:06:02 | `Completed` | `Scheduled` | - |
| 2025-07-16 08:59:08 | 2025-07-16 08:59:59 | `Completed` | `Scheduled` | - |
| 2025-07-15 08:59:12 | 2025-07-15 09:00:08 | `Completed` | `Scheduled` | - |

### Semantic Model: Report Usage Metrics Model
- **Dataset ID**: `170d6635-faf9-4caa-a052-9dfb4136f797`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `False`
- **Configured By**: `OBaliuta@titanmachinery.ua`

*No refresh schedule configured.*

## 4. Power BI Reports Inventory

| Report Name | Report ID | Dataset ID | Web URL |
| :--- | :--- | :--- | :--- |
| **TMEU Multi-Country OPS Package** | `471de82c-9421-44e6-8a48-b7cc89421dcc` | `f3a3451c-616c-4c84-9455-403e1a3c50a4` | [Open Report](https://app.powerbi.com/groups/458b4817-c2e7-4897-9775-47faa2a5a065/reports/471de82c-9421-44e6-8a48-b7cc89421dcc) |
| **Usage Metrics Report** | `f19d20a5-14e7-4b5b-b6dd-cb66be0c2579` | `d73cc21f-1a8e-481b-b023-326d966313e3` | [Open Report](https://app.powerbi.com/groups/458b4817-c2e7-4897-9775-47faa2a5a065/reports/f19d20a5-14e7-4b5b-b6dd-cb66be0c2579) |
| **Report Usage Metrics Report** | `f4bcac61-286e-46a2-a5c8-65dd1c3e7836` | `170d6635-faf9-4caa-a052-9dfb4136f797` | [Open Report](https://app.powerbi.com/groups/458b4817-c2e7-4897-9775-47faa2a5a065/reports/f4bcac61-286e-46a2-a5c8-65dd1c3e7836) |

## 5. Dataflows & Dashboards

*No dataflows or dashboards in this workspace.*

---

## 6. Newcomer Operational Runbook & Notes
- **Primary Contact / Owner**: Refer to workspace access settings in Power BI portal.
- **Troubleshooting**: If a refresh fails in `BI_EOC_OPSPackage`, inspect the failure log under section 3 above and check upstream data gateway connectivity.
