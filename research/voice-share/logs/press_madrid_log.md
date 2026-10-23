# Press coding log: MADRID (Instrument A)

Coded 2026-10-23. Period 2025-10-01 → 2026-09-30. Output: `press_madrid.csv` (50 articles, 86 rows, 75 named speakers).

## Search method

The search engine was Google News RSS (`news.google.com/rss/search`, hl=es, gl=ES), with each query run separately for each calendar month using `after:YYYY-MM-01 before:YYYY-MM+1-01`. Results came back in Google's order. I kept only items whose source was on the outlet list: El Referente, Expansión, Cinco Días, El Confidencial, El Economista, Telemadrid, El Mundo, Madridiario and Capital-Riesgo.es. I did not see any Madridiario item in the primary results.

**Primary queries (5 × 12 months):**
1. `"startup madrileña"`
2. `"startups Madrid"`
3. `"emprendimiento Madrid"`
4. `ronda de financiación startup Madrid`
5. `ecosistema startup Madrid`

**Supplementary query** (used because several months had fewer than 3 eligible primary hits): `startup Madrid site:<outlet> after:… before:…`, run for each of the 9 outlet domains and each month. I took the top 10 per site and per month, and dropped items whose pubDate fell outside the month. These were read in the order Google returned them, site block by site block: elreferente → telemadrid → madridiario → expansion → cincodias → eleconomista → elmundo → elconfidencial → capital-riesgo.

Discarded attempt: a combined OR-of-sites query broke under zsh word-splitting, so its date filter never applied. I did not use any of its results for selection.

**Selection rule:** within each month, go through the primary results (query 1→5, in rank order), then the supplementary ones. Include each eligible article until about 4 are taken. In October and June, more eligible items were taken in order to reach 50. The months with 3 articles (Nov, Feb, Apr, Jul) ran out of eligible, readable items in the order I went through them.

Articles per month: Oct 7, Nov 3, Dec 4, Jan 4, Feb 3, Mar 5, Apr 3, May 4, Jun 6, Jul 3, Aug 4, Sep 4.
Articles per outlet: Telemadrid 16, El Referente 12, Expansión 6, El Mundo 6, Capital-Riesgo.es 6, El Economista 4. Cinco Días 0, El Confidencial 0 and Madridiario 0 (reasons below).

**How articles were read:** pages were opened in Chrome and the article text was read directly. Telemadrid, El Referente and Capital-Riesgo.es were read through targeted DOM text extraction. Every speaker row comes from page text I read. The exception is MAD02 (Capital-Riesgo Q3 report), which was read through a WebFetch summary.

## Skipped or failed URLs

- **Cinco Días (cincodias.elpais.com): every article was unreadable** (Premium paywall, or no text rendered). The skipped items were: Clevergy (2025-10-06), Omnia (2025-10-15), Adcities (2025-12-01), eVoost AI (2025-11-21), Algori (2025-12-08), Mito AI (2026-01-29), Traza (2026-04-15), South Summit defensa/IA (2026-05-26), Embat (2026-05-12) and South Summit IA forum (2026-05-11). Laborai, Orbio, Mitiga, megarrondas, Mango/Theker, PLD Space, HappyRobot and the aviation item were not attempted after this pattern was established.
- El Referente returned 403 to WebFetch and curl because of Cloudflare. Reading it through Chrome worked.
- `news.google.com` decoding hit HTTP 429 from the shell, so it was done in the browser instead.
- Madridiario "Somos Mizu" (notas-de-prensa section): no article text rendered. Skipped.
- Telemadrid "El futuro es hoy: los avances tecnológicos dedicados a la gente mayor" (2026-08-14): no article text extracted. Skipped.

## Exclusions (seen in order, not coded)

- **Out of period (Google showed a misleading 07-Oct-2025 date):** Telemadrid Retree (2022), Hoteligy (2022), Invopop (2024), Google for Startups (2020) and Alcampo (2022). Telemadrid "1 de cada 7 madrileños es latino" is not startup news.
- **Not Madrid (primary scope elsewhere, or location not verifiable in a national outlet):**
  - ScrapAd (Expansión Catalunya)
  - Pragmatech (Asturias)
  - Holo (Barcelona)
  - El Mundo foreign entrepreneurs (Barcelona-centred)
  - Nu Quantum (UK)
  - MOVEMENTS (no location stated)
  - Almenara (no location stated)
  - Juan Roig/startup (Valencia)
  - HappyRobot El Mundo (San Francisco HQ)
  - Tentare (Barcelona)
  - Macadam Telemadrid (Barcelona)
  - Lup (Basque)
  - the Valencia, Andalucía, Galicia and Sevilla ecosystem pieces
- **National scope, not Madrid ecosystem:**
  - El Referente media list
  - El Referente TOP15/TOP25 national lists
  - El Referente 25 startups
  - El Referente Scoutyn launch and the Scoutyn top-50 list
  - El Referente Guía de Inversión 2026 (a national guide presented at CDTI Madrid; also self-promotion by the outlet)
  - Expansión lockers sector feature
  - Expansión "capital apuesta…", "atraen inversores internacionales" and "negocios emergentes 2026"
  - El Economista national investment total
  - El Mundo national AI startups
  - El Mundo Javier Megías interview
  - El Confidencial financing options
  - El Confidencial "startups ganan escala"
- **Not startup news:** Telemadrid Ayuntamiento satellite-mapping contract (2026-04-15), Medusa Bay (fashion brand), MiDomo (construction SME), Tech Show Madrid (corporate trade fair).
- **Op-ed:** El Referente "Madrid, un lugar para el crecimiento de las startups" (/opinion/, 2026-07-27).
- **El Referente single-word directory/profile pages** (e.g. "Golden Gamers", "HVR Energy", "Spun", "Matrits"): treated as startup directory entries, not news articles.
- **Telemadrid programme listings** ("Madrid Trabaja DD.MM.2026", "Madrid directo").

## Judgement calls

1. **Startup as headline actor.** When the headline actor is a startup *company* (e.g. "Acoru cierra Serie A…"), I coded `headline_actor=FOUNDER`, meaning the builder side. A city or region as subject ("Madrid lidera…", "La Comunidad de Madrid se consolida como motor…") was coded `NONE`. "Madrid impulsa…" in a Comunidad programme story was coded PUBLIC_OFFICIAL.
2. **CEO without founder status → STARTUP_EMP.** If the text calls someone CEO or director but never says founder, I coded STARTUP_EMP. This applies to 10 speakers: Vig-Sec, Eye4Sky, Usyncro, SleepZzone, Your View, El Pez Jardinero ×2, denarius, and the Chainalysis and KuCoin panelists. It does not change the BUILDERS total. Luzia's CEO "dirigida desde el origen" was coded FOUNDER.
3. **"Presented as speaking" without a quote.** People presented as speaking without a direct quote were coded:
   - Telemadrid "Entrevista a …" interviewees whose text is paraphrased
   - officials who opened or closed an event (MAD45)
   - named panelists (MAD49)

   Future panelists listed in event previews (MAD46) were not coded. Neither were people only in photo captions (Benjumea and the consejera Rocío Albert in MAD32/33), nor a first-name-only instructor ("Marcos", MAD27).
4. **Telemadrid "Madrid Trabaja/Madrid Directo" startup segments** were included as Madrid-region coverage even when the text does not state the startup's city (MAD14, MAD15, MAD41). Each is flagged in notes.
5. **South Summit and MERGE articles were included** (MAD30, 32, 33, 45, 46, 49) because these are Madrid flagship events, even where the winner is from outside Madrid. MAD46 is borderline because it is corporate-heavy.
6. **Trigger coding for reports:**
   - Fundación madri+d reports, and reports commissioned by the Ayuntamiento, → PUBLIC_ANNOUNCEMENT (MAD02, MAD24, MAD36).
   - El Referente/Scoutyn reports → PRIVATE_ECOSYSTEM (MAD48, MAD50). MAD48 reads like branded content for Las Rozas Innova, which is public. MAD50 was co-produced with madri+d. Both could be argued as PUBLIC_ANNOUNCEMENT.
7. **Other trigger calls:**
   - MAD19 (Ienai, Leganés) → PUBLIC_ANNOUNCEMENT: an agency piece generated by the Government Delegate's visit, although the headline is a startup milestone.
   - MAD11 (Vig-Sec) → PUBLIC_ANNOUNCEMENT: recognition at a Comunidad de Madrid programme demo day.
   - MAD21 (Eye4Sky/Usyncro) → STARTUP_NEWS, although the Retech programme is mentioned.
8. **Speaker category calls:**
   - Álvaro Hita (MIEB, MAD10): a municipal Móstoles accelerator run by a private contractor → PUBLIC_ADJACENT.
   - Fran Ares (MAD37): speaks as a Netmentora mentor → PRIVATE_ECOSYSTEM.
   - AJE award winners running SMEs (Dulce Safari, Carbón Neutral Consulting, INMOA) → OTHER. Segofinance (~15-year-old fintech) → FOUNDER, borderline.
   - Kraken → CORPORATE; Chainalysis and KuCoin → STARTUP_EMP (scale-ups).
   - MyInvestor (a neobank leading a debt round) → INVESTOR.
9. **pr=yes** (7 articles):
   - Capital-Riesgo.es items bylined by a firm or carrying "Fuente:" lines (MAD01, 02, 06, 17, 31, 36)
   - El Economista Komvo, bylined only "elEconomista.es" (MAD37, unsure)
10. **Duplicate deals in two outlets are kept as separate articles:** Acoru (MAD01/05), Anyformat (MAD06/08), Bcas (MAD17/18). Ienai appears twice in different contexts (MAD19 official visit, MAD23 profile).

## Results snapshot

- **Speakers (n=75):**

  | Category | Speakers |
  |---|---|
  | FOUNDER | 32 |
  | STARTUP_EMP | 10 |
  | PRIVATE_ECOSYSTEM | 9 |
  | PUBLIC_OFFICIAL | 8 |
  | OTHER | 6 |
  | CORPORATE | 5 |
  | INVESTOR | 4 |
  | PUBLIC_ADJACENT | 1 |

- **Headline groups:** BUILDERS 42 (56.0%); INSTITUTIONS 9 (12.0%).
  - Excluding pr=yes articles: 37 builders and 9 institutions out of 66 speakers.
  - Excluding the MAD49 panel outlier: 40 builders and 9 institutions out of 68 speakers.
- **Triggers (n=50 articles):** STARTUP_NEWS 30, PRIVATE_ECOSYSTEM 12, PUBLIC_ANNOUNCEMENT 7, OTHER 1.
- **lead_voice:** FOUNDER 20, NONE 10, PRIVATE_ECOSYSTEM 6, STARTUP_EMP 5, INVESTOR 3, PUBLIC_OFFICIAL 3, PUBLIC_ADJACENT 1, CORPORATE 1, OTHER 1.
- **headline_actor:** FOUNDER 33, NONE 8, INVESTOR 3, CORPORATE 2, PRIVATE_ECOSYSTEM 2, PUBLIC_OFFICIAL 1, PUBLIC_ADJACENT 1.
- **Coverage:** 31 of 50 articles contain at least one builder voice, 7 contain at least one institutional voice, and 10 have no named speaker.

## Limitations

- **Outlet mix is skewed.** Cinco Días is entirely missing because of its paywall. El Confidencial and Madridiario contributed nothing eligible. Telemadrid (16 of 50) is over-represented, and its Madrid Trabaja segments are almost all founder-interview formats, so they favour builder voice by format. If the Basque sample leans on outlets like El Correo or Deia with an institutional-press-release diet, the outlet mix alone could drive the difference.
- **Supplementary site-queries were needed for about half the months.** Their ordering (site block by site block) is a choice of mine, not a pure search-rank order.
- **Google News RSS is not a complete index,** and its pubDates are sometimes wrong. Out-of-period re-indexed Telemadrid items were caught and excluded.
- **Some articles were included with the startup's location unverified** (Telemadrid regional segments, MAD38 tagged only "Comunidad de Madrid").
- **Speaker extraction for Telemadrid, El Referente, Capital-Riesgo and some Expansión pages used targeted text filters** (speech verbs, quote marks, role words) rather than a full read of every paragraph. A speaker introduced with no role word and no quote could be missed.
- **This is a single coder with no inter-coder reliability check.**
