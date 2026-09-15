# Workspace Documentation: BI_TMB Accounting Support

**Workspace ID**: `aba0f3c6-4eb0-42bf-8601-fe380e16f002`  
**Type**: `Fabric / PowerBI Workspace`  
**Capacity ID**: `70650ed2-f7a2-46df-96e8-8089f25db80e`  
**Description**: TMB accounting space

---

## 1. Executive Summary & Newcomer Overview
This document contains operational and technical details for the **BI_TMB Accounting Support** workspace. It is designed to give new team members full visibility into key items, data models, report lineage, and refresh schedules.

## 2. Native Fabric Items Inventory

| Item Name | Item Type | Item ID | Description |
| :--- | :--- | :--- | :--- |
| **ICO Elimination** | `Report` | `f771bc20-3759-4b1c-bc71-3654b8a272e6` | - |
| **Purchase_sales report TMB** | `Report` | `24e55cf8-497e-4584-88cf-7baeb147ec4b` | - |
| **AMT Report for posting** | `Report` | `11cd083b-8933-4f5a-8ad9-0f99fec0bd6e` | - |
| **Usage Metrics Report** | `Report` | `4324ee91-485b-44f6-8031-1b31e7ff0d44` | - |
| **ICO Elimination** | `SemanticModel` | `1f0eed45-707a-4912-a259-64b7ab64762d` | - |
| **Purchase_sales report TMB** | `SemanticModel` | `5adb9f5a-1ad4-448e-8c83-830d6f51a60b` | - |
| **AMT Report for posting** | `SemanticModel` | `0178ab0e-aeea-4807-bdd0-5ac7ed552f8a` | - |
| **Usage Metrics Report** | `SemanticModel` | `12cc3550-f4f8-4830-8043-e1362e209224` | - |

## 3. Semantic Models (Datasets) & Refresh Schedules

### Semantic Model: ICO Elimination
- **Dataset ID**: `1f0eed45-707a-4912-a259-64b7ab64762d`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `04:00` (FLE Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `Web` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/Collaboration/Shared%20Documents/INT_POWERBI_HELPER/TMB/Accounting/WG%20Purchases%20IC.xlsx'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2023-07-03 01:01:13 | 2023-07-03 01:01:13 | `Disabled` | `Scheduled` | - |
| 2023-07-02 01:01:08 | 2023-07-02 01:05:23 | `Completed` | `Scheduled` | - |
| 2023-07-01 01:02:09 | 2023-07-01 01:10:59 | `Completed` | `Scheduled` | - |
| 2023-06-30 01:02:11 | 2023-06-30 01:10:33 | `Completed` | `Scheduled` | - |
| 2023-06-29 01:02:13 | 2023-06-29 01:12:01 | `Completed` | `Scheduled` | - |

### Semantic Model: Purchase_sales report TMB
- **Dataset ID**: `5adb9f5a-1ad4-448e-8c83-830d6f51a60b`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `N/A`

**Configured Refresh Schedule** (DISABLED ❌):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `22:00` (UTC)

### Semantic Model: AMT Report for posting
- **Dataset ID**: `0178ab0e-aeea-4807-bdd0-5ac7ed552f8a`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `04:00` (FLE Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `Web` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/Collaboration/Shared%20Documents/INT_POWERBI_HELPER/TMB/Accounting/AMT%20Exports%20Work%20file.xlsx'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2026-09-15 01:00:18 | 2026-09-15 01:02:00 | `Completed` | `Scheduled` | - |
| 2026-09-14 01:00:31 | 2026-09-14 01:04:12 | `Completed` | `Scheduled` | - |
| 2026-09-13 01:01:18 | 2026-09-13 01:05:08 | `Completed` | `Scheduled` | - |
| 2026-09-12 01:00:21 | 2026-09-12 01:02:32 | `Completed` | `Scheduled` | - |
| 2026-09-11 01:00:35 | 2026-09-11 01:03:03 | `Completed` | `Scheduled` | - |

### Semantic Model: Usage Metrics Report
- **Dataset ID**: `12cc3550-f4f8-4830-8043-e1362e209224`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `09:34` (UTC)

**Connected Data Sources (Lineage)**:
- Type: `Extension` | Connection: `{'path': 'UsageMetricsDataConnector', 'kind': 'UsageMetricsDataConnector'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2025-07-21 09:34:04 | 2025-07-21 09:34:04 | `Disabled` | `Scheduled` | - |
| 2025-07-20 09:34:15 | 2025-07-20 09:45:46 | `Completed` | `Scheduled` | - |
| 2025-07-19 09:34:03 | 2025-07-19 09:44:30 | `Completed` | `Scheduled` | - |
| 2025-07-18 09:35:08 | 2025-07-18 09:44:59 | `Completed` | `Scheduled` | - |
| 2025-07-17 09:34:06 | 2025-07-17 09:45:03 | `Completed` | `Scheduled` | - |

## 4. Power BI Reports Inventory

| Report Name | Report ID | Dataset ID | Web URL |
| :--- | :--- | :--- | :--- |
| **ICO Elimination** | `f771bc20-3759-4b1c-bc71-3654b8a272e6` | `1f0eed45-707a-4912-a259-64b7ab64762d` | [Open Report](https://app.powerbi.com/groups/aba0f3c6-4eb0-42bf-8601-fe380e16f002/reports/f771bc20-3759-4b1c-bc71-3654b8a272e6) |
| **Purchase_sales report TMB** | `24e55cf8-497e-4584-88cf-7baeb147ec4b` | `5adb9f5a-1ad4-448e-8c83-830d6f51a60b` | [Open Report](https://app.powerbi.com/groups/aba0f3c6-4eb0-42bf-8601-fe380e16f002/reports/24e55cf8-497e-4584-88cf-7baeb147ec4b) |
| **AMT Report for posting** | `11cd083b-8933-4f5a-8ad9-0f99fec0bd6e` | `0178ab0e-aeea-4807-bdd0-5ac7ed552f8a` | [Open Report](https://app.powerbi.com/groups/aba0f3c6-4eb0-42bf-8601-fe380e16f002/reports/11cd083b-8933-4f5a-8ad9-0f99fec0bd6e) |
| **Usage Metrics Report** | `4324ee91-485b-44f6-8031-1b31e7ff0d44` | `12cc3550-f4f8-4830-8043-e1362e209224` | [Open Report](https://app.powerbi.com/groups/aba0f3c6-4eb0-42bf-8601-fe380e16f002/reports/4324ee91-485b-44f6-8031-1b31e7ff0d44) |

## 5. Dataflows & Dashboards

*No dataflows or dashboards in this workspace.*

---

## 6. Newcomer Operational Runbook & Notes
- **Primary Contact / Owner**: Refer to workspace access settings in Power BI portal.
- **Troubleshooting**: If a refresh fails in `BI_TMB Accounting Support`, inspect the failure log under section 3 above and check upstream data gateway connectivity.
