"""Synthetic tests: no municipal source data required."""
import sys
from pathlib import Path
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'analysis'))
from summary import count_address_episodes, summarize  # noqa: E402


def test_anchored_episode_window_not_rolling():
    dates = pd.to_datetime(['2025-04-01', '2025-04-15', '2025-04-30'])
    data = pd.DataFrame({'Address':['A','A','A'],'Opened_Date':dates,'Has_Coordinates':[True]*3})
    found = count_address_episodes(data)
    assert found['episode_at_address'].tolist() == [1, 1, 2]
    assert found['start'].dt.strftime('%Y-%m-%d').tolist() == [
        '2025-04-01','2025-04-01','2025-04-30'
    ]


def test_four_season_totals_and_distinct_locations():
    data = pd.DataFrame({
        'Season':['Winter','Spring','Summer','Fall'],
        'Has_Coordinates':[True,True,False,True],
        'Address':['A','A',None,'B'],
        'Service_Family':['Road Maintenance']*4
    })
    out = summarize(data, 100)
    assert out['cart_service_requests'] == 4
    assert out['geocoded_reports'] == 3
    assert out['distinct_geocoded_addresses'] == 2
    assert out['all_reports_by_season']['Summer'] == 1
    assert out['geocoded_reports_by_season']['Summer'] == 0
