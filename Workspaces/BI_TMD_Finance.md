# Workspace Documentation: BI_TMD_Finance

**Workspace ID**: `f5523a6b-bc30-4214-aabb-6f9b705f2e93`  
**Type**: `Fabric / PowerBI Workspace`  
**Capacity ID**: `70650ed2-f7a2-46df-96e8-8089f25db80e`  
**Description**: No description provided.

---

## 1. Executive Summary & Newcomer Overview
This document contains operational and technical details for the **BI_TMD_Finance** workspace. It is designed to give new team members full visibility into key items, data models, report lineage, and refresh schedules.

## 2. Native Fabric Items Inventory

| Item Name | Item Type | Item ID | Description |
| :--- | :--- | :--- | :--- |
| **DB_PNL_Branch_MTD** | `Dashboard` | `d33d46ba-a392-4681-ae13-45490871ad43` | - |
| **DB_PNL_Branch_YTD** | `Dashboard` | `35d3d22d-cd9b-45d1-859c-c2df7028d89c` | - |
| **DB_B_YTD_Freienwalde** | `Dashboard` | `0c0678c8-f6fb-4c42-86cd-4df482f713b4` | - |
| **DB_B_YTD_Burkau** | `Dashboard` | `eb11aeb3-596c-4563-adcf-c52e699d2103` | - |
| **DB_B_YTD_Cunnesdorf** | `Dashboard` | `1513a554-1d14-4cbe-a8d2-438788c7cffd` | - |
| **DB_B_YTD_Freiberg** | `Dashboard` | `0921d6b9-a9d1-4743-a3c2-e266bab9ed07` | - |
| **DB_B_YTD_Gingst** | `Dashboard` | `856f89e3-f181-4651-a955-8ffb7c4be5a0` | - |
| **DB_B_YTD_Guetzkow** | `Dashboard` | `f2550d9e-ca6f-412f-b924-af0074056a65` | - |
| **DB_B_YTD_Muehlengeez** | `Dashboard` | `125bcb71-ecc3-4ae2-9049-d46674da7848` | - |
| **DB_B_YTD_Radelubbe** | `Dashboard` | `3b17f60f-7995-4b17-910c-f6eb9f3ff28d` | - |
| **DB_B_YTD_Rollwitz** | `Dashboard` | `74da4405-2390-4029-800c-7a8927e4bcc1` | - |
| **TMD P&L** | `Report` | `f30392d3-03d6-46e3-9acd-b0c4c396be06` | - |
| **Usage Metrics Report** | `Report` | `6264d83a-4051-45e4-8834-7748c3ee2cde` | - |
| **TMD P&L** | `SemanticModel` | `1ddfad2b-4696-456a-a20e-0cb62789ba8f` | - |
| **Usage Metrics Report** | `SemanticModel` | `9c313ca1-aaa2-45fe-965f-550042e80e39` | - |

## 3. Semantic Models (Datasets) & Refresh Schedules

### Semantic Model: TMD P&L
- **Dataset ID**: `1ddfad2b-4696-456a-a20e-0cb62789ba8f`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `05:00` (FLE Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `ODBC` | Connection: `{'connectionString': 'dsn=timeline - tmd'}`
- Type: `SharePointList` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/collaboration/'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2026-09-15 02:00:26 | 2026-09-15 02:29:09 | `Completed` | `Scheduled` | - |
| 2026-09-14 02:00:26 | 2026-09-14 02:28:26 | `Completed` | `Scheduled` | - |
| 2026-09-13 02:01:06 | 2026-09-13 02:26:51 | `Completed` | `Scheduled` | - |
| 2026-09-12 02:00:27 | 2026-09-12 02:27:27 | `Completed` | `Scheduled` | - |
| 2026-09-11 02:01:06 | 2026-09-11 02:23:57 | `Completed` | `Scheduled` | - |

### Semantic Model: Usage Metrics Report
- **Dataset ID**: `9c313ca1-aaa2-45fe-965f-550042e80e39`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `13:37` (UTC)

**Connected Data Sources (Lineage)**:
- Type: `Extension` | Connection: `{'path': 'UsageMetricsDataConnector', 'kind': 'UsageMetricsDataConnector'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2025-07-21 13:37:06 | 2025-07-21 13:37:06 | `Disabled` | `Scheduled` | - |
| 2025-07-20 13:37:12 | 2025-07-20 13:43:11 | `Completed` | `Scheduled` | - |
| 2025-07-19 13:37:05 | 2025-07-19 13:45:03 | `Completed` | `Scheduled` | - |
| 2025-07-18 13:37:03 | 2025-07-18 13:42:28 | `Completed` | `Scheduled` | - |
| 2025-07-17 13:37:05 | 2025-07-17 13:44:02 | `Completed` | `Scheduled` | - |

## 4. Power BI Reports Inventory

| Report Name | Report ID | Dataset ID | Web URL |
| :--- | :--- | :--- | :--- |
| **TMD P&L** | `f30392d3-03d6-46e3-9acd-b0c4c396be06` | `1ddfad2b-4696-456a-a20e-0cb62789ba8f` | [Open Report](https://app.powerbi.com/groups/f5523a6b-bc30-4214-aabb-6f9b705f2e93/reports/f30392d3-03d6-46e3-9acd-b0c4c396be06) |
| **Usage Metrics Report** | `6264d83a-4051-45e4-8834-7748c3ee2cde` | `9c313ca1-aaa2-45fe-965f-550042e80e39` | [Open Report](https://app.powerbi.com/groups/f5523a6b-bc30-4214-aabb-6f9b705f2e93/reports/6264d83a-4051-45e4-8834-7748c3ee2cde) |

## 5. Dataflows & Dashboards

**Dashboards**:
- **DB_PNL_Branch_MTD** (ID: `d33d46ba-a392-4681-ae13-45490871ad43`)
- **DB_PNL_Branch_YTD** (ID: `35d3d22d-cd9b-45d1-859c-c2df7028d89c`)
- **DB_B_YTD_Freienwalde** (ID: `0c0678c8-f6fb-4c42-86cd-4df482f713b4`)
- **DB_B_YTD_Burkau** (ID: `eb11aeb3-596c-4563-adcf-c52e699d2103`)
- **DB_B_YTD_Cunnesdorf** (ID: `1513a554-1d14-4cbe-a8d2-438788c7cffd`)
- **DB_B_YTD_Freiberg** (ID: `0921d6b9-a9d1-4743-a3c2-e266bab9ed07`)
- **DB_B_YTD_Gingst** (ID: `856f89e3-f181-4651-a955-8ffb7c4be5a0`)
- **DB_B_YTD_Guetzkow** (ID: `f2550d9e-ca6f-412f-b924-af0074056a65`)
- **DB_B_YTD_Muehlengeez** (ID: `125bcb71-ecc3-4ae2-9049-d46674da7848`)
- **DB_B_YTD_Radelubbe** (ID: `3b17f60f-7995-4b17-910c-f6eb9f3ff28d`)
- **DB_B_YTD_Rollwitz** (ID: `74da4405-2390-4029-800c-7a8927e4bcc1`)

---

## 6. Newcomer Operational Runbook & Notes
- **Primary Contact / Owner**: Refer to workspace access settings in Power BI portal.
- **Troubleshooting**: If a refresh fails in `BI_TMD_Finance`, inspect the failure log under section 3 above and check upstream data gateway connectivity.
