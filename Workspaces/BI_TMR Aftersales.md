# Workspace Documentation: BI_TMR Aftersales

**Workspace ID**: `c5bfd987-780a-4abe-8a5f-9877fd3db52a`  
**Type**: `Fabric / PowerBI Workspace`  
**Capacity ID**: `70650ed2-f7a2-46df-96e8-8089f25db80e`  
**Description**: Workspace for TMR Parts and Service Reports

---

## 1. Executive Summary & Newcomer Overview
This document contains operational and technical details for the **BI_TMR Aftersales** workspace. It is designed to give new team members full visibility into key items, data models, report lineage, and refresh schedules.

## 2. Native Fabric Items Inventory

| Item Name | Item Type | Item ID | Description |
| :--- | :--- | :--- | :--- |
| **Report Usage Metrics Report** | `Report` | `797b9b5e-1361-4517-aae7-12668fbff2fb` | - |
| **Usage Metrics Report** | `Report` | `9e62283a-c8aa-4a89-9325-52be70972d48` | - |
| **Report Usage Metrics Model** | `SemanticModel` | `e1a7bae6-facc-45a1-8f93-5dbebb2b5078` | - |
| **Usage Metrics Report** | `SemanticModel` | `e20aaa75-e95a-490e-8e3c-3a8458186e41` | - |

## 3. Semantic Models (Datasets) & Refresh Schedules

### Semantic Model: Report Usage Metrics Model
- **Dataset ID**: `e1a7bae6-facc-45a1-8f93-5dbebb2b5078`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `False`
- **Configured By**: `OBaliuta@titanmachinery.ua`

*No refresh schedule configured.*

### Semantic Model: Usage Metrics Report
- **Dataset ID**: `e20aaa75-e95a-490e-8e3c-3a8458186e41`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `07:23` (UTC)

**Connected Data Sources (Lineage)**:
- Type: `Extension` | Connection: `{'path': 'UsageMetricsDataConnector', 'kind': 'UsageMetricsDataConnector'}`

**Recent Refresh History (Last 5 Runs)**:
| Start Time | End Time | Status | Refresh Type | Service Exception |
| :--- | :--- | :--- | :--- | :--- |
| 2024-08-03 07:23:03 | 2024-08-03 07:23:03 | `Disabled` | `Scheduled` | - |
| 2024-08-02 07:23:02 | 2024-08-02 07:23:14 | `Completed` | `Scheduled` | - |
| 2024-08-01 07:23:00 | 2024-08-01 07:23:12 | `Completed` | `Scheduled` | - |
| 2024-07-31 07:23:25 | 2024-07-31 07:23:39 | `Completed` | `Scheduled` | - |
| 2024-07-30 07:23:13 | 2024-07-30 07:23:51 | `Completed` | `Scheduled` | - |

## 4. Power BI Reports Inventory

| Report Name | Report ID | Dataset ID | Web URL |
| :--- | :--- | :--- | :--- |
| **Report Usage Metrics Report** | `797b9b5e-1361-4517-aae7-12668fbff2fb` | `e1a7bae6-facc-45a1-8f93-5dbebb2b5078` | [Open Report](https://app.powerbi.com/groups/c5bfd987-780a-4abe-8a5f-9877fd3db52a/reports/797b9b5e-1361-4517-aae7-12668fbff2fb) |
| **Usage Metrics Report** | `9e62283a-c8aa-4a89-9325-52be70972d48` | `e20aaa75-e95a-490e-8e3c-3a8458186e41` | [Open Report](https://app.powerbi.com/groups/c5bfd987-780a-4abe-8a5f-9877fd3db52a/reports/9e62283a-c8aa-4a89-9325-52be70972d48) |

## 5. Dataflows & Dashboards

*No dataflows or dashboards in this workspace.*

---

## 6. Newcomer Operational Runbook & Notes
- **Primary Contact / Owner**: Refer to workspace access settings in Power BI portal.
- **Troubleshooting**: If a refresh fails in `BI_TMR Aftersales`, inspect the failure log under section 3 above and check upstream data gateway connectivity.
