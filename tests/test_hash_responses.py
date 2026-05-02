#!/usr/bin/env python3
"""Tests for hash_responses.py"""

import os
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from scripts.hash_responses import (
    hash_file_sha256, hash_file_blake3, scan_directory, generate_index, verify_index
)


def test_hash_file_sha256():
    with tempfile.NamedTemporaryFile(delete=False) as f:
        f.write(b"test content")
        f.flush()

    hash_value = hash_file_sha256(f.name)
    expected = "6ae8a75555209fd6c44157c0aed8016e763ff435a19cf186f76863140143ff72"
    assert hash_value == expected, f"Expected {expected}, got {hash_value}"
    os.unlink(f.name)


def test_scan_directory():
    with tempfile.TemporaryDirectory() as tmpdir:
        (Path(tmpdir) / "file1.pdf").write_text("test")
        (Path(tmpdir) / "file2.docx").write_text("test")
        (Path(tmpdir) / "file3.txt").write_text("test")

        files = scan_directory(tmpdir, max_depth=3, extensions=None)
        assert len(files) == 3

        files = scan_directory(tmpdir, max_depth=3, extensions=".pdf,.docx")
        assert len(files) == 2
        assert all(f.endswith((".pdf", ".docx")) for f in files)


def test_generate_index():
    with tempfile.TemporaryDirectory() as tmpdir:
        (Path(tmpdir) / "file1.pdf").write_text("test1")
        (Path(tmpdir) / "file2.pdf").write_text("test2")

        files = [
            str(Path(tmpdir) / "file1.pdf"),
            str(Path(tmpdir) / "file2.pdf")
        ]
        output_dir = Path(tmpdir) / "forensic"
        output_dir.mkdir()

        csv_path = generate_index(files, "Test Custodian", "Test Notes", str(output_dir))
        assert os.path.exists(csv_path)
        assert os.path.exists(csv_path.replace(".csv", ".md"))


def test_verify_index():
    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = Path(tmpdir) / "test.txt"
        test_file.write_text("verify me")

        files = [str(test_file)]
        output_dir = Path(tmpdir) / "forensic"
        output_dir.mkdir()

        csv_path = generate_index(files, "Test", "Notes", str(output_dir))
        ok = verify_index(csv_path)
        assert ok


if __name__ == "__main__":
    test_hash_file_sha256()
    test_scan_directory()
    test_generate_index()
    test_verify_index()
    print("All hash_responses tests passed!")
