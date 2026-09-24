# Power Automate Workflows Documentation

This document serves as the central directory for all active **Power Automate** workflows that integrate with or depend on our Fabric & Power BI environment.

> [!IMPORTANT]
> **System Account & Ownership**
> All Power Automate flows in this ecosystem are maintained and stored under the key service user account: **`powerplatform02@titanmachinery.net`**. 

---

## Master List of Workflows

| Flow Name | Trigger Type | Link |
| :--- | :--- | :--- |
| **AzureUsageNewResourceCheck** | `Scheduled` | [View Details](https://make.powerautomate.com/environments/Default-b99e8d15-ec60-4e7d-9387-253b0b6c7136/flows/9f457500-2856-4db9-acc0-bb27a5ad8023/details) |
| **csi_files_sending** | `Scheduled` | [View Details](https://make.powerautomate.com/environments/Default-b99e8d15-ec60-4e7d-9387-253b0b6c7136/flows/shared/8108258b-4425-42a3-b0d1-38795019c5fb/details) |
| **DevOPS post message** | `Automated` | [View Details](https://make.powerautomate.com/environments/Default-b99e8d15-ec60-4e7d-9387-253b0b6c7136/flows/d90d8da0-cec7-45c3-96f8-9e97d9a892d9/details) |
| **EUInvoiceRequestLineUpdate** | `Instant` | [View Details](https://make.powerautomate.com/environments/Default-b99e8d15-ec60-4e7d-9387-253b0b6c7136/flows/shared/1094e112-a67d-4ff5-b459-e2aed55af237/details) |
| **HR Dashboard Monthly Summaries** | `Instant` | [View Details](https://make.powerautomate.com/environments/Default-b99e8d15-ec60-4e7d-9387-253b0b6c7136/flows/shared/3608116a-3750-4b0c-87af-94dc8fe44aec/details) |
| **HR Dashboard YE Summaries** | `Instant` | [View Details](https://make.powerautomate.com/environments/Default-b99e8d15-ec60-4e7d-9387-253b0b6c7136/flows/shared/838b289b-f8d0-48a0-ae16-e78f2e9ad51f/details) |
| **HR HC to Helper Folder Copying** | `Automated` | [View Details](https://make.powerautomate.com/environments/Default-b99e8d15-ec60-4e7d-9387-253b0b6c7136/flows/shared/4f2f0bbf-c59b-4bec-a376-ae4da3e33c40/details) |
| **OnDemandNewResourceCheckAzureUsage** | `Instant` | [View Details](https://make.powerautomate.com/environments/Default-b99e8d15-ec60-4e7d-9387-253b0b6c7136/flows/shared/89ba5ad0-8fd6-4e68-8602-86276fe519c5/details) |
| **parts_items_translation** | `Scheduled` | [View Details](https://make.powerautomate.com/environments/Default-b99e8d15-ec60-4e7d-9387-253b0b6c7136/flows/shared/6982cc7a-c6b7-4b73-a429-60d99f9052e9/details) |
| **TMB aging saving to csv** | `Scheduled` | [View Details](https://make.powerautomate.com/environments/Default-b99e8d15-ec60-4e7d-9387-253b0b6c7136/flows/shared/068e5a91-cb70-4b06-93bd-1553eecbf953/details) |
| **TMB Service Performance Sendings** | `Scheduled` | [View Details](https://make.powerautomate.com/environments/Default-b99e8d15-ec60-4e7d-9387-253b0b6c7136/flows/shared/725ea850-d349-4991-afd2-c90f329f0f51/details) |
| **TME IT Users Devices SP List Job** | `Scheduled` | [View Details](https://make.powerautomate.com/environments/Default-b99e8d15-ec60-4e7d-9387-253b0b6c7136/flows/shared/cc04d9f1-8daf-4ff6-ae36-10c0789e571d/details) |
| **tmeu_timesheet_reminders** | `Scheduled` | [View Details](https://make.powerautomate.com/environments/Default-b99e8d15-ec60-4e7d-9387-253b0b6c7136/flows/9855db5f-6021-429e-82f7-c8c3076083cc/details) |
| **TMR aging saving to csv** | `Scheduled` | [View Details](https://make.powerautomate.com/environments/Default-b99e8d15-ec60-4e7d-9387-253b0b6c7136/flows/shared/4e5e08a7-db65-41cf-8f21-e60aec42dcf4/details) |
| **TMU aging saving to csv** | `Scheduled` | [View Details](https://make.powerautomate.com/environments/Default-b99e8d15-ec60-4e7d-9387-253b0b6c7136/flows/shared/4e6d67d2-5efb-4753-a62e-88288c362156/details) |
| **TMU Customer Interactions Sending** | `Scheduled` | [View Details](https://make.powerautomate.com/environments/Default-b99e8d15-ec60-4e7d-9387-253b0b6c7136/flows/shared/1750bf0e-a478-4947-8b2f-36f0d17038f1/details) |
| **TMU HR Data Movement** | `Automated` | [View Details](https://make.powerautomate.com/environments/Default-b99e8d15-ec60-4e7d-9387-253b0b6c7136/flows/shared/cafb4263-e9f4-4870-a396-6fee00ee96c4/details) |
| **TMU Not Maintained Customers Sending** | `Scheduled` | [View Details](https://make.powerautomate.com/environments/Default-b99e8d15-ec60-4e7d-9387-253b0b6c7136/flows/shared/f8657bc6-9785-49ef-a1dd-7b83cdc17000/details) |
| **userOnBoard** | `Automated` | [View Details](https://make.powerautomate.com/environments/Default-b99e8d15-ec60-4e7d-9387-253b0b6c7136/flows/dfe7440f-254f-4b8c-98a7-9ebf160a56b6/details) |

---

## Detailed Flow Documentation

### AzureUsageNewResourceCheck
* **Purpose:** Monitors the IT Usage Cost data to detect if any new Azure resources have been spun up.
* **Action/Outcome:** Automatically triggers and sends an alert email to the TMA IT Manager if a new resource is found.

### tmeu_timesheet_reminders
* **Purpose:** TMA HR flow designed to ensure compliance with monthly timesheet submissions.
* **Action/Outcome:** Automatically sends reminder emails to employees who have not submitted their working hours sheet in the HR app by the end of the month.

### DevOPS post message
* **Purpose:** Automates visibility and communication for Azure DevOps activity.
* **Action/Outcome:** Automatically triggers whenever an Azure DevOps item is created or updated, posting a notification message directly to a dedicated Microsoft Teams channel.

### userOnBoard
* **Purpose:** Facilitates user onboarding by streamlining the Microsoft user creation request process (primarily utilized by the IT Manager).
* **Action/Outcome:** When a new user is added to a dedicated SharePoint list, this flow can be triggered to automatically generate and send a Microsoft user creation request to IT support.

### [Country] aging saving to csv (TMB, TMR, TMU)
> [!WARNING]
> **Legacy Flow (Pending Review)**
> *Consider deprecating these flows and migrating the process to a Data Factory pipeline pointing to a Delta Lake.*
* **Purpose:** Legacy flows used for storing parts inventory history data.
* **Action/Outcome:** Saves the aging inventory snapshot data to CSV formats for the respective countries.

### HR Dashboard Summaries (Monthly & YE)
* **Purpose:** Interactive flows triggered directly by users via buttons embedded within the HR Dashboard.
* **Action/Outcome:** Automates the creation of timesheet files and summarizes HR data for either Monthly or Year-End (YE) periods.

### csi_files_sending
* **Purpose:** Acts as the delivery mechanism for CSI (Customer Satisfaction Index) data required by the manufacturer (CNH).
* **Action/Outcome:** Extracts CSI files from a dedicated Power BI semantic model and emails them to the IT team for manual submission to the CNH portal.

### EUInvoiceRequestLineUpdate & OnDemandNewResourceCheckAzureUsage
* **Purpose:** Dedicated flows for tracking and managing Azure consumption data.
* **Action/Outcome:** On-demand (instant) flows that pull Azure usage and cost data from a dedicated Power BI report and push it into a targeted SharePoint list for IT tracking and invoice line updates.

### TMB Service Performance Sendings
* **Purpose:** Automates the visibility of service personnel performance in Bulgaria.
* **Action/Outcome:** Scheduled flow that executes a weekly email distribution of Service KPIs, detailed on a per-person basis.

### TMU Customer Interactions Sending
* **Purpose:** Ensures the TMU ESC (Equipment Sales Consultant) team can properly track their customer engagement.
* **Action/Outcome:** Scheduled flow that sends the ESC team their assigned customer data along with their logged interactions (calls and appointments).

### parts_items_translation
> [!WARNING]
> **Pending Usage Review**
> *This flow exists solely to feed the downstream `TMEU Parts Item List` report. Verify if that specific report is still actively used. **If it is still active, consider switching this translation process to a Notebook approach.***
* **Purpose:** Automates the translation of parts item descriptions from country-native languages into English.
* **Action/Outcome:** Provides English-translated data specifically for the dedicated `TMEU Parts Item List` report.

### TMU Not Maintained Customers Sending
* **Purpose:** Proactively drives customer engagement for the TMU ESC (Equipment Sales Consultant) team.
* **Action/Outcome:** Scheduled flow that sends each ESC a list of their specific customers who require attention, based on company-defined maintenance criteria.

### HR Data Intactness & Movement (TMU HR & HC)
> [!WARNING]
> **Pending Architectural Review**
> *These flows have been used for years to maintain HR data integrity, but their functionality should likely be migrated to native Fabric pipelines / Dataflows.*
* **Flows:** `TMU HR Data Movement` and `HR HC to Helper Folder Copying`.
* **Purpose:** Automated legacy flows that copy and move HR data files to ensure data is kept intact and properly archived across helper folders.
