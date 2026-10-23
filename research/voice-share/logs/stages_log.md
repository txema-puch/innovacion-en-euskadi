# Instrument B: stages log (v1, coded 2026-10-23)

Output: `stages.csv` (600 rows: one row per unique named speaker per event). Codebook: `codebook.md` (v1).
Raw pages that were read are saved under `web/`. Every row comes from one of those pages. Scripts: `inwink_extract.py`, `inwink_sessions.py` (South Summit inwink state blobs), `build.py` (assembles the CSV), `ss_codes.txt` (manual codes for South Summit Madrid, by row index).

## Results

| Region | Event | Edition | n | BUILDERS | INSTITUTIONS | INVESTOR |
|---|---|---|---|---|---|---|
| EUSKADI | B-Venture 2026 (El Correo) | 2026-04-21/22 | 43 | 7 (16%) | 11 (26%) | 4 |
| EUSKADI | South Summit Industry & Energy Bilbao-Bizkaia 2025 | 2025-11-26/27 | 24 | 8 (33%) | 8 (33%) | 1 |
| EUSKADI | BIND Demo Day 2026 (partial: no agenda) | 2026-07-02 | 2 | 0 | 1 | 0 |
| MADRID | South Summit Madrid 2026 (full speaker directory) | 2026-06-03/05 | 477 | 138 (29%) | 70 (15%) | 94 (20%) |
| BAYAREA | TechCrunch Disrupt 2025, Disrupt Stage | 2025-10-27/29 | 40 | 9 (22%) | 1 (2.5%) | 24 (60%) |
| BAYAREA | YC Startup School 2026 | 2026-07-25/26 | 14 | 8 (57%) | 1 (7%) | 0 |

Pooled by region (unweighted sum of the speakers coded):
- EUSKADI: n=69, BUILDERS 22%, INSTITUTIONS 29%. Excluding BIND: n=67, 22% vs 28%.
- MADRID: n=477, BUILDERS 29%, INSTITUTIONS 15%.
- BAYAREA: n=54, BUILDERS 31%, INSTITUTIONS 4%. INVESTOR is the largest group at 44%, and most of those are Battlefield judges.

Robustness splits:
- **South Summit Madrid by the site's own display tier** (`speakerorder` field: A is the headliners, Z is the end of the list).
  - Tier A (n=4): BUILDERS 100%, INSTITUTIONS 0%.
  - Tier B (n=54): BUILDERS 41%, INSTITUTIONS 4%.
  - Tier C (n=98): BUILDERS 41%, INSTITUTIONS 3%.
  - Tier D (n=284): BUILDERS 24%, INSTITUTIONS 17%.
  - Tier Z (n=33): BUILDERS 15%, INSTITUTIONS 45%.
  - Officials make up much of the full roster, but the organiser does not feature them.
- **South Summit Madrid without MCs and OTHER** (n=445): BUILDERS 31%, INSTITUTIONS 16%.
- **Disrupt Stage without Startup Battlefield judges** (n=18): BUILDERS 50%, INSTITUTIONS 6%, INVESTOR 17%.

### Who opens and closes each event

| Event | Opening | Closing |
|---|---|---|
| B-Venture 2026 | Welcome by Iñigo Barrenechea (El Correo, organiser), Javier Garcinuño (Bilbao Ekintza), Andoitz Korta (Basque Gov. viceconsejero) and Ainara Basurko (Diputación de Bizkaia). That is three of four PUBLIC_OFFICIAL. Inaugural keynote by Teresa Busto (Indra board). | "CIERRE" on both days, with no named speaker. The last named session is Guillermo Marco-Gardoqui (Grifols). |
| SS Industry & Energy Bilbao 2025 | Welcome by María Benjumea (South Summit) and Joseba Mariezkurrena (Diputación de Bizkaia, DG Emprendimiento). Day 2 opening remarks by Liz Fleming (South Summit). | Final Remarks by María Benjumea and Ainara Basurko (Diputada, Diputación de Bizkaia). The event is co-organised by the Diputación. |
| BIND Demo Day 2026 | Andoitz Korta (Basque Gov. viceconsejero), per the press release. | Not published. The event is a Basque Government programme. |
| South Summit Madrid 2026 | Official inauguration by Óscar López (Minister for Digital Transformation) on the Arena Stage. The opening was chaired by María Benjumea, and Lee Newman (IE dean) also spoke (IE press release 2026-06-03). | Isabel Díaz Ayuso (President, Comunidad de Madrid) closed and presented the Startup Competition awards. This comes from a single secondary source (ecosistemastartup.com) and she is not in the speaker directory, so she is not coded. King Felipe VI visited on Day 2 and is not coded either. |
| TC Disrupt 2025 | There is no welcome slot on the agenda. The first Disrupt Stage session is Startup Battlefield S1 (5 VC judges). Day 3 opens with SF Mayor Daniel Lurie, "Rebuilding the City that Builds Startups". | "Announcing the Winner of Startup Battlefield", with no named speaker. The last named speaker is Tristan Thompson. |
| YC Startup School 2026 | No running order is published on the event page. | Same: not published. |

## Event selection

The rule from the brief: the largest or most-cited recurring events whose purpose is the regional startup ecosystem, held 2025-10-01 → 2026-09-30, preferring events that publish an agenda or speaker list. Candidates were checked by web search and by fetching their pages.

### EUSKADI
1. **B-Venture 2026** (El Correo, Palacio Euskalduna, 21–22 Apr 2026). This is the largest recurring startup congress in the region (11th edition) and has a full published programme.
   - Source: https://www.b-venture.com/programa/
   - Note: the previous edition (20–21 Oct 2025) also falls inside the period. Only the latest edition is coded, to keep one edition per event.
2. **South Summit Industry & Energy Bilbao-Bizkaia 2025** (4th edition, B Accelerator Tower, 26–27 Nov 2025). Co-organised by South Summit and the Diputación Foral de Bizkaia. It has a structured session list and speaker directory (inwink).
   - Sources: https://www.southsummit.io/e/bilbao-bizkaia/sessions and https://www.southsummit.io/e/bilbao-bizkaia/speakers
   - All 24 speakers in the directory were coded, and each was joined to their sessions through speaker IDs.
3. **BIND Demo Day 2026** (BIND 4.0 / SPRI, BEC Barakaldo, 2 Jul 2026, 10th edition). This is the Basque Government's flagship open-innovation startup event.
   - **No agenda or speaker page was published** for 2026: bind.spri.eus only has an .ics file for 2026, and the agenda pages there are for 2024 and 2025.
   - The only two named people come from a pre-event press note and a post-event press release:
     - https://capital-riesgo.es/es/articles/el-gobierno-vasco-presentar-30-proyectos-de-colaboraci-n-entre-startups-de-todo-el-mundo-y-empresas-y-pymes-l-deres-de-euskadi-/
     - https://capital-riesgo.es/es/articles/el-gobierno-vasco-pone-en-marcha-la-11-convocatoria-de-bind-con-un-balance-de-10-millones-de-euros-en-contratos-entre-empresas-vascas-y-startups-en-la-ltima-d-cada-/
   - It is included only as an opening-address record. **Treat it as n/a for shares.**
   - The 2025 Demo Day (3 Jul 2025) is outside the period.

Rejected or failed for Euskadi:
- **Bilbao Slush'D:** last edition 20 Feb 2025, outside the period, and no speaker list was found.
- **South Summit Bilbao 2026:** 25–26 Nov 2026, after the period.
- **B Acceleration Week / Venture on the Road (BAT):** smaller, and no agenda was found.
- **Basque Startup Forum, Ekin Day, BBF:** no 2025–26 editions with agendas were found in search.

### MADRID
1. **South Summit Madrid 2026** (La Nave, 3–5 Jun 2026, 15th edition, co-organised with IE University). This is the region's dominant startup-ecosystem event.
   - Source: the full speaker directory, https://www.southsummit.io/e/madrid/speakers?page=1..17 (487 entries).
   - **Sampling rule: full census of the published directory**, not the main stage only. The agenda (sessions) loads client-side and could not be retrieved, so stage assignment is unknown and `session_type`=other for everyone except the 3 opening speakers.
   - Ten exact or near-exact duplicate entries were removed, leaving n=477. The removed pairs were: Pedro Duque ×2, Lisiane Lemos ×2, Bianca Dragomir ×2, Carlos Flores ×2, Nina Pfifer ×2, Raúl Sánchez ×2, Pablo Viguera ×2, Miguel Nigorra ×2, Jesús González Nieto ×2, and Javier González Navarro ×2 (Junta de Andalucía).

**Second Madrid event: not found.** None of the candidates qualified:
- **DES** (Digital Enterprise Show) moved to Málaga (9–11 Jun 2026), which is not Madrid, and it is an enterprise fair in any case.
- **Madrid Tech Week** (Comunidad de Madrid, first edition Oct–Nov 2025) is an umbrella over the Madrid Tech Show and Global Mobility Call trade fairs at IFEMA. Those are generic industry fairs, which the selection rule excludes, and no speaker list was found.
- **Madrid Innovation Week:** no such event was found.
- **Startup Olé** is held in Salamanca, not Madrid.
- **Horizon Deep Tech Summit** (La Nave) is niche. Its 2026 edition (10–12 Nov) falls after the period, and its site mixes speakers from past editions.
- **MERGE Madrid** is a crypto conference.

Madrid therefore rests on one event, but that event is a 477-speaker census.

### BAYAREA
1. **TechCrunch Disrupt 2025** (Moscone West, 27–29 Oct 2025). This is the largest recurring startup conference in SF.
   - The live agenda URL now redirects to Disrupt 2026 (13–15 Oct 2026, after the period), so the agenda came from a Wayback snapshot taken 2025-10-24, three days before the event: https://web.archive.org/web/20251024071906/https://techcrunch.com/events/tc-disrupt-2025/agenda/
   - **Sampling rule: every named speaker in every Disrupt Stage (main stage) session**: 23 sessions, 40 unique people.
   - Kevin Rose appears twice and is coded once. Roy Lee is named only in a session title. Two sessions (the winner announcement and the Equity podcast) have no named speakers.
   - The other five stages, roundtables and breakouts were not coded.
2. **Y Combinator Startup School 2026** (San Francisco, 25–26 Jul 2026; a successor to the June 2025 "AI Startup School"). This is the canonical founder-ecosystem event.
   - Source: https://events.ycombinator.com/startup-school-2026, which lists 14 speakers (data embedded in the page). All were coded.
   - No session schedule is published, so `session_type`=other.

Rejected or failed for the Bay Area:
- **SF Tech Week** (Oct 2025) is a festival of hundreds of independent side events with no single stage, so it cannot be coded.
- **Startup Grind Conference 2026** (Fox Theatre, Redwood City, 28–29 Apr 2026) would have been the third event. The live site now shows the 2027 edition and a speaker archive that mixes years, and the Wayback Machine was offline ("Temporarily Offline") on two attempts, so it was not coded.
  - The live site does state that the 2026 welcome was given by Amanda Anthony, Economic Development Manager for the City of Redwood City. That is an institutional opening, but at a city-staff level.
- **SaaStr AI Annual 2026** (San Mateo, May 2026) is a B2B SaaS industry conference rather than an ecosystem event, and its speaker pages were still "being finalized".
- **Dreamforce** is excluded by the brief.

## Unnamed stage time (not coded)

The unit is a named speaker, so these are excluded. They all add builder stage time, which means **the CSV understates BUILDERS** for the pitch-heavy events.
- **B-Venture 2026:** 4 pitch blocks on day 1 (24 startup slots, e.g. Akshar Innovation, Dreamshot, Mikrobiomik, Neety, SAMIRA DTx; "BlaBlaNote" is listed twice) and BIC Startup Day (Argit AI, Aidtec Solutions, Polemann, Bikaine). Presenters are not named.
- **SS Bilbao 2025:** three "Meet the Startups" pitch sessions (Industry 4.0, Energy Transition, Mobility) with no named presenters. The press reports 23 startups.
- **BIND Demo Day 2026:** 30 startup–company projects presented, with no named presenters.
- **TC Disrupt 2025:** 4 Startup Battlefield sessions plus the final on the Disrupt Stage. The pitching founders are not named on the agenda.

## Coding conventions and ambiguous calls (details in `notes`)

- **Builder roles:**
  - A CEO of a startup or scale-up whose card does not say "founder" is coded STARTUP_EMP. This affects BUILDERS totals only through the founder/employee split.
  - The four B-Venture "B Founders Club" panellists are coded FOUNDER because of the panel's framing, even though their cards say CEO.
  - Founders of firms older than 15 years who appear as founders (Globant, Box, NVIDIA, Virtualware, ECOALF) are coded FOUNDER, following the codebook clause about founders appearing as founders.
- **Investors:**
  - Co-founders of VC firms (Samaipata, Breega, FJ Labs, 2150, Plus Partners, Shapers, Zigzag, Satgana, Encomenda) are coded INVESTOR, not FOUNDER.
  - Corporate VC (Wayra, Repsol CV, TDK Ventures, Mondragon Ventures) is coded INVESTOR.
- **Public bodies:**
  - Public finance and VC vehicles are coded PUBLIC_OFFICIAL: ENISA, CDTI, AXIS/ICO, COFIDES, EIB, EIF, KfW Capital, CDP Venture Capital, Seed Capital Bizkaia/Crowdfunding Bizkaia.
  - Investment-promotion agencies are coded PUBLIC_OFFICIAL: ICEX, Invest in Madrid, InvestHK, Uruguay XXI, InvestRS.
  - BEAZ, SPRI and Bilbao Ekintza are coded PUBLIC_OFFICIAL.
  - Correos (a state-owned company) is coded PUBLIC_OFFICIAL.
  - An opposition-party official (PP) is coded PUBLIC_OFFICIAL.
- **PUBLIC_ADJACENT:** EIT bodies (EIT Food, EIT Manufacturing, 28DIGITAL), public-university management (UPM, UCM, Nova UCD, Oxford EnSpire), public BICs (CEEI Asturias), BSC, Tecnalia Ventures, Mobile World Capital, London & Partners, Bizkaia Talent, Basque Culinary Center/GOe, CITET, and Eureka.
- **Clusters and employer associations** (Basquefik, Aclima, AFM, Functional Print, CEBEK, TEDAE) are coded PRIVATE_ECOSYSTEM. They are arguably PUBLIC_ADJACENT, because Basque clusters are largely publicly funded. If recoded, Euskadi's INSTITUTIONS share rises by about 7 points (5 of the 67 speakers outside BIND), from 28% to about 36%.
- **IE University** (private, co-organiser of South Summit): executives are coded PRIVATE_ECOSYSTEM and deans/professors ACADEMIC.
  - Enrico Letta is coded ACADEMIC (a former Italian PM, appearing as an IE dean).
  - Carme Artigas is coded ACADEMIC (a former Spanish Secretary of State, appearing as a Harvard fellow).
- **ONCE / Fundación ONCE** (a social public-law corporation) is coded OTHER.
- **Organisers, MCs and media** are coded PRIVATE_ECOSYSTEM. South Summit staff and MCs make up about 20 of the 477 Madrid speakers.
- **Large-company subsidiaries:** Waymo, X and Meta executives are coded CORPORATE, even where the person is a known founder (Alexandr Wang).

## Limitations

1. **The sampling frames differ between events.** Madrid is a full directory census of 477, which includes the long tail of regional officials from all over Spain and LatAm. Disrupt is main-stage only. B-Venture is a full programme. YC is a short headliner list. Shares are not strictly comparable across regions, because a main-stage-only rule favours headline builders and VCs, as the South Summit tier split shows.
2. **Euskadi has no third valid event.** BIND has no agenda, so the region rests on 67 named speakers from two events, one of them co-organised by the Diputación.
3. **Directory and agenda ≠ actual stage.** Pre-event agendas (the Disrupt snapshot from 3 days before the event, the YC page) may differ from what was delivered. VIP drop-ins are not on the agendas: Ayuso's closing and the King's visit at South Summit are not coded.
4. **Pitch time is excluded.** Unnamed pitching founders are not counted, which understates BUILDERS, most of all at B-Venture, SS Bilbao and BIND.
5. **Categories come from page text,** meaning the job title and organisation on each card, plus light outside knowledge (company age, whether a firm is a VC). Around 15 rows have an unverified organisation type and are flagged in `notes`. Most of those are OTHER or STARTUP_EMP.
6. **Coding was done by one coder** (this agent), with no inter-rater check.
