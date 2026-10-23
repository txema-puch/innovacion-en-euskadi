# Talent line, part 2: benchmarks (people who leave and build)

The units we want are:
- (a) the share of staff leaving each year;
- (b) alumni founders per 1,000 staff or leavers;
- (c) alumni in startup leadership.

Few sources measure **people**. Most count **companies** per 1,000 staff. Both kinds are listed below, with the unit labelled. Retrieved 2026-10-23 unless stated.

## Summary table

| Benchmark | Unit | Value | Source quality |
|---|---|---|---|
| Ex-Nokia (Finland), people who left Nokia 2008–2014 | startup entrepreneurs per 1,000 leavers | **23.7** (530 / 22,344) vs **10.7** for leavers of other large Finnish high-tech firms (256 / 24,006) | Primary (ETLA, Statistics Finland register data) |
| Ex-Nokia | any entrepreneurial status (startup, other entrepreneur, self-employed professional, business angel) | **8.27%** of leavers vs **4.96%** control | Primary |
| Ex-Nokia | startup growth | revenue grew **16%** faster than control; **50%** faster if the founder had a prior innovation role | Primary |
| ITRI (Taiwan) | target annual staff turnover | **~15%/yr** target; **~85%** of leavers joined Taiwanese firms | **Secondary** (Asterisk Mag); primary not reached |
| ITRI | alumni in leadership | **~40%** of managers in Hsinchu Science Park firms were ex-ITRI by the late 1990s | Secondary (Asterisk) |
| Fraunhofer | spin-offs per 1,000 staff (companies, not people) | **1.57** per 1,000 employees; **2.8** per 1,000 scientific staff (25 / 8,795) | Primary (Bundestag Drs. 19/14361) |
| Fraunhofer | people employed in surviving spin-offs | **2,965** (2018) | Primary (same) |
| Fraunhofer | institution compensated for staff leaving | Ausgründungsprämie (amount not public) | Primary (fraunhoferventure.de) |
| Euskadi BRTA / Tecnalia | any of the three people units | **not published** (see measurement.md) | — |

## 1. Ex-Nokia: ETLA Brief 158

Rouvinen, Petri; Breznitz, Dan; Pajarinen, Mika (22.4.2025), "Nokiasta lähteneet ryhtyivät innolla yrittäjiksi ja bisnesenkeleiksi: Nokia-kokemus siivitti startupien liikevaihtoja rivakkaan kasvuun" / "Ex-Nokians Eagerly Became Entrepreneurs and Business Angels: Nokia Experience Fueled Rapid Growth of Startups' Turnovers". ETLA Brief 158.
URL: https://www.etla.fi/wp-content/uploads/ETLA-Muistio-Brief-158.pdf (14 pages).

- **Design** (p.1, English abstract): it compares "former Nokia employees with individuals who left other large high-tech companies in Finland, using comprehensive register-based data at Statistics Finland." Leaving window 2008–2014.
- **Definition** (p.7–8, Finnish): a "startup-yrittäjä" owns at least 10% of a small, young limited company in which they work. A business angel owns ≥10% of a company where they do not work.
- **Headline** (p.1): "A significant 8.27% of those who left Nokia became entrepreneurs or business angels. Former Nokia employees were more than twice as likely to become startup entrepreneurs compared to the control group."
- **Growth** (p.1): "startups founded by former Nokia employees grew an average of 16% faster than the control group. When focusing solely on companies founded by individuals with prior innovation roles, this growth rate was an average of 50% faster".
- **Survival** (p.1): "Nokia experience negatively affects entrepreneurial survival but positively influences firm growth."
- **Figure 4** (p.8), counts and shares of leavers:

| | Nokia | Control |
|---|---|---|
| All leavers | 22,344 | 24,006 |
| Startup entrepreneurs | 530 (2.4%) | 256 (1.1%) |
| Other entrepreneurs | 116 (0.5%) | 76 (0.3%) |
| Self-employed professionals (ammatinharjoittajat) | 513 (2.3%) | 400 (1.7%) |
| Business angels | 689 (3.1%) | 458 (1.9%) |
| Sum | 1,848 = 8.27% | 1,190 = 4.96% |

  The bar-to-label mapping was checked arithmetically: the sums reproduce the 8.27% and 4.96% stated in the text.
- **Text** (p.8): "Nokiasta lähteneistä 530 siirtyi startup-yrittäjiksi, mikä on yli 2 kertaa enemmän kuin verrokeista lähteneiden … 530 ex-Nokialaista startup-yrittäjää perustivat (tai he liittyivät) kaikkiaan 427 startup-yritykseen."
- **Derived:** 530 / 22,344 × 1,000 = **23.7** startup founders per 1,000 leavers. Control: 256 / 24,006 × 1,000 = **10.7**.
- **Caveat:** these are leavers of a collapsing corporate, many of them laid off, not researchers at an RTO. The unit is people per 1,000 **leavers**, not per 1,000 staff per year.

## 2. ITRI (Taiwan)
Source: Asterisk Magazine, issue 13, "The Institute Behind Taiwan's Chip Dominance", https://asteriskmag.com/issues/13/the-institute-behind-taiwan-s-chip-dominance (retrieved 2026-10-23).
- "ITRI also aimed for 15% of its staff to turn over each year."
- "About 85% of ITRI's departing staff joined Taiwanese firms, creating an ever-expanding network of shared knowledge and expertise."
- "By the late 1990s, this pattern of movement meant that about 40% of managers in the firms within Hsinchu Science Park had previously worked at ITRI."
- **Caveat:** secondary, and the article gives no footnoted primary source for the 15% target. Attempts to reach primary ITRI pages failed: itri.org.tw English pages are JavaScript-rendered and returned no text via curl or Chrome. Web search was exhausted. The likely primary literature (Mathews 1997, *California Management Review*; Mathews & Cho, *Tiger Technology*, 2000) was not checked. Confidence: low–medium.

## 3. Fraunhofer
- **Spin-off intensity** (companies), Bundestag Drs. 19/14361 (Federal Government reply, 2019), https://dserver.bundestag.de/btd/19/143/1914361.pdf (`sources/txt/bt14361.txt`), p.7:
  - "FhG: 25 Ausgründungen bei 8.795 WMA – rund 2,8 Ausgründungen je 1.000 WMA"
  - "FhG 1,57 und HGF 0,65 Gründungen pro 1.000 Beschäftigte". The same page gives NASA 0.32 and US DoE labs 0.58.
- **People in spin-offs** (p.8): "In den 2018 noch bestehenden Ausgründungen der FhG sind 2.965 Mitarbeiter beschäftigt." This is a stock of jobs, not alumni founders.
- **Compensation to the institute for staff who leave:** Ausgründungsprämie (see rules.md §G).
- **Gap:** no Fraunhofer figure found for annual staff turnover to industry or for alumni founders.

## 4. VTT, imec, TNO, EARTO alumni studies: not reached
- Repo `research/comparisons/README.md` already holds the company counts: VTT 60+ spin-offs (€1.2bn raised), imec 120+ spin-offs, TNO 41 since 2017.
- No people-unit figure (staff turnover, alumni founders, alumni in startup leadership) was found for VTT, imec, TNO or in any EARTO study. Web search was exhausted before these could be searched, so this is a gap, not a confirmed absence.

## 5. Euskadi side, same units
- Tech-centre staff: BRTA 4,372 people in 2024 (memoria 2024 p.6), with 4,100 "personas investigadoras" (p.13). Tecnalia 1,512 staff in 2025 (repo).
- Leavers per year, alumni founders, alumni in startup leadership: **no published figure** (see measurement.md).
- The closest company-unit figure (repo): Tecnalia 3 spin-offs / 1,512 staff ≈ 2.0 per 1,000 staff/yr. BRTA-wide spin-off counts are not published. Ikerbasque: researchers "participating in 41 spin-offs" (2024), against 201 + 112 + 89 = 402 researchers in the three named categories. That cumulative company count is not comparable with an annual rate.
