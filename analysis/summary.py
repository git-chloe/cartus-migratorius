"""Reproduce the public report/season/episode core from an archived Ottawa 311 CSV.

This is a compact independent entrypoint. The full original investigation—including
retailer eligibility decisions and interactive maps—is in notebooks/.

Usage:
    python analysis/summary.py /path/to/Ottawa_311_2025_Original.csv
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import pandas as pd

SEASONS = {
    1: 'Winter', 2: 'Winter', 3: 'Spring', 4: 'Spring', 5: 'Spring',
    6: 'Summer', 7: 'Summer', 8: 'Summer', 9: 'Fall', 10: 'Fall',
    11: 'Fall', 12: 'Winter',
}
SEASON_ORDER = ['Winter', 'Spring', 'Summer', 'Fall']
KNOWN_ARCHIVE_SHA256 = (
    'e85a4dce98af77cb56504e31fdaf12287f3c5b8454a4b5f015cfca5ec6c48f1a'
)


def load_cart_reports(csv_path: Path) -> tuple[pd.DataFrame, int, str]:
    """Parse bilingual field names and isolate descriptions mentioning Shopping Cart."""
    digest = hashlib.sha256(csv_path.read_bytes()).hexdigest()
    source = pd.read_csv(csv_path, low_memory=False, on_bad_lines='warn')
    source.columns = source.columns.str.split('|').str[0].str.strip()
    source['Description_EN'] = (
        source['Description'].astype('string')
        .str.split('|', n=1, regex=False).str[0].str.strip()
    )
    carts = source.loc[
        source['Description_EN'].str.contains('Shopping Cart', case=False, na=False)
    ].copy()
    carts['Opened_Date'] = pd.to_datetime(carts['Opened Date'], errors='coerce')
    carts['Has_Coordinates'] = (
        pd.to_numeric(carts['Latitude'], errors='coerce').notna()
        & pd.to_numeric(carts['Longitude'], errors='coerce').notna()
    )
    carts['Service_Family'] = (
        carts['Description_EN'].str.split(' - ', n=1, regex=False).str[0].str.strip()
    )
    carts['Season'] = carts['Opened_Date'].dt.month.map(SEASONS)
    return carts, len(source), digest


def count_address_episodes(reports: pd.DataFrame, max_days: int = 21) -> pd.DataFrame:
    """Anchor each estimated episode to the first report at the same recorded address.

    Does not identify distinct carts or prove that reports concern one incident.
    """
    episodes = []
    mapped = reports.loc[reports['Has_Coordinates'] & reports['Address'].notna()]
    for address, group in mapped.groupby('Address'):
        start = None
        episode = 0
        for date in group['Opened_Date'].dropna().sort_values():
            day = date.normalize()
            if start is None or (day - start).days > max_days:
                start = day
                episode += 1
            episodes.append({'address': address, 'start': start, 'report_date': day,
                             'episode_at_address': episode})
    return pd.DataFrame(episodes)


def summarize(carts: pd.DataFrame, full_source_rows: int) -> dict:
    mapped = carts[carts['Has_Coordinates']]
    annual_by_season = carts.groupby('Season').size().reindex(SEASON_ORDER, fill_value=0)
    mapped_by_season = mapped.groupby('Season').size().reindex(SEASON_ORDER, fill_value=0)
    family = carts.groupby('Service_Family')['Has_Coordinates'].agg(['sum', 'count'])
    return {
        'full_source_rows': full_source_rows,
        'cart_service_requests': int(len(carts)),
        'geocoded_reports': int(len(mapped)),
        'reports_missing_coordinates': int((~carts['Has_Coordinates']).sum()),
        'distinct_geocoded_addresses': int(mapped['Address'].nunique()),
        'all_reports_by_season': {k: int(v) for k, v in annual_by_season.items()},
        'geocoded_reports_by_season': {k: int(v) for k, v in mapped_by_season.items()},
        'service_family_coverage': {
            str(name): {'geocoded': int(row['sum']), 'total': int(row['count'])}
            for name, row in family.iterrows()
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('archived_csv', type=Path, help='Preserved historical CSV, not live rolling feed')
    parser.add_argument('--output-json', type=Path, help='Optional JSON report output file')
    args = parser.parse_args()
    if not args.archived_csv.is_file():
        parser.error('CSV not found. Download/source your own archived 2025 file.')
    carts, rows, sha = load_cart_reports(args.archived_csv)
    result = summarize(carts, rows)
    result['source_sha256'] = sha
    result['matches_field_journal_archive'] = (sha == KNOWN_ARCHIVE_SHA256)
    result['mapped_estimated_episodes_21d'] = len(count_address_episodes(carts))
    payload = json.dumps(result, indent=2, ensure_ascii=False)
    print(payload)
    if args.output_json:
        args.output_json.parent.mkdir(parents=True, exist_ok=True)
        args.output_json.write_text(payload + '\n', encoding='utf-8')

if __name__ == '__main__':
    main()
