# Titan Machinery Europe (TMEU) — Fabric & Power BI Documentation

Welcome to the **authoritative central knowledge base** for Titan Machinery's European Fabric and Power BI ecosystem. This repository documents all active workspaces, reports, dataflows, semantic models, and their underlying business logic across our European operations.

---

## 🗺️ Navigation & Core Documents

If you are looking for specific information, start with these master indexes:

* **[00_Master_Index.md](./00_Master_Index.md)** 
  *The main entry point.* A categorized list of all workspaces and the items they contain.
* **[01_Workspaces_Catalog.md](./01_Workspaces_Catalog.md)** 
  Technical catalog detailing all Workspace IDs, Types, and Capacity bindings.
* **[02_Refresh_Schedules_&_Operations.md](./02_Refresh_Schedules_&_Operations.md)** 
  Timetables for dataset refresh schedules, import operations, and time zones.
* **[03_Data_Lineage_&_Dependencies.md](./03_Data_Lineage_&_Dependencies.md)** 
  Maps detailing how data flows from source Lakehouses (like `TMEU_Bronze_Lakehouse`) into downstream semantic models.
* **[04_Newcomer_Transition_Guide.md](./04_Newcomer_Transition_Guide.md)** 
  *Essential reading for any new team member.* Contains the business domain primer, organisational structure (including TMA HQ relations), and our core systems landscape (Dynamics 365, Frontu, NAV, 1C).
* **[05_Power_Automate_Workflows.md](./05_Power_Automate_Workflows.md)** 
  Central directory documenting the active Power Automate workflows that integrate with or depend on our Fabric & Power BI environment.

---

## 📂 Workspaces Directory

Detailed technical and operational documentation for each individual workspace is located in the **[`Workspaces/`](./Workspaces)** directory. 

Each file contains:
1. An **Executive Summary** detailing the business purpose and data owner.
2. A **Native Fabric Items Inventory** listing all reports, semantic models, and dataflows.
3. **Refresh Schedules** for active datasets.
4. **Data Lineage** connection strings mapping back to core Lakehouses.
5. **Newcomer Tips & Runbooks** for troubleshooting and operational maintenance.

### Workspace Naming Conventions

* **`BI_TMEU_`**: Europe-wide consolidated workspaces.
* **`BI_TMA_`**: Austria (EU Headquarters / Europe Office Center).
* **`BI_TMR_` / `BI_TMB_` / `BI_TMU_`**: Country-specific workspaces (Romania, Bulgaria, Ukraine).
* **`Fabric_` / `DS_TMEU_`**: Infrastructure, platform, and core data engineering workspaces.
* **`BI_TMINT_`**: Legacy "International" naming convention (requires careful review as scope varies).

---

## ⚠️ Important Scoping Notes

* **In-Scope**: Titan Machinery Europe (TMA/Austria HQ, TMR/Romania, TMB/Bulgaria, TMU/Ukraine).
* **Out-of-Scope**: Titan Machinery US operations are separate legal entities and are not documented here.
* **Excluded**: Legacy TMD (Germany) operations, as the business has exited that market.

---

## 🤖 AI Agent Instructions

If you are an AI assistant working in this repository, you **must** read the **[AGENTS.md](./AGENTS.md)** file before making any changes. It contains critical operational constraints, prefix exclusions, and formatting guidelines to ensure the documentation remains accurate and standardized.
