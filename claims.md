# Claim registry

Every claim this project makes, with its evidence and how sure we are. This is the backbone for the future public "claims + evidence + refute" web.

**Confidence:** `high` = primary source read and verified · `medium` = primary source via secondary, or one source only · `low` = estimate or unverified. **Status:** `supported` · `contested` (evidence both ways) · `against` (evidence contradicts the thesis) · `open` (not yet tested). **Direction:** `for` / `against` the working thesis.

**Facts:** the sourced values each claim stands on live in `facts.csv` (spec: `docs/facts-format.md`), linked back by claim ID. When you add or change a claim, add or update its facts.

Don't delete claims. When evidence changes, update status and add a dated line under History.

| ID | Claim | Evidence (where) | Confidence | Status | Dir |
|---|---|---|---|---|---|
| C-001 | The Emaitek 2026 scorecard for tech centres does not weight spin-offs or startup creation (impact 55%, leadership 25%, specialisation 10%, international 10%). In 2018 spin-off revenue *was* a funding indicator (OECD case study). | research/funding §1; research/tech-centres | high | supported | for |
| C-002 | Hazitek strategic (≥€4M) and transformer (≥€20M) projects must subcontract ≥20% of budget to RVCTI agents; startups can be subcontracted but don't count toward the 20%. | research/funding §1 (BOPV nº250, 29/12/2025, Bases 6.1.c, 6.2.c.2, 7.1.c) | high | supported | for |
| C-003 | Elkartek (€47M) is open only to RVCTI agents and funds fundamental projects at 100%. | research/funding §1 | high | supported | for |
| C-004 | Basque regional aid per tech centre (€18.8M, 2021–23) is ~6x Galicia's (€3.1M). | research/funding §1 (Ministry of Science evaluation, Nov 2025) | high | supported | for |
| C-005 | No evaluation measures the market outcome of Hazitek/Elkartek/Emaitek projects; Hazitek reporting ends at project close. | research/funding §3 | medium (absence of evidence; search budget-limited) | supported | for |
| C-006 | The Basque Country does not report its R&D+I activity to Spain's SICTI. | research/funding §1 (MICIU eval., fn 1) | high | supported | for |
| C-007 | A significant share of centres' "company" revenue is executed inside grant-funded projects that require or allow subcontracting to centres. | research/funding §2 (MICIU eval. p.11, qualitative) | medium (not quantified) | supported | for |
| C-008 | Tecnalia's "51% from companies" (2024) is undefined and not split by grant-funded vs self-funded. | research/funding §2 (HC-2025 p.1) | high | supported | for |
| C-009 | Tecnalia's GDP-impact claims (€914M; €34.10 per €1) have no published methodology and look like input-output modelling, not measured outcomes. | research/tech-centres; research/funding §3 | medium | supported | for |
| C-010 | Public money was 60–85% of Basque startup-round money every year 2018–2024 (77% in 2024), up from 44% in 2017. | research/funding §4 (PIE 2025-28, p.14, UP! Euskadi) | high on the figures; open on definition (loans?) | supported | for |
| C-011 | Euskadi runs ~800 startup programmes/actions and 156 agents against 46 scale-ups and 1 unicorn; the plan itself diagnoses "atomización". | research/funding §4 | high | supported | for |
| C-012 | Tech centres measurably upgrade existing firms (Fraunhofer: +1.3pp client sales growth per 1% contract size). | research/comparisons | high (German evidence; no Basque equivalent) | supported | against |
| C-013 | Tecnalia's spin-off creation rate (~2 per 1,000 staff/yr) is on par with Fraunhofer. | research/tech-centres | medium | supported | against |
| C-014 | Tecnalia's 21 portfolio companies had €8.75M combined revenue (2025), down from €33.5M across 20 companies in 2018 (perimeter not like-for-like). | research/tech-centres | high (own figures) | supported | for |
| C-015 | Tecnalia delivered 2–3 startups/yr against a ~5/yr target; 2027 target of €25M portfolio revenue needs ~3x. | research/tech-centres | medium (target source secondary) | supported | for |
| C-016 | Tecnalia Ventures' CEO asked (OECD case study, 2018 data) for "a public fund to acquire stakes from the RTOs" in consolidated spin-offs. | research/tech-centres (quotes.md, verbatim p.12) | high | supported | for |
| C-017 | BRTA publishes no startups-per-year count or exits; its spin-off revenue figure is inconsistent (€26M / €66M / €37.4M). | research/tech-centres | high | supported | for |
| C-018 | Basque Tek Ventures is designed around the institution: centre <50%, BTV <40%, BTV controls expenses; CEO hired externally. | research/tech-centres (BTV call rules) | high | supported | for |
| C-019 | BTV publishes no fund size, no company names, and no results update since Jan 2025. | research/tech-centres | medium | supported | for |
| C-020 | Euskadi's first unicorn (Multiverse, 2026) did not come from a BRTA centre. | research/comparisons | high | supported | for |
| C-021 | In regional press, Basque founders get substantial voice (44% of speakers, 2025-26). | research/voice-share | medium (AI-coded; outlet mix) | against | against |
| C-022 | Institutions get ~2x the press voice in Euskadi vs Madrid (22% vs 12% of speakers) and are quoted first 3x as often (18% vs 6%). | research/voice-share | medium (small n; human 2nd coder pending) | supported | for |
| C-023 | On Basque startup stages, institutions get more voice than builders (27% vs 19% of named speakers, pitches counted apart); Euskadi is the only region studied where this happens (Madrid 31/14, Bay Area 41/3). Founders are present mainly as pitchers. | research/voice-share (stages v1+v2) | medium | supported | for |
| C-024 | The administration is the news far more often in Spanish startup coverage than in the Bay Area. In regional general dailies: Euskadi 25%, Madrid 56%, Bay Area 5% of articles (v2). The pattern is Spanish, not Basque-specific; in local press it is stronger in Madrid. | research/voice-share (trigger v1 + v2) | medium (paywalls; small n) | against (as a Basque-specific claim) | against |
| C-025 | Heavy public involvement in VC predicts worse outcomes; moderate public alongside private-led predicts better. | research/comparisons (Brander et al. 2015; Grilli & Murtinu 2014) | high (literature) | supported | for |
| C-026 | Business R&D in Gipuzkoa is 21% publicly funded (EU 5%, Germany 3%) and patent productivity is 3–6x below Spain/Germany and falling. | research/funding §3 (Orkestra 2021) | high | supported | for |
| C-027 | Basque VC per capita in 2025 roughly matched Madrid and Catalonia (~€147), but ~€61 without Multiverse's single round. | research/funding §5 | low (mixed sources, estimates) | contested | against |
| C-028 | Nobody in Euskadi measures how many tech-centre alumni go on to found or lead startups: no indicator in BRTA reports 2022–24, the PIE 2025-28 panel, or Tecnalia/CEIT/AZTI reports; no centre publishes an alumni list. Publicly documented alumni founders are few (floor: 5 startups across Tecnalia, CEIT, Ikerlan, Vicomtech). | research/talent §2, §4; facts with claims=C-028 | medium (PCTI 2030 monitoring not checked; counts are floors) | supported | for |
| C-029 | Every Basque startup event studied (6/6) has a local public body as organiser, co-organiser or funder; Madrid 2/3; Bay Area 0/4. | research/voice-share (stages v2, hosts.csv) | medium (Bizkaia-heavy sample) | supported | for |
| C-030 | Headline slots (opening/keynote/closing) go mostly to institutions in Spain (Euskadi 42%, Madrid 54%) vs 7% in the Bay Area; Basque openings had 0 builders among 10 speakers. | research/voice-share (stages v2) | medium (thin Madrid data) | supported | for (Spain-wide, not Basque-specific) |
| C-031 | No Basque public body publishes what became of the startups it funded. SPRI's Ekintzaile beneficiary lists for 2015–2020 were never published; Basque bodies barely reported to BDNS before 2022; GCR's public VC funds (500+ investees claimed) publish no portfolio and say subsidy-publicity rules don't apply to them. | research/public-funded-startups (Findings 1, 4); facts F-0079–F-0081 | medium (absence; transparency request pending) | supported | for |
| C-032 | Ekintzaile-funded companies mostly survive but stay micro. 2021 cohort (65): 78% of known outcomes alive five years on, 1 acquired. 2022–2025 cohorts (309 companies, €5.71M): 275 active, 25 dead (17% of the 2022–23 cohorts); of the 275 active, 246 have 1–9 employees, and none with data has revenue over €2M. | research/public-funded-startups (startups.csv, startups_2022_2025.csv); facts F-0007–F-0013 | medium (ranges; short outcome window for 2024–25) | contested | contested: survival against, size for |
| C-033 | Of 188 traceable Basque centre spin-offs (~35 years), 79 are active, 38 dissolved, 18 acquired (Bunt Planet corrected), 5 dormant, 47 unknown; known survivors are small (~552 staff across the 28 with exact headcount). | research/tech-centres (spinoffs.csv) | medium (registry via empresia; many unknowns) | supported | for |
| C-034 | Centre spin-off exits are mostly undisclosed trade sales to local industrial groups (CAF, CIE, Tubacex, Gamesa…); the largest disclosed price is $17.9M (Optenet → Allot, 2015). | research/tech-centres | medium | supported | for |
| C-035 | Of 80 "active" centre spin-offs, 33 show growth evidence, but only 12 are growing with private/market-led money; 14 are growing mainly on public money (10 with the Basque Tek Ventures pattern overall) and 7 on thin evidence; 3 are zombies, 7 absorbed. | research/tech-centres (active-check) | medium (single coder; amounts often undisclosed) | supported | for |
| C-036 | Barne-Ekintzaile, filed alongside Ekintzaile as entrepreneurship support, mostly funds established firms: at least 59 of 105 awards (2022–24) went to companies 4+ years old, incl. Sidenor, ITP, Fagor Ederlan, and the tech centres CEIT and Vicomtech. | research/public-funded-startups (startups_2022_2025.csv); fact F-0014 | medium | supported | for |
| C-037 | The rules keep people: tech-centre staff who leave to found have no reserved job (only a preferential right to a vacancy); public researchers' leave needs 5 years' seniority and is discretionary; UPV/EHU allows only part-time work in spin-offs; no document rewards a centre or a person for staff leaving to build. The Government's own plan lists "liberación - excedencias" as a gap. | research/talent §1 (rules.md); facts with claims=C-037 | medium (agreements for most centres not found) | supported | for |
| C-038 | The founder role in Basque centre spin-offs is designed to be filled from outside: BTV asks researchers for a 1-year CTO commitment for conditional equity and recruits the CEO later; 5 spin-offs have a confirmed externally hired founding CEO; only 4 of 188 have a founder/CEO publicly documented as staff of their own centre. | research/talent §1–2; facts with claims=C-038 | medium (floors; search-limited) | supported | for |
| C-039 | Where experienced staff are released, they found companies at about twice the base rate: ex-Nokia leavers founded startups at 23.7 per 1,000 vs 10.7 in a control group, and their startups grew faster (ETLA). ITRI targeted ~15% annual turnover. | research/talent §3; research/comparisons; facts with claims=C-039 | high (Nokia); low (ITRI, secondary) | supported | for |

## History

- 2026-10-23 — registry created from first research pass.
- 2026-10-23 — C-023 revised after stages v2 (pitches added); C-029, C-030 added.
- 2026-10-23 — Rule adopted: pitches counted apart from voice; C-023 back to supported.
- 2026-10-23 — C-031, C-032 added (public-funded startups pilot).
- 2026-10-23 — Spin-off table: C-014 corrected (earlier "one documented exit" was Tecnalia's own reporting; table finds 17 acquisitions across centres); C-016 verbatim; C-001 nuanced; C-033, C-034 added.
- 2026-10-23 — Active-check of 80 spin-offs: C-035 added; Bunt Planet corrected to acquired in spinoffs.csv (C-033 counts now 79 active / 18 acquired).
- 2026-10-23 — Trigger v2 (regional dailies only): C-024 reframed — institution-as-news is a Spanish pattern, stronger in Madrid's local press than in Euskadi's.
- 2026-10-23 — Census Ekintzaile 2022–2025 + Barne-Ekintzaile 2022–24 added: C-032 extended; C-036 added; facts F-0007–F-0014.
- 2026-10-23 — Talent line: C-028 tested (supported, medium); C-037, C-038, C-039 added; facts F-0015–F-0078.
- 2026-10-23 — Census of other programmes (822 entities): C-031 strengthened; facts F-0079–F-0084.
