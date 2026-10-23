# Sources: extension of the Basque publicly funded startup census (registry3)

Compiled 2026-10-23. Scope: everything except SPRI Ekintzaile 2022–2025 and Barne-Ekintzaile (covered by another agent). Each source is marked **OBTAINED**, **PARTIAL**, **NOT PUBLIC** or **NOT REACHABLE**.

## 1. SPRI Ekintzaile 2015–2020: NOT PUBLIC (verified three ways)

- **BOPV issue-by-issue scan.** BOPV publishes a per-issue summary XML at `https://www.euskadi.eus/bopv2/datos/YYYY/MM/sYY_NNNN.xml` (month folder must be right; issue number is sequential). All 2,001 issues of 2015–2022 plus 2023 were downloaded (`scripts/bopv_sum.sh`) and every title grepped (`scripts/bopv_grep.py`). Result: no Ekintzaile beneficiary list in any year before the 2021 call (published 2023, `2300801a`). The only Ekintzaile items 2015–2020 are a rules change (`1706199a`, Nov 2017). SPRI's only beneficiary publications in BOPV 2015–2020 were for internationalisation programmes (Global Training etc.).
- **BOPV full-text search (Chrome, read-only).** "Ekintzaile" in the full text of all dispositions: 53 hits, 2003–2026. Every hit before 2023 is a programme rule/convocatoria or amendment (2004, 2005, 2006, 2010, 2012, 2014, 2017, 2021, 2022). Zero beneficiary lists before the 2021 call.
- **SPRI transparency portal.** The document API behind `https://www.spri.eus/es/portal-transparencia/grupo-spri/` (`POST /es/wp-json/mi-tema/v1/filtrar-documentos`, type `spri`) lists 324 documents. "Subvenciones aprobadas" tables exist only from the 2022 call onward (Ekintzaile 2022–2025, Ekintzaile+ 2023–2025, Barnekintzaile 2022–2025, and ~25 other programmes). Nothing for 2015–2021.
- **Wayback Machine.** CDX of `spri.eus/archivos/*` (44,767 captures) and the 2019/2022 snapshots of the transparency portal: no Ekintzaile beneficiary file pre-2022.
- **Conclusion:** the 2015–2020 Ekintzaile beneficiary lists were never published (SPRI is a public company and only began BOPV publicity of Ekintzaile awards with the 2021 call). Only SPRI can produce them.

**Substitute obtained: Gauzatu-Industria 2014–2022 (OBTAINED).** Basque Government programme "de impulso a la creación y desarrollo de pymes de base tecnológica y/o innovadoras" (reimbursable advances, €100k–€1.5M). Yearly beneficiary lists in BOPV: 1501097a (2014), 1600304a (2015), 1700448a (2016), 1800489a (2017), 1901044a (2018), 2000663a (2019), 2100425a (2020), 2200613a (2021), 2205803a (2022), URL pattern `https://www.euskadi.eus/bopv2/datos/YYYY/MM/<id>.pdf`. 431 awards, 397 entities, €222.4M. CIF printed from 2018 on. Caveat: most recipients are established industrial SMEs, not startups; each row carries an age test (incorporation year vs first award: ≤5 yrs = YOUNG).

## 2. Bizkaia

- **DFB "Creación de Empresas Innovadoras" 2023–2026 (OBTAINED via BDNS).** Organ 6531. Calls: Área 1 (proyectos empresariales innovadores) 680654, 740080, 770297, 804568, 835008, 878819; Área 2 (nuevas empresas innovadoras) 680655, 701647, 740090, 770416, 804569, 835010, 878820; Área 4 (aceleración) 740096, 804571, 878825; Área 5 878827. 2026 second calls (916113–916116) have no awards yet. Awards come with CIF and name: `https://www.infosubvenciones.es/bdnstrans/api/concesiones/busqueda?vpd=GE&numeroConvocatoria=<n>&pageSize=500`. 243 awards: 213 to legal entities (189 distinct) and 30 to natural persons; €6.10M to entities.
- **DFB pre-2022 (NOT PUBLIC in usable form).** Bizkaia reports to BDNS only from April 2022. The predecessor programme's awards are not in BDNS. BOB resolutions were not searched (no scriptable BOB index was found this session).
- **Seed Capital Bizkaia (PARTIAL).** `https://www.seedcapitalbizkaia.eus/portfolio/` is a "selection" of logos per fund (Fondo I, Fondo BI, FEIS, Start, Konfekoop, BAF). 97 gallery items; 70 company names were identifiable from image alt text or file names; ~15 logos are unnamed. The BAF tab lists fund-of-funds holdings (Easo, Inverady, Nuclio and others) and was excluded. No amounts or dates are given, and it is explicitly not the full portfolio.
- **BEAZ:** `beaz.eus` does not resolve. `beaz.bizkaia.eus` loads but publishes no list of supported companies. NOT PUBLIC.

## 3. Gipuzkoa

- **DFG grants open data (OBTAINED, partial coverage).** "Subvenciones concedidas por la Diputación Foral de Gipuzkoa" on Open Data Euskadi: CSVs for 2021–2026 (`api.gipuzkoairekia.eus/dataset/recurso/<id>/descargar`). Beneficiaries appear as **CIF only, no names**. The startup programme "Programa para el acompañamiento en el proceso de creación de empresas de base tecnológica y/o innovadoras" appears only in the 2026 file (awards Sept 2025–Aug 2026): TXEKINTEK (new companies) and BARNETEKIN (intrapreneurship by existing firms). 196 payments: 61 entities (CIF), 4 natural persons, €1.25M. The dataset itself says some Promoción Económica lines "are not yet included", so earlier years of this programme are missing.
- **DFG 2013–2020 (NOT PUBLIC as data).** The "Histórico" dataset is only an index of BOG resolution links. Its only entrepreneurship entry is the comarcal ecosystem programme (grants to development agencies, not startups).
- **BIC Gipuzkoa (OBTAINED, names only).** `https://bicgipuzkoa.eus/empresas-impulsadas/` lists 132 incubated companies. No years or amounts. BIC Gipuzkoa is publicly owned and is the tutor for Gipuzkoa Ekintzaile projects, so this list is the best available proxy for Gipuzkoa's pre-2021 Ekintzaile cohort, though it is not equivalent to it.
- BDNS (organ 4062) has only 9 Gipuzkoa calls, none for startups.

## 4. Araba: NOT PUBLIC / NOT REACHABLE

- BDNS organ 2267 has 3 calls, none for startups.
- `bicaraba.eus/empresas/` renders its company directory via JavaScript and exposes no API in the HTML. Not retrieved; it could be read in a browser.
- No Álava startup grant beneficiary list was found.

## 5. BIND 4.0 (OBTAINED for editions 1–8)

- `bind40.com` is unreachable live, so the Wayback snapshots of `https://bind40.com/area/<n>-edition/` were used: ed. 1 (2016–17), 12 startups; ed. 2, 28; ed. 3, 32; ed. 4, 39; ed. 5, 31; ed. 6, 28; ed. 7, 26.
- Ed. 8 (2024): 20 startups from the post `2024/01/26/25-open-innovation-projects-via-bind-4-0-in-2024`.
- SPRI also published `https://www.spri.eus/archivos/2020/11/pdf/listado-startupsbind2020.pdf` (ed. 5, with country).
- Editions 9–10: not found (site down, no snapshots).
- BIND is acceleration plus paid corporate pilots, not a grant to the startup.
- Basque filter: a startup is kept only if it matches a company registered in Araba, Bizkaia or Gipuzkoa (infoempresa), or if the BIND page says "Basque Country". 212 names → 84 kept. 63 matched to non-Basque registrations and 86 unmatched (mostly foreign) were excluded.

## 6. Public VC portfolios (GCR): NOT PUBLIC

- The GCR transparency portal (`/es/capital-riesgo/portal-transparencia/`, doc type `capitalr`) publishes no portfolio list. Its "Subvenciones y ayudas" document states that GCR SGEIC, Ezten FCR, Basque FCR, Lanpar 2013 FCR, Seed Gipuzkoa SCR and BasketekVenture FCR "carecen de competencias para conceder ayudas y subvenciones". Their investments therefore fall outside every subsidy-publicity rule.
- The landing page claims more than 500 companies invested in but names none.
- Press-confirmed holdings, from SPRI blog posts that name GCR in the text: Inmedical Therapeutics, Optidel Biosystems (BasketekVenture FCR), Orbik Cybersecurity, USA Group (Ezten FCR), InspectRail (BasqueTek Ventures).
- Multiverse Computing and Oncomatryx are filed under SPRI's "fondos de capital riesgo" blog category, but the post text does not name GCR.
- Basque Fondo (`/es/ayudas/basque-fondo/`): up to €100k per company for Ekintzaile alumni under 3 years old. No beneficiaries are published.

## 7. Outcome sources

| Source | Use | Note |
|---|---|---|
| infoempresa `/sugerencias?q=<CIF or name>` (JSON autocomplete) | CIF↔name resolution, registered province, **last presented accounts year** | Rate-limited (CloudFront 403) after ~1,100 calls; recovered after ~1 h |
| empresia.es `/empresa/<slug>/` | status, constitution date, CNAE, nominal capital, count of capital increases, dated BORME acts (latest first), "ventas" band, last accounts deposited | Shows CIF masked; slug found by name, by infoempresa URI, or by empresia `/busqueda/?q=` |
| infoempresa company page | employee and revenue ranges | Fetched for a systematic sample only (see log.md) |
| Guessed domains (`<name>.com/.es/.eus/.io`) | website liveness, © year, parked domains | Accepted only if the brand appears in the page |

Not public or not free: real revenue and headcount (Registro Mercantil accounts, about €10 per filing); round sizes (BORME shows nominal capital only); cooperatives (Basque cooperative register, absent from BORME aggregators); any outcome follow-up by SPRI, GCR or the Diputaciones.
