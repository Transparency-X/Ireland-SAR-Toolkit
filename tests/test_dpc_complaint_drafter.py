#!/usr/bin/env python3
"""Tests for dpc_complaint_drafter.py"""

import os
import sys
import tempfile
from pathlib import Path
from datetime import datetime, timedelta

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from scripts.dpc_complaint_drafter import draft_complaints


def test_draft_complaints():
    with tempfile.TemporaryDirectory() as tmpdir:
        csv_path = Path(tmpdir) / "tracker.csv"
        overdue_date = (datetime.now() - timedelta(days=35)).strftime("%Y-%m-%d")
        csv_path.write_text(
            f"Agency,Date_Sent,Day_30_Deadline,Status,Letter_Hash\n"
            f"Gardaí,2026-04-01,{overdue_date},Pending,abc123"
        )

        output_dir = Path(tmpdir) / "output"
        output_dir.mkdir()

        draft_complaints(str(csv_path), "Test User", str(output_dir))

        complaint_files = list(output_dir.glob("DPC_Complaint_*.md"))
        assert len(complaint_files) == 1
        with open(complaint_files[0]) as f:
            content = f.read()
            assert "Gardaí" in content
            assert "Test User" in content
            assert "abc123" in content


if __name__ == "__main__":
    test_draft_complaints()
    print("All dpc_complaint_drafter tests passed!")
