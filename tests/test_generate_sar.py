#!/usr/bin/env python3
"""Tests for generate_sar.py"""

import os
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from scripts.generate_sar import generate, load_config, validate_config, discover_agencies


def test_discover_agencies():
    with tempfile.TemporaryDirectory() as tmpdir:
        templates_dir = Path(tmpdir) / "templates"
        templates_dir.mkdir()
        (templates_dir / "test_sar.md").write_text("Test template: $full_name")
        (templates_dir / "another_sar.md").write_text("Another template: $dob")

        import scripts.generate_sar as gen_sar
        original = gen_sar.TEMPLATE_DIR
        gen_sar.TEMPLATE_DIR = str(templates_dir)

        agencies = discover_agencies()
        assert "test" in agencies
        assert "another" in agencies

        gen_sar.TEMPLATE_DIR = original


def test_generate_sar():
    with tempfile.TemporaryDirectory() as tmpdir:
        templates_dir = Path(tmpdir) / "templates"
        templates_dir.mkdir()
        (templates_dir / "generic_sar.md").write_text("Test: $full_name, $date_today")

        output_dir = Path(tmpdir) / "output"
        user_data = {
            "full_name": "Test User",
            "dob": "01/01/2000",
            "current_address": "123 Test St",
            "email": "test@example.com"
        }

        import scripts.generate_sar as gen_sar
        original = gen_sar.TEMPLATE_DIR
        gen_sar.TEMPLATE_DIR = str(templates_dir)

        result = generate("test", user_data, str(output_dir), dry_run=True)
        assert result is None

        result = generate("test", user_data, str(output_dir), dry_run=False)
        assert result is not None
        assert os.path.exists(result[0])

        with open(result[0]) as f:
            content = f.read()
            assert "Test User" in content
            assert "Test:" in content

        gen_sar.TEMPLATE_DIR = original


def test_validate_config():
    valid_config = {
        "full_name": "Test User",
        "dob": "01/01/2000",
        "current_address": "123 Test St",
        "email": "test@example.com"
    }
    validate_config(valid_config)

    invalid_config = {"full_name": "Test User"}
    try:
        validate_config(invalid_config)
        assert False, "Should have raised SystemExit"
    except SystemExit:
        pass


if __name__ == "__main__":
    test_discover_agencies()
    test_generate_sar()
    test_validate_config()
    print("All generate_sar tests passed!")
