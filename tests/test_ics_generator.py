#!/usr/bin/env python3
"""Tests for ics_generator.py"""

import os
import sys
import tempfile
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from scripts.ics_generator import generate_ics, escape_ics, create_event


def test_escape_ics():
    assert escape_ics("test;value") == "test\\;value"
    assert escape_ics("test,value") == "test\\,value"
    assert escape_ics("test\nvalue") == "test\\nvalue"
    assert escape_ics(None) == ""
    assert escape_ics("") == ""


def test_create_event():
    start_date = datetime(2026, 5, 15, tzinfo=ZoneInfo("Europe/Dublin"))
    event = create_event("test-uid", "Test Event", start_date, "Test Description")
    assert "BEGIN:VEVENT" in event
    assert "UID:test-uid" in event
    assert "SUMMARY:Test Event" in event
    assert "DESCRIPTION:Test Description" in event
    assert "END:VEVENT" in event


def test_generate_ics():
    with tempfile.TemporaryDirectory() as tmpdir:
        csv_path = Path(tmpdir) / "tracker.csv"
        csv_path.write_text("Agency,Date_Sent\nGardaí,2026-05-01\nDSP,2026-05-02")

        output_dir = Path(tmpdir) / "output"
        output_dir.mkdir()

        generate_ics(str(csv_path), str(output_dir))

        ics_path = output_dir / "sar_deadlines.ics"
        assert os.path.exists(ics_path)
        with open(ics_path) as f:
            content = f.read()
            assert "BEGIN:VCALENDAR" in content
            assert "Gardaí" in content
            assert "SAR DEADLINE" in content
            assert "SAR Reminder" in content


if __name__ == "__main__":
    test_escape_ics()
    test_create_event()
    test_generate_ics()
    print("All ics_generator tests passed!")
