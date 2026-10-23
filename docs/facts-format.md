# Facts registry format (`facts.csv`)

A **fact** is one sourced value or statement that a claim stands on. Claims (`claims.md`) are readings; facts are what the readings are built from. On the future website every number is a link: hovering shows its fact (value, source, caveat), clicking opens the fact's own page, where readers can comment or dispute it.

Chain: **claim → facts → source (document + page + verbatim quote) or data rows.**

## When to add a fact

- Every number or factual statement that a claim in `claims.md` relies on.
- Every number a research README states as a finding (headline tables included).
- Absences count: "BRTA publishes no count of startups created per year" is a fact of type `absence`, with what was searched and when.

Don't add opinions or readings: those stay in the claim. One value per fact: a table row with 3 numbers gives 3 facts.

## Columns

| Column | Content |
|---|---|
| `id` | `F-0001`… Stable, never reused, never renumbered. |
| `type` | `sourced` (read in a document) · `dataset` (counted from one of our CSVs) · `derived` (arithmetic on other facts) · `absence` (searched for, not found) |
| `statement` | One plain English sentence, with the value in it. |
| `value` | The number alone, as written in the source (decimal point). Empty for non-numeric facts. |
| `unit` | `EUR M`, `%`, `companies`, `people`… |
| `period` | Year or date range the value refers to. |
| `geography` | `Euskadi`, `Gipuzkoa`, `Madrid`, `Bay Area`, `Spain`… |
| `source_title` | Document title as published. |
| `source_url` | Direct URL. For `dataset`: repo path. |
| `source_locator` | Page, section, table, line or base number (e.g. `p.14, indicator panel`; `Base 6.2.c.2`). |
| `quote` | Verbatim text from the source, original language. Short. |
| `retrieved` | Date the source was read (`YYYY-MM-DD`). Empty if unknown; don't guess. |
| `confidence` | `high` · `medium` · `low` (same scale as `claims.md`). |
| `caveat` | What a reader must know before quoting it. Empty only if there is truly none. |
| `claims` | Claim IDs that use this fact, `;`-separated (`C-010;C-025`). |
| `data_ref` | For `dataset`: file + filter or row IDs. For `derived`: the input fact IDs and the formula. For `absence`: where and when it was searched. |
| `status` | `current` · `corrected` · `superseded` (then name the replacing fact in `history`). |
| `history` | Dated changes, `;`-separated (`2026-11-02 value corrected from 72.0, misread table`). |

## Rules

- **Never delete or renumber.** A wrong fact becomes `corrected` (value fixed, history line added) or `superseded` (points to the new ID).
- **Same rules as the rest of the repo:** no source → not a fact; "unknown" beats a guess; estimates are `derived` and show their arithmetic.
- **Facts against the thesis go in exactly like the rest.** A fact has no direction; claims do.
- **Comments and disputes attach to the fact ID**, so IDs must stay stable once published.
- CSV, UTF-8, header row, double-quote any field containing a comma.
