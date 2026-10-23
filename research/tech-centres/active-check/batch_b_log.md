# Batch B log: active spin-offs, indices 40-79

Run date: 2026-10-23. The split was computed with `python3 -I`: `status=='active'` gives 80 rows, and this batch is `[40:80]`, Trebe through SIAPS (40 companies).

## Method / pages read
- **empresia.es** (fetched with curl, parsed locally): one company page each for all 40 companies, plus follow-up pages. The follow-ups were `makby-eva`, `idelt-ingenieria-de-desarrollo-de-prototipos`, `avs-added-value-industrial-engineering-solutions` and `grupo-empresarial-alcor`, and search pages for makby, ml humanoids, idelt, i tribomat, meshind, mizar and medical innovation technologies. I extracted acts, boards, capital, the sales band and the years of accounts.
- **infoempresa.com** (curl): 35 company pages. Its employee and revenue ranges are mostly the default "1-9 / <2M", so I treat them as modelled and weak.
- **Company websites** (curl home pages, plus news, legal and about pages where they exist): trebe.org (+blog), makby.com (+about, privacy), emaiahealth.com, emedicahealth.com (+blog, privacy, terms), idelt.com (+noticias, privacy), a-v-s.es, atten2.com (+noticias), masermic.com (+noticias), h2greem.com (+blog), i-tribomat.eu (+about, impressum), optidelbiosystems.com (+blog), bioplastics4health.com, ltkcryo.com, meshind.com, cidecell.com, lanzobatteries.com, kudebatt.com, emissarycosmetics.com (+noticias), kera-coat.com, lipiwell.com (+blog), basquevolt.com, bcaremb.com (+news), simuneatomistics.com, evolgene.com (+about), optec4life.com, novananomed.com, taldeki.com, atlasmolecularpharma.com (+investors, partners), adaptamtx.com, bideroad.com.
- **WebFetch:** bcaremb.com/en/news, meshind.com, makby.com, i-tribomat.eu/about, atten2.com/noticias, the Vicomtech ML Humanoids announcement, and graphenea.com/blogs/graphene-news. Curl got HTTP 429 on Graphenea, but WebFetch worked.
- **WebSearch (working):** about 20 queries. They were for Atlas/Inveready, Taldeki, OBS, Graphenea, Itsas Balfegó, Kudebatt, Atten2, AVS, LANZO, H2Greem, Trebe, Matxitxako, Evolgene, CIDEcell, SIAPS, Optec4life, IDELT, Emaia, Kera-Coat and Basquevolt.
- **Chrome (claude-in-chrome): not used.** I read no pages through Chrome.

## Failures / not resolved
- Sites that did not resolve: makby.com without www (www works), mlhumanoids.com, itsasbalfego.com, prospectbiotech.com, hylezitek.com, akribea.com, siaps.eu/.es, obsbattery.com. protellix.com is a domain-for-sale page.
- MESHIND has no empresia match under its brand name, so its legal entity is unknown. ML Humanoids is not yet in empresia (announced 16/10/2026).
- I could not read the empresia page for Mizar Health SL (the slug redirects to search), so the current status of the eMedica owner is unknown.
- i-TRIBOMAT is an Austrian GmbH. I did not check the Austrian Firmenbuch.
- librebor.me and einforma were not needed and were not used.
- Many news pages carry no dates: Atten2, BCARE, Graphenea, IDELT, Taldeki. Those items are recorded as undated.

## Judgement calls
- **Funding:** I counted a capital increase or VC entry in the last 24 months as funding evidence and classified it GROWING. That applies even when the nominal amount is tiny (Simune, SIAPS, Prospect, Optec4life), because the share premium is unknown. Those are weak GROWING calls.
- **eMedica → ABSORBED.** EMEDICA SL was sold to Grupo Empresarial Alcor in 2020 and absorbed into Mizar Health SL (extinguished 18/11/2022). Alcor has been in concurso since 11/02/2025 and in liquidation since 25/03/2025. The brand site is still live, but its legal notice names the extinct entity. I set insolvency_flag at the parent level.
- **IDELT → ABSORBED.** Its parent is Walter Pack SL (per infonif) and it sits within NER Group.
- **OBS → ABSORBED.** The company was created by MAIER and MAIER chairs the board. KUDEBATT is controlled by Hondaner (sole administrator) but has several shareholders, so I kept it OPERATING.
- **AVS:** the empresia slug `added-value-solutions` is an unrelated Valencia accounting firm. The correct entity is AVS ADDED VALUE INDUSTRIAL ENGINEERING SOLUTIONS SL (B20912408). The CESCE revenue series ends in 2022.
- **Makby:** the CSV caveat that it might be French is resolved. The site's privacy policy names Makby Eva SL, Paseo Mikeletegi 65, Donostia, constituted Oct 2025.
- **Lipiwell:** BORME shows initial capital of 3,000 and a May 2026 increase to 20,000. The CSV's "20,000 at constitution" is wrong. The 2026 money came from AZTI, not an outside investor, so I classified it OPERATING.
- **Emissary:** the empresia "Cargos" panel still shows CIDETEC as socio único. That is stale, because BORME recorded the loss of single-shareholder status in Jun 2020.
- **Kera-Coat → UNCLEAR, not ZOMBIE.** The website is frozen at 2017, but accounts for 2024 were deposited and report 4 employees.
- **Matxitxako → UNCLEAR, not ZOMBIE.** There have been no registry acts since 2020, but accounts for 2023 were filed.
- **Hylezitek → UNCLEAR.** Its only recent acts are tax-AIE memberships.
- **ML Humanoids and Protellix → UNCLEAR.** Both are under 2 weeks old.
- **i-TRIBOMAT → UNCLEAR.** The last dated news is June 2024.
- **SIAPS:** search results suggest Lortek's own weld-inspection startup is SIAWELD, a different company. SIAPS is BTV-backed, with Lortek on its board.
- The empresia "Últimas cuentas" years come from its availability table: years marked "Inmediata" were treated as deposited.
