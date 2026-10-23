# Talent line, part 3: does anyone in Euskadi measure researchers leaving to build?

Supports claim C-028 ("Nobody in Euskadi measures how many tech-centre alumni go on to found or lead startups").

Method: full-text search of each document's text extract. Terms searched, in Spanish, Basque context and English: rotaci, excedencia, alumni, antiguos, fuga, retenc/retener, emprendedor, spin, "transferencia de investigadores", "a la industria", salida, movilidad, plus a manual read of each "en cifras" / indicator page. Searched 2026-10-23. Extracts are in the repo at `sources/txt/`; page numbers are PDF pages.

## Verdict

No Basque document checked has any indicator, in any year, for:
- staff turnover or leavers;
- staff moving to industry or startups;
- alumni who founded companies;
- alumni in startup leadership.

Every indicator found counts **companies** (spin-offs, startups) or **inputs** (people employed, PhDs, theses). BRTA states the transfer of researchers to industry as a remit (2019) and states retention as a goal (2023), but reports on neither.

## Document by document

| Document | What it does report on people | Mobility/alumni indicator? | Locator / evidence |
|---|---|---|---|
| BRTA presentation 2019 (SPRI), https://www.spri.eus/archivos/2019/11/pdf/3-Presentación-Centros-BRTA-Rikardo-Bueno.pdf | ~3,500 people; theses/year | **No.** But p.9 sets "la transferencia de investigadores a la industria" as a BRTA talent remit | p.9 (remit); p.25 (people/theses) |
| BRTA memoria 2022, https://brta.euskadi.eus/contenidos/informacion/brta_memoria/es_def/adjuntos/2022_BRTA_memoria-anual_CAS-EUS.pdf | Personas (4,110), doctoral theses, publications, patents | **No** | p.7 and p.14 ("PERSONAS EN BRTA"). Searched terms: 0 hits except "spin" ×2 (revenue of spin-offs) |
| BRTA memoria 2023, https://brta.euskadi.eus/contenidos/informacion/brta_memoria/es_def/adjuntos/BRTA_2023_web.pdf | Personas, theses | **No.** Letter: "debemos crear las condiciones para mantenerlos" + Plan de Carrera Profesional | p.3 (letter). No figures on leavers |
| BRTA memoria 2024, https://brta.euskadi.eus/contenidos/informacion/brta_memoria/eu_def/adjuntos/2024_BRTA_memoria-anual_CAS-EUS.pdf | 4,372 people (1,955 women / 2,417 men), 37% doctors, 2,405 client firms; 4,100 researchers, 665 theses supervised, 1,556 publications, 137 patents | **No** | p.6 ("BRTA en cifras"), p.13. Every searched term: 0 hits |
| PIE 2025-2028, indicator panel and Annex 3, https://www.euskadi.eus/contenidos/plan_departamental/pie_2028/es_def/adjuntos/PIE-2025-2028.pdf | 25 indicators (incl. PIE budget). The only knowledge-agent one is "Intraemprendimiento – Spin-offs de agentes CTI y nuevos proyectos empresariales", i.e. "Número de nuevas spin-offs de agentes de conocimiento (RVCTI y Sistema Universitario Vasco) / Nº proyectos de emprendimiento empresarial", measured by "IUNE, BRTA, INNOBASQUE, SPRI, DFG, DFA, DFB PE" | **No** people indicator | Panel: PDF p.16 / printed p.14. Annex 3: PDF p.44 / printed p.42 |
| PIE panel values for that indicator | 2017: 24/98 · 2018: 24/110 · 2019: 21/119 · 2020: 16/110 · 2021: 16/119 · 2022: 18/102 · 2023: 19/165 · 2024: "En construcción" | — | PDF p.16 |
| Tecnalia balances 2020, 2021, 2023, 2025 (cms.tecnalia.com, see sources/README.md) | Staff; jobs in investee companies ("104 personas que trabajan en las empresas participadas", 2023) | **No** leaver or alumni figure | tec2023 l.84. Searched terms: 0 hits |
| CEIT memorias 2024, 2025 | Plantilla (279 in 2025: 151 + 60 researchers by type) | **No** | ceit2025 "PLANTILLA" block |
| AZTI memoria 2025 | Talent mentioned qualitatively | **No** | 0 hits on mobility terms |
| Ministry of Science evaluation of tech centres (Nov 2025) | R&D staff (FTE) and spin-offs per 1,000 R&D staff | **No** staff-mobility indicator; spin-offs only (95, 54 Basque) | PDF p.37, p.50, p.53 |
| UPV/EHU Reglamento de Creación de Empresas (BOPV 23-06-2026) | Registro de spin-off (companies, equity, results licensed); annual accounts of investee firms incl. "contratación de personal" | **No** tracking of staff who leave | arts. 10, 21 (p.7, p.11) |
| Ikerbasque 2024 results page, https://www.ikerbasque.net/en/node/3619 | 402 researchers (201 Research Professors, 112 Research Fellows, 89 Research Associate Professors); 1,643 professionals in their groups; "participating in 41 spin-offs" | **No** people-level count; spin-off participation only (cumulative or annual not stated) | read 2026-10-23 |

## Not checked (gaps, with reasons)

- **PCTI Euskadi 2030** (plan and its annual monitoring reports): not retrieved.
  - Direct URL guesses on euskadi.eus returned 404.
  - The Wayback Machine was "Temporarily Offline" on 2026-10-23.
  - Web search budget was exhausted.
  - Absence is **not established** for PCTI. This needs a follow-up: fetch the PCTI 2030 PDF and its "Informe de seguimiento", and check whether the indicator system has any researcher-mobility indicator. The EU RIS/EIS-type "researchers in business" indicator would be a stock, not a flow.
- **Tecnalia annual / sustainability reports** (beyond the press balances in the repo) and the **Memorias de Sostenibilidad / EINF**. Non-financial statements usually report employee turnover ("rotación"). Not fetched. If found, that would give leavers per year, though not where they go.
- **BRTA Plan de Carrera Profesional** (mentioned in memoria 2023 p.3): not public / not found.
- **Ikerbasque annual reports (memorias)**: only the 2024 results web page was read.

## Facts-level absences proposed (see facts_draft_rules.csv)
1. BRTA memorias 2022–2024 publish no indicator of staff leaving, staff moving to industry or startups, or alumni founders.
2. PIE 2025-28 indicator panel (25 indicators) has no researcher-mobility or alumni indicator. Its only knowledge-agent indicator counts spin-offs, and the 2024 value is "En construcción".
3. Tecnalia balances (2020, 2021, 2023, 2025) publish no leaver or alumni figure.
4. The UPV/EHU 2026 regulation sets up a registry of spin-off companies but no tracking of the people who leave.
