# Newcomer Transition & Onboarding Guide

Welcome! This guide is designed to help a newcomer quickly get up to speed with Titan Machinery's Fabric & Power BI environment.

## 1. Key Operational Concepts
- **Fabric Workspaces**: Logical containers holding Lakehouses, Data Pipelines, Notebooks, Semantic Models, and Power BI Reports.
- **OneLake & Direct Lake Mode**: Datasets configured with Direct Lake mode read directly from Delta tables in OneLake without needing import refresh steps.
- **Import Mode Datasets**: Refreshed on a schedule (documented in `02_Refresh_Schedules_&_Operations.md`).

## 2. Common Maintenance Workflows
### Monitoring Daily Refreshes
1. Open `02_Refresh_Schedules_&_Operations.md` to see expected daily refresh windows.
2. In the Power BI Service, navigate to the specific Workspace.
3. Check dataset Refresh History for any `Failed` status.

### Handling Refresh Failures
1. Inspect the error payload under the individual workspace documentation file (`Workspaces/<Workspace_Name>.md`).
2. Check On-Premises Data Gateway status if the source is on-prem SQL/Oracle/Excel.
3. Re-run dataset refresh manually via the Power BI portal or REST API.

