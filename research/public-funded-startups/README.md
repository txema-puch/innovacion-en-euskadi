# Publicly funded startups: what became of each one

**Question.** Basque public startup money is public, so its recipients should be traceable. For every startup that received it: is it alive, how many people does it employ, what does it earn, what is it worth?

Position behind this: public money must be a way to the *next* thing, and the next thing must be named and tracked. If nobody tracks it, that is itself the finding.

## Finding 1: the outcome is not published, and for 2015–2021 the recipients are barely traceable

- **BDNS (Spain's national grants database)** works (open API, no key), but **Basque bodies barely reported to it before 2022**: SPRI's records start with the 2022 call year (all registered from June 2024); Basque Government departments from Oct 2023; Bizkaia from 2022; Gipuzkoa from 2024 (9 calls); Álava from 2022 (3). BDNS cannot answer the question for anything funded 2015–2021.
- **BOPV** has yearly Ekintzaile beneficiary lists 2021–2025, without CIF. 2015–2020 lists could not be retrieved by script (stateful search form).
- **Not public:** the portfolios of the public venture funds (GCR: Basque Fondo, Ekintzaile fund, BasketekVenture FCR, Hazten); Seed Capital Bizkaia's portfolio names; real revenue and headcount (only in paid annual accounts, ~€10/filing); size of private rounds (BORME shows nominal capital only); cooperatives (separate Basque register).
- No public body publishes what became of the startups it funded.

Details: `sources.md`.

## Finding 2: pilot cohort, Ekintzaile 2021 (five years on)

Cohort: all legal-entity beneficiaries of SPRI's Ekintzaile 2021 call (BOPV n.º 32, 15/02/2023): **65 of 124 beneficiaries, €1.17M of €2.16M** (€6k–€30k each). The 59 natural persons are excluded because the company they later formed isn't named. Three entries aren't startups (Gamesa Electric, Energía Distribuida del Norte, Metal Stamping & Hot Industry) and are flagged.

| Status (registry, Oct 2026) | Companies | Grant € |
|---|---|---|
| Active | 45 | 834k |
| Acquired | 1 (Nanokide → Hermes Lifescience; terms not public) | 20k |
| Dead (5 extinct, 3 dissolved, 5 dormant) | 13 | 224k |
| Unknown (2 cooperatives, 4 unresolved matches) | 6 | 94.5k |

- Of known outcomes, **78% still exist, 22% are dead.** "Active" = not wound up, not necessarily operating: 7 have had no registry act since founding; 26 had one in 2025–26; 17 have live websites.
- **Every active startup is in the "1–9 employees, under €2M revenue" band** (Infoempresa ranges). The only exception is the corporate Gamesa Electric.
- 26 of 46 survivors have had ≥1 capital increase, 11 have had ≥3: a weak signal of outside money.
- Proxy top 10 (nominal capital ≠ funding raised): Nanokide (acquired), Acustrain, Induplast Recycling, Whitehole Data, Optidel Biosystems, Nuuk Technologies, Trak Health Solutions, Fisify Technology, Normo Delivery Systems, Trantor MKT.

Reading: survival is decent for a pre-seed grant, which is small (€6k–€30k) and early, the kind of public money the literature says works. Five years on, though, none of the 65 has broken out of micro-company size.

## Method and limits

`method.md`. Status from empresia.es (registry-based) and infoempresa.com; libreborme and einforma were blocked. Funding rounds not yet filled (search budget ran out). Single cohort, single programme: don't generalise to all Basque startup money yet.

## Full census size

Ekintzaile 2021–25 ≈ 350–400 beneficiaries (~200 companies); Barne-Ekintzaile ≈ 106; Bizkaia innovative-startup programmes ≈ 100–200; Ekintzaile 2015–2020, if the lists can be obtained (manual BOPV search or a request to SPRI), ≈ 600–900 more. **Total ≈ 1,000–1,500 entities.** Status checks are automatable; exact revenue/headcount ≈ €10 per company per year in registry fees.

## Next steps

1. Add funding rounds and exits (press, El Referente, Crunchbase).
2. Extend to Ekintzaile 2022–24 (BDNS, with CIF) and the Bizkaia programmes.
3. **Request the 2015–2020 lists and the public funds' portfolios from SPRI/GCR** (transparency request under Ley 19/2013 / Basque Ley 2/2016 if needed). A refusal or non-answer is itself evidence.

## Files

- `startups.csv`: one row per company, every non-unknown value with a URL.
- `sources.md`: source map, access method, coverage, what isn't public.
- `method.md`: cohort rule and limitations.
- `scripts/`: reproducible fetch/parse scripts (raw downloads in `../../raw/registry/`, local only).
