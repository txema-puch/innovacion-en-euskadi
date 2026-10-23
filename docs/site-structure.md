# Website: structure and decisions

What the public site will be, agreed with Txema on 2026-10-23. The site reads from this repo (`claims.md`, `facts.csv`, `positions.md`, the research CSVs, `docs/open-gaps.md`); it never holds its own copy of the data. Visual ideas: `visualization-ideas.md`. Brand sketch: claude.ai artifact "Euskadi Evidence Brand Brief".

## Goal and readers

- **Goal:** let anyone check, in under a minute, where a claim about Basque innovation comes from, and argue with it in public.
- **Primary readers:** journalists and institutions (the people who will quote and dispute). **Builders** a close second. Then policy people elsewhere.
- Design for the skeptic: every reader arrives looking for the weak point.

## Three layers, every number clickable

```
Position  P-001   what we argue (labelled as an argument, never as a finding)
  └─ Claim  C-0xx  a reading of the evidence, with status, confidence, for/against
       └─ Fact  F-0xxx  one sourced value: source, page, verbatim quote, caveat
            └─ Source document or data rows
```

- Hovering any number shows its fact (value, source, caveat). Clicking opens the fact page.
- **Comments and disputes** attach to a fact (the number or the source is wrong) or to a claim (the reading is wrong). IDs must stay stable once published.

## Site map

```
Home        the question, the thesis (labelled "to be tested"), the chapters,
            a prominent "show only the evidence against" filter
Chapters    Money · Voice · Companies · People · Elsewhere
Claims      registry with filters (for/against, status, confidence, chapter) → claim page
Facts       fact pages (reached from numbers and claims)
Positions   what we argue and what would change our mind
Data        every CSV browsable, one link per row, download
Unknowns    what we don't know yet (from open-gaps.md) and transparency requests with their answers
Method      codebooks, caveats, how to verify, how to dispute, changelog
Disputes    every open objection and its answer
```

**Chapters:**
- **Money:** public vs private share of startup rounds by year; the Hazitek loop (≥20% back to RVCTI agents); programme rules; nobody measures the outcome.
- **Voice:** press, stages, who opens the event, who hosts the room. Pitches counted apart.
- **Companies:** two halves of equal weight: tech-centre spin-offs, and startups funded by public programmes (Ekintzaile census and the rest). Same treatment for both: outcome Sankey + searchable table.
- **People:** talent. Rules that keep people in, founders recruited from outside, nobody measures alumni, Nokia/ITRI benchmarks (`research/talent/`).
- **Elsewhere:** Fraunhofer, imec, ITRI, Israel, Finland, TNO, Catapults + the literature.

**Chapter template:** stick-figure picture → numbers with receipts → claims for and against side by side, same size → the data rows.

**Claim page:** statement · status and confidence · picture · facts · rows · **what would refute this** · history · dispute thread.

**Fact page:** statement and value · verbatim quote, locator, link, retrieved date · caveat and confidence · claims that use it · rows behind it · history · comments.

## Rules for the site

- Evidence against the thesis gets the same box, type and weight as evidence for it. No raw for/against claim count (claims don't weigh the same).
- **No verdict colours** (no red/green). Outcomes are shown with figure poses; Sankeys from `visualization-ideas.md` are drawn in the brand palette.
- Positions are always labelled as positions and link to the claims that test them.
- Unknowns are drawn (dashed figures), not left as empty cells.

## Languages

Spanish, Basque and English, with a language selector and one URL per language (`/es/`, `/eu/`, `/en/`). Opens in the browser language, falls back to Spanish. The repo stays in English as the source; site copy lives in translation files. Quotes and programme names stay in the original language. Basque copy needs native review before launch.

## Brand

White paper, black ink, one blue ("stamp") for institutions and public money, grey for everyone else, dashed grey for unknown. Stick figures: round head = builder, square head = institution. Money: a € coin, filled blue when public, white when private; it only ever moves from a source to a destination. Motion only when the reader asks (year, region, play). Figures are never named people and never caricatures. Type: Archivo, wide for headlines and numbers, normal width for text.

## Open

- **Name:** a short handle in Basque, tech/innovation flavoured. Leading candidate *Abian* ("underway, launched"); *Kontuak* liked but less about innovation. Avoid *Sortu*, *Ekin*, *Hazi*.
- Stack and hosting: not decided yet.
