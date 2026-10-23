# Voice-share codebook (v1, 2026-10-23)

Question: in the public conversation about startups/entrepreneurship in a region, who is the protagonist — the builders (founders, startup employees) or the institutions (officials, public agencies)?

Period: 2025-10-01 → 2026-09-30. Regions: EUSKADI (Basque Country, CAPV), MADRID (Comunidad de Madrid), BAYAREA (SF + Silicon Valley).

## Two instruments

### A. Press
Unit 1 = article. Unit 2 = each named person who is quoted (direct or indirect quote) or presented as speaking/announcing in the article.

Inclusion: article is primarily about the region's startup/entrepreneurship/tech-ecosystem news (a startup, a round, a programme, an event, an ecosystem policy, an ecosystem ranking). Exclude: pure big-corporate news, opinion columns written by the person themselves (record separately as `op_ed=yes` if you want, but do not include in main counts), job ads, press releases republished verbatim with no outlet byline (flag `pr=yes` instead of excluding when unsure).

Sampling: spread across the 12 months (aim ≥3 articles per month). Use fixed search queries (record them). Take results in the order the search returns them; don't cherry-pick. Target 50 articles per region.

### B. Stages
Unit = each named speaker/panellist/keynote on the published agenda of the region's 2–3 flagship recurring startup-ecosystem events held in the period (or the latest edition if none fell in the period — record date).

## Speaker categories (pick ONE, the role in which they appear)

- `FOUNDER` — founder / co-founder / CEO-founder of a startup or scale-up (company < ~15 years old, venture-style growth ambition). Includes founders of companies that became large if they appear as the founder.
- `STARTUP_EMP` — non-founder employee/executive of a startup or scale-up.
- `INVESTOR` — private VC, angel, private fund, family office, corporate VC.
- `PUBLIC_OFFICIAL` — politician, government department, public agency or public company staff (e.g. SPRI, BEAZ, Diputación, ayuntamiento, ENISA, CDTI, ICO/Axis, Innobasque, public VC vehicles like Basque Fondo/Seed Capital Bizkaia, city of SF, Governor's office).
- `PUBLIC_ADJACENT` — publicly funded intermediaries: technology centres (Tecnalia, Vicomtech, BRTA…), public BICs/incubators, public university management (rector, TT office), chambers of commerce.
- `CORPORATE` — executive of an established large company (non-startup).
- `PRIVATE_ECOSYSTEM` — private accelerators, associations, community organisers, consultancies, law firms, media/event organisers not public.
- `ACADEMIC` — researcher/professor speaking as expert.
- `OTHER` — anything else; explain in notes.

Grouping for headline metrics:
- BUILDERS = FOUNDER + STARTUP_EMP
- INSTITUTIONS = PUBLIC_OFFICIAL + PUBLIC_ADJACENT

## Article-level codes

- `trigger` — what generated the news:
  - `STARTUP_NEWS` (a startup's round, launch, customer, milestone, exit)
  - `PUBLIC_ANNOUNCEMENT` (a programme, grant, public fund, plan, institutional event, award given by a public body, official visit)
  - `PRIVATE_ECOSYSTEM` (private event, private fund launch, ranking by private actor)
  - `OTHER`
- `lead_voice` — category of the first person quoted (or NONE).
- `headline_actor` — category of the actor named in the headline (or NONE).

## Output format (CSV, UTF-8, comma-separated, quote fields with commas)

Press, one row per speaker (articles with no speakers get one row with category NONE):
`region,article_id,date,outlet,url,headline,trigger,headline_actor,lead_voice,speaker_name,speaker_org,category,pr,notes`

Stages, one row per speaker:
`region,event,edition_date,agenda_url,speaker_name,speaker_org,category,session_type(keynote|panel|pitch|other),notes`

Record ambiguous calls in `notes`. Never invent people or articles: every row must come from a page you actually read.
