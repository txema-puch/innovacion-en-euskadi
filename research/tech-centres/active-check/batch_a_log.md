# Batch A log: active spin-offs, indices 0–39 (H2SITE … Nuuk Technologies), checked 2026-10-23

Scope fix: Trebe, Makby, Emaia, eMedica and ML Humanoids (indices 40–44) were excluded, as the coordinator instructed.

## Method
- **Registry:** empresia.es company pages fetched with curl. Raw HTML is in `dl_a/em_*.html` and the parsed timelines in `em_summary_a.txt`. Current boards are in `admins_a.txt`. The parser is `scripts_a/em.py` and the CSV builder is `scripts_a/build.py`.
- **Websites:** homepages fetched with curl into `dl_a/web/`. For WordPress sites, the latest posts came from `/wp-json/wp/v2/posts`.
- **Other sources:** infoempresa.com via curl, a limited number of WebSearch queries, and WebFetch for pages that return 403 to curl.
- **Empresia slugs resolved through its own search page:**
  - goi-alde-high-speed
  - irisbond-crowdbonding (also irisbond-bat, extinguished 2023)
  - tekmetall-metallurgical-solutions
  - linqcase-industrial-solutions

## Pages read through Chrome (read-only; new tab, then closed)
- https://librebor.me/borme/empresa/bidasoa-metal-78/: paywalled. It shows only "Activa", last updated 30/04/2026, and 3 masked directors since 01/01/2024.
- https://www.empresia.es/empresa/bidasoa-metal-78/: the page redirected away, so no text was read. The tab was closed.

## Failures
- **Empresia server errors** (a generic page on every try) for go4it-solutions, metaposta and bidasoa-metal-78. For these the infoempresa "último anuncio BORME" date is used, so the act type is unknown.
- **librebor.me** returns 403 to curl and is paywalled in Chrome.
- **BATTIA:** no legal entity found on empresia. These were tried and none exist:
  - battia-recycling-technologies
  - battia-technologies
  - battia-recycling
  - battia-tech
  - battia-battery-recycling
- **403 to curl** (read with WebFetch instead): smowl.net, biokemik.eu, fastflooding.com.
- **techleap.nl** returns 403. The Metal 78 round was taken from capital-riesgo.es and otamotz.eus search results.
- **WebSearch** worked, but returned nothing useful for GO4IT, Metaposta, Kaizen Play or Smowltech 2025–26.

## Caveats on the data
- **Empresia's "accounts_years" list** shows 2020–2024 even for companies founded in 2025, so it is a template. Only "Últimas cuentas depositadas" was trusted, and "unclear" is used where it is blank.
- **Revenue ranges** are the empresia "Ventas" label (0.5M, 1M or 2.5M) and are reported verbatim. They are band labels, not figures.
- **The empresia timeline shows about 17 events**, so older capital increases may be missing where the timeline was truncated (H2SITE, NEOS, Optimitive, Irisbond, Veltis, FIK, Diede). Empresia's total act counts are noted where they matter.
- **Empresia's "Consejo de administración" block** lists historical "Socio Único" declarations next to current directors. A past sole shareholder was not treated as a current one.

## Judgement calls
- **Bunt Planet (ex-Donewtech): ABSORBED.** BORME 18/07/2024 records it absorbed and extinguished by Siemens Industry Software SL, yet empresia still shows ACTIVA. The domain redirects to siemens.com. The `status=active` in spinoffs.csv is wrong: it should be absorbed/extinct.
- **Orbik:** BORME on 14/10/2024 published the decision to transform the SLU into a mixed worker cooperative. Its later capital and governance acts sit in the Basque cooperative registry, which was not checked. GROWING rests on the company's own May 2026 release: more than 50 staff, more than €2M revenue in 2025, and a €2M capital increase.
- **Smowltech:** Vicomtech's page says "Exit in 2025". Capital reductions in Mar 2025 (−€10k) and Dec 2025 fit a buy-back of Vicomtech's shares, but this is an inference. Founder Ricardo Vea left the chair on 23/02/2026. Vesmo Legacy Capital (likely the Vea family vehicle, also an inference) is now president, with Jorge and Alejandro Vea Sanz on the board.
- **Addilan: ABSORBED.** On 22/07/2025 the board was replaced by ONA Electroerosión and Maher Holding as joint administrators. Tecnalia's director left, and Addilan is not on Tecnalia's partly-owned page.
- **Diede: ABSORBED.** Gestamp Automoción has been sole administrator since 2017.
- **Goialde: ABSORBED (low confidence).** The entity matched is Goi Alde High Speed SL. Fundación Tekniker has been a director since Dec 2021, which confirms the centre link, and the company sits inside the Goialde group. Goialde Precision SL is a 100% subsidiary of Punteados Goi Alde and was not used.
- **AMETS and INNKIA: GROWING, not ABSORBED.** They were corporate or cooperative joint ventures from birth, not independents folded into a group. Corporate control is flagged in the justification instead.
- **FIK Advanlife: ZOMBIE.** It is a holding company whose last accounts are for 2021. Its registry sheet was closed and then reopened (Art. 378.5 RRM, Aug 2024), and there is no operating activity.
- **DIGIMET: ZOMBIE.** There has been no registry act since Sep 2022 and no blog post since Sep 2021. It is still on Tecnalia's board but has been dropped from the partly-owned page.
- **Acustrain: UNCLEAR.** The only recent acts are powers granted and revoked (2024–26), plus membership of an R&D AIE (2024). The site is frozen at 2022 and the company has 1 employee. It could be dormant, but evidence is short of the 3-year rule.
- **Solarcraft and Revalheat: UNCLEAR.** Each has only its incorporation on record. Both are under 3 years old, so ZOMBIE cannot apply.
- **Kaizen Play: UNCLEAR.** It is an SLU whose sole shareholder is Kayzen Play Ltd. Its only acts are from 2024 and its site carries a 2024 copyright. It is not on Ikerlan's startups page and no link to Ikerlan was found, so the Ikerlan attribution looks wrong.
- **Biolan:** classified GROWING on product launches in 2026 and the Biolan Health merger. Tecnalia's origin claim is unverified. tekniker.es has a "governing-board/biolan-microbiosensores" page, so Biolan's link may be to Tekniker rather than Tecnalia.
- **Metal 78:** classified GROWING on the €4.2M round (Feb 2026) and the Zumárraga plant. Infoempresa says the last ordinary accounts filed are for 2020, which is a compliance red flag next to the growth.
- **Izpitek:** classified GROWING on the 2025 capital increases with IDAE joining. Its website is still a "Coming soon" placeholder.
- **v2 subgroups:**
  - Optimitive and NEOS are WEAK under the literal rule: the lead investors are unnamed and no public investor is named, even though Optimitive disclosed €5M.
  - Metal 78, InspectRail and Irisbond are PUBLIC_LED under the no-lead-identified rule, because a public investor (CDTI or GCRPV/COFIDES) is named alongside the private ones.

## Centre portfolio pages read (2026-10-23)
- **Tecnalia partly-owned page** lists 12 companies: Intellialert, Veltis, Acustrain, Izpitek, NEOS, Nautilus, Ingredalia, H2SITE, GO4IT, FESIA, Biokemik, Aurea.
- **Ikerlan startups page** lists 4: Orbik, INNKIA, Battbelt, AMETS.
- **Vicomtech spin-offs page** lists Irisbond, Smowltech ("Exit in 2025"), Nuuk, Trebe, Makby and Emaia.
