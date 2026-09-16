# Newcomer Transition & Onboarding Guide

## 0. Titan Machinery — Business Domain Primer

Before diving into the technical environment, every newcomer needs to understand the core business model and organisational structure that all BI reports are built around.

---

### 0.1 Core Business Lines

Titan Machinery is an **agricultural machinery dealer** operating across multiple European countries. The entire business runs on three core revenue lines, grouped into two reporting domains:

| Business Line | Common Name | Abbreviation | Description |
|:---|:---|:---|:---|
| Machinery Sales | **Wholegoods** | **WG** | Sale of new and used large agricultural and construction machines (tractors, combines, harvesters, etc.) |
| Spare Parts Sales | **Parts** | *(part of AS)* | Sale of OEM and aftermarket spare parts for machinery |
| Machine Servicing | **Service** | *(part of AS)* | Workshop labour: repairs, maintenance, warranty work, and technical support |

**Parts + Service are collectively called Aftersales (AS).** Aftersales is a critical profitability driver for dealerships because it generates recurring revenue long after the initial machine sale.

**Primary manufacturer & strategic partner: CNH Industrial (CNHI) — brands: Case IH, CASE Construction.** Titan Machinery holds an **exclusive dealership** for CNH in Romania, Bulgaria, and part of Ukraine — meaning no other company is authorized to sell CNH machinery on those territories. The majority of WG sales, parts revenue, and service work is CNH-related. When you see "CNH" in a workspace or report name, it refers to this brand specifically.

When reading workspace or report names:
- **"Wholegoods" / "WG"** → relates to equipment unit sales, order intake, machine inventory
- **"Aftersales" / "AS"** → relates to Parts and/or Service KPIs combined
- **"Parts"** → spare parts only (when tracked separately from service)
- **"Service"** → workshop operations only (repair orders, technician utilisation, warranty claims)

---

### 0.2 Organisational Structure

Titan Machinery Europe is headquartered in **Austria (TMA)**. The EU organisation is structured as follows:

```
TMA — Austria (EU Headquarters / Europe Office Center)
└── General Director
    ├── Finance Manager       ← also owns Wholegoods (WG) responsibility
    ├── Aftersales Manager    ← Parts + Service across all EU countries
    ├── IT Manager            ← Technology & BI across all EU countries
    └── Country Managers
        ├── TMB — Bulgaria
        ├── TMR — Romania
        └── TMU — Ukraine
```

**Dotted-line management:** TMA functional managers (Finance/WG, Aftersales, IT) also provide functional direction to their counterparts at country level (e.g. country finance manager, country WG sales manager, country aftersales manager). This means a country manager owns their P&L, but functional strategy and standards flow from TMA.

---

### 0.3 Systems Landscape

The countries use different source systems for ERP and CRM, which is reflected in pipeline naming and workspace structure:

#### ERP (Enterprise Resource Planning)

| ERP System | Countries | Data Destination |
|:---|:---|:---|
| **Microsoft Dynamics NAV** | TMA (Austria), TMR (Romania), TMB (Bulgaria) | `TMA_NAV_Lakehouse` and `TMEU_ERP_RAW_Lakehouse` |
| **1C / 1S** | TMU (Ukraine) | `TMU_Bronze_Lakehouse` (schema: `dbo`) via custom web API pipelines |

> **Note:** "1C" and "1S" are interchangeable spellings of the same Ukrainian ERP system.

##### How Ukraine (1C) Data Gets into Fabric

Unlike NAV countries where data is copied via standard CopyJobs, Ukraine uses a **bespoke custom web API workflow** for each dataset:

1. **Business defines the need** — a user or analyst identifies what data they need in a report.
2. **Datasource is defined in 1C** — together with the business, the data engineer defines the exact dataset/view to expose from the 1C ERP.
3. **Custom API is requested** — the 1C support team (external) builds a dedicated **custom web endpoint** for that specific dataset.
4. **Pipeline is built** — a new pipeline is created in `Fabric_Prod_Workspace` (grouped under the `TMU 1C` pipeline items) to call that endpoint and push data into `TMU_Bronze_Lakehouse` under the `dbo` schema.

> [!IMPORTANT]
> Each 1C dataset has its **own dedicated API endpoint and pipeline**. There is no generic bulk extract — every new Ukrainian data requirement goes through this full workflow. Coordinate with the 1C support team before committing to a new data request, as lead time for API delivery can vary.

#### CRM (Customer Relationship Management)

| CRM System | Countries | BI Workspaces |
|:---|:---|:---|
| **Microsoft Dynamics 365** | TMR (Romania), TMB (Bulgaria), TMU (Ukraine) | `BI_TMR_CRM`, `BI_TMB_CRM`, `BI_TMU_CRM` |

> **Note:** TMA (Austria) does not have a CRM workspace — as a procurement/management entity with no retail market, TMA does not manage customer-facing sales activities directly.

---

### 0.4 TMA's Unique Business Role

> [!IMPORTANT]
> **TMA (Austria HQ) does not have its own retail market.** It is a purchasing and management entity, not a sales entity.

This is a common source of confusion when reading TMA data:

- **WG (Wholegoods) purchases**: TMA acts as the **central buyer** for Wholegoods on behalf of country entities. TMA procures machines from the manufacturer and supplies them to **TMR** (primarily) and sometimes **TMU**.
- **TMR's own purchases**: Romania also directly purchases **spare parts**, **small machines**, and **trade-in machines** independently — these appear in TMR's own NAV data and reports.
- As a result, TMA's NAV data predominantly reflects **inter-company procurement transactions**, not retail sales.

**Practical implication for BI:** When analysing WG sales data at country level:
- **TMR sales will include machines procured by TMA** on their behalf — cross-company flows must be accounted for to avoid double-counting at the EU consolidation level.
- **TMA can also appear as the legal selling entity** for sales that are economically Romanian — i.e. a sale is executed by Romanian salespeople and delivered to a Romanian customer, but is legally booked under TMA. There are no TMA salespeople involved; it is purely a legal/accounting structure. This means TMA figures in ERP and financial reports may include Romanian-origin business.

---

### 0.5 Abbreviation & Prefix Glossary

All workspaces and reports follow a naming convention based on these abbreviations:

| Abbreviation | Full Name | Role |
|:---|:---|:---|
| **TMEU** | Titan Machinery Europe | EU-wide consolidation — covers all country entities together |
| **TME** | Titan Machinery Europe | Legacy abbreviation — identical in meaning to TMEU |
| **TMA** | Titan Machinery Austria | EU Headquarters |
| **EOC** | Europe Office Center | Operational name for TMA (Austria HQ); EOC workspaces are HQ-owned |
| **TMB** | Titan Machinery Bulgaria | Country entity |
| **TMR** | Titan Machinery Romania | Country entity |
| **TMU** | Titan Machinery Ukraine | Country entity |
| **TMD** | Titan Machinery Deutschland | Germany — exited market, legacy only, not maintained |
| **WG** | Wholegoods | Machinery sales business line |
| **AS** | Aftersales | Parts + Service business lines combined |
| **DS** | Datasets | Data engineering / source-layer workspaces (not end-user reports) |
| **ESC** | Equipment Sales Consultant | Field sales representative role |
| **Dozor** | Dozor GPS | Ukrainian fleet GPS tracking service. ESC vehicles carry Dozor trackers; stop/location data is ingested into Fabric and cross-referenced with CRM customer visit records to validate field sales activity |
| **Lectura** | Lectura | External used machinery market valuation service. Used in the Wholegoods inventory impairment process to assess whether used machine book values should be written down to market value |
| **CNH / CNHI** | CNH Industrial | Primary manufacturer and strategic partner. Brands include **Case IH** (agriculture) and **CASE** (construction). Titan Machinery is the exclusive CNH dealer in Romania, Bulgaria, and part of Ukraine. The largest share of WG sales, parts, and service revenue is CNH-related. Also referred to as **Case IH** or **CASE** in reports and workspaces |
| **OPS Package** | Operations Package | The fundamental monthly operations report used in monthly OPS calls to wrap up the month. Acts as the **source of truth** for operational KPIs across business lines. Present in every country workspace (`BI_{country}_OPSpackage`). See individual workspace docs for details |
| **Freshservice** | Freshservice | Titan Machinery's IT service management and ticketing tool. Ticket data is ingested via API into Fabric for IT dashboard reporting |

---

### 0.6 OPS Package — The Monthly Operations Report

**OPS Package** (Operations Package) is the most important recurring report in the Titan Machinery BI environment. Every newcomer will encounter it.

#### What it is
A set of Power BI reports **automatically calculated from ERP data flows** and published monthly. The reports are used as the **presentation material during monthly OPS calls**, where management reviews and closes out the previous month's performance across all three business lines — Wholegoods, Parts, and Service — for a given country or region. Because the data is driven by automated ERP pipelines, the numbers are consistent and auditable, making them the agreed source of truth.

#### Why it matters
- It is the **source of truth** for month-end operational KPIs across the business.
- Management decisions, targets, and follow-up actions are based on OPS Package numbers.
- It is also used as a **data source** by downstream pipelines (e.g. IT cost reporting reads OPS Package data via `IT Costs to SQL`).

#### Where to find it
Every country and the EU consolidation level has its own OPS Package workspace:

| Workspace | Scope |
|:---|:---|
| `BI_TMB_OPSpackage` | Bulgaria |
| `BI_TMR_OpsPackage` | Romania |
| `BI_TMU_OPSpackage` | Ukraine |
| `BI_EOC_OPSPackage` | Austria HQ (EOC / TMA) — **Legacy**, currently used only as a datasource for some reports |
| `BI_TMU_OPSPackage_reports` | Ukraine (extended reporting) |

> [!NOTE]
> Full documentation of OPS Package content, KPIs, and data model will be added to the individual workspace files. For now, treat any `*OPSpackage*` workspace as high-priority and business-critical.

---




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

