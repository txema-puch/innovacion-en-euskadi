# Log: registry3 (extension beyond Ekintzaile 2021–25 and Barne-Ekintzaile)

Date: 2026-10-23. Work dir: this folder. Pilot method and scripts were reused from `~/Claude/innovacion-en-euskadi/research/public-funded-startups/`; that repo was not edited. Downloads are in `dl/` and scripts in `scripts/`. Python was run with `-I`, and a venv (xlrd/openpyxl) was used only for the Gipuzkoa xls files.

## Steps

1. **BOPV summary scan.** `scripts/bopv_sum.sh` fetched every issue summary XML for 2015–2023 (2,001 issues for 2015–22, plus 2023). `scripts/bopv_grep.py` grepped the titles.
   - No Ekintzaile beneficiary list exists before the 2021 call.
   - Found Gauzatu-Industria yearly beneficiary lists for 2014–2022 and downloaded the 9 PDFs. `scripts/parse_gz.py` parsed them: 431 awards, CIF from 2018.
2. **BOPV full-text search in Chrome** (read-only, see the access log below). "Ekintzaile" in full text returns 53 hits. None is a beneficiary list before the 2021 call.
3. **SPRI transparency.**
   - Sitemap: 15,302 URLs.
   - Transparency document API, `POST https://www.spri.eus/es/wp-json/mi-tema/v1/filtrar-documentos` with types `spri` and `capitalr`: 324 documents. Beneficiary tables start with 2022.
   - GCR's "Subvenciones y ayudas" PDF says its funds "carecen de competencias para conceder ayudas".
4. **Wayback.**
   - CDX of `spri.eus/archivos/*` (44,767 captures): no pre-2022 Ekintzaile list.
   - CDX of `bind40.com/*` (5,238): edition pages `area/<n>-edition/` for editions 1–7 and the edition-8 post. `scripts/bind_parse.py` parsed them.
   - SPRI's BIND 2020 list PDF and the 2019 startup dossier were downloaded.
5. **BDNS.** Pulled every call for Bizkaia (6531, 1,693 calls), Gipuzkoa (4062, 9) and Álava (2267, 3), then the awards for the 24 Bizkaia "Creación de Empresas Innovadoras" calls (Áreas 1, 2, 4 and 5).
6. **Open Data Euskadi.** Gipuzkoa grants CSVs for 2021–2026 plus the historic index for 2013–2020 (`scripts/gip_dump.py`). TXEKINTEK and BARNETEKIN appear only in the 2026 file.
7. **Lists by web page.**
   - BIC Gipuzkoa empresas impulsadas: 132.
   - Seed Capital Bizkaia gallery: 97 items, 70 named.
   - GCR holdings from SPRI blog posts: 5 that name GCR, plus 2 in the category that don't.
   - BIC Araba (JS-only) and BEAZ (no list) produced nothing.
8. **Assembly.** `scripts/assemble.py` produced `recs.json` with 1,249 programme records.
9. **Entity resolution.**
   - `scripts/sug2.py` sends each CIF or name to the infoempresa JSON autocomplete (`/sugerencias?q=`). This returns the registered name, province and **last presented accounts year**.
   - `scripts/match.py` matches by exact CIF. Failing that, it matches by exact normalised name, preferring a Basque province. Failing that, it accepts a unique Basque prefix match, rejecting coop→SL. When a CIF is not in the index, it falls back to the name.
   - `scripts/entities.py` deduplicates by CIF or normalised name, giving 1,035 entities.
10. **Status.**
    - `scripts/fetch_em.py` fetches the empresia page by slug. `scripts/fetch_em2.py` falls back to empresia's own search, and a retry derives slugs from the infoempresa URI or a former name.
    - 18 notable brands were picked by hand from empresia search results (`manual_alias.json`). These are flagged in `notes`.
    - Empresia gives status, constitution date, CNAE, nominal capital, number of capital increases, dated BORME acts (latest first), the "ventas" band and the last accounts deposited.
11. **Websites.** `scripts/web.py` tried guessed domains (`<name>.com/.es/.eus/.io`) for every non-dead Basque entity: 799 probed, 511 with the brand string on the page. It also detects parked domains and the © year. Guesses can be false positives: for example, ditto.com for Ditto Educación is almost certainly a different company.
12. **Employee and revenue ranges** (infoempresa company pages). infoempresa CloudFront blocked us twice (403). A **systematic sample** was therefore fetched instead of every company:
    - **all GROWING and ABSORBED rows, plus every 3rd other row (in CSV order) that has an infoempresa URI**: 167 targeted, 165 fetched;
    - plus the top-45 cohort-A candidates by "ventas" band and capital increases (10 more before the second block).
    - About 175 rows have a range; the rest are `unknown`. Ranking by headcount is therefore incomplete.
13. **Build.** `scripts/build3.py` writes `startups_other.csv`. Rows that resolve to the same empresia page are merged (renamed firms listed under an old and a new name, or brand vs legal name). No CIF conflicts were found in the merges.

## Inclusion rules

- **Included:** companies registered in Araba, Bizkaia or Gipuzkoa, plus unresolved names from Basque-only programmes.
- **BIND rows:** kept only if they resolve to a Basque registration or the BIND page says "Basque Country". 63 rows with non-Basque registrations and 86 unmatched BIND names (mostly foreign) were dropped.
- **Natural persons are counted, not named:**
  - DFB: 30 awards to natural persons (29 in Área 1, 1 in Área 2).
  - DFG TXEKINTEK: 12 payments to 4 distinct natural-person IDs.
- **Gauzatu-Industria** is a creation-and-development programme for technology-based SMEs, so many of its recipients are established firms. Each row's notes carry an age test: YOUNG if incorporated 5 years or less before the first award (empresia constitution date). The headline "startup cohort" (cohort A) means the startup programmes (DFB, DFG TXEKINTEK, BIC Gipuzkoa, BIND-Basque, Seed Capital Bizkaia, GCR) plus Gauzatu YOUNG firms.
  - Caveat: a re-incorporated newco of an old firm also tests YOUNG. Examples: Vicrila Industrias del Vidrio SL (founded 2018, >249 staff) and Viralgen Vector Core.

## Classification rules (as of 2026-10-23)

- **DEAD:** empresia status EXTINGUIDA, DISUELTA or CIERRE HOJA REGISTRAL, with no merger act. This category is not in the brief; it was added because a wound-up company is not a "zombie".
- **ABSORBED:** wound up **and** a BORME merger/absorption act. Active companies with merger acts are treated as the absorber and noted.
- **GROWING:** active, with a BORME capital increase dated on or after 2024-10-23 (funding signal, last 24 months). Hiring, plant and customers cannot be observed for free, so this is a funding-only test.
- **OPERATING:** active, not GROWING, with at least one sign of life since 2023-10-23: a BORME act, accounts filed for 2023 or later (empresia or infoempresa), or a live branded website. Companies with no empresia page but an infoempresa record showing accounts filed for 2023 or later are also OPERATING, with status "unknown (registered; last accounts filed YYYY)".
- **ZOMBIE:** active (or registered) with no sign of life in 3 years or more.
- **UNCLEAR:** not resolved to a registry entity. These are cooperatives (Basque cooperative register), CIF-only Gipuzkoa beneficiaries absent from infoempresa's index, brand names that could not be matched, and very new firms.

## Fields

- `status_source`, `last_registry_act_*` and `capital_increases` come from the empresia URL in `status_source`. The count of capital increases is the empresia badge total over the company's life; their dates are only partly visible.
- `sector` is the CNAE division label from that same empresia page.
- `revenue_eur` is the infoempresa range if sampled, otherwise the empresia "ventas" band (bands seen: 0.5M, 1M, 2.5M €; exact meaning undocumented).
- `employees` comes only from the infoempresa sample.
- `private_funding_eur`, `exit_or_valuation` and `revenue_year` are unknown (no web search, and BORME shows nominal capital only).
- Every programme source URL is in `notes`.

## Chrome access log (read-only; tab opened by this agent, closed after use)

1. `https://www.euskadi.eus/web01-bopv/es/p43aBOPVWebWar/buscarAvanzada.do?idioma=es`: blank form.
2. `https://www.euskadi.eus/web01-bopv/es/p43aBOPVWebWar/realizarBusquedaAvanzada.do?submit=cargar&idioma=es`: HTTP 500.
3. `https://www.euskadi.eus/web01-bopv/es/bopv2/datos/Ultimo.shtml` → "Consulta avanzada" → `buscarAvanzada.do?idioma=es&tipoBusqueda=2`. Filled "Texto de la disposición" = Ekintzaile and pressed Buscar (read-only search). Read results pages 1, 6, 5 and 4 (`realizarBusquedaAvanzada.do`).

No logins, no submissions that change anything, and no other Chrome pages. WebSearch was not used, and no search engines were scripted. Site-internal search and autocomplete (empresia `/busqueda/`, infoempresa `/sugerencias`) were used as registry lookups.

## Known gaps

- Ekintzaile 2015–2020 is not public (see sources.md).
- DFB pre-2022 (BOB not searched).
- DFG startup programme before Sept 2025 (not in open data).
- Araba: nothing.
- BIND editions 9–10.
- About 15 unnamed Seed Capital logos.
- GCR portfolio.
- Headcount for the roughly 650 rows outside the sample.
