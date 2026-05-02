#!/usr/bin/env python3
"""
hash_responses.py v2.1
Forensic indexing with SHA-256 and optional Blake3, chain-of-custody metadata,
and verification mode.

Usage:
    python hash_responses.py --scan responses/ --custodian "Your Name"
    python hash_responses.py --verify forensic/evidence_index_YYYYMMDD.csv
"""

import argparse
import csv
import hashlib
import os
import sys
from datetime import datetime

try:
    import blake3
    HAS_BLAKE3 = True
except ImportError:
    HAS_BLAKE3 = False


def hash_file_sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def hash_file_blake3(path):
    if not HAS_BLAKE3:
        return None
    h = blake3.blake3()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def scan_directory(directory, max_depth=3, extensions=None):
    files = []
    seen_paths = set()
    ext_list = None
    if extensions:
        ext_list = [ext.strip().lower() for ext in extensions.split(",") if ext.strip()]

    for root, dirs, filenames in os.walk(directory):
        depth = root[len(directory):].count(os.sep)
        if depth >= max_depth:
            del dirs[:]
            continue
        for fname in filenames:
            path = os.path.realpath(os.path.join(root, fname))
            if path in seen_paths:
                continue
            seen_paths.add(path)
            if ext_list:
                if not any(fname.lower().endswith(ext) for ext in ext_list):
                    continue
            files.append(path)
    return files


def generate_index(files, custodian, notes, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    csv_path = os.path.join(output_dir, f"evidence_index_{timestamp}.csv")
    md_path = os.path.join(output_dir, f"evidence_index_{timestamp}.md")

    headers = [
        "Evidence_ID", "Filename", "Relative_Path", "SHA_256", "BLAKE3",
        "File_Size_Bytes", "Modified_Time", "Indexed_At", "Custodian",
        "Received_Date", "Received_Method", "Notes"
    ]

    rows = []
    md_lines = [
        "# Forensic Evidence Index",
        "",
        f"**Generated:** {datetime.now().isoformat()}",
        f"**Custodian:** {custodian}",
        f"**Total Files:** {len(files)}",
        "",
        "| Evidence_ID | Filename | SHA_256 | BLAKE3 | Size | Indexed_At | Notes |",
        "|-------------|----------|---------|--------|------|------------|-------|"
    ]

    for idx, filepath in enumerate(sorted(files), 1):
        evidence_id = f"EVD-{timestamp}-{idx:04d}"
        sha = hash_file_sha256(filepath)
        bl = hash_file_blake3(filepath)
        size = os.path.getsize(filepath)
        mtime = datetime.fromtimestamp(os.path.getmtime(filepath)).isoformat()
        now = datetime.now().isoformat()
        rel_path = os.path.relpath(filepath)
        fname = os.path.basename(filepath)

        row = [
            evidence_id, fname, rel_path, sha,
            bl if bl else "N/A", size, mtime, now, custodian, "", "", notes
        ]
        rows.append(row)
        blake_display = f"`{bl[:16]}...`" if bl else "N/A"
        md_lines.append(
            f"| {evidence_id} | {fname} | `{sha[:16]}...` | {blake_display} | {size} | {now} | {notes} |"
        )
        print(f"[{idx}/{len(files)}] {fname}")

    with open(csv_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)

    with open(md_path, "w") as f:
        f.write("\n".join(md_lines))

    print(f"\nCSV index: {csv_path}")
    print(f"Obsidian index: {md_path}")
    return csv_path


def verify_index(csv_path):
    print(f"Verifying index: {csv_path}")
    with open(csv_path, "r") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    passed = 0
    failed = 0
    for row in rows:
        path = row.get("Relative_Path", "")
        expected_sha = row.get("SHA_256", "")
        if not os.path.exists(path):
            print(f"  MISSING: {path}")
            failed += 1
            continue
        actual_sha = hash_file_sha256(path)
        if actual_sha == expected_sha:
            passed += 1
        else:
            print(f"  FAIL: {path}")
            print(f"    Expected: {expected_sha}")
            print(f"    Actual:   {actual_sha}")
            failed += 1

    print(f"\nVerification complete: {passed} passed, {failed} failed.")
    return failed == 0


def main():
    parser = argparse.ArgumentParser(description="Forensic SAR Response Hasher v2.1")
    parser.add_argument("--scan", help="Directory to scan")
    parser.add_argument("--output", default="forensic", help="Output directory")
    parser.add_argument("--custodian", default=os.getenv("USER", "Data Subject"),
                        help="Chain of custody custodian")
    parser.add_argument("--notes", default="", help="Global notes for this batch")
    parser.add_argument("--max-depth", type=int, default=3, help="Max recursion depth")
    parser.add_argument("--extensions", default="",
                        help="Comma-separated file extensions to hash (e.g., .pdf,.docx)")
    parser.add_argument("--verify", help="Verify existing CSV index against files")
    args = parser.parse_args()

    if args.verify:
        ok = verify_index(args.verify)
        sys.exit(0 if ok else 1)

    if not args.scan:
        print("ERROR: Provide --scan <directory> or --verify <csv>")
        sys.exit(1)

    if not os.path.exists(args.scan):
        print(f"Directory not found: {args.scan}")
        sys.exit(1)

    files_found = scan_directory(args.scan, args.max_depth, args.extensions or None)
    if not files_found:
        print("No files found.")
        return

    print(f"Found {len(files_found)} files. Hashing...")
    generate_index(files_found, args.custodian, args.notes, args.output)


if __name__ == "__main__":
    main()
