# Workspace Documentation: BI_TMR_Sales_Aftersales_Analysis

**Workspace ID**: `1abda0ff-086b-4873-ac67-ae60c2c6a267`  
**Type**: `Fabric / PowerBI Workspace`  
**Capacity ID**: `70650ed2-f7a2-46df-96e8-8089f25db80e`  
**Description**: No description provided.

---

## 1. Executive Summary & Newcomer Overview
This document contains operational and technical details for the **BI_TMR_Sales_Aftersales_Analysis** workspace. It is designed to give new team members full visibility into key items, data models, report lineage, and refresh schedules.

## 2. Native Fabric Items Inventory

| Item Name | Item Type | Item ID | Description |
| :--- | :--- | :--- | :--- |
| **TMR Sales Aftersales Analysis** | `Report` | `10114169-ffa6-4050-bf89-77e29dba6c96` | - |
| **Usage Metrics Report** | `Report` | `58cb5db1-fe4f-40b1-956c-e66cf54216d2` | - |
| **TMR Sales Aftersales Analysis** | `SemanticModel` | `d19e057c-3b00-4220-ad19-b9a3fddfcf96` | - |
| **Usage Metrics Report** | `SemanticModel` | `966ea4fa-cdd1-4582-b0a2-3bef9f2d2567` | - |

## 3. Semantic Models (Datasets) & Refresh Schedules

### Semantic Model: TMR Sales Aftersales Analysis
- **Dataset ID**: `d19e057c-3b00-4220-ad19-b9a3fddfcf96`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `01:00` (FLE Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `Sql` | Connection: `{'server': '10.75.1.7', 'database': 'jetnavdwh'}`
- Type: `SharePointList` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/collaboration/'}`
- Type: `Web` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/Collaboration/Shared%20Documents/INT_POWERBI_HELPER/TMR/TMR%20Sales%20Analysis/prediction_basis.xlsx'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmr_opspackage', 'database': 'tmr ops package'}`
- Type: `Extension` | Connection: `{'path': 'titanromania.crm4.dynamics.com', 'kind': 'CommonDataService'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2026-09-14 22:01:03 | 2026-09-14 22:15:47 | `Completed` | `Scheduled` | - |
| 2026-09-13 22:01:15 | 2026-09-13 22:13:05 | `Completed` | `Scheduled` | - |
| 2026-09-12 22:01:15 | 2026-09-12 22:13:26 | `Completed` | `Scheduled` | - |
| 2026-09-11 22:01:16 | 2026-09-11 22:14:13 | `Completed` | `Scheduled` | - |
| 2026-09-10 22:01:19 | 2026-09-10 22:13:19 | `Completed` | `Scheduled` | - |

### Semantic Model: Usage Metrics Report
- **Dataset ID**: `966ea4fa-cdd1-4582-b0a2-3bef9f2d2567`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `03:33` (UTC)

**Connected Data Sources (Lineage)**:
- Type: `Extension` | Connection: `{'path': 'UsageMetricsDataConnector', 'kind': 'UsageMetricsDataConnector'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2025-07-21 03:33:05 | 2025-07-21 03:33:05 | `Disabled` | `Scheduled` | - |
| 2025-07-20 03:33:07 | 2025-07-20 03:45:40 | `Completed` | `Scheduled` | - |
| 2025-07-19 03:33:04 | 2025-07-19 03:46:05 | `Completed` | `Scheduled` | - |
| 2025-07-18 03:33:03 | 2025-07-18 03:46:47 | `Completed` | `Scheduled` | - |
| 2025-07-17 03:33:17 | 2025-07-17 03:46:17 | `Completed` | `Scheduled` | - |

## 4. Power BI Reports Inventory

| Report Name | Report ID | Dataset ID | Web URL |
| :--- | :--- | :--- | :--- |
| **TMR Sales Aftersales Analysis** | `10114169-ffa6-4050-bf89-77e29dba6c96` | `d19e057c-3b00-4220-ad19-b9a3fddfcf96` | [Open Report](https://app.powerbi.com/groups/1abda0ff-086b-4873-ac67-ae60c2c6a267/reports/10114169-ffa6-4050-bf89-77e29dba6c96) |
| **Usage Metrics Report** | `58cb5db1-fe4f-40b1-956c-e66cf54216d2` | `966ea4fa-cdd1-4582-b0a2-3bef9f2d2567` | [Open Report](https://app.powerbi.com/groups/1abda0ff-086b-4873-ac67-ae60c2c6a267/reports/58cb5db1-fe4f-40b1-956c-e66cf54216d2) |

## 5. Dataflows & Dashboards

*No dataflows or dashboards in this workspace.*

---

## 6. Newcomer Operational Runbook & Notes
- **Primary Contact / Owner**: Refer to workspace access settings in Power BI portal.
- **Troubleshooting**: If a refresh fails in `BI_TMR_Sales_Aftersales_Analysis`, inspect the failure log under section 3 above and check upstream data gateway connectivity.
