# Workspace Documentation: BI_TMEU_Segment Dashboard

**Workspace ID**: `61dfd683-a3ff-4f12-a49c-d2fd22aad3e9`  
**Type**: `Fabric / PowerBI Workspace`  
**Capacity ID**: `70650ed2-f7a2-46df-96e8-8089f25db80e`  
**Description**: No description provided.

---

## 1. Executive Summary & Newcomer Overview

> [!WARNING]
> **Legacy Workspace (Pending Deletion Review)**
> This workspace contains legacy reports built in 2024. Their ongoing usage hasn't been proven. TMA Management Team should be involved in evaluating this priority upon request, as they were the initial requesters. Clarify the necessity of these reports and decommission/delete them if confirmed as unused.

This document contains operational and technical details for the **BI_TMEU_Segment Dashboard** workspace. It is designed to give new team members full visibility into key items, data models, report lineage, and refresh schedules.

## 2. Native Fabric Items Inventory

| Item Name | Item Type | Item ID | Description |
| :--- | :--- | :--- | :--- |
| **TMEU Segment Dashboard Multi-country** | `Dashboard` | `c4307b5c-2af2-4884-87cb-21f8d181ca7d` | - |
| **TMB Segment Dashboard** | `Report` | `621f101e-50ec-459b-874a-3a0eae4367be` | - |
| **TMD Segment Dashboard** | `Report` | `951918ec-833a-40b2-a3db-33f6c04f3d18` | - |
| **TMR Segment Dashboard** | `Report` | `07f2f4d8-01a8-4c5c-b109-a950ca45b2b1` | - |
| **TMU Segment Dashboard** | `Report` | `a501ecee-f970-4310-8f54-442310e342dc` | - |
| **Report Usage Metrics Report** | `Report` | `c7a06923-54dd-4774-ac3c-615761238bd3` | - |
| **Usage Metrics Report** | `Report` | `38371562-8b03-4fd3-ab8d-4e8ff46b925e` | - |
| **TMB Segment Dashboard** | `SemanticModel` | `ff0ef19b-3faf-48a4-addc-0b2feddcced2` | - |
| **TMD Segment Dashboard** | `SemanticModel` | `fe8040c4-16ab-4fdc-b6bd-78f0aabcb42c` | - |
| **TMR Segment Dashboard** | `SemanticModel` | `ad06fb6a-9dd0-4f70-b9a4-c19ac8f4cca0` | - |
| **TMU Segment Dashboard** | `SemanticModel` | `052625b6-55c1-40dd-a004-1c099be02a8b` | - |
| **Report Usage Metrics Model** | `SemanticModel` | `13cada7e-f054-4c43-8614-0252bcc840da` | - |
| **Usage Metrics Report** | `SemanticModel` | `036e2329-062d-43e7-8e2b-b3fc07ae0e7d` | - |

## 3. Semantic Models (Datasets) & Refresh Schedules

### Semantic Model: TMB Segment Dashboard
- **Dataset ID**: `ff0ef19b-3faf-48a4-addc-0b2feddcced2`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (DISABLED ❌):
- **Frequency**: Sunday
- **Scheduled Times**: `23:00` (GTB Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmb_opspackage', 'database': 'tmb ops package'}`
- Type: `Web` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/Collaboration/Shared%20Documents/INT_POWERBI_HELPER/TMB/TIV/TIV%20inputs.xlsx'}`
- Type: `Web` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/Collaboration/Shared%20Documents/INT_POWERBI_HELPER/TMB/headcount_division/headcount_by_division.xlsx'}`
- Type: `Web` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/Collaboration/Shared%20Documents/INT_POWERBI_HELPER/TMB/serv_rec_rate/gross_sal_serv.xlsx'}`


### Semantic Model: TMD Segment Dashboard
- **Dataset ID**: `fe8040c4-16ab-4fdc-b6bd-78f0aabcb42c`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday
- **Scheduled Times**: `23:00` (GTB Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `Web` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/Collaboration/Shared%20Documents/INT_POWERBI_HELPER/TMD/TIV/TIV%20inputs.xlsx'}`
- Type: `Web` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/Collaboration/Shared%20Documents/INT_POWERBI_HELPER/TMD/headcount_division/headcount_by_division.xlsx'}`
- Type: `Web` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/Collaboration/Shared%20Documents/INT_POWERBI_HELPER/TMD/serv_rec_rate/gross_sal_serv.xlsx'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmd_finance', 'database': 'tmd p&l'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmd_crm', 'database': 'tmd crm'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmd_aftersales', 'database': 'tmd service kpi new'}`


### Semantic Model: TMR Segment Dashboard
- **Dataset ID**: `ad06fb6a-9dd0-4f70-b9a4-c19ac8f4cca0`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday
- **Scheduled Times**: `23:00` (GTB Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmr_opspackage', 'database': 'tmr ops package'}`
- Type: `Web` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/Collaboration/Shared%20Documents/INT_POWERBI_HELPER/TMR/headcount_division/headcount_by_division.xlsx'}`
- Type: `Web` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/Collaboration/Shared%20Documents/INT_POWERBI_HELPER/TMR/serv_rec_rate/gross_sal_serv.xlsx'}`
- Type: `Web` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/Collaboration/Shared%20Documents/INT_POWERBI_HELPER/TMR/TIV/TIV%20inputs.xlsx'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmr_crm', 'database': 'tmr crm'}`


### Semantic Model: TMU Segment Dashboard
- **Dataset ID**: `052625b6-55c1-40dd-a004-1c099be02a8b`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (DISABLED ❌):
- **Frequency**: Sunday
- **Scheduled Times**: `23:00` (GTB Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmu_opspackage_reports', 'database': 'p&l tmu'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmu_opspackage_reports', 'database': 'service kpi'}`
- Type: `Web` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/Collaboration/Shared%20Documents/INT_POWERBI_HELPER/TMU/serv_rec_rate/gross_sal_serv.xlsx'}`
- Type: `Web` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/Collaboration/Shared%20Documents/INT_POWERBI_HELPER/TMU/TIV/TIV%20inputs.xlsx'}`
- Type: `Web` | Connection: `{'url': 'https://titanmachinery365.sharepoint.com/sites/Collaboration/Shared%20Documents/INT_POWERBI_HELPER/TMU/headcount_division/headcount_by_division.xlsx'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_tmu_crm', 'database': 'tmu crm'}`


### Semantic Model: Report Usage Metrics Model
- **Dataset ID**: `13cada7e-f054-4c43-8614-0252bcc840da`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `False`
- **Configured By**: `OBaliuta@titanmachinery.ua`

*No refresh schedule configured.*

### Semantic Model: Usage Metrics Report
- **Dataset ID**: `036e2329-062d-43e7-8e2b-b3fc07ae0e7d`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `21:43` (UTC)

**Connected Data Sources (Lineage)**:
- Type: `Extension` | Connection: `{'path': 'UsageMetricsDataConnector', 'kind': 'UsageMetricsDataConnector'}`


## 4. Power BI Reports Inventory

| Report Name | Report ID | Dataset ID | Web URL |
| :--- | :--- | :--- | :--- |
| **TMB Segment Dashboard** | `621f101e-50ec-459b-874a-3a0eae4367be` | `ff0ef19b-3faf-48a4-addc-0b2feddcced2` | [Open Report](https://app.powerbi.com/groups/61dfd683-a3ff-4f12-a49c-d2fd22aad3e9/reports/621f101e-50ec-459b-874a-3a0eae4367be) |
| **TMD Segment Dashboard** | `951918ec-833a-40b2-a3db-33f6c04f3d18` | `fe8040c4-16ab-4fdc-b6bd-78f0aabcb42c` | [Open Report](https://app.powerbi.com/groups/61dfd683-a3ff-4f12-a49c-d2fd22aad3e9/reports/951918ec-833a-40b2-a3db-33f6c04f3d18) |
| **TMR Segment Dashboard** | `07f2f4d8-01a8-4c5c-b109-a950ca45b2b1` | `ad06fb6a-9dd0-4f70-b9a4-c19ac8f4cca0` | [Open Report](https://app.powerbi.com/groups/61dfd683-a3ff-4f12-a49c-d2fd22aad3e9/reports/07f2f4d8-01a8-4c5c-b109-a950ca45b2b1) |
| **TMU Segment Dashboard** | `a501ecee-f970-4310-8f54-442310e342dc` | `052625b6-55c1-40dd-a004-1c099be02a8b` | [Open Report](https://app.powerbi.com/groups/61dfd683-a3ff-4f12-a49c-d2fd22aad3e9/reports/a501ecee-f970-4310-8f54-442310e342dc) |
| **Report Usage Metrics Report** | `c7a06923-54dd-4774-ac3c-615761238bd3` | `13cada7e-f054-4c43-8614-0252bcc840da` | [Open Report](https://app.powerbi.com/groups/61dfd683-a3ff-4f12-a49c-d2fd22aad3e9/reports/c7a06923-54dd-4774-ac3c-615761238bd3) |
| **Usage Metrics Report** | `38371562-8b03-4fd3-ab8d-4e8ff46b925e` | `036e2329-062d-43e7-8e2b-b3fc07ae0e7d` | [Open Report](https://app.powerbi.com/groups/61dfd683-a3ff-4f12-a49c-d2fd22aad3e9/reports/38371562-8b03-4fd3-ab8d-4e8ff46b925e) |

## 5. Dataflows & Dashboards

**Dashboards**:
- **TMEU Segment Dashboard Multi-country** (ID: `c4307b5c-2af2-4884-87cb-21f8d181ca7d`)

---

## 6. Newcomer Operational Runbook & Notes
- **Primary Contact / Owner**: Refer to workspace access settings in Power BI portal.
- **Troubleshooting**: If a refresh fails in `BI_TMEU_Segment Dashboard`, inspect the failure log under section 3 above and check upstream data gateway connectivity.
