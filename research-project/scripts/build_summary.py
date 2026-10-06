#!/usr/bin/env python3
"""Print weekly totals from the workshop's attendance exports.

Run from the project folder containing data/raw. Output is CSV on stdout.
"""

import csv
from pathlib import Path
import sys


def weekly_totals():
    rows = []
    for week in (1, 2):
        source = Path("data/raw") / f"attendance_week{week}.csv"
        with source.open(newline="", encoding="utf-8") as handle:
            sessions = list(csv.DictReader(handle))
        rows.append((week,
                     sum(int(row["registered"]) for row in sessions),
                     sum(int(row["attended"]) for row in sessions)))
    return rows


def main():
    try:
        rows = weekly_totals()
    except FileNotFoundError as exc:
        print(f"Cannot find {exc.filename}. Run from the project folder "
              "containing data/raw.", file=sys.stderr)
        return 1
    except (KeyError, ValueError) as exc:
        print(f"Could not read attendance totals: {exc}", file=sys.stderr)
        return 1
    writer = csv.writer(sys.stdout, lineterminator="\n")
    writer.writerow(("week", "registered", "attended"))
    writer.writerows(rows)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
