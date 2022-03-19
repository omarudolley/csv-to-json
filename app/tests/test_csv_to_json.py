from pathlib import Path

import main
from app.tests.conftest import Snapshotter

test_path = Path("app/tests/data/all-data.csv")


def test_csv_to_json_snapshot(snapshotter: Snapshotter):
    main.cvs_to_json(test_path, test_path.parent)
    snapshotter.assert_match(test_path.parent / "all-data.json")
