# Visualization ideas (for the future website)

Notes for whoever builds the visual layer. Data stays in the CSVs; these are views on top of it. Every chart must also be available as a table, with sources and caveats one click away.

## 1. Outcome flow as a Sankey diagram ("what became of them")

Reference style: an income-statement Sankey (e.g. the widely shared "Apple FY22 Income Statement" chart). Grey flows merge on the left, then split into green (good outcomes) and red (losses) on the right; each node shows its label, value and a secondary metric. Same idea, applied to companies instead of money.

### 1a. Tech-centre spin-offs (`research/tech-centres/spinoffs.csv` + `active-check/`)

```
Centres (Tecnalia+predecessors, CEIT, Vicomtech, CICs, CIDETEC, Ikerlan, Tekniker, AZTI, …)
  → 188 spin-offs
      → Dissolved (38)            [red]
      → Dormant (5)               [red]
      → Unknown (47)              [grey]
      → Acquired (17)             [neutral: mostly undisclosed trade sales to local industry]
      → Active (80 checked)
          → Zombie (3)            [red]
          → Absorbed (7)          [neutral]
          → Unclear (11)          [grey]
          → Operating (26)        [light green]
          → Growing (33)
              → Private-led (12)  [green]
              → Public-led (14)   [amber]
              → Weak evidence (7) [light amber]
```

- Node width = number of companies. Toggle: weight by headcount where known.
- Secondary labels per node: e.g. headcount sum, € raised, "price disclosed for 1 of 17" on Acquired.
- Highlight the Basque Tek Ventures pattern (centre chairs + public fund on board) as a stripe or tag across nodes.
- Counts in the active/growing branches come from `active-check/active_check.csv` (merged). Note Bunt Planet moved from active to acquired after the check, so the spin-off totals are 79 active / 18 acquired.

### 1b. Publicly funded startups (`research/public-funded-startups/`)

```
Programmes (Ekintzaile by year, Barne-Ekintzaile, Bizkaia/Gipuzkoa/Araba programmes, BIND 4.0, public VC funds)
  → € granted / companies funded
      → Dead (extinct / dissolved / dormant)   [red]
      → Acquired                               [neutral]
      → Unknown                                [grey]
      → Alive
          → Zombie                             [red]
          → Micro (1–9 employees)              [light green]
          → Growing: private-led / public-led / weak
```

- Two weightings worth offering: by **companies** and by **public €** (where did the money end up?).
- A second Sankey by cohort year (2015 → 2025) shows how outcomes mature over time.

### 1c. Money flows (`research/funding/`)

- Public R&D money → centres (Emaitek, Elkartek, Azpitek) vs companies (Hazitek) → Hazitek's ≥20% subcontracting back to RVCTI agents → "company revenue" of the centres. This shows the circularity in one picture. Label clearly which flows are measured and which are estimates.
- Startup rounds per year: public € vs private € (stacked), 2017–2024.

## 2. Voice share (`research/voice-share/`)

- Small-multiple bars per region: builders vs institutions (press; stages without pitches). Pitches shown as a separate bar, never mixed in.
- "Who opens the room": a row of event cards per region, each showing who gave the opening/keynote/closing, coloured by category.
- "Who hosts the room": 6/6 vs 2/3 vs 0/4 as a simple dot matrix.

## 3. Claims (`claims.md`)

- Each claim card: statement, status chip (supported / contested / against / open), confidence chip, for/against tag, links to the chart and the rows behind it, dispute thread.
- Filter: show only claims *against* the thesis. That filter should be prominent.
