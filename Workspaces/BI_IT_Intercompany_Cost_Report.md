# Workspace Documentation: BI_IT_Intercompany_Cost_Report

**Workspace ID**: `9f447ecc-5345-4f0c-a342-77ee82fe1541`  
**Type**: `Fabric / PowerBI Workspace`  
**Capacity ID**: `70650ed2-f7a2-46df-96e8-8089f25db80e`  
**Description**: No description provided.

---

## 1. Executive Summary & Newcomer Overview

> [!NOTE]
> **Intercompany IT Cost Reporting**
> This workspace contains reporting for **shared Azure IT costs** between the European business and the US market. The underlying data for these reports is maintained and fed by a dedicated pipeline running out of the `Fabric_Prod_Workspace`.

This document contains operational and technical details for the **BI_IT_Intercompany_Cost_Report** workspace. It is designed to give new team members full visibility into key items, data models, report lineage, and refresh schedules.

## 2. Native Fabric Items Inventory

| Item Name | Item Type | Item ID | Description |
| :--- | :--- | :--- | :--- |
| **IT Service and Fee Overview Report** | `Report` | `be1dfded-85be-44da-9655-03d9b3d8be7d` | - |
| **Direct_IT Service and Fee Overview Report** | `Report` | `1bbf0cb3-9cfe-45ed-963d-cab7756475ad` | - |
| **Usage Metrics Report** | `Report` | `b42e213d-999d-433c-b089-3faeabd78ac5` | - |
| **IT Service and Fee Overview Report** | `SemanticModel` | `a5afe3f8-9b4f-4edc-a49b-d6ebbbede8c1` | - |
| **Direct_IT Service and Fee Overview Report** | `SemanticModel` | `79ac26e9-a25a-4ae9-920e-285609e55548` | - |
| **Usage Metrics Report** | `SemanticModel` | `b6058f61-abb1-4a9c-b1e9-3edf596b0e10` | - |

## 3. Semantic Models (Datasets) & Refresh Schedules

### Semantic Model: IT Service and Fee Overview Report
- **Dataset ID**: `a5afe3f8-9b4f-4edc-a49b-d6ebbbede8c1`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `11:00` (Romance Standard Time)

**Connected Data Sources (Lineage)**:
- Type: `SharePointList` | Connection: `{'url': 'https://titanmachinery365europe.sharepoint.com/sites/it-dataset/'}`
- Type: `AnalysisServices` | Connection: `{'server': 'powerbi://api.powerbi.com/v1.0/myorg/bi_it_intercompany_cost_report', 'database': 'direct_it service and fee overview report'}`
- Type: `Sql` | Connection: `{'server': 'cwgz5ola5r6u5e4heu5qw3drgy-zzqhzdizzmcurky2zbgw4gw7la.datawarehouse.fabric.microsoft.com', 'database': 'tmeu_bronze_lakehouse'}`


### Semantic Model: Direct_IT Service and Fee Overview Report
- **Dataset ID**: `79ac26e9-a25a-4ae9-920e-285609e55548`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `rb.admin@titanmachinery.com`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `08:00` (UTC)

**Connected Data Sources (Lineage)**:
- Type: `SharePointList` | Connection: `{'url': 'https://titanmachinery365europe.sharepoint.com/sites/it-dataset/'}`
- Type: `Extension` | Connection: `{'path': 'Enrollment Number;72928766', 'kind': 'AzureCostManagement'}`
- Type: `Web` | Connection: `{'url': 'https://management.azure.com/providers/Microsoft.Billing/billingAccounts/72928766/invoices'}`


### Semantic Model: Usage Metrics Report
- **Dataset ID**: `b6058f61-abb1-4a9c-b1e9-3edf596b0e10`
- **Target Storage Mode**: `Abf`
- **Is Refreshable**: `True`
- **Configured By**: `OBaliuta@titanmachinery.ua`

**Configured Refresh Schedule** (ENABLED ✅):
- **Frequency**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
- **Scheduled Times**: `23:05` (UTC)

**Connected Data Sources (Lineage)**:
- Type: `Extension` | Connection: `{'path': 'UsageMetricsDataConnector', 'kind': 'UsageMetricsDataConnector'}`


## 4. Power BI Reports Inventory

| Report Name | Report ID | Dataset ID | Web URL |
| :--- | :--- | :--- | :--- |
| **IT Service and Fee Overview Report** | `be1dfded-85be-44da-9655-03d9b3d8be7d` | `a5afe3f8-9b4f-4edc-a49b-d6ebbbede8c1` | [Open Report](https://app.powerbi.com/groups/9f447ecc-5345-4f0c-a342-77ee82fe1541/reports/be1dfded-85be-44da-9655-03d9b3d8be7d) |
| **Direct_IT Service and Fee Overview Report** | `1bbf0cb3-9cfe-45ed-963d-cab7756475ad` | `79ac26e9-a25a-4ae9-920e-285609e55548` | [Open Report](https://app.powerbi.com/groups/9f447ecc-5345-4f0c-a342-77ee82fe1541/reports/1bbf0cb3-9cfe-45ed-963d-cab7756475ad) |
| **Usage Metrics Report** | `b42e213d-999d-433c-b089-3faeabd78ac5` | `b6058f61-abb1-4a9c-b1e9-3edf596b0e10` | [Open Report](https://app.powerbi.com/groups/9f447ecc-5345-4f0c-a342-77ee82fe1541/reports/b42e213d-999d-433c-b089-3faeabd78ac5) |

## 5. Dataflows & Dashboards

*No dataflows or dashboards in this workspace.*

---

## 6. Newcomer Operational Runbook & Notes
- **Primary Contact / Owner**: Refer to workspace access settings in Power BI portal.
- **Troubleshooting**: If a refresh fails in `BI_IT_Intercompany_Cost_Report`, inspect the failure log under section 3 above and check upstream data gateway connectivity.
