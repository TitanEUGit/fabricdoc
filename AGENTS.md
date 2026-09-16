# Titan Machinery — Fabric & Power BI Documentation Agent Instructions

This file contains standing instructions for any AI agent working in this repository.
It is automatically loaded by Antigravity (AGY) and compatible agents.

---

## 1. Repository Purpose

This repository is the **authoritative documentation hub** for Titan Machinery's
Microsoft Fabric and Power BI environment. It covers all workspaces, lakehouses,
semantic models, Power BI reports, data lineage, and refresh schedules.

**Organization:** Titan Machinery Inc. This repository documents the **European divisions** of the business.
Out-of-scope businesses (US) are separate legal entities and are not documented here.
TMD (Germany) - has exited the market, it is  not a part of Titan anymore, so it should not be documented here.

---

## 2. Repository Structure

```
fabric documentation/
├── AGENTS.md                            <- You are here (agent instructions)
├── 00_Master_Index.md                   <- Entry point: workspace directory & navigation
├── 01_Workspaces_Catalog.md             <- Full catalog with Workspace IDs & capacity
├── 02_Refresh_Schedules_&_Operations.md <- Refresh timetables for all datasets
├── 03_Data_Lineage_&_Dependencies.md    <- Lineage maps & cross-workspace dependencies
├── 04_Newcomer_Transition_Guide.md      <- Onboarding guide & operational runbooks
└── Workspaces/
    └── <WorkspaceName>.md               <- One file per workspace (items, datasets, reports)
```

### Always Start Here
- **`00_Master_Index.md`** — master index of all workspaces with item counts and links.
- **`Workspaces/<WorkspaceName>.md`** — detailed inventory for a specific workspace.

---

## 3. Key Concepts & Terminology

| Term | Meaning |
|:---|:---|
| **Workspace** | A Fabric/Power BI logical container holding all Fabric items |
| **Lakehouse** | Delta-format storage layer in OneLake (used as data source) |
| **Semantic Model** | Power BI dataset (Import or Direct Lake mode) |
| **Direct Lake** | Mode where models read directly from Delta tables — no scheduled refresh needed |
| **Import Mode** | Model copies data on a schedule; refresh schedules are in `02_Refresh_Schedules_&_Operations.md` |
| **SQLEndpoint** | Read-only T-SQL endpoint auto-generated for each Lakehouse |
| **CopyJob** | Fabric item that copies data into a Lakehouse from an ERP source |
| **Dataflow Gen2** | ETL item that transforms data and lands it into Lakehouses |
| **Capacity ID** | `70650ed2-f7a2-46df-96e8-8089f25db80e` — the primary Fabric capacity for most workspaces |

### Workspace Naming Conventions

| Prefix | Region / Division | In Scope? |
|:---|:---|:---|
| `BI_TMEU_` | Titan Machinery Europe (EU-wide consolidation) | ✅ Yes |
| `BI_TME_` | Titan Machinery Europe — **legacy abbreviation**, identical in meaning to TMEU | ✅ Yes |
| `BI_TMA_` | Titan Machinery Austria — **EU headquarters**, where central operations & management reside | ✅ Yes |
| `BI_EOC_` | Europe Office Center — **operational name for TMA (Austria HQ)**; EOC workspaces are HQ-owned | ✅ Yes |
| `BI_TMB_` | Titan Machinery Bulgaria | ✅ Yes |
| `BI_TMR_` | Titan Machinery Romania | ✅ Yes |
| `BI_TMU_` | Titan Machinery **Ukraine** — country entity under TMA | ✅ Yes |
| `DS_TMEU_` | Data engineering / source-layer workspaces for EU | ✅ Yes |
| `Fabric_` | Infrastructure / platform workspaces | ✅ Yes |
| `TMRO_` | Titan Machinery Romania (Finance) | ✅ Yes |
| `BI_TMINT_` | Legacy "International" prefix — **may represent EU-wide scope** | ⚠️ Caution |
| `BI_TMD_` | Titan Machinery Deutschland / Germany (exited market) | ❌ Excluded |

> **⚠️ `BI_TMINT_` caution:** The `TMINT` prefix is a legacy naming convention that was used
> for workspaces serving the entire European organisation. Always inspect the workspace content
> before deciding whether it is in scope — if it contains EU-relevant data, document it.

> **❌ Excluded prefixes:** Do **not** create, update, or reference documentation for
> `BI_TMD_` (Germany) workspaces.
> Germany is a legacy/exited market.

---

## 4. Primary Lakehouses

These are the core storage objects that most reports and semantic models connect to.
They all reside in **`Fabric_Prod_Workspace`**.

| Lakehouse | Purpose | In Scope? |
|:---|:---|:---|
| **TMEU_Bronze_Lakehouse** | EU region consolidated bronze ERP data | ✅ Yes |
| **TMEU_ERP_RAW_Lakehouse** | EU ERP raw landing zone | ✅ Yes |
| **TMEU_Freshservice_Lakehouse** | Freshservice IT helpdesk data (EU) | ✅ Yes |
| **TMA_NAV_Lakehouse** | Austria headquarters NAV/ERP data | ✅ Yes |
| **StagingLakehouseForDataflows_20260408083147** | Auto-generated staging lakehouse for Dataflow Gen2 | ✅ Yes |
| **TMU_Bronze_Lakehouse** | Ukraine ERP data from the 1C source system | ✅ Yes |
| **TMU_Competition_Lakehouse** | Ukraine competitor intelligence: government Customs import records and VAT database. Populated manually on demand by TMU business leaders via notebooks in `Fabric_Prod_Workspace`. | ✅ Yes |

---

## 5. Agent Behavioral Guidelines

### Documentation Updates
- When updating workspace documentation, always keep the **item count** in
  `00_Master_Index.md` and `01_Workspaces_Catalog.md` in sync with the
  `Workspaces/<WorkspaceName>.md` detail file.
- Preserve all existing IDs (Workspace ID, Item ID) exactly — never fabricate GUIDs.
- Prefer **tables** for structured inventory data; use bullet lists for prose/notes.
- Use backtick formatting for item types: `Lakehouse`, `SemanticModel`, `Report`, etc.

### Answering Questions
- **Always check `00_Master_Index.md` first** to orient on workspace structure.
- For refresh/schedule questions → read `02_Refresh_Schedules_&_Operations.md`.
- For lineage/dependency questions → read `03_Data_Lineage_&_Dependencies.md`.
- For a specific workspace's items → read `Workspaces/<WorkspaceName>.md`.
- Cross-reference connection strings (`database:` field) to identify which lakehouse
  a semantic model is consuming.

### What NOT to Do
- Do **not** invent or guess Workspace IDs, Item IDs, or GUIDs.
- Do **not** modify the `scripts/` directory without being asked explicitly.
- Do **not** rename existing workspace files — filename must match workspace name exactly.
- Do **not** assume a workspace uses Direct Lake without confirming in its detail file.

---

## 6. Common Tasks & How to Handle Them

### "What workspaces do we have?"
-> Read `00_Master_Index.md` and summarize the workspace table.

### "What lakehouses do we have?"
-> Search for `type: Lakehouse` entries across `Workspaces/*.md`
   (concentrated in `Workspaces/Fabric_Prod_Workspace.md`).

### "What reports does workspace X have?"
-> Read `Workspaces/<X>.md` and list entries with type `Report`.

### "When does dataset Y refresh?"
-> Search `02_Refresh_Schedules_&_Operations.md` for the dataset name.

### "What sources does workspace X depend on?"
-> Read `03_Data_Lineage_&_Dependencies.md` filtered to that workspace.

### Adding a new workspace
1. Create `Workspaces/<NewWorkspaceName>.md` following the pattern of existing files.
2. Add a row to the table in `00_Master_Index.md`.
3. Add a row to `01_Workspaces_Catalog.md` with the Workspace ID and capacity.
4. If datasets have refresh schedules, add entries to `02_Refresh_Schedules_&_Operations.md`.

### Adding a new dataset/report to an existing workspace
1. Update `Workspaces/<WorkspaceName>.md` — add the item to the appropriate section.
2. Increment the item counts in `00_Master_Index.md` and `01_Workspaces_Catalog.md`.
3. If the report has a refresh schedule, add it to `02_Refresh_Schedules_&_Operations.md`.

---

## 7. Data Source Connection Reference

Most semantic models connect to Lakehouses via the SQL Endpoint. The connection
string pattern is:

```
server: cwgz5ola5r6u5e4heu5qw3drgy-zzqhzdizzmcurky2zbgw4gw7la.datawarehouse.fabric.microsoft.com
database: <lakehouse_name_lowercase>
```

Common database values and what they map to:

| `database` value | Lakehouse |
|:---|:---|
| `tmeu_bronze_lakehouse` | TMEU_Bronze_Lakehouse |
| `tmeu_erp_raw_lakehouse` | TMEU_ERP_RAW_Lakehouse |
| `tma_nav_lakehouse` | TMA_NAV_Lakehouse (Austria headquarters) |
| `tmu_bronze_lakehouse` | TMU_Bronze_Lakehouse *(out of scope — US entity, but EU models may cross-reference it)* |

---

*Last updated: 2026-09-15 (TMA = Austria HQ in scope; US/Germany excluded; TMINT caution added) | Maintained by: Titan Machinery IT / BI Team*
