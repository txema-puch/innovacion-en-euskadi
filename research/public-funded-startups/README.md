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

## Finding 3: Ekintzaile 2022–2025 and Barne-Ekintzaile 2022–24 (`startups_2022_2025.csv`)

414 awards, one row each. Sources: BDNS (with CIF) for 2022–24; BOPV 2603645a for Ekintzaile 2025 (CIF from infoempresa). Method: `method_2022_2025.md`; log: `log_2022_2025.md`; manual overrides with evidence: `manual_overrides_2022_2025.json`; natural-person tallies (counts only): `natural_persons_tally_2022_2025.json`.

| Call | Companies | € to companies | Natural persons (counted, not named) |
|---|---|---|---|
| Ekintzaile 2022 | 65 | €1.15M | 36, €592k |
| Ekintzaile 2023 | 57 | €1.10M | 36, €564k |
| Ekintzaile 2024 | 88 | €1.60M | 52, €905k |
| Ekintzaile 2025 | 99 | €1.87M | 33, €578k |
| Barne-Ekintzaile 2022 / 23 / 24 | 31 / 39 / 35 | €0.67M / €0.80M / €0.79M | — |

**Ekintzaile 2022–2025 (309 companies, €5.71M), status Oct 2026:** 275 active, 25 dead (18 extinct, 7 dormant), 9 unknown. The 2022–23 cohorts: 21 of 122 dead (17%); 2022 alone 15 of 65.

| Classification | Companies | € |
|---|---|---|
| Growing | 77 | €1.58M |
| Operating | 151 | €2.69M |
| Zombie | 22 | €0.36M |
| Dead | 25 | €0.46M |
| Absorbed | 4 | €65k |
| Unclear | 30 | €0.56M |

- **Growing is a loose label here:** it almost always means a capital increase in the last 24 months; only 5 companies qualify on headcount. Operating counts filed FY2024+ accounts as a sign of life.
- **Survivors are micro:** of 275 active, 246 have 1–9 employees, 5 have 10–49, 24 unknown; none with data has revenue over €2M. 164 have had no capital increase at all.
- 32 had a corporate sole shareholder when funded (incl. foreign subsidiaries and corporate spin-offs such as Ikerlan → Orbik, CIDETEC → CIDETEC Cells).
- Proxy top outcomes: Trebezia, Vali AI Europe, Olive Robotics, Mauvisoft (10–49 staff); Agria Zero Emissions/Zetrack, Nurdoc, Ditto Educación, QCentroid, Surion Wind, Izpitek, Bihar Batteries, Cloudtainer, Qubiz (most capital increases). Exits, no terms public: Syngoi → Artis Biosolutions (US), Dinaiz → Smartlog, Dealrock → Zorraquino, Quanvia → Qubiz.
- Failures include insolvencies (Ialtitude Health, Isauki Superfood, Motmo, Social Impact Code, Dive Medical, Roble Academy; Circular Replay in concurso) and companies wound up soon after a €30k grant (Exaquao2, Treebium Studios, Alloy Medical Implants).
- **Barne-Ekintzaile is not a startup programme:** at least 59 of 105 awards went to companies 4+ years old (Alavés, ITP, Sidenor, Fagor Ederlan, Lantek, Ideko, CEIT, Vicomtech…); ~13 beneficiaries are under 4 years old.
- **The only public link between a person-grantee and the company they later formed** is BDNS recording the company: 1 case in 2022, 18 in 2024.

Caveats: outcome window is 1–4 years (for 2025, "active" says little); infoempresa blocked access partway (~35 rows without ranges); websites found by guessing domains; funding rounds not checked; cooperatives/foundations outside BORME; Ekintzaile+ (21 companies, up to €100k) out of scope; possible SPRI data error on AIDTEC/Qlarix 2024 (both kept).

## Finding 4: other programmes and public funds (`startups_other.csv`, 822 entities)

Sources and access: `sources_other.md`; method and Chrome log: `log_other.md`; manual name matches: `manual_alias_other.json`.

| Programme | Years | Obtained | Basque entities |
|---|---|---|---|
| Gauzatu-Industria (Basque Gov. reimbursable advances to "pymes de base tecnológica y/o innovadoras", BOPV) | 2014–2022 | 431 awards, 397 entities, €222M | 348 |
| Bizkaia "Creación de Empresas Innovadoras" (BDNS, with CIF) | 2023–2026 | 213 awards, 189 entities, €6.1M (+30 to natural persons, not named) | 185 |
| Gipuzkoa TXEKINTEK / BARNETEKIN (open data, CIF only) | Sep 2025–Aug 2026 | 61 entities, €1.25M (+4 natural persons) | 44 + 16 |
| BIC Gipuzkoa incubated companies | – | 132 names | 127 |
| BIND 4.0, editions 1–8 | 2016–2024 | 212 startups | 84 |
| Seed Capital Bizkaia portfolio ("selection") | – | 70 named | 66 |
| GCR public VC (named in SPRI posts) | – | 7 | 7 |

Deduplicated: 822 rows. **Startup cohort** (excluding Gauzatu established firms and BARNETEKIN): 575.

| Classification | All 822 | Startup cohort 575 |
|---|---|---|
| Operating | 488 | 318 |
| Growing (capital increase in last 24 months; funding-only proxy) | 101 | 94 |
| Dead | 92 | 69 |
| Unclear | 108 | 81 |
| Zombie | 20 | 8 |
| Absorbed | 13 | 5 |

- **Gauzatu: young firms die more.** Incorporated ≤5 years before the award: 31% dead (34 of 109). Established: 13% (23 of 171).
- Where sampled, headcount in the startup cohort is overwhelmingly 1–9 employees (104 of 122).
- Proxy top outcomes: Vivebiotech (ex-Inbiomed) and Viralgen Vector Core (50–249 staff); Barbara IoT and Fastbase (10–49); most capital increases: Oncomatryx, Ubikare, Optimitive, Histocell, Nymiz, Citiservi, Satlantis, Koiki, Mikrobiomik, Ironchip, Multiverse Computing (which registered a "declaración de unipersonalidad", i.e. a single shareholder, in Oct 2026; to be checked).
- Failures include Stemtek Therapeutics (insolvency, extinct), 13 dead BIC Gipuzkoa companies (Ecomagnet, Kusudama, Indicate Solutions, Big Data Sport, Urdin Break…), Enigmedia (no accounts since 2021).

**What is not public (the strongest finding):**
- **SPRI's Ekintzaile beneficiary lists for 2015–2020 were never published.** ~2,000 BOPV issue summaries 2015–2023 searched; BOPV full-text search for "Ekintzaile" (53 hits, 2003–2026) shows only rules and calls before 2021; SPRI's transparency portal and its Wayback archive hold beneficiary tables only from 2022.
- **GCR's public VC portfolios are not published.** GCR claims 500+ investees and names none; its transparency document says its funds "carecen de competencias para conceder ayudas", so subsidy-publicity rules don't reach them.
- Bizkaia before 2022 not in BDNS (BOB not searched); Gipuzkoa open data before Sep 2025 omits the programme; Araba has no startup calls in BDNS; BEAZ publishes no list; BIND editions 9–10 offline.

Caveats: name-only matches flagged in `notes`; websites by guessed domain (false positives possible); the age test misreads re-incorporated old firms as young; revenue bands coarse; funding rounds and exits not filled (no web search).

## Method and limits

`method.md`. Status from empresia.es (registry-based) and infoempresa.com; libreborme and einforma were blocked. Funding rounds not yet filled (search budget ran out). Single cohort, single programme: don't generalise to all Basque startup money yet.

## Full census size

Ekintzaile 2021–25 ≈ 350–400 beneficiaries (~200 companies); Barne-Ekintzaile ≈ 106; Bizkaia innovative-startup programmes ≈ 100–200; Ekintzaile 2015–2020, if the lists can be obtained (manual BOPV search or a request to SPRI), ≈ 600–900 more. **Total ≈ 1,000–1,500 entities.** Status checks are automatable; exact revenue/headcount ≈ €10 per company per year in registry fees.

## Next steps

1. Add funding rounds and exits (press, El Referente, Crunchbase).
2. ~~Extend to Ekintzaile 2022–24~~ done (2022–2025). Other programmes done (Finding 4); 2015–2020 Ekintzaile lists were never published → transparency request.
3. **Request the 2015–2020 lists and the public funds' portfolios from SPRI/GCR** (transparency request under Ley 19/2013 / Basque Ley 2/2016 if needed). A refusal or non-answer is itself evidence.

## Files

- `startups.csv`: one row per company, every non-unknown value with a URL.
- `sources.md`: source map, access method, coverage, what isn't public.
- `method.md`: cohort rule and limitations.
- `scripts/`: reproducible fetch/parse scripts (raw downloads in `../../raw/registry/`, local only).
