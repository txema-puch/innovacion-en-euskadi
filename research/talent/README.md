# Talent: does the system turn trained people into builders, or keep them?

**Question.** Basque tech centres, CICs/BERCs and universities train thousands of researchers and engineers. Does the system turn them into founders and startup builders, or keep them?

**Position (not a finding):** talent leaving to build is an output, not a leak. A centre that cared about impact would measure how many of its alumni found companies or lead tech at startups.

**Short answer from the evidence so far:** the rules keep people, the founder role is designed to be filled from outside, and nobody measures alumni outcomes. All numbers on alumni are *floors*: the session's web-search budget ran out, so counts are the minimum publicly documented, not estimates.

Facts behind every number: `../../facts.csv` (filter `claims` = C-028, C-037, C-038, C-039; F-0015–F-0078).

## 1. Rules and incentives (`rules.md`: verbatim quotes, articles, pages)

- **Tech-centre staff have no guaranteed way back.** Centres are private foundations, so their staff fall under general labour law, not the Science Law's researcher provisions (Ley 14/2011 art. 12 covers only public universities and public research bodies). Voluntary leave runs 4 months to 5 years, but the worker "conserva solo un derecho preferente al reingreso en las vacantes" (Estatuto de los Trabajadores art. 46.5).
- **Tekniker's collective agreement 2023-24, art. 13:** a reserved job only for family reasons/short study (≤6 months) or training "que con posterioridad puedan ser incorporados a la propia empresa" (≤1 year), each capped at 2% of staff. No clause on spin-offs, equity or staff inventions. (Read via a wageindicator.org mirror; the official bulletin returned errors.)
- **No published agreement or spin-off/staff regulation found** for Tecnalia, CEIT, Ikerlan, Vicomtech or the CICs (partial absence: registries not fully searched).
- **Public researchers (Science Law as amended by Ley 17/2022):** art. 17.4 allows up to 5 years' leave to join a private company with a reserved job, but needs "una antigüedad mínima de cinco años" and "se subordinará a las necesidades del servicio"; silence counts as refusal. Art. 18: part-time only in companies "creadas o participadas por la entidad". Art. 17.7 leaves the conditions to each region: **no Basque rule found**.
- **UPV/EHU:** new company-creation regulation (BOPV 23-06-2026) allows only part-time work in a spin-off ("mediante un contrato de trabajo a tiempo parcial", art. 14.1), with two governing-body approvals; nothing on leave, founder equity or reward. Its own consultation document (Nov 2025, p.5): "En ningún caso la UPV/EHU participa en el capital social de estas spin-offs", and calls the 10% cap and board ban "un claro efecto desincentivador".
- **Basque Tek Ventures (both calls, p.6–7):** "Incorporación del CTO a la startup o dedicación del equipo investigador … durante al menos 1 año … (a cambio del equity)"; the team's stake is "participación significativa en función del grado de consecución de los hitos fijados" (centre <50%, BTV <40%). Founder talent is searched for later (Phase 5); Dec 2023 CEO searches asked for "a partir de 30 años" and sales experience. Nothing on the researcher's employment status during that year.
- **The government's own plan names the gap:** PIE 2025-28 (printed p.27) lists "liberación - excedencias … participación en propiedad de spin-offs" as things to promote.
- **What BRTA says it wants:** 2019: "la transferencia de investigadores a la industria" is part of its talent remit. 2023 report: "debemos crear las condiciones para mantenerlos".
- **Contrast, Fraunhofer:** pays institutes a spin-off premium to compensate for "den Verlust von Know-how, der durch den Weggang von Mitarbeitenden in eine Ausgründung entsteht", and allows founders part-time work up to 2 years / leave up to 3 years (Bundestag 19/30834, medium confidence).

## 2. Alumni count (`method_alumni.md` written before counting; `alumni_startups.csv`, `founders_public.csv`, `founder_origins.csv`)

| Centre | Alumni-linked startups found | People | Companies |
|---|---|---|---|
| Tecnalia | 2 | 2 | FESIA, GO4IT |
| CEIT | 0 | 0 | No founder of any CEIT spin-off named in any source reached (1996–today) |
| Ikerlan | 1 | 1 | Orbik |
| Vicomtech | 2 | 3 | Emaia Health; Nuavis (low confidence) |

- 4 of these 5 are formal spin-offs. Across all centres, 12 startups with publicly named centre staff/alumni founders; 11 formal spin-offs; **0 found outside Euskadi**. That reflects the method (discovery started from Basque centre pages): it is not evidence that alumni stay.
- **Reverse check, where founders came from:**
  - 188 centre spin-offs: 50 checked against a source → 18 centre, 14 industry (corporate JVs coded industry), 1 university, 17 unknown. Only **4 of 188** have a named founder/CEO publicly documented as staff of the spin-off's own centre (FESIA, GO4IT, Orbik, Prospect Biotech).
  - **5 have a confirmed externally hired founding CEO** (Battbelt, LTK Cryosolutions, Taldeki, Protellix, H2SITE). With BTV and BeAble budgeting for CEO recruitment, the outside CEO looks built into recent spin-offs.
  - Ekintzaile 2021 (65 companies): of 15 with a known founder origin, 2 centre, 3 university, 10 industry. No founder publicly described as ex-Tecnalia, CEIT, Ikerlan or Vicomtech.
- Per-person rows (`founders_public.csv`, 33) only for people whose origin is publicly stated, with the URL. Everything else stays in `raw/` (gitignored).

## 3. Benchmarks (`benchmarks.md`)

| Benchmark | Figure | Source quality |
|---|---|---|
| Ex-Nokia leavers 2008–14 (ETLA Brief 158, Statistics Finland data) | 530 of 22,344 became startup founders vs 256 of 24,006 in the control group: **23.7 vs 10.7 per 1,000** | Primary |
| Ex-Nokia, any entrepreneurial status | 8.27% vs 4.96% | Primary |
| Ex-Nokia startups | revenue grew 16% faster; 50% faster if the founder had an innovation role; lower survival | Primary |
| ITRI | target 15% staff turnover/year; ~85% of leavers to Taiwanese firms; ~40% of Hsinchu managers ex-ITRI by late 1990s | Secondary only, low |
| Fraunhofer | 1.57 spin-offs per 1,000 staff (2.8 per 1,000 scientific staff); 2,965 people in surviving spin-offs (2018) | Primary (Bundestag 19/14361) |

No people-based figure found for VTT, imec, TNO or EARTO studies.

## 4. Does anyone measure it? (`measurement.md`)

No. BRTA annual reports 2022–24: staff, PhDs, theses, publications, patents; nothing on leavers, moves to industry or alumni founders. PIE 2025-28 panel: 25 indicators, none on people; the only knowledge-centre indicator counts spin-offs (19 in 2023; 2024 "En construcción"). Tecnalia, CEIT and AZTI reports and the Ministry of Science evaluation: nothing. UPV/EHU's new registry tracks companies, not people. Ikerbasque counts 41 spin-offs its 402 researchers took part in: companies, not people.

## Caveats

- Web search ran out early for both agents: alumni counts are floors. elreferente.es, crunchbase.com and the Wayback Machine were unreachable; LinkedIn was not used.
- Results lean towards formal spin-offs (what centres publicise); founders of 1996–2010 spin-offs and startups abroad are hard to trace.
- Single coder, no second check.

## Open questions

- PCTI Euskadi 2030 indicators and monitoring reports (URLs 404 at the time): the main open item for C-028.
- Tecnalia's non-financial (EINF) reports probably publish staff turnover.
- Ikerbasque researcher terms; Basque (foral) tax treatment of employee stock options.
- Re-run alumni discovery with search available, starting from startups (outside Euskadi too) rather than from centre pages.
- Ask the centres directly whether they track alumni (transparency request).
