# Method: tech-centre alumni and startup founders (C-028 gap)

Written 2026-10-23, before any counting. Research line "talent" for `innovacion-en-euskadi`.

## Questions

1. **Alumni → startups.** How many people publicly presented as former staff/researchers of Tecnalia, CEIT, Ikerlan, Vicomtech (in that order; others if time) founded, co-founded, or held CTO/early roles in startups — anywhere?
2. **Founders → origin.** For the centre spin-offs (`research/tech-centres/spinoffs.csv`) and the publicly funded startups (`research/public-funded-startups/startups.csv`, Ekintzaile 2021), where did the founders come from?

This is a **findable-evidence census, not a population estimate**. Output counts are lower bounds of what is publicly documented, not of what exists.

## Definitions

- **Centre ex-staff ("alumni")**: a person whose public founder bio, company team page, press article or centre news says they worked/researched/did a PhD or thesis at the centre (or a named predecessor: Fatronik, Inasmet, Labein, Robotiker, ESI for Tecnalia). PhD students and interns at the centre count (flagged "PhD/thesis at centre" in notes) because the centres train them. Contractual staff of a centre still employed there while founding a formal spin-off count as alumni (they are the centre's own talent).
- **Founder**: publicly presented as founder or co-founder. **CEO/CTO at founding** counts as founder-equivalent if press says so.
- **Early role**: CTO, CSO, or "one of the first employees"/joined within ~2 years of founding, when the source says so. Later senior hires (e.g. a CEO appointed 10 years in) are NOT early roles; noted separately if found.
- **Startup**: a company founded to commercialise a new product/technology with growth intent, typically <10 years old at the time of the person's involvement. Excluded: consultancies/engineering service firms that are clearly a one-person practice, established-company subsidiaries, joint ventures created by corporates (unless presented as a startup), and the centres themselves.
- **Formal spin-off**: the startup appears in `spinoffs.csv` (any centre). Otherwise "independent".
- **Location**: registered/headquarters city as on the company site or registry; "Euskadi" vs "rest of Spain" vs "abroad".
- **Origin categories (Step 2)**: `centre` (any Basque tech centre/BRTA member), `university` (academic staff/PhD at a university, incl. UPV/EHU, Mondragon Unibertsitatea, Deusto, TECNUN when not via CEIT), `industry` (prior employment at an established company), `abroad` (prior career mainly outside Spain), `first_job` (founded straight out of studies), `unknown`. A company with mixed founders gets the category of the lead founder, mixed noted in notes. Corporate JVs → `industry`.

## Sources (in order of preference)

1. Data already in the repo: `spinoffs.csv` (`founder_type`, notes), `active_check.csv` (`founders_still_in`), and the URLs cited there.
2. Company websites: team/about pages (direct URLs, Wayback if down).
3. Centre news and success-story pages (tecnalia.com, ceit.es, ikerlan.es, vicomtech.org).
4. Press articles (URLs in repo CSVs; direct URLs to known outlets).
5. Public Crunchbase pages (if reachable without login), public LinkedIn pages only one at a time manually, without login, never via the user's Chrome session.
6. BORME administrator names via empresia.es: only to match a named founder to a company, never to infer career history.

WebSearch may be exhausted; no workaround (no curl-based search engines). Read-only Chrome only for non-LinkedIn blocked pages, new tab, closed after, logged in `log.md`.

## Personal-data rules

- Per-person rows (`founders_public.csv`) only for people publicly presented as founder/executive on a company site or in press, with that URL.
- Recorded: name, company, role, centre/origin as stated in the public bio, source URL. Nothing else: no ages, contact data, education beyond the origin field, or career detail beyond the public founder bio.
- People who appear only in BORME (no public founder presentation) are not recorded by name in deliverables; they may contribute to company-level origin counts only if a public source states the origin.

## Biases (expected direction)

- **Findability**: people with English-language, startup-style public profiles (VC-backed, press-covered) are over-represented; founders of small, local, Spanish/Basque-language companies are under-represented. Centre staff who founded engineering SMEs may not call themselves "founders".
- **Survivorship**: failed/dissolved startups lose websites and team pages; Wayback helps partially. Counts of alumni-founded startups skew to survivors and recent companies.
- **Self-presentation**: founders may emphasise or omit centre affiliation (a centre credential helps in deep-tech fundraising; it may be omitted in software/consumer startups). Centres publicise their formal spin-offs, not alumni who left to found independently → formal spin-offs are over-represented in Step 1.
- **Language**: sources in Spanish/Basque/English; Basque-only pages may be missed.
- **Selection by method**: without a search engine, discovery leans on known names (repo CSVs, centre pages), which biases toward formal spin-offs and press-covered companies. Independent alumni startups abroad are the hardest to find and will be under-counted. This bias works *against* the "leaving the region" story, so any outside-Euskadi count is a floor.
- **Single coder**, no second check.

## What I will NOT do

- No automated scraping of LinkedIn or any people-search site; no logged-in sessions; no forms.
- No estimates of the total alumni population or founder rates presented as facts; any ratio is labelled `derived` with arithmetic and denominator caveat.
- No inference of a person's origin from name, surname or location.
- No private details; no people who are not publicly presented as founders/executives.
- No editing or committing in the repo.
- Absence of evidence for a given company is recorded as `unknown`, not as "not from a centre".
