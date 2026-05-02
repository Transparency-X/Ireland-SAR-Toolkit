#!/usr/bin/env python3
"""Tests for export_tracker_md.py"""

import os
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from scripts.export_tracker_md import csv_to_md


def test_csv_to_md():
    with tempfile.TemporaryDirectory() as tmpdir:
        csv_path = Path(tmpdir) / "test.csv"
        csv_path.write_text("Agency,Status\nGardaí,Pending\nDSP,Completed")

        md_path = Path(tmpdir) / "output.md"
        csv_to_md(str(csv_path), str(md_path))

        assert os.path.exists(md_path)
        with open(md_path) as f:
            content = f.read()
            assert "# SAR Tracker Export" in content
            assert "Gardaí" in content
            assert "DSP" in content


if __name__ == "__main__":
    test_csv_to_md()
    print("All export_tracker_md tests passed!")
