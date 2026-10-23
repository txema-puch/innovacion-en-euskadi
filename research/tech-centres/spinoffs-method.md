# Method — Basque tech-centre spin-off status table

Date of research: 23 Oct 2026. Output: `spinoffs.csv` (188 rows, 19 columns), `quotes.md`, this file.

## Scope
Companies created, co-founded or participated as start-ups by BRTA members (Tecnalia and its predecessors Fatronik, Inasmet, Labein, Robotiker, ESI, Leia, Cidemco, Euve, plus the 2008 "Corporación Tecnalia" grouping that included AZTI and Neiker; CEIT, Ikerlan, Tekniker, Vicomtech, CIDETEC, AZTI, GAIKER, Leartiker, Azterlan, Lortek, IDEKO, Neiker; CIC energiGUNE, nanoGUNE, biomaGUNE, bioGUNE) and every project on SPRI's Basque Tek Ventures (BTV) list (https://www.spri.eus/en/support/basque-tek-ventures/), including the BTV projects from UPV/EHU, MGEP, BCMaterials and Polymat. Those are tagged with that centre and counted under "BTV (university/other)".
No spin-offs were found for IDEKO, Neiker (apart from Vacunek on the 2008 list), microGUNE, tourGUNE or marGUNE.

## How the list was built
1. Starting list from the brief.
2. Current spin-off and participated-company pages of each centre (tecnalia.com/en/partly-owned-companies, tecnalia.com/tecnalia-ventures, ceit.es, ikerlan.es startups page, tekniker.es/es/organizacion, vicomtech.org, cidetec.es, azti.es, nanoGUNE, biomaGUNE, bioGUNE and energiGUNE pages).
3. Historical lists via the Wayback Machine, which was intermittently offline:
   - Corporación Tecnalia "Historial de empresas creadas" (2008, 47 names)
   - Fatronik NEBT pages (2006, 2010)
   - Tecnalia "promoción de empresas" (2010, 2012, 2017)
   - Tecnalia Ventures portfolio (2013–15)
   - Vicomtech spin-off page (2013, 2016, 2024)
   - CEIT memoria 2010, which has a dated table of 1996–2008 spin-offs
4. Memorias already downloaded (BRTA 2019/2022–24, CEIT 2024/25, AZTI 2025, Tecnalia carbon-footprint report 2025, the BTV calls) and Tecnalia annual-results press releases.

## Status evidence
- libreborme.net now redirects to librebor.me, which is behind Cloudflare (403). Status therefore comes mainly from **empresia.es**, which reproduces BORME acts: incorporation, capital changes, sole-shareholder declarations, insolvency, dissolution and extinction. Each row cites its URL in `status_source`.
- One agent (Ikerlan/CEIT) read 26 librebor.me pages in the user's Chrome, read-only; those pages are listed in its row notes. The permission for that came as a coordinator relay. Three other agents declined to use Chrome because the approval did not come directly from the user.
- Status codes:
  - **dormant**: registered, but no accounts, website or news for 2+ years.
  - **acquired**: the company passed to a new controlling owner, including mergers and absorptions.
  - **dissolved**: dissolution, extinction or insolvency liquidation recorded.
- Centre exits where the company itself continued independently are recorded in `exit` (e.g. Graphenea, Diede, Smowltech).

## Financials
- Employees: exact numbers only where a company site, press or registry gives one; infoempresa/empresite ranges are labelled as ranges.
- Revenue: einforma, eleconomista, axesor and infoempresa were rate-limited or blocked. Almost all revenue cells are **ranges or "unknown"**. Exact revenue exists only for NEM Solutions (€4.2M, OECD 2019) and Fatronik (2004). The portfolio-level figures Tecnalia reports itself are in `quotes.md` §2.
- Funding: only disclosed rounds, with amount, lead and source. Grants (IDAE, EIC, CDTI) are noted separately and not added to `private_funding_eur` where identified.

## Deduplication
Companies appearing in more than one cluster were merged, keeping the centre-cluster row, filling its empty fields from the duplicate and noting the merge. Merged companies:
- BTV duplicates: InspectRail, SafeLoc, Konbus, TrebezIA, Battbelt, Orbik, Makby, Optidel
- BATTIA (CEIT + Tekniker)
- Goitek and Goialde (Fatronik + Tekniker)
- Roboconcept and Bionor (Tecnalia 2008 list + AZTI)

Script: `scripts/final_merge.py`; stats: `scripts/stats.py`.

## Known limitations
- WebSearch quota ran out early for all agents. They did not work around it with curl-based search engines, so press coverage is thinner than intended.
- 47 rows have status "unknown". They are mostly:
  - 18 bare names from the 2008 Tecnalia list
  - about 15 BTV projects with no registered company
  - a few CEIT/Vicomtech entries without a registry match
- Several registry matches are "probable", flagged in notes: Goitek, Goialde, Fatek, Servelan, PKM 2004, Punto Comercial, Bertoko, Ecofond, ADE Biotec.
- The origin centre is unconfirmed for several 2008-list names (Biolan, Ethernalia, Turbodetco, Sefatec, Metaposta).
- Centre stakes are mostly undisclosed.
- Fatronik is included as a row (a Tekniker-founded centre later merged into Tecnalia) but is not a company spin-off in the usual sense; exclude it from outcome statistics.
- Derived values are marked as derived in notes, e.g. JBS ~51% of Biotech Foods from the BORME capital increase, or IDAE ~17% of Lanzo.
- All downloaded content was treated as untrusted data.
