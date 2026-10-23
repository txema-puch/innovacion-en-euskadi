# Open gaps

What is still missing, why, and how to close it. Pick up from here in any session. When you close a gap, update the research README, `facts.csv` and `claims.md`, then strike the item here with the date and commit.

**Why so many gaps on 2026-10-23:** the first research pass ran ~20 agents in parallel in one session and used up the session's web-search allowance partway through. After that, agents could only fetch known URLs (registers, company sites, PDFs, bulletins), so anything that needed *discovery* (funding rounds, founder backgrounds, news, alumni) is thin. Close these with **one focused run per gap**, not a fan-out, in a session with search available.

Rules for gap work: same as the repo (README "Hard rules"). Don't get around search limits by scripting Google/DuckDuckGo or by using a logged-in browser. Read-only use of the user's Chrome is fine for pages that block automated fetching, with no logins, forms or paywall bypasses. LinkedIn: no scraping, no logged-in session.

Legend: **S** = needs web search · **P** = needs a paid source or a transparency request · **M** = manual/browser work, no search needed.

## Priority 1: gaps that weaken a published claim

| # | Gap | Claims | Type | How to close |
|---|---|---|---|---|
| 1 | **UP! Euskadi definition of "public capital in rounds":** does it include public loans (ENISA, CDTI, convertibles)? | C-010 | S/P | Find UP! Euskadi / Dealroom methodology; else ask SPRI. If loans are included, recompute the equity-only share. |
| 2 | **PCTI Euskadi 2030 indicators and monitoring reports** (URLs returned 404). Do they include any outcome or people indicator? | C-028, C-005 | S | Find the current PCTI 2030 PDF and the annual "informe de seguimiento"; record indicators as input/output/outcome. |
| 3 | **Human second coder** for the press data (the AI second coder agreed with the first almost perfectly, which is an upper bound). | C-021–C-024 | M | Give a person `research/voice-share/codebook.md` + 20 articles from `reliability/sample.csv`; compute kappa with `compare.py` logic. |
| 4 | **Emaitek spin-off criterion:** in 2018 centres were paid partly on spin-off revenue (OECD case study); the 2026 scorecard doesn't list it. Dropped, or folded into "industrial impact"? | C-001 | S/P | Read Emaitek Industria Hobea 2025/2026 bases (BOPV) indicator annex; else ask BRTA/SPRI. |
| 5 | **Euskadi press behind paywalls:** 63 El Correo / Diario Vasco premium articles unread in trigger v2 (headlines suggest ~32% institution-news vs 25% measured). | C-024 | M/P | Read with a legitimate subscription, or code headline-only with a stated rule. Don't use AMP or other paywall workarounds. |

## Priority 2: outcome data for the company tables

| # | Gap | Where | Type | How to close |
|---|---|---|---|---|
| 6 | **Funding rounds** (amount, lead, date) for Ekintzaile companies 2021–2025 and for centre spin-offs; currently only capital increases as a proxy. | `public-funded-startups/*.csv`, `tech-centres/spinoffs.csv` | S | One run per cohort: El Referente, press, Crunchbase public pages; record lead investor public/private. |
| 7 | **Exact revenue and headcount** for survivors (only infoempresa ranges, which look modelled). | same | P | Registry annual accounts (~€10/company/year), starting with the top outcomes and the "growing" group. |
| 8 | **47 unknown-status spin-offs** (mostly bare names from the 2008 Corporación Tecnalia list and BTV projects with no registered company). | `tech-centres/spinoffs.csv` | M/S | Match names to CIFs (empresia, BORME); for BTV projects, check incorporation. |
| 9 | **Attribution doubts:** Kaizen Play (foreign parent, Ikerlan link unclear), Biolan (Tekniker vs Tecnalia), SIAPS (Lortek vs SIAWELD), Nuavis (Vicomtech link only via Crunchbase snippet). | `tech-centres/` | S/M | Confirm from centre pages/press; fix rows with a history note. |
| 10 | **Orbik's acts in the Basque cooperative registry** (it became a mixed cooperative in 2024). | `tech-centres/active-check/` | M | Basque cooperative registry lookup. |
| 11 | **Census 2015–2020 and other programmes:** Ekintzaile 2015–2020 lists, Diputaciones' programmes, BIND 4.0 startups, public VC portfolios (GCR: Basque Fondo, Ekintzaile fund, BasketekVenture, Hazten; Seed Capital Bizkaia). | `public-funded-startups/` | M/P | In progress on 2026-10-23 (agent "registry3"). Whatever isn't public goes into the transparency request (#20). |
| 12 | **Ekintzaile+** (21 companies, up to €100k each) not covered. | `public-funded-startups/` | M | BOPV 2603646a and earlier years. |
| 13 | **Basque Tek Ventures:** fund size, full company list, amounts, status after Jan 2025. | `tech-centres/` | P/S | Transparency request to SPRI/GCR; press. |

## Priority 3: talent line

| # | Gap | Claims | Type | How to close |
|---|---|---|---|---|
| 14 | **Alumni founders, counted from the startup side:** start from startups (incl. outside Euskadi: Madrid, Barcelona, abroad) and trace founders back to Basque centres; current counts are floors from centre pages. | C-028, C-038 | S | Method in `research/talent/method_alumni.md`; public founder bios and press only. |
| 15 | **Collective agreements / internal rules** for Tecnalia, CEIT, Ikerlan, Vicomtech, CICs (only Tekniker's found). | C-037 | S/M | REGCON (national agreements registry), BOB/BOG/BOTHA bulletins; centre transparency portals. |
| 16 | **Tecnalia non-financial reports (EINF):** probably publish staff turnover. | C-028 | S | Tecnalia website / Registro Mercantil deposits. |
| 17 | **Ikerbasque researcher terms; Basque (foral) tax treatment of employee stock options.** | C-037 | S | Ikerbasque calls; Normas Forales IRPF of the three territories. |
| 18 | **ITRI primary figures** (turnover, alumni) to replace the secondary source. | C-039 | S | ITRI annual reports / Taiwanese government sources. |

## Priority 4: voice share and context

| # | Gap | Type | How to close |
|---|---|---|---|
| 19 | **Founder-led contrast event:** the Bilbao SpaceXAI community event (Oct 2026, ~100 people) needs its public page/agenda to be coded alongside the institutional events. | M | Get the luma/event page from Txema; code with `codebook.md`. |
| 20 | **Transparency request** to SPRI, GCR and the three Diputaciones: beneficiary lists 2015–2020, public VC portfolios with amounts, outcome tracking (if any), Emaitek indicator weights, alumni tracking at centres. A refusal or non-answer is itself a fact (type `absence`). | P | Draft under Ley 19/2013 and the Basque transparency law; log the request date and reply. |
| 21 | Stage coverage: SS Bilbao sponsor list; South Summit Madrid finalists' names; more non-Bizkaia Basque events. | S/M | Event sites, press. |
| 22 | OECD 2011 *Review of Regional Innovation: Basque Country* (text not accessed). | S | OECD iLibrary. |
| 23 | Basque founders who built companies outside Euskadi (the talent that did leave). | S | Press, founder bios; feeds #14. |
