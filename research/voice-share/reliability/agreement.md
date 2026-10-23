# Inter-coder reliability: press voice share (codebook v1)

Second coder: independent agent, coded blind from the article text. It did not open the first coder's CSVs or logs until `second_coder.csv` was written.
Sample: 20 article_ids per region drawn with `random.Random(42).sample(sorted(unique_ids), 20)` (`sample.py`, `sample.csv`). That gives 60 articles, 98 speakers matched by name, and 113 coded rows in total.

## Read this first: what the numbers mean

The agreement is almost perfect, and that is a warning sign. Both coders are LLM agents and probably run on the same model. They converged on the same unwritten conventions, often in near-identical note wording:
- a startup named in the headline maps to FOUNDER
- the lead voice is the first *named* speaker
- a CEO whose founder status isn't stated is STARTUP_EMP
- first-name-only members of the public are coded OTHER

So these kappas measure **self-consistency of one coding model**, not how reliably the codebook transfers between people. Treat them as an upper bound. A human second coder on about 20 articles is still needed before the reliability numbers go into anything external. The "latent disagreement" list below shows where a human would most likely diverge.

## Agreement

| Variable | Unit | n | % agree | Cohen's κ |
|---|---|---|---|---|
| trigger | article | 60 | 96.7% | **0.95** |
| lead_voice | article | 60 | 98.3% | **0.98** |
| speaker category (matched by name) | speaker | 98 | 99.0% | **0.99** |
| headline_actor | article | 60 | 96.7% | 0.95 |
| pr flag | article | 60 | 96.7% | 0.87 |

By region:
- trigger κ: Euskadi 1.00, Madrid 1.00, Bay Area 0.82
- lead_voice κ: Euskadi 0.94, Madrid 1.00, Bay Area 1.00

Speaker detection:
- **Only the first coder found 3 speakers.** All three are in EUS-P16: Pradales, Jauregi and d'Anjou, who appear in the photo caption only.
- **Only the second coder found 1 speaker.** BA41: Mayor Daniel Lurie, quoted directly near the end of the piece.

## BUILDERS / INSTITUTIONS share (speaker level, sampled articles only)

| Region | Coder 1: speakers / B / I | Coder 2: speakers / B / I | Δ builders | Δ institutions |
|---|---|---|---|---|
| Euskadi | 30 / 26.7% / 43.3% | 27 / 25.9% / 37.0% | −0.8 pp | **−6.3 pp** |
| Madrid | 34 / 52.9% / 14.7% | 34 / 52.9% / 14.7% | 0 | 0 |
| Bay Area | 37 / 37.8% / 5.4% | 38 / 36.8% / 7.9% | −1.0 pp | +2.5 pp |

The lead-voice counts (builder or institution) are identical across coders except for Euskadi institutions: 6 for coder 1, 5 for coder 2. Each share delta comes from **one rule**:
- Euskadi: whether people named only in a photo caption count as speakers
- Bay Area: Lurie, whom coder 1 missed

The Euskadi institutional share is sensitive to the caption rule. With n≈30 speakers, one article moves it by 6 points.

## Every disagreement

| Article | Variable | Coder 1 | Coder 2 | Reason | Codebook-supported reading |
|---|---|---|---|---|---|
| EUS-P16 | speakers + lead_voice | Pradales, Jauregi, d'Anjou (PUBLIC_OFFICIAL); lead PUBLIC_OFFICIAL | none; lead NONE | The three are named only in the photo caption ("en la presentación"). The quotes in the text go to unnamed "responsables económicos". | **Ambiguous.** "Presented as speaking/announcing" can cover a presenter in a caption. The stricter reading (coder 2) is more defensible because no words are attributed to anyone. Needs a rule (v2 #1). |
| BA41 | missed speaker | – | Daniel Lurie, PUBLIC_OFFICIAL | Lurie is quoted directly in the closing section. Coder 1 stopped early or overlooked him. | **Coder 2.** The codebook includes every named person who is quoted. |
| EUS-P09 | category | Carlos Escobar = FOUNDER | OTHER | The text says the project was "impulsado por Maceira y Escobar" and calls him a cardiologist at La Paz. It never calls him co-founder. | **Coder 2, weakly.** FOUNDER should need an explicit founder role. Coder 1's own note admits "could be ACADEMIC/OTHER" (v2 #4). |
| BA02 | trigger | OTHER | STARTUP_NEWS | Trend piece on AI-company coffee pop-ups, hung on Perplexity's Seoul café launch. | **Ambiguous.** A launch is STARTUP_NEWS, but the codebook has no rule for features or trend pieces (v2 #5d). |
| BA41 | trigger | OTHER | STARTUP_NEWS | Analysis of the local impact of upcoming OpenAI/Anthropic IPOs. | **Coder 2 for consistency.** Coder 1 coded the twin piece BA35, an IPO-impact analysis from another outlet, as STARTUP_NEWS. Same rule gap (v2 #5d). |
| BA16 | headline_actor | FOUNDER | NONE | "San Francisco is home to the AI boom. But where exactly are these companies?" | **Coder 1.** Coder 2 mapped the collective "AI companies" to FOUNDER in BA02 and BA28 but not here, so coder 2 is the inconsistent one (v2 #3). |
| BA35 | headline_actor | FOUNDER | NONE | "The AI IPOs are coming…" | **Coder 1, same logic.** The IPOs belong to named startups in the standfirst (v2 #3). |
| EUS-P08 | pr | yes | no | JSON-LD `author` = "Diputación Foral de Bizkaia". The institution wrote the text. | **Coder 1.** Coder 2 missed the byline (v2 #6). |
| MAD48 | pr | no | yes | The Las Rozas piece reads like sponsored municipal promotion, but there is no explicit sponsor marker. | **Coder 1, weakly.** No hard evidence. The codebook says flag when unsure, so this is borderline (v2 #6). |

## Latent disagreements: same code from both coders, judgement flagged in notes

Both coders made the same call on each of these and noted it was a judgement call. A human coder would probably split on several:

1. **Epigraph or general quotes.** In EUS-P03, Scott Aaronson's paraphrased line in the lede makes lead_voice ACADEMIC instead of FOUNDER. Both coders kept it.
2. **Unnamed spokespeople.** In BA06, BA33, BA45 and MAD37, "a Sierra spokesperson" or "desde Komvo" speaks first. Lead voice was taken as the first *named* speaker, which the codebook does not say.
3. **CEO without founder evidence.** MAD28 (Landa) and MAD35 (Naranjo) were coded STARTUP_EMP. MAD03 (Cuadrado, "creador") was coded FOUNDER. The builder total is unaffected, but FOUNDER vs STARTUP_EMP is unstable.
4. **Public money into a startup:**
   - EUS-P14: SETT stake, minister quoted first, headline frames the Government as the actor
   - EUS-P49: IDAE grant
   - MAD28: startup inside a Comunidad programme

   All were coded STARTUP_NEWS. A reasonable coder could call them PUBLIC_ANNOUNCEMENT, which would move the "institution-triggered" share in Euskadi.
5. **Joint private/public reports** (EUS-P33 Scoutyn + Gobierno Vasco, MAD50 Scoutyn + madri+d) were coded PRIVATE_ECOSYSTEM. The public madri+d report (MAD02) was coded PUBLIC_ANNOUNCEMENT.
6. **Private events with public sponsors or speakers:**
   - MAD45 MERGE: only public officials speak
   - EUS-P38: programme mainly funded by Ayuntamiento de Durango
   - EUS-P03: El Correo's B-Venture, sponsored by four public bodies

   All were coded PRIVATE_ECOSYSTEM or STARTUP_NEWS.
7. **Hybrid actors:**
   - Zoox (Amazon-owned): coded CORPORATE
   - a16z Speedrun GM: coded INVESTOR
   - a16z Academy CEO: coded PRIVATE_ECOSYSTEM
   - Gemnote CEO, a VC-backed vendor: coded PRIVATE_ECOSYSTEM
   - Colliers researcher: coded CORPORATE
   - BAT tower: coded PUBLIC_ADJACENT
   - Beaz staff: coded PUBLIC_OFFICIAL
8. **Non-venture entrepreneurs.** In MAD07, Dulce Safari, Carbon Neutral Consulting and INMOA were coded OTHER. The OTHER bucket hides "SME owner".
9. **Outlet-produced data pieces** (BA16, BA28) were coded OTHER, while third-party rankings were coded PRIVATE_ECOSYSTEM.

## Codebook v2 proposals

1. **Speaker eligibility.** A speaker is a named person to whom the *body text* attributes words, direct or indirect ("said", "explained", "according to X"), or who is described as speaking at the event covered ("abrió", "clausuró", "intervino").
   - Exclude: photo captions, related-link teasers, attendee lists, and people only "named" or "present".
   - Include first-name-only members of the public as OTHER, with `name_partial=yes`.
2. **Lead voice.** `lead_voice` is the category of the first *eligible named* speaker in body order. Add `lead_unnamed` to record an earlier unnamed source (e.g. "company spokesperson" → STARTUP_EMP). Decide whether an epigraph or general quote unrelated to the story's actors counts. Recommendation: exclude it, and flag `epigraph=yes`.
3. **Headline actor.** Code the grammatical subject or protagonist of the headline, mapping organisations through a fixed table:

   | Headline subject | Code |
   |---|---|
   | Startup or startups collectively ("AI companies", "ocho startups") | FOUNDER |
   | VC / fund | INVESTOR |
   | Government, agency, public company | PUBLIC_OFFICIAL |
   | Public foundation, park or BIC | PUBLIC_ADJACENT |
   | Place, aggregate statistic, programme with no named owner | NONE |

   If the headline has two actors, take the first-named one.
4. **Founder evidence.** FOUNDER needs an explicit founder, co-founder or "creador" label in the text or on the company's site. A CEO or DG without that label is STARTUP_EMP, with `founder_unverified=yes`. Clinical, academic or business collaborators of a startup are OTHER or ACADEMIC, never FOUNDER.
5. **Trigger tie-breakers:**
   - (a) **Public money into a single named startup** (grant, public VC stake) is STARTUP_NEWS, plus a new flag `public_money=yes`. It is PUBLIC_ANNOUNCEMENT only when the item announces a programme or call rather than one company's money.
   - (b) **Events** are coded by organiser, not by sponsor or speaker. If the organiser is public (including public companies such as Beaz or SPRI), the code is PUBLIC_ANNOUNCEMENT.
   - (c) **Reports** are coded by the lead author's sector. A joint private-public report is PRIVATE_ECOSYSTEM, with `copub=yes`.
   - (d) **Analysis, trend and data pieces** produced by the outlet, with no news peg in the previous 7 days, are OTHER. If they hang on a peg, they get the peg's trigger. Write the peg in `notes`.
6. **The pr flag** is "yes" in any of these cases:
   - the byline or JSON-LD author is an institution or company
   - there is an "About X" boilerplate
   - there is a branded-content marker ("Content Service", "patrocinado")
   - two or more paragraphs match the company's release

   Check JSON-LD `author` routinely.
7. **Hybrid-actor list.** Put these in the codebook:
   - startup subsidiaries of corporates: CORPORATE once acquired
   - VC-run accelerators and schools: INVESTOR if the person is a fund partner, otherwise PRIVATE_ECOSYSTEM
   - vendors or agencies commenting on startups: PRIVATE_ECOSYSTEM even if they are themselves startups
   - real-estate and brokerage researchers: CORPORATE
   - public-company staff (Beaz, SPRI, Mubil, Las Rozas Innova): PUBLIC_OFFICIAL
   - publicly promoted incubators or accelerators (BAT, BICs): PUBLIC_ADJACENT

   The exact split doesn't affect INSTITUTIONS totals, but it does affect category kappa.
8. **New category SME_OWNER** for founders of non-venture businesses (franchises, consultancies, clinics), so they leave OTHER. Keep them outside BUILDERS, but report them.
9. **Reliability protocol.** The second coder must be human, or at least a different model with no shared tooling or notes. It should be blind to the first coder's logs as well as the CSVs. Run it on a stratified sample that over-represents the edge cases in the latent list above.

## Source access log

- **Direct fetch (curl):** 53 of the 60 articles.
- **Blocked articles** (HTTP 403):
  - **EUS-P14** (Cinco Días): read through the r.jina.ai reader proxy. The first coder's saved copy `raw_eus/pages/c38.html` was copied into `raw/` but not used for coding.
  - **MAD07, MAD48** (El Referente): reader proxy. A Wayback copy was also downloaded but not used for coding.
  - **MAD37** (elEconomista), **MAD38, MAD45, MAD50** (El Referente): reader proxy only.
- **Chrome (claude-in-chrome):** approved mid-task but not used. No article needed it.
- **Live page differs from the sample:** MAD38's headline has changed since sampling. The sample headline was kept in the CSV.
- **Paywalled DV/El Correo/Expansión pages** were coded from JSON-LD `articleBody`. EUS-P48 is a photo gallery, so only captions were available.
