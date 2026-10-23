# Log — talent line (alumni → startups)

- 2026-10-23 Read repo README, claims C-028, docs/facts-format.md, spinoffs.csv (188), active_check.csv, startups.csv (65). Repo untouched (read-only).
- method.md written before any counting.
- WebSearch tested: working (standard mode). Used sparingly; no workaround engines.
- Step 1 discovery: ~20 WebSearch queries (ES/EN phrasings "ex investigador de Tecnalia/Ikerlan/Vicomtech/CEIT", founder bios) returned almost nothing — the engine does not honour quoted phrases and centre alumni are not tagged anywhere public. Crunchbase-restricted queries yielded 2 leads (Nuavis, Bloowatch).
- WebFetch on crunchbase.com → 403. Chrome (read-only, new tab 962816100) opened crunchbase.com/organization/nuavis: page returned no text (bot challenge / JS wall). Did not attempt to bypass. Tab closed. No further Chrome use for Crunchbase.
- Helper agents launched (background): (A) Ekintzaile 2021 founder origins → raw/ekintzaile_*.csv; (B) spinoffs.csv founder origins → raw/spinoff_*.csv. Shared rules raw/AGENT_RULES.md.
- WebSearch budget (session-wide 200) EXHAUSTED during Step 1 (~25 of my queries; helpers used the rest). No workaround used (no curl search, no proxies, no Wayback via tool — WebFetch cannot reach web.archive.org).
- Helper A (Ekintzaile 2021): 65 rows → raw/ekintzaile_origins.csv, raw/ekintzaile_people.csv (28), raw/ekintzaile_log.md. ~19 companies never searched.
- Helper B (spin-offs): 188 rows → raw/spinoff_origins.csv (50 checked against a source, 59 repo-coded, 42 not researched, rest unresolved), raw/spinoff_people.csv (62), raw/spinoff_log.md; script scripts/build_origins.py. Helper B used repo-local copies under repo raw/spinoffs/dl/ (read-only).
- Built deliverables with ../talent_build_final.py and ../talent_facts.py (outside talent/):
  - alumni_startups.csv: 12 startups (5 for the four target centres, 7 for CIC centres).
  - founders_public.csv: 33 people — only those whose centre/origin is publicly stated (data minimisation: names with "not stated" origin left in raw/ only). Nuavis rows rest on Crunchbase search snippets (flagged low confidence).
  - founder_origins.csv: 253 rows (188 spin-offs + 65 Ekintzaile), with basis flag (checked / repo-coded / not researched / not resolved).
  - facts_draft_alumni.csv: 25 draft facts (dataset/derived/absence), id and claims empty.
- Not used: LinkedIn (none), Chrome only once (Crunchbase, no text, closed). Bloowatch/OpenCoast (Tecnalia alum per Crunchbase snippet) kept in raw/step1_candidates.md only: company unverifiable.
