#!/usr/bin/env python3
"""Recheck links in sources/sources.csv without changing research data."""
import csv
import urllib.error
import urllib.request
from pathlib import Path

path = Path(__file__).resolve().parents[1] / "sources" / "sources.csv"
with path.open(newline="", encoding="utf-8") as handle:
    rows = list(csv.DictReader(handle))

for row in rows:
    request = urllib.request.Request(
        row["url"],
        headers={"User-Agent": "Mozilla/5.0", "Range": "bytes=0-1024"},
        method="GET",
    )
    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            print(response.getcode(), row["url"])
    except urllib.error.HTTPError as error:
        print(error.code, row["url"])
    except Exception as error:
        print("ERROR", type(error).__name__, row["url"])
