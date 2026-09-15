# Workspace Documentation: Fabric_TMU_Webscraping

**Workspace ID**: `f31cbde2-9ab7-408f-8796-c397d6f9e611`  
**Type**: `Fabric / PowerBI Workspace`  
**Capacity ID**: `70650ed2-f7a2-46df-96e8-8089f25db80e`  
**Description**: No description provided.

---

## 1. Executive Summary & Newcomer Overview
This document contains operational and technical details for the **Fabric_TMU_Webscraping** workspace. It is designed to give new team members full visibility into key items, data models, report lineage, and refresh schedules.

## 2. Native Fabric Items Inventory

| Item Name | Item Type | Item ID | Description |
| :--- | :--- | :--- | :--- |
| **TMU_Webshop_Scraping** | `SQLEndpoint` | `c46afe58-45fd-437a-8a99-a15c62e05396` | - |
| **TMU_Webshop_Scraping** | `Lakehouse` | `0eab8216-10f2-49f5-82ec-4bc17da4aa19` | - |
| **TMU_Webshop_Scraping_Files_to_Bronze_TDon** | `Notebook` | `35fa39ec-cc64-40f4-a22e-dd6deb1cc255` | - |
| **TMU_Webshop_Scraping_Bronze_to_Silver_TDon** | `Notebook` | `249e9aa8-0d55-4818-a2c6-776d988ffcf8` | - |
| **PPL_Scraped_Data_Layers** | `DataPipeline` | `34a25964-d550-4bd3-9d15-83af6f2e4cdc` | - |
| **TMU_Webshop_Scraping_Files_to_Bronze_Amaco** | `Notebook` | `4cdc379f-ba9e-4750-bdfc-265dfd2a0f4d` | New notebook |
| **FilesRestorationSnippet** | `Notebook` | `3c39daac-2728-4af7-b216-02703fd2b9ac` | - |
| **TMU_Webshop_Scraping_Bronze_to_Silver_Amaco** | `Notebook` | `1f8ee664-9826-4688-bb76-d2b7c83a0ab4` | New notebook |
| **TMU_Webshop_Scraping_Files_to_Bronze_NFM** | `Notebook` | `32e20bdf-6dea-469c-b519-44e1eeea49f1` | New notebook |
| **TMU_Webshop_Scraping_Bronze_to_Silver_NFM** | `Notebook` | `9c5d4b6c-101c-48cf-bd7f-1f0b092c9e57` | New notebook |
| **TMU_Webshop_Scraping_Silver_to_Gold** | `Notebook` | `1ad6cabe-3775-426f-babe-1380420af1db` | - |
| **CNH_Parts_Scraping** | `Notebook` | `d10706db-e555-466d-afd6-a27f3a679868` | - |

## 3. Semantic Models (Datasets) & Refresh Schedules

*No semantic models/datasets found in this workspace.*

## 4. Power BI Reports Inventory

*No Power BI reports found in this workspace.*

## 5. Dataflows & Dashboards

*No dataflows or dashboards in this workspace.*

---

## 6. Newcomer Operational Runbook & Notes
- **Primary Contact / Owner**: Refer to workspace access settings in Power BI portal.
- **Troubleshooting**: If a refresh fails in `Fabric_TMU_Webscraping`, inspect the failure log under section 3 above and check upstream data gateway connectivity.
