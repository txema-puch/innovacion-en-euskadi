# Voice share: who is the protagonist of the startup conversation?

**Question.** In the public conversation about startups in a region, who speaks — the builders (founders, startup employees) or the institutions (public officials, publicly funded intermediaries)? And how often is the administration itself the news?

No published metric of this exists (searched Oct 2026: Endeavor, Kauffman, Startup Genome measure connectedness, not voice). This is original work.

## Method (v1)

- **Regions:** Euskadi, Comunidad de Madrid, Bay Area (SF + Silicon Valley).
- **Period:** 2025-10-01 → 2026-09-30.
- **Codebook:** `codebook.md` (v1). Categories: FOUNDER, STARTUP_EMP, INVESTOR, PUBLIC_OFFICIAL, PUBLIC_ADJACENT, CORPORATE, PRIVATE_ECOSYSTEM, ACADEMIC, OTHER. **BUILDERS** = founder + startup employee. **INSTITUTIONS** = public official + public-adjacent (tech centres, public incubators, public university management, chambers).
- **Instrument A, press:** ~50 articles per region from regional/business/startup press, ≥3 per month, fixed queries, results taken in returned order. Every named person quoted or presented as speaking is coded. Article-level: `trigger` (what generated the news), `lead_voice` (first person quoted), `headline_actor`.
- **Instrument B, stages:** every named speaker on the agendas of each region's flagship recurring startup events.
- Data: `data/`. Full search queries, exclusions and judgement calls: `logs/`.

## Results v1

### Press (speaker level)

| Region | Articles | Speakers | Builders | Institutions | Official quoted first | Trigger = public announcement |
|---|---|---|---|---|---|---|
| Euskadi | 51 | 79 | 44% | **22%** | **18%** (9/51) | 18% (9/51) |
| Madrid | 50 | 75 | 56% | 12% | 6% (3/50) | 14% (7/50) |
| Bay Area | 50 | 134 | 32% | 10% | 8% (4/50) | 2% (1/50) |

Reading: Basque founders do get press, when they have news (Multiverse Computing is in 18% of Basque headlines). What separates Euskadi from Madrid is institutional voice: about 2x the share of speakers, and 3x as often the first voice in the article. The "administration is the news" trigger separates Spain from the US more than Euskadi from Madrid.

### Stages (named speakers, v1)

| Region | Events | n | Builders | Institutions | Who opens |
|---|---|---|---|---|---|
| Euskadi | B-Venture 2026; South Summit Industry & Energy Bilbao-Bizkaia 2025 | 67 | **22%** | **28%** (≈36% if clusters coded public-adjacent) | Officials at every event (Basque Gov. viceconsejero, Diputación, Bilbao Ekintza) |
| Madrid | South Summit Madrid 2026 (full census) | 477 | 29% | 15% | Minister Óscar López; closed by Ayuso. Top-tier speakers: ~42% builders, ~3% institutions |
| Bay Area | TechCrunch Disrupt 2025 (main stage); YC Startup School 2026 | 54 | 31% (57% at YC) | **4%** | Disrupt: no welcome slot; SF Mayor on day 3. YC: no running order |

B-Venture 2026, the largest Basque startup event: **16% builders, 26% institutions, 21% corporate.** Euskadi is the only region where institutions outnumber builders on stage.

### Stages v2: pitches, prominence, who hosts (`data/stages_v2.csv`, `data/hosts.csv`)

v2 adds pitching founders (mostly as counts, since only 25 are named: 5 at B-Venture, 20 at Disrupt; the rest are "[unnamed founder] <startup>"), a prominence tier per slot, and the organisers/sponsors of each event. It also adds events: Bizkaia Foro de Inversión V, BizkAIa Summit 2026, B Acceleration Week 2026 (Euskadi); Horizon Deep Tech Summit 2025, Startup Grind Madrid (Madrid); Startup Grind Conference 2026, YC Demo Day W26 (Bay Area).

**Rule: pitches are counted apart from voice.** A pitch is a founder being evaluated, not a founder setting the agenda. The headline voice-share figures exclude pitches; pitch counts are reported separately as a measure of how many founders are on stage *as candidates*.

Voice share (named speakers, pitches excluded), builders % / institutions %:

| Region | Original 6 events | All events |
|---|---|---|
| Euskadi | **22 / 29** | **19 / 27** |
| Madrid | 29 / 15 | 31 / 14 |
| Bay Area | 31 / 4 | 41 / 3 |

Pitch presence, reported separately (counts per event in `data/stages_v2.csv`, `session_type=pitch`): Euskadi ~110 pitch slots across B-Venture (~28), SS Bilbao (24), BIND Demo Day (29, upper bound), Bizkaia Foro de Inversión (8) and others; Madrid ~100 South Summit finalists (unnamed) plus Horizon; Bay Area ~20 Disrupt Battlefield and the YC W26 batch (197, roster not confirmed presenters). For reference only, mixing the two: Euskadi 60/13, Madrid 45/12, Bay Area 84/1.

**Headline slots (opening + keynote + closing):**

| Region | n | Builders | Institutions |
|---|---|---|---|
| Euskadi | 26 | 12% | **42%** |
| Madrid | 13 | 0% | **54%** (thin: South Summit has no session data) |
| Bay Area | 15 | 40% | 7% |

- Openings: Euskadi 10 opening speakers, **0 builders, 6 public officials**. Madrid 4, 1 official (the minister). Bay Area: no named opening slots.
- Reading: institutional headline slots are a **Spanish** pattern, not only a Basque one. Bay Area stages give headline slots to builders and investors.

**Who hosts the room:**

| Region | Events with a local public body as organiser, co-organiser or funder |
|---|---|
| Euskadi | **6 of 6** (4 organised/co-organised, 2 funded). B-Venture's "Impulsan" block: SPRI, Basque Government, Diputación de Bizkaia, Ayuntamiento de Bilbao; sponsors also ENISA, Beaz, Up!Euskadi |
| Madrid | 2 of 3 (South Summit: private organisers, institutional support from State, Comunidad and Ayuntamiento) |
| Bay Area | **0 of 4** (only foreign agencies buying pavilions: JETRO, KOTRA, PAIH, IDA Ireland…) |

The cleanest stage finding: **every Basque startup event studied has a public body behind it; no Bay Area one does.** Founder-led contrast cases found: Startup Grind Madrid (chapter series), Startup Grind Conference and YC events (Bay Area). None found in Euskadi in the period. The founder-led Bilbao event of Oct 2026 (SpaceXAI community, ~100 people) falls outside the period and needs its page to be coded.

v2 caveats: BIND Demo Day pitch rows are an upper bound (SPRI lists 30 projects, not who presented); South Summit Madrid's ~100 finalists counted, not named; added Basque events are all in Bizkaia and some partial; YC Demo Day rows are the batch roster; SS Bilbao's sponsor list not found. Single coder.

## Reliability

- AI second coder, blind, 60 articles (20/region): κ = 0.95 trigger, 0.98 lead voice, 0.99 speaker category. See `reliability/agreement.md`.
- **This is an upper bound**: both coders are LLM agents, likely the same model, and converged on the same unwritten conventions.
- **A human second coder on ~20 articles is required before external use.**

## Caveats (read before quoting any number)

1. **Outlet mix differs by region.** Euskadi: mostly regional dailies; El Referente (which republishes SPRI/government releases) was blocked, so institutional voice is likely a floor. Madrid: 16/50 Telemadrid founder segments (inflates builders). Bay Area: TechCrunch funding briefs quote the CEO by design (inflates founders); SF Business Times and Mercury News were unreachable.
2. **Small n.** ~30 builder+institution speakers per region; one article moves the Euskadi institutional share by ~6 points.
3. **Stage coverage is thin.** 2 usable Basque events, 1 Madrid event; sampling frames differ (full census vs main stage). Pitching founders are mostly unnamed on agendas, which understates builders everywhere.
4. **Single coder per region**, with judgement calls on ~1 in 5 articles (all in `notes` columns and logs).

## In progress

- **Trigger deep-dive:** 60 articles per region from general regional dailies only (controls outlet type), finer trigger taxonomy, and whether the startup is the protagonist or a **prop** in a public story.
- **Codebook v2** (from the reliability check): speaker needs attributed words in body text; founder needs explicit label; tie-break rules for public money into a single startup; explicit list of hybrid actors (SPRI, BEAZ, BICs…); new SME_OWNER category.

## Files

- `codebook.md` — v1 codebook.
- `data/press_{euskadi,madrid,bayarea}.csv` — one row per speaker (articles with none have one NONE row).
- `data/stages.csv` — one row per stage speaker.
- `logs/` — queries, exclusions, blocked sites, judgement calls per region; `stages_madrid_codes.txt` = manual codes for the South Summit census.
- `reliability/` — second coder sample, codes and agreement report.
- Raw scraped pages: `../../raw/voice/` (gitignored, local only).
