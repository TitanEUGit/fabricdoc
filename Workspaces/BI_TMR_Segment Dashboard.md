# Workspace Documentation: BI_TMR_Segment Dashboard

**Workspace ID**: `5667c18f-5bbe-404c-9f6e-9ed41b4b6969`  
**Type**: `Fabric / PowerBI Workspace`  
**Capacity ID**: `70650ed2-f7a2-46df-96e8-8089f25db80e`  
**Description**: No description provided.

---

## 1. Executive Summary & Newcomer Overview

> [!WARNING]
> **Legacy Workspace (Pending Deletion Review)**
> This workspace contains legacy reports built in 2024. Their ongoing usage hasn't been proven. TMA Management Team should be involved in evaluating this priority upon request, as they were the initial requesters. Clarify the necessity of these reports and decommission/delete them if confirmed as unused.

This document contains operational and technical details for the **BI_TMR_Segment Dashboard** workspace. It is designed to give new team members full visibility into key items, data models, report lineage, and refresh schedules.

## 2. Native Fabric Items Inventory

| Item Name | Item Type | Item ID | Description |
| :--- | :--- | :--- | :--- |
| **TMR Segment Dashboard** | `Report` | `567d4465-c018-400b-a058-58adf4c76c09` | - |
| **Report Usage Metrics Report** | `Report` | `4ba66fc0-a676-4a9e-b071-96e891b5d50d` | - |
| **Usage Metrics Report** | `Report` | `2e0b1424-5846-4890-b2c3-7103e6ce4f7d` | - |
| **TMR Segment Dashboard** | `SemanticModel` | `54a431cb-3489-4920-9a69-d945bb6b6431` | - |
| **Report Usage Metrics Model** | `SemanticModel` | `0dbd2eeb-5b39-4c71-9d79-3aa4ea72bf56` | - |
| **Usage Metrics Report** | `SemanticModel` | `84e7641c-be24-47d1-b76b-2bdfa1e2030a` | - |

## 3. Semantic Models (Datasets) & Refresh Schedules

### Semantic Model: TMR Segment Dashboard
- **Dataset ID**: `54a431cb-3489-4920-9a69-d945bb6b6431`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Monday
- **Scheduled Times**: `23:00` (GTB Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmr_opspackage', 'database': 'tmr ops package'}`
- Type: `Web` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/Collaboration/Shared%20Documents/INT_POWERBI_HELPER/TMR/TIV/TIV%20inputs.xlsx'}`
- Type: `Web` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/Collaboration/Shared%20Documents/INT_POWERBI_HELPER/TMR/headcount_division/headcount_by_division.xlsx'}`
- Type: `Web` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/Collaboration/Shared%20Documents/INT_POWERBI_HELPER/TMR/serv_rec_rate/gross_sal_serv.xlsx'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmr_crm', 'database': 'tmr crm'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2025-07-28 20:01:16 | 2025-07-28 20:01:16 | `Disabled` | `Scheduled` | - |
| 2025-07-21 20:01:15 | 2025-07-21 20:10:26 | `Completed` | `Scheduled` | - |
| 2025-07-14 20:01:10 | 2025-07-14 20:07:28 | `Completed` | `Scheduled` | - |
| 2025-07-07 20:00:06 | 2025-07-07 20:01:31 | `Completed` | `Scheduled` | - |
| 2025-06-30 20:01:10 | 2025-06-30 20:07:35 | `Completed` | `Scheduled` | - |

### Semantic Model: Report Usage Metrics Model
- **Dataset ID**: `0dbd2eeb-5b39-4c71-9d79-3aa4ea72bf56`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `False`
- **Configured By**: `OBaliuta@titanmachinery.ua`

*No refresh schedule configured.*

### Semantic Model: Usage Metrics Report
- **Dataset ID**: `84e7641c-be24-47d1-b76b-2bdfa1e2030a`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `21:01` (UTC)

**Connected Data Sources (Lineage)**:
- Type: `Extension` | Connection: `{'path': 'UsageMetricsDataConnector', 'kind': 'UsageMetricsDataConnector'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2024-05-25 21:03:20 | 2024-05-25 21:03:20 | `Disabled` | `Scheduled` | - |
| 2024-05-24 21:04:08 | 2024-05-24 21:17:21 | `Completed` | `Scheduled` | - |
| 2024-05-23 21:05:51 | 2024-05-23 21:18:44 | `Completed` | `Scheduled` | - |
| 2024-05-22 21:05:01 | 2024-05-22 21:18:24 | `Completed` | `Scheduled` | - |
| 2024-05-21 21:07:28 | 2024-05-21 21:19:49 | `Completed` | `Scheduled` | - |

## 4. Power BI Reports Inventory

| Report Name | Report ID | Dataset ID | Web URL |
| :--- | :--- | :--- | :--- |
| **TMR Segment Dashboard** | `567d4465-c018-400b-a058-58adf4c76c09` | `54a431cb-3489-4920-9a69-d945bb6b6431` | [Open Report](https://app.powerbi.com/groups/5667c18f-5bbe-404c-9f6e-9ed41b4b6969/reports/567d4465-c018-400b-a058-58adf4c76c09) |
| **Report Usage Metrics Report** | `4ba66fc0-a676-4a9e-b071-96e891b5d50d` | `0dbd2eeb-5b39-4c71-9d79-3aa4ea72bf56` | [Open Report](https://app.powerbi.com/groups/5667c18f-5bbe-404c-9f6e-9ed41b4b6969/reports/4ba66fc0-a676-4a9e-b071-96e891b5d50d) |
| **Usage Metrics Report** | `2e0b1424-5846-4890-b2c3-7103e6ce4f7d` | `84e7641c-be24-47d1-b76b-2bdfa1e2030a` | [Open Report](https://app.powerbi.com/groups/5667c18f-5bbe-404c-9f6e-9ed41b4b6969/reports/2e0b1424-5846-4890-b2c3-7103e6ce4f7d) |

## 5. Dataflows & Dashboards

*No dataflows or dashboards in this workspace.*

---

## 6. Newcomer Operational Runbook & Notes
- **Primary Contact / Owner**: Refer to workspace access settings in Power BI portal.
- **Troubleshooting**: If a refresh fails in `BI_TMR_Segment Dashboard`, inspect the failure log under section 3 above and check upstream data gateway connectivity.
