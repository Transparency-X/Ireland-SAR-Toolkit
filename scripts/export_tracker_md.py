#!/usr/bin/env python3
"""
Export tracker CSV to Obsidian markdown table.
Usage: python export_tracker_md.py <tracker.csv> <output.md>
"""

import csv
import sys
from datetime import datetime


def csv_to_md(csv_path, md_path):
    with open(csv_path, "r") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    if not rows:
        print("No rows to export.")
        return

    headers = list(rows[0].keys())
    lines = ["| " + " | ".join(headers) + " |"]
    lines.append("| " + " | ".join(["---"] * len(headers)) + " |")

    for row in rows:
        if not any(row.values()):
            continue
        lines.append("| " + " | ".join(row.get(h, "") for h in headers) + " |")

    with open(md_path, "w") as f:
        f.write(f"# SAR Tracker Export\n\n*Generated: {datetime.now().isoformat()}*\n\n")
        f.write("\n".join(lines))

    print(f"Obsidian table written to: {md_path}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python export_tracker_md.py <tracker.csv> <output.md>")
        sys.exit(1)
    csv_to_md(sys.argv[1], sys.argv[2])
