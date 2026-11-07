"""JSON and CSV: the two most common text formats for data on disk."""

import csv
import json
import tempfile
from datetime import date
from pathlib import Path
from typing import Any

# --- JSON ------------------------------------------------------------------
config = {"name": "ARSNEL", "tags": ["python", "learn"], "version": 1.5, "beta": None}
text = json.dumps(config, indent=2, sort_keys=True)  # dict -> str
print(text)
assert json.loads(text) == config  # str -> dict (None <-> null, tuples -> lists)


# json knows only dict, list, str, int, float, bool and None.
# For anything else, teach the encoder with ``default=``.
def encode(obj: Any) -> Any:
    if isinstance(obj, set):
        return sorted(obj)
    if isinstance(obj, date):
        return obj.isoformat()
    raise TypeError(f"cannot serialise {type(obj).__name__}")


record = {"when": date(2024, 3, 14), "colours": {"red", "blue"}}
print(json.dumps(record, default=encode, sort_keys=True))

try:
    json.loads("{'single': 'quotes'}")  # not valid JSON
except json.JSONDecodeError as exc:
    print("bad JSON:", exc.msg, "at column", exc.colno)

with tempfile.TemporaryDirectory() as tmp:
    json_path = Path(tmp) / "config.json"
    with open(json_path, "w", encoding="utf-8") as fh:
        json.dump(config, fh)
    with open(json_path, encoding="utf-8") as fh:
        print("round trip equal:", json.load(fh) == config)

    # --- CSV -----------------------------------------------------------------
    csv_path = Path(tmp) / "people.csv"
    rows = [
        {"name": "Ada", "age": 36, "note": "likes, commas"},
        {"name": "Linus", "age": 54, "note": 'says "hi"'},
    ]
    # newline="" lets the csv module control line endings itself.
    with open(csv_path, "w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=["name", "age", "note"])
        writer.writeheader()
        writer.writerows(rows)

    print(csv_path.read_text(encoding="utf-8").splitlines())  # quoting is automatic

    with open(csv_path, encoding="utf-8", newline="") as fh:
        for row in csv.DictReader(fh):
            # Everything comes back as str - convert numbers yourself.
            print(row["name"], int(row["age"]) + 1, "|", row["note"])
