# Press coding log — BAYAREA (Instrument A)

Coded 2026-10-23. Codebook v1 (`codebook.md`). Output: `press_bayarea.csv`, with 50 articles and 134 speaker appearances (123 distinct people) plus 7 articles that have no named speaker (one `NONE` row each).

## 1. Sources and access

| Outlet (preferred list) | Status |
|---|---|
| SF Standard (sfstandard.com) | Accessible. Full text read. 20 articles |
| SF Chronicle (sfchronicle.com) | Accessible with curl. Full article text is in the HTML, so no paywall truncation was seen. 9 articles |
| KQED (kqed.org) | Accessible. 5 articles |
| TechCrunch (techcrunch.com) | Accessible. Used only when the article text places the startup or firm in the Bay Area. 16 articles |
| SF Business Times / Silicon Valley Business Journal (bizjournals.com) | **Not accessible.** The search tool refuses the domain ("not accessible to our user agent"), and curl gets HTTP 403. 0 articles |
| Mercury News / SiliconValley.com | **Not accessible.** The search tool refuses both domains. 0 articles |
| SF Examiner (sfexaminer.com) | It appeared in the search results, but fetches returned **HTTP 429** (WebFetch, tried twice) or a bot "Security Check" challenge page (curl). Every Examiner result was skipped (see §4). 0 articles |

Fetch method: curl (desktop UA), then extraction of the `<p>`/`<h2>`/`<blockquote>` text into `dl/` and `txt/`. Speakers were found by reading every sentence that carries an attribution verb or a quotation mark, and the article body was read when context was needed (the full texts are in `txt/`).

## 2. Queries used

All searches used the WebSearch tool in "standard" mode. Each fixed query had the month appended, e.g. `San Francisco startup October 2025`.

**Round 0 (unrestricted, Oct 2025, all 5 queries).** This returned mostly event listings, newsletters and aggregators that are not regional press. It was discarded as a sampling frame.

**Round 1 (main frame).** `allowed_domains = [sfstandard.com, sfchronicle.com, kqed.org, sfexaminer.com, techcrunch.com]`. An earlier attempt that also listed bizjournals.com, mercurynews.com and siliconvalley.com errored (inaccessible domains).

| Month | Queries run |
|---|---|
| 2025-10 | all 5 fixed queries |
| 2025-11 | all 5 |
| 2025-12 | all 5 |
| 2026-01 | San Francisco startup; Bay Area startup funding; SF tech ecosystem; Silicon Valley startup raises |
| 2026-02 | all 5 |
| 2026-03 | San Francisco startup; Silicon Valley startup raises; San Francisco AI startups city |
| 2026-04 | San Francisco startup; SF tech ecosystem; Bay Area startup funding |
| 2026-05 | San Francisco startup; SF tech ecosystem; San Francisco AI startups city; Bay Area startup funding |
| 2026-06 | San Francisco startup; SF tech ecosystem; Silicon Valley startup raises |
| 2026-07 | San Francisco startup; SF tech ecosystem; Bay Area startup funding |
| 2026-08 | San Francisco startup; SF tech ecosystem; San Francisco AI startups city |
| 2026-09 | all 5 |

**Round 2 (gap-filling for thin months and outlets).**
- `San Francisco AI startups city` and `San Francisco startup`, both with no month, `allowed_domains=[kqed.org]`. KQED never surfaced in the Round 1 mixes.
- `San Francisco startup February 2026` on [sfstandard, sfchronicle, kqed].
- `SF tech ecosystem February 2026` on [sfstandard, kqed].
- `San Francisco AI startups city February 2026` on [sfstandard, kqed, sfchronicle].
- `San Francisco startup October 2025` and `San Francisco startup May 2026`, both on [sfstandard, sfchronicle, kqed].
- `Silicon Valley startup raises February 2026` on [sfstandard, kqed, sfchronicle] **failed: the session web-search budget ran out.**

**Important:** the search engine does **not** filter by date. Every query, whatever month it named, returned much the same pool of URLs. The sample is therefore best described as "the in-period, in-scope URLs from the pooled results, assigned to their actual publication month." Within each month, items were taken in the order first seen, until the month had at least 3 (usually 4–5). The pool was then filled to 50 from the gap-filling rounds.

## 3. Inclusion rules applied (judgement calls)

1. **Scope.** The article must mainly cover the Bay Area's startup, VC or tech-ecosystem news: a startup (round, launch, lease, profile, dispute), a VC fund or accelerator, an ecosystem trend or labour-market story about tech, or city–tech relations. Included:
   - stories about SF AI companies' office leases, since the startup is the actor;
   - tech-jobs stories;
   - city-economist and mayor stories about AI or tech.
2. **Spillover stories excluded.** Pieces where AI wealth is only the backdrop for another sector were left out (housing prices, restaurants, general city recovery, tourism). The exception is a piece where a startup is the main actor, such as Brownstone's pods in the KQED housing story, which is included.
3. **TechCrunch locator rule.** A TechCrunch article was included only when its text places the company in the Bay Area. National "$100M+ AI rounds" and unicorn lists were excluded.
4. **Outlet self-promotion excluded.** TechCrunch Disrupt, StrictlyVC and Startup Battlefield ticket, countdown, side-event and "how to watch" posts were excluded. The editorial report of the mayor's Disrupt talk is included.
5. **Gossip and op-eds excluded.** The SF Standard's "The Waggle" gossip column and the SF Standard opinion piece of 2026-06-30 were left out.

## 4. Skipped, failed or excluded URLs

**Fetch failures / blocked (not read, not coded)**
- sfexaminer.com, every URL. Tested: `.../why-venture-capital-just-couldnt-quit-san-francisco-in-2025/...` (429 and a curl challenge page) and `.../san-franciscos-ai-startups-ramp-up-hiring/...` (429). Other Examiner results were not tried after that: sf-startups-set-yearly-funding-record, ai-startups-reap-rewards…, sf-ai-startups-benefitting-from-2025…, san-francisco-ai-boom-tech-jobs-plateau, ai-industry-boomed-in-2025…, donald-trump-100000-visa-fee…, more-than-half-of-venture-dollars…, sf-bay-area-get-record-portion… Q1, venture-industry-marked-by-extreme-concentration-in-q1, sf-could-soon-see-ai-jobs-boom…, bay-area-billionaire-launches-contest…, coalition-pledges-25-million…
- The SF Chronicle Bezos/Prometheus page failed through WebFetch (a JS error page) but **loaded fine with curl** and is coded.

**Read but out of period:**
- KQED `news/12052247` (2025-08-14)
- KQED `news/12103983` "AI Founders Cheer Trump…" (2026-10-11)

**Out of period by URL or date (not fetched):** TC Town Series B (2026-10-19), TC Flapping Airplanes (2026-10-21), TC Etched $40B (2026-10-05), TC Apate (2026-10-14), SFS "AI agent craze" (2026-10-19), Examiner Q3 venture drop (Oct 2026), Chron Goldman Sachs conference (Sep 2025), Chron Microsoft Ignite announcement (pre-period).

**Read and excluded as out of scope:**
- SFS 2025-10-08 "Your dream home in SF just got pricier. Thanks, AI." Housing spillover.
- TC 2025-10-23 "San Francisco Mayor Daniel Lurie is coming to Disrupt 2025". Outlet event promo with no quotes.
- Chron 2025-12-22 "Buyouts and NDAs: How the AI boom is feeding into S.F. restaurants". Restaurant spillover.
- SFS 2026-01-08 "Boom loop watch… 19 charts". General city recovery.
- TC 2025-12-19 "OpenAI is reportedly trying to raise $100B". No regional locator in the text.
- TC 2026-01-18 Sequoia investing in Anthropic. No regional locator.
- TC 2026-02-04 SNAK Venture Partners fund. No regional locator.
- TC 2026-06-18 Baseten reportedly raising $1.5B. No regional locator.
- TC 2026-07-21 Sila raises $300M. No regional locator.
- TC 2026-07-30 Simile raises $200M. No regional locator.
- TC 2026-09-10 Mach Industries. Huntington Beach, Southern California.
- KQED 2026-03-21 "Facade Mash". A founder's side-project website; local culture, not startup news.
- SFS 2026-02-21 "The Waggle" gossip column. Mostly celebrities, sports and politics.

**Excluded by title or type without fetching (clearly non-regional, promo, spillover or off-topic):**
- Non-regional: TC Lovable (Stockholm), TC Meta buys Manus, TC Positron (Reno), TC Thrive Holdings, TC Pool app, TC Instinct/Meta Muse, TC Anthropic ID verification.
- National roundups: the TC lists of "$100M+ US AI startups" (2025 and 2026), the unicorn lists, the fusion list, the 2025 layoffs list, "AI got a vibe check", "AI startups eating venture", "AI seed valuations".
- All TC Disrupt, StrictlyVC and Startup Battlefield promo pages.
- General economy or spillover:
  - SFS "AI IPO clock is ticking… buy your home now" (2026-02-17, housing), SFS "year it became cool to bet on SF real estate" (housing), TC "SF housing market has lost its mind".
  - SFS "How do San Franciscans feel about AI", SFS hospitality/tech jobs (2026-06-26), SFS surveillance (2026-03-25).
  - Chron unemployment rises, Chron tourism and conferences, Chron downtown small-business fund, Chron housing nonprofit fund, Chron "biggest challenges facing California's economy".
- Big-corporate or trade-show stories: Chron Semicon West move, Chron 2026 tech layoffs, the Chronicle 200 list, SFS Tubi.
- Op-ed: SFS opinion 2026-06-30.

**In-scope candidates seen but not coded (target of 50 already reached):**
- SFS 2026-06-19 Midjourney spa in Union Square
- SFS 2026-09-30 Corgi cafe expansion
- Chron Corgi cafe review (~Sep 2026)
- Chron Databricks downtown lease (~Apr 2026)
- Chron "tech firms move toward Showplace Square" (~Jan 2026)

These would have added more STARTUP_NEWS-type items.

## 5. Coding conventions and judgement calls

- **Organisation as headline actor.** The codebook categories describe people, but many headlines name a company. A startup or "AI companies" as headline actor was mapped to `FOUNDER` (the builder side), a VC firm to `INVESTOR`, and "San Francisco" or the city to `PUBLIC_OFFICIAL`. Places with no actor got `NONE`. This mapping inflates headline_actor = FOUNDER (30 of 50). Use headline_actor only with that caveat.
- **lead_voice** is the first *named* speaker. Anonymous sources and unnamed spokespeople were skipped. This applies to the Sierra lease story (2025-11-03), where an anonymous source and an unnamed spokesperson come first.
- **Not coded as speakers:**
  - organisation-only statements ("the company said", JLL/Cushman data);
  - unnamed sources;
  - people who appear only in photo captions;
  - people who are mentioned but do not speak;
  - the outlet's own hosts or reporters.
- **Indirect quotes count**, as do quotes re-used from earlier interviews, X/LinkedIn posts and blog posts. Each case is flagged in `notes`.
- **First name only** (e.g. "Shaun", "Steven", "Stephanie"): coded as named persons in `OTHER`, with a flag.
- **CEO versus founder.** If the article says founder or co-founder, the person is FOUNDER. If it says only "CEO", FOUNDER was used where founder status is well known (Litman/Aescape, Laqua/Corgi, Stallworth/Brownstone), with the note "founder status from general knowledge". Known non-founder CEOs are STARTUP_EMP (Dulianinov, Bright Machines).
- **Universities.** Public-university tech-transfer and career-services staff are `PUBLIC_ADJACENT` (UC Berkeley, SF State, WARF/UW-Madison). Entrepreneurship centres and career offices at private universities are `PRIVATE_ECOSYSTEM` (CMU Swartz, UChicago Polsky, USF career services). Researchers speaking as experts are `ACADEMIC`. This is a judgement call. Treating all university staff as PUBLIC_ADJACENT would add 3 to INSTITUTIONS (17 instead of 14).
- **VC-run programmes.** a16z Speedrun's GM is coded `INVESTOR`. The a16z-backed Horowitz Andreessen Academy CEO is coded `PRIVATE_ECOSYSTEM`. YC's Paul Graham is coded `PRIVATE_ECOSYSTEM` (accelerator).
- **Big-tech or large-company executives are `CORPORATE`.** Examples: Zoox (Amazon-owned), Uber CTO, Salesforce's Benioff, Indeed, CoStar, JLL, Colliers, Compass.
- **Founders of now-large companies** count as FOUNDER when speaking as founders, e.g. Patrick Collison commenting on a startup.
- **Federal officials are PUBLIC_OFFICIAL but not regional.** RFK Jr. (HHS) and the Presidio Trust (a federal agency) are coded PUBLIC_OFFICIAL. Emil Michael (DoD official, speaking about his time at Uber) is coded `OTHER`.
- **Trigger calls:**
  - Mayor Lurie at TechCrunch Disrupt: `PRIVATE_ECOSYSTEM` (private event).
  - Midwestern university hub: `PUBLIC_ANNOUNCEMENT`. It is an institutional programme run by a mixed public/private consortium.
  - Data features, trend features and labour-market pieces: `OTHER`.
  - Prospective-IPO analysis: `OTHER`.
  - The Anthropic IPO-filing story: `STARTUP_NEWS`.
- **pr flag:** no articles were flagged. None looked like a republished press release.

## 6. Repeated voices (speaker-level counts are appearances, not people)

- Ted Egan (SF chief economist): 5 appearances, half of all PUBLIC_OFFICIAL appearances (5 of 10).
- Daniel Lurie (mayor): 3.
- Enrico Moretti (UC Berkeley): 3.
- Bret Taylor, Scott Wu, Sam Altman: 2 each.
- There are 123 distinct people.

## 7. Limitations

1. **The outlet mix differs from the brief.** Business Times/SVBJ and Mercury News could not be reached, and the Examiner was blocked. The sample is therefore SF Standard 20, TechCrunch 16, SF Chronicle 9 and KQED 5. TechCrunch is national tech trade press and is founder-heavy by design (funding briefs quote the CEO). The SF Standard and Chronicle lean toward real-estate, culture and labour angles, where economists and brokers speak. The result is SF-centric: there is little South Bay or Peninsula coverage.
2. **No date filter, so sampling is not cleanly "in order".** Results recur across monthly queries, and allocation was "first-seen, in-period, in-scope". February 2026 has only **2** articles, below the target of 3: in-scope February results were scarce and the search budget ran out. March has 7.
3. **Search-engine ranking is itself a filter.** It favours popular feature pieces and TechCrunch, so this is not a census or a random sample of regional coverage.
4. **Coding was done by one coder with no reliability check.** Speaker extraction used attribution-sentence filtering plus reading; a missed attribution is possible in long features. The organisation-to-category mapping for headline_actor is a convention, not something the codebook specifies.
5. **The Bay Area's institutional voice is largely economists and the mayor**, not programme agencies. Only one PUBLIC_ANNOUNCEMENT trigger appeared in 50 articles, which is itself a finding but could partly reflect the outlet mix.
