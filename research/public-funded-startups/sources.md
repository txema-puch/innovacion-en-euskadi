# Source map: Basque public startup funding and what happened to the companies

Compiled 2026-10-23. Each source is marked **WORKS**, **PARTIAL**, **NOT PUBLIC**, or **NOT TESTED** (not checked this session).

## A. Who got the money (grant and investment registers)

### A1. BDNS / Infosubvenciones (national grants database): PARTIAL, and the gaps are themselves a finding
- **Access:** a public JSON API with no key. The spec is at `https://www.infosubvenciones.es/bdnstrans/estaticos/doc/snpsap-api.json`.
  - Calls (open-call) search: `GET /bdnstrans/api/convocatorias/busqueda?vpd=GE&organos=<id>&page=&pageSize=`
  - Awards search: `GET /bdnstrans/api/concesiones/busqueda?vpd=GE&numeroConvocatoria=<n>&pageSize=500`. Each award row includes the beneficiary's CIF and name, the amount and the award date.
  - Organ IDs: SPRI = 6709. Diputación Foral de Bizkaia = 6531 (350 is empty). Gipuzkoa = 4062. Álava = 2267 (7234 is empty). You get them from `/api/organos?vpd=GE&idAdmon=A|L`.
  - Dates use the `dd/mm/yyyy` format. The `descripcion` filter on `/concesiones` is effectively ignored, so filter by call number instead.
- **Coverage:**
  - **SPRI:** 87 calls in BDNS, all registered from June 2024 onward and back-filled only to the 2022 call year. SPRI Ekintzaile awards are in BDNS with CIF for 2022 (65 awards, €1.15M), 2023 (57, €1.09M) and 2024 (88, €1.60M). Barne-Ekintzaile (intrapreneurship) has 2022: 31, 2023: 39 and 2024: 36 awards.
  - **Basque Government departments:** no BDNS records before October 2023. The older department organs, such as 6828 "Desarrollo Económico, Sostenibilidad y Medio Ambiente", have zero calls.
  - **Diputación Foral de Bizkaia:** records from April 2022 (1,693 calls). These include the "Emprendimiento e innovación" programme: Área 1 innovative projects, Área 2 "Nuevas empresas innovadoras" and Área 4 acceleration. Example award counts: 680655 has 9 awards, 701647 has 18 and 740090 has 6. Bizkaia also funds a very large volume of small-business entrepreneurship grants ("fomento de iniciativas emprendedoras", 5,000+ awards). Most of these are not startups.
  - **Gipuzkoa:** only 9 calls in total, all from 2024 onward. **Álava:** only 3 calls, all from 2022 onward.
- **Gap:** Basque public bodies did not report to BDNS before roughly 2022–2023. **BDNS cannot answer the question for the 2015–2021 cohorts.**

### A2. BOPV (Basque official gazette) beneficiary resolutions: WORKS for Ekintzaile 2021+
- SPRI publishes an annual resolution "por la que se da publicidad a la relación de entidades beneficiarias … «Ekintzaile»". It gives the file number, beneficiary name and amount, but **no CIF**.
  - 2021: BOPV n.º 32, 15/02/2023. https://www.euskadi.eus/bopv2/datos/2023/02/2300801a.pdf (124 beneficiaries, €2,163,700). **This is the pilot's source.**
  - 2022: BOPV n.º 238, 09/12/2024 (2405627a)
  - 2023: BOPV n.º 97, 26/05/2025 (2502255a)
  - 2024: BOPV n.º 102, 02/06/2025 (2502427a)
  - Ekintzaile+ 2024: 2502429a
  - Ekintzaile+ 2025: BOPV n.º 156, 18/08/2026 (2603646a)
  - Ekintzaile 2025: BOPV 2603645a (corrected 2026-10-23: earlier listed here as Barne-Ekintzaile). Barne-Ekintzaile awards are in BDNS for 2022–24.
  - These locations were found through search before the search budget ran out. Only the 2021 PDF was downloaded and parsed.
- **Not found: Ekintzaile lists for 2015–2020.** The BOPV advanced search (`p43aBOPVWebWar/realizarBusquedaAvanzada.do`) is a stateful JSP form. A scripted POST returned only the blank form. These years need either a manual BOPV search or a records request to SPRI.
- Individuals: about half of the Ekintzaile beneficiaries are natural persons, because the grant is paid before incorporation. Their later company is not named anywhere in the resolution.

### A3. Programmes on the original list
- **Hazitek, Gauzatu, Basque Fondo, GCR funds** (Basque Fondo, Ekintzaile fund, Basque Tek Ventures, Hazten Scale-up FCR): **NOT PUBLIC**.
  - Gauzatu Industria and Gauzatu Internacional: only the 2022+ awards are in BDNS.
  - Hazitek: the awards resolutions are in the BOPV. Startups are not flagged as such, and these lists were not tested this session.
  - GCR / Basque Fondo: participative loans and equity are not grants, so they are outside BDNS. `www.spri.eus/es/basque-fondo/` returns 404 and `gcrpv.eus` gives no response. **No public portfolio list was found.** Portfolio holdings of public venture-capital vehicles appear to be undisclosed. The annual accounts of the GCR fund manager (filed at the Registro Mercantil, paid access) would be the only route.
- **BIND 4.0:** `bind40.com` gave no response (connection failed from this machine), so the startup list for each edition was not retrieved. BIND is mainly an acceleration programme with corporate pilots, not grants to the startup. **NOT TESTED.**
- **Seed Capital Bizkaia** (a Diputación Foral de Bizkaia vehicle): `seedcapitalbizkaia.eus/portfolio/` loads, but the portfolio is rendered by JavaScript and paginated, and no company names are in the HTML. Fund vehicles: Fondo I, BI, BAF, Start Bizkaia, FEIS, Konfekoop, MicroEurope. **PARTIAL.** It would need a browser read. Investment amounts are not shown.
- **BIC Gipuzkoa:** `bicgipuzkoa.eus/empresas-impulsadas/` lists about 70+ "empresas impulsadas" by name, with no amounts or years. **PARTIAL.**
- **BEAZ** (`beaz.eus`) gave no response. **BIC Araba:** **NOT TESTED.**

## B. What became of each company (outcome sources)

| Source | Access | What it gives | Verdict |
|---|---|---|---|
| empresia.es `/empresa/<slug>/` | curl, no block | BORME-derived status with extinction date, registered seat, objeto social, nominal capital, count of capital increases, dated BORME acts | **WORKS.** Primary status source |
| infoempresa.com `/es-es/es/empresa/<slug>-sl` | curl, no block | CIF, status, **employee range and revenue range** | **WORKS**, but the ranges are very coarse ("1-9 employees", "<€2M") |
| libreborme.net | 403 | status | Blocked |
| einforma.com | 429 | revenue range | Blocked (rate-limited) |
| axesor.es | 404 on guessed slug | revenue range | Not usable without search |
| Company websites (guessed domains) | curl | liveness, acquisition notices | **WORKS** for about 17 of 46 active companies |
| Search engines / press (El Referente, Crunchbase, Google News) | — | funding rounds, exits | Unavailable this session: the WebSearch budget was exhausted and scripted search engines are off-limits |

### Not public, or not free (a key finding)
- **Real revenue and headcount figures** sit in the annual accounts deposited at the Registro Mercantil. These cost about €9–€12 per filing through registradores.org. Free aggregators expose only ranges.
- **Private funding raised:** BORME shows *nominal* capital increases only, not the share premium (prima de emisión). It therefore reveals *that* a round happened but not how big it was. Round sizes come only from press releases, El Referente or Crunchbase.
- **Cooperatives (S.Coop.)** are registered in the Basque Cooperatives Register, not the Registro Mercantil. They are invisible to every BORME-derived source.
- **Grant outcome follow-up by SPRI or the Diputaciones:** no published evaluation of the beneficiary cohorts (survival, jobs, follow-on funding) was found. This was not exhaustively verified because web search was unavailable.

## Access log
- No pages were read through the user's Chrome. The coordinator approved this, but it was not needed for the sources used.
