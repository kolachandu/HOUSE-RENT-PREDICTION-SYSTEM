from csv import DictReader, DictWriter
from pathlib import Path


def read_csv(path):
    with Path(path).open(newline="", encoding="utf-8") as file:
        return list(DictReader(file))


def write_csv(path, rows):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        return
    with path.open("w", newline="", encoding="utf-8") as file:
        writer = DictWriter(file, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
