# Methodology and limitations

**Study:** *Cartus migratorius: The Great Ottawa Shopping Cart Migration Study of 2025*  
**Type:** Independent descriptive and exploratory research  
**Principal evidence:** Archived 2025 City of Ottawa 311 service-request CSV; analyst-screened 2026 Overture places snapshot for certain retailer comparisons.

## Four different units of observation

| Unit | What it means | Documented 2025 count |
|---|---|---:|
| Original shopping-cart-related 311 reports | Filtered service requests, not distinct carts | 411 |
| Geocoded reports | Reports with both latitude and longitude | 247 |
| Distinct mapped reporting addresses | Address labels in the geocoded sample | 214 |
| Provisional reporting episodes | Same-address reporting grouped under an explicit 21-day rule | 227 across all geocoded reports (original study estimate) |

These units answer different questions. Converting between them without explanation would distort the story.

## Source preparation

1. Use an archived historical 2025 input, rather than assuming the moving `lastyear` URL still points to 2025.
2. Validate file provenance with the SHA-256 recorded in the notebook.
3. Load the bilingual CSV and split heading/description fields into English components for classification.
4. Preserve raw request rows, then derive a working population by matching shopping-cart descriptions.
5. Calculate coordinate completeness independently from the reported municipality/service family.
6. Do not interpret administrative closure timestamps as known physical remediation dates. A 2026 closure-date concentration was documented in Chapter 3, but its actual cause was not established.

## Known reporting blind spots

- **Property Standards:** 104 reports, 0 with public coordinates.
- **Road Maintenance:** 251 reports, 191 with public coordinates.
- **Park Maintenance:** 36 reports, all geocoded.
- **City Building Maintenance:** 20 reports, all geocoded.

The mapped sample is systematically incomplete in observed service-family terms. Summer had 134 original reports, whereas spring narrowly led the mappable sample (85 versus 82 for summer). These are descriptive reporting totals, not a causal seasonal migration effect.

## Episode heuristic

Within each recorded address, order reports by opening date. Start an estimated episode at the first report; include subsequent reports occurring at most **21 calendar days after the first date**; start a new episode once that limit is exceeded. The comparison is anchored to the **episode’s first report**, not continually extended by the newest date. Alternative windows were explored in Chapter 4. It is a heuristic for reporting events, not a deduplication proof or estimate of actual carts.

## Geography and retailer candidates

- All proximity distances are calculated using latitude/longitude and great-circle/Haversine comparisons, not road routes or verified cart paths.
- Chapter 6 explores nearest **other distinct reported address** (e.g., 11.04 km for the 2890 Munster Road observation).
- Chapter 7 screens Overture places entries into analyst-defined core and extended candidates (150 core and 272 extended after review). The nearest core candidate to Munster is about **9.69 km**; neither it nor any other retailer is a confirmed cart origin.
- Chapter 8's Double Isolation Score is `min(nearest other recorded cart location, nearest eligible candidate retailer)`; 1 km and 1.5 km membership cutoffs are exploratory.
- The 2026 places archive is later than the 2025 311 records. Some source POIs may not have operated as qualifying retail stores in 2025.

## Chapter 9 seasonal sensitivity

- Meteorological seasons: winter Dec–Feb; spring Mar–May; summer Jun–Aug; fall Sep–Nov. Calendar-year winter is **not** a continuous meteorological winter.
- 20 of 214 addresses had multiple geocoded reports, 10 appeared across two seasons, and one two-season appearance was separated by just six days (1720 Innes Road).
- Annual Park Maintenance reporting: 36 requests; 22 were opened April–May, across 15 distinct addresses.
- Under the 21-day heuristic, the 22 April–May reports collapse to **15 estimated Park episodes**; the annual Park total is **29 estimated episodes**.
- Two Woodroffe addresses separated by **225.3 metres**, with two days between episode starts, were the only pair to satisfy a 300 m / 21 day screen among **406** possible episode pairs. This does not show that they concern one cart or one underlying event.
- Sensitivity removing the Woodroffe pair, **without deleting the original records**, reduced the April–May share of original Park reports from **22/36 = 61.1%** to **14/28 = 50.0%**, and April–May estimated episodes from **15/29 = 51.7%** to **13/27 = 48.1%**. The full spring share remains just over 50% under both measures.

## What cannot be inferred

The investigation cannot establish the origin, travel routes, physical count, arrival time or disappearance of identifiable shopping carts. Reporting practices and service classifications might contribute to observed patterns; a single 2025 year cannot demonstrate annual seasonality. Exploratory thresholds and comparisons are not causal or statistical significance tests. The inferences stay descriptive.

## Code inspection

- [`notebooks/Cartus_Migratorius_Field_Journal.ipynb`](notebooks/Cartus_Migratorius_Field_Journal.ipynb) — full 9 chapters, 71 code cells, 22 Markdown cells; execution outputs stripped.
- [`analysis/summary.py`](analysis/summary.py) — compact runnable reporting/season/episode analysis with source file argument.
- [`tests/test_summary.py`](tests/test_summary.py) — synthetic checks for season totals and the first-report-anchored 21-day episode rule.
- [`docs/maps/`](docs/maps/) — seven Folium/Leaflet maps extracted from the notebook's saved execution outputs, keeping original legends/layers.

The private notebook's live source archives are not supplied. The full original notebook is therefore a transparent research record, but **not a single-click end-to-end reproducibility claim**. See [SOURCES.md](SOURCES.md) for full attribution and snapshot limitations.
