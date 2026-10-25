# Code and reproducibility

The original **nine-chapter, 71-code-cell Field Journal** is included at [`../notebooks/Cartus_Migratorius_Field_Journal.ipynb`](../notebooks/Cartus_Migratorius_Field_Journal.ipynb). All Python source cells are preserved from the final edited notebook; a few residual plural Markdown references were normalized for singular authorship in the public edition. The execution outputs were intentionally cleared for publication. The original research was conducted in Google Colab with local source snapshots mounted from Google Drive, and the source code retains those local import paths.

## Run the compact analysis independently

```bash
python -m pip install -r requirements.txt
python analysis/summary.py /path/to/Ottawa_311_2025_Original.csv
python -m pytest -q
```

`summary.py` reproduces the **core reported population**, seasonal reporting by numerator, service-family coordinate coverage, and mapped 21-day address-anchored episode counts. It **does not** reproduce all 71 field-journal code cells or the retailer candidate/geometry screening. The full analysis is in the notebook. `tests/` uses synthetic fixtures and does not contain unpublished municipal source data.

The original archived historical 2025 CSV had SHA-256:

`e85a4dce98af77cb56504e31fdaf12287f3c5b8454a4b5f015cfca5ec6c48f1a`

The municipal `311opendata_lastyear.csv` URL is a **rolling last-year feed**, not a permanent 2025 snapshot. Downloading it in a later year will not necessarily reproduce 2025 numbers. The archived file and full 2026 Overture GeoJSON source are deliberately not included in this repository. If a file differs, the script reports the checksum mismatch without silently substituting an assumption.

## Full notebook requirements and caveats

- Google Colab and a user-provided 2025 source snapshot in Drive, or adjusted paths.
- `pandas`, `numpy`, `matplotlib`, `scikit-learn`, `folium`, `branca`, `requests`, Colab notebook features.
- A separate 2026 Overture Places GeoJSON archive for the retailer analyses in Chapter 7 onward. The snapshot's precise release ID was not recorded in the publication copy.
- Some Chapter 7 source preparation cells install supporting tools at runtime; review before executing.
- Historical data may have malformed CSV rows; the original import uses `on_bad_lines="warn"` and logs one skipped row.
- No complete end-to-end rerun against the exact archived inputs was performed as part of packaging this public repository. Saved Folium maps were exported from executed outputs in the uploaded final notebook.

The code is provided so that analytical choices can be inspected. **Estimated episodes, retailer candidates and distances are exploratory constructs, not confirmed individual-cart movements.**
