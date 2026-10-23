# Method: pilot registry

## Cohort rule
- **Programme:** SPRI Ekintzaile (grants for new innovative companies), **2021 call**. This is the oldest year for which a complete official beneficiary list could be retrieved: BOPV n.º 32, 15/02/2023 (https://www.euskadi.eus/bopv2/datos/2023/02/2300801a.pdf).
- **Inclusion:** every beneficiary that is a legal entity, meaning an S.L., S.L.L., S.L.U., S.A., S.Coop. or AIE. Two names without a legal suffix (Nutrenaissance, Impulso Cognitivo) are also included, because both resolve to registered S.L.s.
- **Result: N = 65 of 124 beneficiaries**, receiving €1,172,200 of the €2,163,700 total. This is a full census of that segment, not a sample.
- **Excluded:** 59 natural persons. Ekintzaile pays promoters before incorporation, and the resolution does not name the company they later formed. Tracking them needs SPRI's file-to-CIF mapping, which is not public.
- **Why not 2015–2020:** neither BDNS (Basque bodies report only from 2022–23 onward) nor a scriptable BOPV search produced earlier lists. See `sources.md`.
- **Outcome window:** grants were awarded in 2021, and outcomes were observed in October 2026, about five years later.

## Field rules
- **status:** taken from the BORME-derived status on empresia.es.
  - ACTIVA maps to active.
  - EXTINGUIDA maps to extinct.
  - DISUELTA maps to dissolved.
  - CIERRE HOJA REGISTRAL maps to **dormant**. A closed registry sheet usually follows tax deregistration or a failure to file accounts. One of these (Playeron) is also in insolvency (concurso), per Infoempresa.
  - Infoempresa is the fallback source.
  - **acquired** is used only where a primary source says so (Nanokide's own website).
  - When the name match was uncertain, status is **unknown** and the candidate entity is given in `notes`.
- **active** means "not wound up in the registry". It does not mean "operating". Seven of the active companies have had no BORME act since the year they were incorporated: Holocam, Limpieza Criogénica Blaster, Fincatecnia, Iprint3dspares, Droneboard, Colada App and Run Now. Treat them as possible zombies.
- **employees / revenue:** the Infoempresa *range* (for example "1-9 (range)" or "<2000000 (range)") is recorded only for active companies. No exact figures were available for free. **revenue_year** is unknown throughout.
- **private_funding_eur:** **unknown for every company.** Round sizes need press, El Referente or Crunchbase, and web search was unavailable. As a weak proxy, `notes` gives the number of BORME capital increases and the current nominal capital. Nominal capital excludes the share premium, so it understates any round and is not funding raised.
- **sector:** my short label, paraphrasing the objeto social registered in BORME (via empresia).
- **cif:** from Infoempresa. The BOPV list does not include it.
- **URLs:** every value that is not "unknown" cites the page it came from. empresia and infoempresa URLs are deterministic slugs and were fetched on 2026-10-23.

## Limitations
1. **One programme and one year.** Ekintzaile is SPRI's flagship seed grant, but it is small (€5k–€30k per company) and is not the whole of Basque public startup money.
2. The cohort includes **non-startups**: Gamesa Electric S.A. (a corporate subsidiary), Energía Distribuida del Norte S.A. (€1.28M nominal capital) and Metal Stamping & Hot Industry (€300k). They are flagged in `notes`.
3. **Acquisitions are under-detected.** Without press search, an acquisition is visible only through a website notice or a BORME merger. Paravalves' domain now serves Arnett Valves (US), which is unverified.
4. **Name matching** used slugified names. Six companies are unresolved: two cooperatives outside BORME, plus Biotek, Ipsum Solutions, Basque Pay and Heliotrope Europe.
5. Company websites were found by guessing domains (`<name>.com/.es/.io/.eus`). Matches were accepted only where the page clearly belongs to the company.

## Reproducing
Scripts are in `scripts/`; raw downloads are in `dl/`.
1. `parse2021.py` parses the BOPV PDF into `ek2021.json`.
2. `fetch.py` downloads the empresia and infoempresa pages.
3. `extract.py` and `em.py` parse those pages.
4. `webguess.py` probes the guessed website domains.
5. `build.py` writes `startups.csv`.

## Census sizing (next step)
- **Ekintzaile 2021–2025** is about 124 + 65 + 57 + 88 beneficiaries, plus Ekintzaile+ 2024–25: **roughly 350–400 beneficiaries, about 200 of them legal entities.**
- **Barne-Ekintzaile 2022–24:** about 106.
- **Bizkaia "Nuevas empresas innovadoras" and acceleration areas, 2022–2026:** about 100–200.
- **Hazitek startup beneficiaries:** unknown.
- **Pre-2021 Ekintzaile:** about 100–150 per year if the lists can be obtained. That would add roughly 600–900 more for 2015–2020.
- **Total:** a realistic full census is **about 1,000–1,500 entities**.
- **Cost:** status via empresia is automatable, at about 2 HTTP requests per company. Real revenue and employee figures would need paid Registro Mercantil accounts at about €10 per company per year.
