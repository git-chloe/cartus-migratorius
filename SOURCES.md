# Data provenance, permissions & credits

## Ottawa 311 public records

> **Contains information licensed under the Open Government Licence – City of Ottawa.**

- Source publisher: **City of Ottawa**, Open Ottawa service-request public dataset, 2025.
- Study field: reported shopping-cart-related 311 requests, derived from the bilingual description.
- Dataset reference: [Open Ottawa – Previous Year Service Requests](https://open.ottawa.ca/) and the [recorded rolling CSV endpoint](https://311opendatastorage.blob.core.windows.net/311data/311opendata_lastyear.csv).
- Licence: [Open Data Licence v2.0 — City of Ottawa](https://ottawa.ca/en/city-hall/open-transparent-and-accountable-government/open-data/open-data-licence-version-20).
- Historical extraction: the original notebook loaded a saved local file, `Ottawa_311_2025_Original.csv`; 372,069 parsed requests, one malformed CSV record skipped, 411 matched cart descriptions.
- Archived-source SHA-256: `e85a4dce98af77cb56504e31fdaf12287f3c5b8454a4b5f015cfca5ec6c48f1a`.
- **Important:** `lastyear.csv` changes with time. It is a provenance reference, not a fixed link to the October 2026 analysis snapshot.
- Public/private geographic records may have different location disclosure: 164 of the 411 studied requests had no publicly usable coordinate pair. Do not infer where they occurred.
- The study is independent and is **not affiliated with or endorsed by** the City of Ottawa. No official City symbols are used.

## Retailer candidate locations

- Source: **Overture Maps Foundation**, Places data, 2026 extract used in the author's original notebook.
- [Overture Places documentation](https://docs.overturemaps.org/guides/places/) · [Licensing and attribution](https://docs.overturemaps.org/attribution/).
- Original extract `Ottawa_Places_Original_Field_Notes.geojson` was archived privately and is **not included**.
- The exact archive release identifier is not established from the final uploaded notebook. It would be misleading to invent one.
- Candidate counts are analyst-screened snapshots, not a comprehensive confirmed 2025 registry of stores that issued carts.
- Sources underlying Overture places can carry different licences, attribution and notices. Consult Overture documentation for reuse of raw/derived sources.

## Basemap and mapping libraries

- Maps created with **Folium/Leaflet**, exported from the final executed Colab notebook.
- Base layer: **Esri World Light Gray** tile service. Original map credits include **Esri, HERE, Garmin, OpenStreetMap contributors, GIS user community**. Attribution is preserved in map HTML and visible in map imagery.
- Folium map HTML loads JavaScript/CSS from third-party CDNs; the interactive maps require internet access.
- Maps show recorded location points and straight-line comparisons; they are not navigation aids.

## Scope and publication policy

- The numeric story refers to the saved 2025 311 source snapshot, not up-to-date cart incidence.
- The public repository contains **aggregated results, a source-only notebook, a compact reproducible analysis script, tests and Folium visualizations**. The original raw CSV, private learning guides, private notebook outputs, and privately archived retailer extract are withheld.
- No AI-tool coauthor credit is required by these municipal data licences. Follow any separate institutional/editorial disclosure policy if later submitting the work elsewhere.
