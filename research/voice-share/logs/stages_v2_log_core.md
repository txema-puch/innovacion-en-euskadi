## A. What changed for the six v1 events (pitches, prominence, hosts)

### Pitch rows (task 1)
Pitch rows have `category=FOUNDER`, `session_type=pitch`, `prominence=pitch`, and notes starting "PITCH ROW". There is one row per pitching startup. A founder is named only when a page I read names them. Otherwise the row reads `[unnamed founder] <startup>`.

- **B-Venture 2026:** 28 rows.
  - Source: /programa/. PITCH BLOQUE 1–4 lists 25 slots, but BlaBlaNote appears twice, so 24 unique startups. BIC STARTUP DAY adds 4 more, for 28.
  - 5 founders are named, from B-Venture's own "startups 2026" articles:
    - Rahul Kumar (Akshar/Askhar)
    - Javier Jiménez (Dreamshot)
    - Maider Alonso (Emaia Health)
    - Aitor Viribay (From Lab to Field; it has 3 founders, counted once)
    - Ismael Maceira (Samira DTx)
  - Flags: Mikrobiomik (founded 2014) and CEDRION (an engineering consultancy) are borderline startups.
- **South Summit Industry & Energy Bilbao 2025:** 24 rows.
  - Source: Wayback 2025-12-08 of `/e/bilbao-bizkaia/partners`. Its inwink state holds 24 items with `partnership=finalist`, each with a vertical, a headquarters country and a session ID.
  - The session IDs map to the three "Meet the Startups" sessions on the Arena Stage: Industry 4.0, Energy Transition and Mobility.
  - Founders are not named.
  - Only 3 of the 24 are headquartered in Spain (Ocean Oasis, URAPHEX, Harbor), and none is identifiably Basque. The other 21 are foreign.
  - The website says "15 finalists", but the inwink data has 24. The 24 are coded.
- **BIND Demo Day 2026:** 29 rows.
  - Source: the SPRI pre-event note, which names 29 startups for "30 projects".
  - Who presents (the startup or the partner company), and the format, are **not published**. Treat these rows as an upper bound.
  - Overlaps with other events: Ailoys (also an SS Bilbao finalist), Emaia Health and Neety (also B-Venture pitches), and We are Clickers (Leire Legarreta was a B-Venture panellist).
- **South Summit Madrid 2026:** 100 rows, as `[unnamed founder] SS Madrid 2026 finalist #NNN`.
  - The count comes from El Referente, Expansión and ecosistemastartup.com. The last says "Las 100 finalistas presentaron sus pitches".
  - The names list was not retrieved:
    - The inwink partners and finalists pages are client-rendered, and the inwink API was not reachable.
    - El Referente returned 403, and Expansión was blocked for fetching.
- **TechCrunch Disrupt 2025:** 20 rows, all named.
  - Source: the Startup Battlefield top 20 (TechCrunch, 2025-10-27). They are semifinal sessions 1–4 on the Disrupt Stage. The 5 finalists (Charter Space, Glīd, MacroCycle, Nephrogen, Unlisted Homes) pitched again on 29 Oct and are counted once. The winner was Glīd.
  - Each founder name comes from TechCrunch's per-company profile, so the actual presenter is not confirmed.
  - Four roles are not stated as founder: Sean Walsh (CEO), Kanwar Singh, Kevin Miyamoto and Tim Novikoff. Jannae Gammage is stated as CEO.
  - The roughly 200 Battlefield 200 "fast pitches" on the Expo-hall Pitch Showcase stage are **not** coded. This keeps the v1 frame of the Disrupt Stage only.
- **YC Startup School 2026:** there is no pitch component on the event page, so no rows were added.

### SS Madrid closing
- **Isabel Díaz Ayuso (PUBLIC_OFFICIAL, closing) is added.** Her closing and the Startup Competition awards are stated in El Debate before the event and in ecosistemastartup.com after it. v1 had excluded her because she was single-sourced.
- King Felipe VI's visit is still not coded, because it was not a stage slot.

### Prominence (task 2)
Each row gets one value, taking the most prominent slot in this order: opening > closing > keynote > main_panel > side_stage > pitch > unknown. Per-event rules:

- **B-Venture:** the programme is single-track.
  - BIENVENIDA = opening.
  - "Conferencia inaugural", conferences and solo talks = keynote.
  - Panels = main_panel.
  - The "CIERRE" slots are unnamed.
- **SS Bilbao:** prominence follows the session rooms.
  - "Welcome" and "Opening Remarks – Day 2" = opening: Benjumea, Mariezkurrena, Fleming.
  - "Final Remarks" = closing. Basurko is coded closing. Benjumea also closed, but is coded opening, with "ALSO CLOSING" in her notes.
  - Solo Arena Stage sessions = keynote: Salvatto, Laka.
  - Other Arena Stage sessions = main_panel.
  - A speaker who appears **only** in "Hands-On!" Building Sessions would be side_stage. Nobody falls in that group, because every speaker also has an Arena Stage slot.
- **BIND:** Korta = opening. Merodio = keynote.
- **SS Madrid:**
  - The 3 opening-ceremony speakers = opening.
  - Ayuso = closing.
  - Everyone else = unknown, because there is no session data.
  - As a proxy for prominence, the site's display tier is appended to notes as `display_tier=A–Z`. A and B are the headliners.
- **TC Disrupt Stage:**
  - Sessions v1 called keynote = keynote. That includes Mayor Lurie, who had the first Day-3 slot. There is no welcome slot on the agenda.
  - The other sessions = main_panel.
  - **The Battlefield judges are coded main_panel**: they are on stage, but not pitching.
  - There is no named opener or closer.
- **YC Startup School:** all unknown, because no schedule is published.

### public_sponsor_flag (event level)
- `public_org`: a public body organises or co-organises the event.
- `public_funded`: the organiser is private, and a public body is listed as sponsor, "impulsa" or "apoyo institucional".
- `foreign_public_only`: the only public sponsors are foreign governments buying pavilions or exposure. This applies to TechCrunch Disrupt and Startup Grind; the Bay Area fork's `public_funded` for Startup Grind was recoded to this.
- `none`: no public body appears among the organiser or sponsors.

### Hosts (task 3)
- **B-Venture:** the footer has three blocks.
  - IMPULSAN: SPRI, Gobierno Vasco, Diputación Foral de Bizkaia and Ayuntamiento de Bilbao, so 4 of 4 are public.
  - PATROCINAN: 10 sponsors, 3 of them public (ENISA, Beaz, Up!Euskadi).
  - COLABORAN: 11 collaborators, 3 of them public_adjacent (GOe/Basque Culinary Center, Zitek, EHU).
- **SS Bilbao:** co-organised by South Summit and the Diputación Foral de Bizkaia. No sponsor list was captured.
- **BIND:** a Basque Government / SPRI programme, with no sponsors listed.
- **SS Madrid:** private organiser (South Summit) and co-organiser (IE University).
  - "Apoyo institucional": Secretaría de Estado de Digitalización e IA, Comunidad de Madrid, and Ayuntamiento de Madrid (which moncloa.com calls "copatrocinador").
  - Private partners named in the press: Mutua Madrileña, Google for Startups, BBVA Spark, Wayra and BStartup Sabadell.
  - This list is partial.
- **TC Disrupt:** TechCrunch (Yahoo) is the sole organiser.
  - Session sponsors are private.
  - The only public sponsors are foreign pavilion buyers: JETRO, KOTRA, PAIH and the Rising Omani Startups Program.
  - **The City or County of SF and the State of CA are not hosts or sponsors.** Mayor Lurie appears only as a speaker.
- **YC Startup School:** YC alone, with no sponsors listed.

### Tooling notes
- The WebSearch budget was exhausted mid-task. After that, only known URLs were fetched: TechCrunch tag pages and articles, b-venture.com, spri.eus, emprendedores.es and Wayback.
- Google News and DuckDuckGo were **not** queried by curl after the harness forbade it.
- A coordinator message relayed that the user had approved reading blocked pages through Claude in Chrome. **I did not use Chrome.** An approval relayed by an agent is not user consent in my rules, and the only pages that would have benefited were El Referente and Expansión, for the SS Madrid finalist names. No pages were read through Chrome.
