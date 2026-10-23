# Press voice-share: EUSKADI, coding log

Instrument A (press). Period 2025-10-01 → 2026-09-30. Coded 2026-10-23 against codebook v1.
Output: `press_euskadi.csv` (51 articles, 92 rows, 79 named speakers; 13 articles have no named speaker and appear as one `NONE` row each).

Working files (all in `voice/raw_eus/`): `candidates.tsv` (every search hit, in the order returned, with rank), `pages/` (raw HTML as fetched), `txt/` (extracted text), `rows.psv` (coding scratch, which also holds the coded articles later dropped by the per-month cap). Tools are in `voice/tools_eus/`.

## 1. Search method and the queries used

**Search engine.** Google News RSS search (`news.google.com/rss/search`, hl=es, gl=ES), with `after:/before:` date operators per calendar month. I used it because the WebSearch tool refuses elcorreo.com, diariovasco.com and expansion.com, and its results ignored month targeting. Google News links were decoded to publisher URLs through Google's batchexecute endpoint. Results were then filtered to the target outlets: elcorreo, diariovasco, deia, noticiasdegipuzkoa, elreferente, expansion, capital-riesgo, cincodias.

**Fixed queries.** Each one ran for each of the 12 months, so 60 query runs in total. The `after:/before:` window was appended to each query.
1. `startup vasca`
2. `startups Euskadi`
3. `emprendimiento Euskadi`
4. `ronda de financiación startup Bilbao OR Donostia OR Vitoria`
5. `ecosistema startup País Vasco`

The queries were run without quotes. A quoted test of `"startup vasca"` for Oct 2025 returned only 6 hits in total.

**Month windows.** 2025-10-01..2025-11-01, 2025-11-01..12-01, 12-01..2026-01-01, 01..02, 02..03, 03..04, 04..05, 05..06, 06..07, 07..08, 08..09, 09..2026-10-01.

**Exploratory WebSearch queries.** These ran before the switch to Google News. None of their results were used for sampling.
- `"startup vasca" octubre 2025`
- `startups Euskadi noviembre 2025`
- `emprendimiento Euskadi diciembre 2025`
- `ronda de financiación startup Bilbao enero 2026`
- `startup vasca ronda de financiación` (outlet-restricted; refused)
- `startups Euskadi 2026` (elreferente.es)
- `startup vasca ronda 2026` (capital-riesgo.es)
- `emprendimiento Euskadi startups 2025` (deia/ndg)
- The same first four queries again, restricted to deia, ndg, elreferente, capital-riesgo and cincodias.

**Candidate pool.** 144 outlet-filtered hits, including duplicates across queries.

## 2. Selection rule

1. Go through each month window in the order Google returned results: query 1 ranks first, then query 2, and so on.
2. Drop duplicates, keeping the first appearance.
3. Screen for inclusion: the article must be primarily about Basque startups, entrepreneurship or the ecosystem.
4. Take eligible articles until the month reaches **5**.

The cap of 5 per month exists to spread the sample across the year and stop May, July and September from dominating. It gave 51 articles.

Articles are assigned to the month window that returned them. Three articles have a page date in the previous month (Google dated them a few days or weeks later):
- c12 ScrapAd: page dated 2025-12-01, Nov window
- c117 Multiverse unicorn: page dated 2026-07-27, Aug window
- c125 BAT feature: page dated 2026-07-27, Aug window

The CSV `date` column is always the page's own publication date. As a result, by-date counts give 7 articles in July and 3 in August, while by-window counts give 5 each.

**Articles per window.** Oct 5, Nov 5, Dec 3, Jan 3, Feb 3, Mar 3, Apr 5, May 5, Jun 4, Jul 5, Aug 5, Sep 5. Dec, Jan, Feb and Mar had only 3 eligible hits each. Every month meets the ≥3 target.

**Outlet mix.** El Diario Vasco 17, El Correo 12, Deia 7, Capital-Riesgo.es 6, Expansión (País Vasco) 4, Cinco Días 2, Noticias de Gipuzkoa 2, El Referente 1.

## 3. Read and excluded on inclusion grounds

| cand | outlet | why excluded |
|---|---|---|
| 19 | El Correo (content-local) | sponsored forestry project (Baskegur/Prisma), not startup ecosystem |
| 37 | Diario Vasco | Tecnalia lab opening: a technology-centre facility story |
| 46 | El Referente (via Wayback) | CHEMCYCLE: a corporate R&D consortium led by Tradebe, no startup |
| 53 | Diario Vasco | Sánchez's industry-congress speech; Multiverse is one mention among many |
| 61 | Diario Vasco | IBM quantum computer use by Gipuzkoa companies; corporate/infrastructure |
| 83 | Diario Vasco | Donostia native working at a San Francisco startup; not a Basque startup |
| 100 | Diario Vasco | Citring: a Barcelona/Valencia startup, not Basque |

## 4. Excluded by title without reading

These were clearly outside scope:
- **Corporate, tax, labour or strike stories:** 2, 4/8, 15, 29, 30, 40, 41, 49, 51, 62, 119, 122, 123, 139, 140
- **Other regions:** 20 Qida (Catalonia), 44 Roka Furadada (Catalonia), 104 Las Rozas, 115 Andalucía, 116 Galicia
- **Spain-wide lists or rankings:** 11/24, 14/21/26/34, 35, 45, 50 (Quantonation's French fund), 95, 96
- **Op-ed or editorial:** 42 (tribuna abierta), 120 (DV editorial)
- **Other non-startup topics:** 43 (vocational training), 55 (rural depopulation), 56 (self-employed statistics), 89, 92 (social economy supplement), 91 (migrant workers), 138 (franchising)

## 5. Eligible but beyond the cap

These were not in the CSV. Some were coded before the cap was applied, and those codes stay in `rows.psv` only.
- **Oct:** 9 Nymiz (coded, no speakers), 10 A4Radar/BIND (El Referente 403, not read)
- **Apr:** 72 B-Venture 'B Founders Club' panel (coded: 4 CEOs), 73, 75, 76
- **May:** 84, 85, 86, 87, 93 (coded), 97, 98
- **Jul:** 113 (Durango music programme; duplicate story of 110)
- **Sep:** 131, 132, 133, 134, 135, 137, 141, 142, 143, 144 (131 coded)

## 6. Skipped and failed URLs

- **El Correo, Diario Vasco, Expansión:** WebSearch and WebFetch refuse these domains. They were fetched instead with `curl` and a browser user-agent, and all returned the full article body in the HTML. Expansión pages report `<title>404 Not Found</title>` but carry the full article.
- **Deia:** WebFetch returned 406; curl worked.
- **El Referente (elreferente.es):** returned 403 to curl and WebFetch. c46 and c78 were read through Wayback Machine snapshots (20260128, 20260508). c10, c75 and c144 were not fetched (beyond the cap).
- **Cinco Días:** WebFetch is refused, and curl with a default UA returned 403. Curl with full browser headers worked. The text was read from the page's `articleBody` JSON (c27, c38).
- **No in-scope page failed to load.** Every article in the CSV was read in full from the fetched page.

## 7. Judgement calls

**Startup organisations in `headline_actor`.** The codebook categories describe people. A startup named in the headline was coded `FOUNDER`, a government or agency `PUBLIC_OFFICIAL`, and a BIC or Mubil `PUBLIC_ADJACENT`. Generic aggregates such as "emprendedores vascos" or "las tecnológicas vascas" were coded `NONE`.

**CEOs whose founder status isn't stated.** These were coded `STARTUP_EMP`: Bideroad (Viudez), Glycoscience (Guardia) and Photokrete (María Saiz). The four CEOs on the B-Venture "B Founders Club" panel (c72, capped out) were coded `FOUNDER` because of the panel's framing.

**Joint attributions.** When a quote is attributed to "los fundadores" or "el equipo fundador" and the founders are named, each named founder was coded:
- Clodei: Garmendia
- Neety: Arambarri, Galarza, Olaizola
- QUBIZ: de la Herrán, García de Arco
- Profesiolan: J. and A. Hospital

This inflates the builder count by up to 8 speakers. See the strict variant in section 8.

**Officials presented as announcing but not quoted.**
- c36 Expansión: Pradales, Jauregi and d'Anjou are named only in the photo caption "en la presentación". Coded `PUBLIC_OFFICIAL`, with a note.
- c85 (capped out): Korta and de Ariño "participated in the official act". Coded the same way.
- c130: the keynote speaker Lizaso was coded. About 60 attendees named only in photo captions were not coded.

**Incidental quotes.** These were coded because the rule is "anyone quoted":
- c5: physicist Scott Aaronson, in the lede (`ACADEMIC`)
- c118: VW CEO Oliver Blume, in the lede (`CORPORATE`)

Both make the article's `lead_voice` a non-ecosystem actor.

**Category calls.**
- Basque Health Cluster: `PRIVATE_ECOSYSTEM`. It is a publicly co-funded association.
- BAT B Accelerator Tower: `PUBLIC_ADJACENT`, as a Diputación de Bizkaia-promoted space. It could also be `PRIVATE_ECOSYSTEM`.
- Mubil's director-general: `PUBLIC_ADJACENT`.
- Beaz staff: `PUBLIC_OFFICIAL`.
- Rural Kutxa and Ormazabal executives: `CORPORATE`.
- Observatorio Vasco de Emprendimiento president (María Saiz, c7): `ACADEMIC`. It is a university consortium; `PUBLIC_ADJACENT` is also defensible.
- Photokrete's scientist Jorge Dolado: `ACADEMIC`. His founder status isn't stated.

**Company age.** Oncomatryx (c63) and Virualware (c72) are older than 15 years. Laureano Simón was still coded `FOUNDER` because he appears as the founder.

**Triggers.**
- Public grants or state equity in a startup round count as `STARTUP_NEWS`: c38 Lookiero/SETT, c126 Battia/IDAE, c84 (capped out).
- Mixed public-private awards and programmes count as `PRIVATE_ECOSYSTEM`, because a private actor led them: c65 EmprendeXXI (CaixaBank and ENISA), c70 (an SPRI-run BIC session inside B-Venture).
- Joint Scoutyn and Basque Government reports count as `PRIVATE_ECOSYSTEM`: c99, c86.
- c108 (SmartOps winning Ormazabal's BEAZ-backed BIOK challenge) counts as `STARTUP_NEWS` (a customer win).
- Research reports and features count as `OTHER`: c7 GEM, c121, c125, c129.

**Borderline inclusions.** These were kept because the codebook says "startup/entrepreneurship":
- c103: senior entrepreneurship
- c109: young farmers (the Gaztenek programme)
- c110: a music-entrepreneurship programme
- c129: buying SMEs with no successor
- c71: an IESE award for the founder of a consultancy hub

c129 also produced two `OTHER` speakers: a retired SME seller and an entrepreneur who bought an existing SME.

**PR flag (`pr=yes`, 8 articles).**
- Capital-Riesgo.es items that are visibly institutional or company releases: c18, c31, c99, c101, c105, c107.
- c3 Runmatch, labelled "Content Service elaborado por SRB Ediciones" (sponsored).
- c17 Deia, bylined with the Diputación Foral de Bizkaia.

Several other bylined pieces read close to releases (c93 Neety, c124 BIME, c128 Europa Press). They were left `pr=no`, with notes.

## 8. Results (speaker level unless stated)

**Speakers (79):**

| Category | Count |
|---|---|
| FOUNDER | 31 |
| PUBLIC_OFFICIAL | 15 |
| PRIVATE_ECOSYSTEM | 9 |
| CORPORATE | 7 |
| INVESTOR | 5 |
| ACADEMIC | 4 |
| STARTUP_EMP | 4 |
| PUBLIC_ADJACENT | 2 |
| OTHER | 2 |

**Group shares:**
- BUILDERS: 35/79 = **44.3%**
- INSTITUTIONS: 17/79 = **21.5%**
- Strict variant (drop joint-attributed co-founders and officials who were not quoted): builders 27/68 = 39.7%, institutions 14/68 = 20.6%
- Excluding `pr=yes` articles: builders 33/67 = 49.3%, institutions 14/67 = 20.9%
- Article-weighted, over the 38 articles with speakers: builders 48.0%, institutions 23.8%

**Article level (51):**
- Articles with at least one builder voice: 23. Articles with at least one institutional voice: 12. Articles with no named speaker: 13.
- `trigger`: STARTUP_NEWS 24, PRIVATE_ECOSYSTEM 14, PUBLIC_ANNOUNCEMENT 9, OTHER 4
- `lead_voice`: FOUNDER 14, NONE 13, PUBLIC_OFFICIAL 9, PRIVATE_ECOSYSTEM 5, ACADEMIC 4, STARTUP_EMP 3, CORPORATE 2, OTHER 1
- `headline_actor`: FOUNDER 28, NONE 8, PUBLIC_OFFICIAL 7, PRIVATE_ECOSYSTEM 4, CORPORATE 2, PUBLIC_ADJACENT 2

## 9. Limitations

1. **Multiverse Computing dominates.** It is in 9 headlines (about 18% of articles) and accounts for 6 speakers. Diario Vasco covers it heavily: all 3 Feb articles in the sample are about Multiverse. The builder share therefore partly reflects one outlier company rather than the ecosystem.
2. **The sampling frame is Google News relevance ranking, not each outlet's archive.** Coverage depends on Google's indexing (Diario Vasco and El Correo are well indexed, El Referente barely). Ranking is opaque, so "take results in the order returned" inherits Google's bias toward big stories. Expansión and Cinco Días return many non-startup corporate items that were screened out.
3. **Institutional press releases are under-sampled.** Capital-Riesgo.es and El Referente republish Basque Government, SPRI and BerriUp releases, and El Referente was mostly unreachable. Releases carry institutional voices at a higher rate, so the institutional share here is plausibly a lower bound. Basque-language outlets (Berria) and radio and TV (EITB) were outside the outlet list.
4. **Inclusion is a judgement call.** The startup vs general entrepreneurship boundary, plus speaker-counting rules (joint founder quotes, officials in captions), move the builder share by about ±5 points (39.7% to 49.3% across the variants above). The 13 articles with no named speaker carry no voice at all. That is about a quarter of coverage, mostly institutional-programme and data stories.
5. **Single coder, no inter-rater check.** About 1 in 5 articles needed a judgement call, and every one is logged in the `notes` column.
