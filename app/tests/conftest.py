from pathlib import Path

from pytest import fixture
from pytest_snapshot.plugin import Snapshot


class Snapshotter:
    def __init__(self, snapshot: Snapshot):
        self.snapshot = snapshot

    def assert_match(self, filepath: Path) -> None:
        pth = Path(filepath)
        contents = pth.read_text(encoding="utf-8")
        self.snapshot.assert_match(contents, pth.name)


@fixture
def snapshotter(snapshot) -> Snapshotter:
    return Snapshotter(snapshot)
