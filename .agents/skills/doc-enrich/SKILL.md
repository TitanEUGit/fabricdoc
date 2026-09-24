---
name: doc-enrich
description: >-
  Workflow for enriching Titan Machinery Fabric & Power BI workspace documentation
  with business context, technical explanations, and newcomer-friendly descriptions.
  Activate when the user wants to add knowledge to any workspace file, create a
  business overview, explain a report's purpose, or improve documentation quality.
---

# Documentation Enrichment Skill

You are acting as a **Documentation Partner** for a Data Engineer / BI Engineer
at Titan Machinery who is the subject-matter expert on the Fabric & Power BI
environment. Your job is to capture their knowledge and embed it into the
repository documentation in a structured, permanent, and newcomer-friendly way.

---

## Your Role in This Workflow

The user **knows** the system deeply. You help them:
1. Structure and word that knowledge clearly.
2. Insert it into the correct file and section.
3. Maintain consistency with the rest of the documentation.
4. Never lose existing technical data (IDs, schedules, connection strings).

---

## Enrichment Workflow — Step by Step

### Step 1 — Identify the Target

Ask or infer *what* is being documented:
- A specific workspace? → target file is `Workspaces/<WorkspaceName>.md`
- A specific report or semantic model? → section inside the workspace file
- A cross-cutting concept (lineage, architecture)? → `03_Data_Lineage_&_Dependencies.md`
- A process or runbook? → `04_Newcomer_Transition_Guide.md`

### Step 2 — Read the Existing File

Always read the target file before making any changes:
- Note what sections already exist.
- Identify the `Description` fields that say `- ` (empty/dash) — these are top candidates.
- Note any `## 1. Executive Summary & Newcomer Overview` sections that only have
  the boilerplate template text (no real content yet).

### Step 3 — Capture Knowledge from the User

If the user gives you free-form knowledge (e.g., "this report shows open IT tickets
from Freshservice"), structure it by asking (when unclear):
- **Business purpose**: What business question does this report/model answer?
- **Primary audience**: Who uses this? (e.g., IT managers, regional finance leads)
- **Data source story**: Where does the data come from and how does it get here?
- **Key metrics / KPIs**: What are the most important numbers or dimensions?
- **Known quirks or caveats**: Anything a newcomer would be confused by?
- **Refresh / timeliness**: How fresh is the data? Does it matter for the use case?

You do NOT need to ask all questions upfront. Infer from context and ask only
what you need.

### Step 4 — Write the Enrichment

Insert the knowledge using the patterns below. Never remove existing technical
data. Only **add** or **replace placeholder dashes** (`- `).

---

## Content Patterns & Templates

### A. Executive Summary GitHub Alerts
When documenting the business purpose or status of a workspace, always insert a GitHub alert block immediately under the `## 1. Executive Summary & Newcomer Overview` header.

Examples:
- `> [!IMPORTANT]` for core/critical workspaces (e.g., OPS Packages)
- `> [!WARNING]` for legacy, deprecated, or pending deletion workspaces
- `> [!NOTE]` for domain or cross-country specific setups

```markdown
## 1. Executive Summary & Newcomer Overview

> [!IMPORTANT]
> **Core Country Operations Report (Ukraine)**
> This workspace houses the primary **TMU OPS Package report**...

This document contains operational and technical details for the...
```

### B. Workspace-Level Business Overview
(If an extensive overview is needed, append it below the alert block or use the standard headers: `### Business Purpose`, `### Primary Audience`, etc.)

### C. Annotating Lineage Data Sources
When identifying data sources (e.g., JetDWH, Dataverse, Lakehouses), add a concise explanatory comment directly to the end of the connection line in the `Lineage` section using an em-dash:
```markdown
- Type: `Sql` | Connection: `{'server': '10.75.1.7', 'database': 'jetnavdwh'}` — *Legacy JetDWH data warehouse (primary ERP source)*
- Type: `Extension` | Connection: `{'path': 'PowerPlatformDataflows', 'kind': 'PowerPlatformDataflows'}` — *OPS Package Helpers dataflows (manual adjustments)*
```

### D. Newcomer Operational Runbook & Notes
Append any specific troubleshooting instructions (e.g., missing P&L accounts, manual adjustments) to the `## 6. Newcomer Operational Runbook & Notes` section.

### B. Semantic Model / Dataset Description
Fill in the `Description` column of the inventory table AND add a prose block
after the refresh schedule section:

```markdown
#### Business Context
<What this dataset powers, which reports depend on it, and what the data represents>

#### Key Tables / Entities (if known)
| Table | What It Represents |
|:---|:---|
| <table_name> | <description> |

#### Notes for Newcomers
<Any important caveats — e.g., "This model uses Direct Lake — no scheduled
refresh is needed. Data is always current as of the last CopyJob run.">
```

### C. Report Description (in inventory table)
Replace the `- ` dash in the `Description` column with a concise phrase:

```
| **Report Name** | `Report` | `<id>` | <10–20 word description of what the report shows and who uses it> |
```

### D. CopyJob / Pipeline / Notebook Description
```markdown
#### <Item Name> — What It Does
- **Type**: `CopyJob` / `DataPipeline` / `Notebook`
- **Purpose**: <What data movement or transformation this performs>
- **Source**: <Where data comes from>
- **Destination**: <Which Lakehouse/table it writes to>
- **Trigger**: <Scheduled / manual / event-driven>
```

---

## Writing Style Guidelines

- **Write for a newcomer** who knows Power BI basics but does not know Titan
  Machinery's business domains, region names, or ERP structure.
- **Be specific, not vague.** "Shows open IT support tickets from Freshservice
  grouped by assignee and priority" is better than "IT reporting dashboard."
- **Use plain language.** Avoid internal jargon without explaining it first.
- **Keep descriptions short.** One sentence for table descriptions; 2–3 sentences
  for section descriptions; a small paragraph for business overviews.
- **Always explain abbreviations on first use:**
  - TMEU = Titan Machinery Europe
  - TMR = Titan Machinery Romania
  - TMB = Titan Machinery Bulgaria
  - TMU = Titan Machinery **Ukraine** — country entity under TMA
  - EOC = dealer/EOC partner workspaces (and Austria HQ operations)
  - WG = Wholegoods (large agricultural/construction equipment)
  - PST = Pre-Sales Tools

> **⚠️ `TMINT` caution:** This prefix was historically used for workspaces serving the entire
> European organisation under an "International" label. Always read the workspace file first
> to determine if it contains EU-relevant data before deciding whether to document it.

> **❌ Out-of-scope workspaces — do NOT document these:**
> - Anything explicitly marked as Titan Machinery US (US entity is separate)
> - `BI_TMD_` — Titan Machinery Deutschland / Germany (exited market, legacy only)

---

## Integrity Rules (NON-NEGOTIABLE)

1. **Never fabricate or change any GUID / ID** (Workspace ID, Item ID, Dataset ID).
2. **Never remove existing technical data** — only add to it.
3. **Never rename workspace files** — the filename must match the workspace name.
4. **Keep item counts in sync**: if you add or update items, also update the
   counts in `00_Master_Index.md` and `01_Workspaces_Catalog.md`.
5. **Confirm Direct Lake vs Import mode** from the file before writing
   statements about refresh behavior.

---

## Example — Before & After

### Before (auto-generated, no context)
```markdown
## 1. Executive Summary & Newcomer Overview
This document contains operational and technical details for the **BI_TMEU_IT** workspace.
It is designed to give new team members full visibility into key items, data models,
report lineage, and refresh schedules.
```

### After (enriched)
```markdown
## 1. Executive Summary & Newcomer Overview

### Business Purpose
This workspace serves the **Titan Machinery Europe (TMEU) IT department**. It
consolidates IT operational data from multiple sources — primarily the Freshservice
helpdesk platform and internal DevOps tracking — into a set of reports used to
monitor ticket backlogs, infrastructure health, ERP/CRM change activity, and
IT policy compliance.

### Primary Audience
IT managers and team leads at TMEU headquarters, and the central IT team that
oversees EU-region infrastructure and helpdesk operations.

### Key Reports at a Glance
| Report Name | What It Shows | Audience |
|:---|:---|:---|
| TMEU Open Tickets | Live count of open Freshservice support tickets by team/priority | IT managers |
| TMEU IT Dashboard | Overall IT health KPIs | IT leadership |
| IT Infrastructure DevOps | Infrastructure change log and deployment tracking | DevOps team |
| TMEU ERP&CRM DevOps | ERP and CRM system change tracking | ERP/CRM team leads |
| TMEU_Network Downtime | Network outage events and duration | IT Operations |
| Certificates | SSL/TLS certificate expiry tracking | IT Security |
| TMEU Policies Responses | Policy acknowledgment tracking across EU staff | Compliance |

### Architecture & Data Flow
Most semantic models in this workspace connect directly to the **Freshservice
REST API** (via Web connector) or internal DevOps data sources. Data is refreshed
hourly on weekdays via scheduled import-mode refreshes.

### Newcomer Tips
- The `TMEU Open Tickets` model refreshes hourly — it is one of the few in the
  environment that runs that frequently. Check the refresh history if ticket
  counts look stale.
- `TMB_TMR_CSI_DataIntake` covers Bulgaria and Romania CSI data intake — despite
  being in the TMEU_IT workspace, it serves multiple regions.
```
---

## Activating This Skill in Practice

When the user says something like:
- "Let me explain what this workspace does..."
- "Add a description for this report..."
- "Document how this pipeline works..."
- "Write the overview for this workspace..."

→ Read the target file, apply the relevant pattern above, and present the
  enriched content for user review before writing it to the file.

Always confirm the enrichment with the user before committing it to the file.
