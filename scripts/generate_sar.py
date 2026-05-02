#!/usr/bin/env python3
"""
generate_sar.py v2.1.1
Generates agency-specific SAR letters with validation, logging, and forensic hashing.

Usage:
    python generate_sar.py --agency Dept_of_Justice --output output/ --custodian "Your Name"
    python generate_sar.py --all --output output/ --custodian "Your Name"
    python generate_sar.py --list-agencies
    python generate_sar.py --all --dry-run
"""

import argparse
import csv
import hashlib
import json
import os
import re
import sys
from datetime import datetime, timedelta
from string import Template

CONFIG_FILE = "config/my_details.json"
TEMPLATE_DIR = "templates"
TRACKER_FILE = "tracking/sar_tracker.csv"
LOG_FILE = "output/generation.log"


def log(msg):
    ts = datetime.now().isoformat()
    line = f"[{ts}] {msg}"
    print(line)
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    with open(LOG_FILE, "a") as f:
        f.write(line + "\n")


def load_config():
    if not os.path.exists(CONFIG_FILE):
        log(f"ERROR: {CONFIG_FILE} not found.")
        print("\n>>> SETUP REQUIRED <<<")
        print("1. Copy the template:  cp config/my_details_template.json config/my_details.json")
        print("2. Edit the file:      nano config/my_details.json")
        print("3. Fill in your personal details (name, DOB, address, email, etc.)")
        print("4. Ensure valid JSON:  all strings quoted, commas between items, no trailing commas\n")
        sys.exit(1)

    try:
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        log(f"ERROR: {CONFIG_FILE} contains invalid JSON.")
        print(f"\n>>> JSON SYNTAX ERROR in {CONFIG_FILE} <<<")
        print(f"Location: line {e.lineno}, column {e.colno}")
        print(f"Details:  {e.msg}")
        print(f"\nCommon fixes:")
        print("  - Ensure all strings use double quotes (\"name\") not single quotes")
        print("  - Add commas between each field, but NO comma after the last field")
        print("  - Do not leave trailing commas before closing } brackets")
        print("  - Validate online: https://jsonlint.com/")
        print(f"\nRun this to see the file:  cat {CONFIG_FILE}\n")
        sys.exit(1)
    except Exception as e:
        log(f"ERROR: Could not read {CONFIG_FILE}: {e}")
        sys.exit(1)


def validate_config(data):
    required = ["full_name", "dob", "current_address", "email"]
    missing = [f for f in required if not data.get(f)]
    if missing:
        log(f"ERROR: Missing required fields: {', '.join(missing)}")
        print(f"\n>>> MISSING REQUIRED FIELDS in {CONFIG_FILE} <<<")
        print(f"Required: {', '.join(required)}")
        print(f"Missing:  {', '.join(missing)}")
        print("\nPlease fill in all required fields and try again.\n")
        sys.exit(1)
    if not re.match(r"^\d{2}/\d{2}/\d{4}$", data.get("dob", "")):
        log("WARNING: DOB format should be DD/MM/YYYY")


def hash_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def discover_agencies():
    """Discover all agency templates in the templates directory.

    Matches files ending in _sar.md (standard SAR templates) or _f20.md
    (An Garda Siochana F20 form variant).
    """
    agencies = []
    if not os.path.exists(TEMPLATE_DIR):
        return agencies
    for f in sorted(os.listdir(TEMPLATE_DIR)):
        if f.endswith("_sar.md") or f.endswith("_f20.md"):
            # Strip the suffix to get the agency key
            if f.endswith("_sar.md"):
                agencies.append(f.replace("_sar.md", ""))
            else:
                agencies.append(f.replace("_f20.md", ""))
    return agencies


def generate(agency, user_data, out_dir, dry_run=False):
    # Check for agency-specific template (either _sar.md or _f20.md variant)
    agency_file_sar = os.path.join(TEMPLATE_DIR, f"{agency}_sar.md")
    agency_file_f20 = os.path.join(TEMPLATE_DIR, f"{agency}_f20.md")
    generic_file = os.path.join(TEMPLATE_DIR, "generic_sar.md")

    if os.path.exists(agency_file_f20):
        template_path = agency_file_f20
    elif os.path.exists(agency_file_sar):
        template_path = agency_file_sar
    else:
        template_path = generic_file
    if not os.path.exists(template_path):
        log(f"ERROR: No template found for {agency}")
        return None

    with open(template_path, "r") as f:
        template = Template(f.read())

    payload = {k: v for k, v in user_data.items()}
    payload["date_today"] = datetime.now().strftime("%d %B %Y")
    payload["agency_name"] = agency.replace("_", " ")

    result = template.safe_substitute(payload)

    unresolved = re.findall(r"\$[a-zA-Z_]+", result)
    if unresolved:
        log(f"WARNING: Unresolved variables in {agency}: {set(unresolved)}")

    out_path = os.path.join(
        out_dir, f"SAR_{agency}_{datetime.now().strftime('%Y%m%d')}.md"
    )

    if dry_run:
        log(f"[DRY RUN] Would generate: {out_path}")
        return None

    os.makedirs(out_dir, exist_ok=True)
    with open(out_path, "w") as f:
        f.write(result)

    file_hash = hash_file(out_path)
    log(f"Generated: {out_path} | SHA-256: {file_hash}")
    return out_path, file_hash


def update_tracker(agency, filepath, file_hash, custodian):
    os.makedirs(os.path.dirname(TRACKER_FILE), exist_ok=True)
    file_exists = os.path.exists(TRACKER_FILE)

    with open(TRACKER_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow([
                "Request_ID", "Agency", "Date_Sent", "Method_Sent", "Letter_Hash",
                "Day_30_Deadline", "Extended_Deadline", "Status", "Reference_Number",
                "DPO_Email", "Custodian", "Notes"
            ])

        req_id = hashlib.sha256(
            f"{agency}{datetime.now().isoformat()}".encode()
        ).hexdigest()[:16]
        deadline = (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d")
        writer.writerow([
            req_id, agency, datetime.now().strftime("%Y-%m-%d"), "Pending", file_hash,
            deadline, "", "Draft Generated", "", "", custodian, f"Template: {agency}"
        ])
        log(f"Tracker updated: {req_id}")


def main():
    parser = argparse.ArgumentParser(description="Ireland SAR Letter Generator v2.1")
    parser.add_argument("--agency", help="Specific agency key (e.g., Dept_of_Justice)")
    parser.add_argument("--output", default="output", help="Output directory")
    parser.add_argument("--all", action="store_true", help="Generate for all discovered agencies")
    parser.add_argument("--list-agencies", action="store_true", help="List available agency templates")
    parser.add_argument("--custodian", default=os.getenv("USER", "Unknown"), help="Chain of custody custodian")
    parser.add_argument("--dry-run", action="store_true", help="Preview output without writing files")
    args = parser.parse_args()

    if args.list_agencies:
        agencies = discover_agencies()
        print("Available agency templates:")
        for a in agencies:
            print(f"  - {a}")
        sys.exit(0)

    user_data = load_config()
    validate_config(user_data)

    agencies = []
    if args.agency:
        agencies = [args.agency]
    elif args.all:
        agencies = discover_agencies()

    if not agencies:
        log("ERROR: Specify --agency <name>, --all, or --list-agencies")
        sys.exit(1)

    for agency in agencies:
        result = generate(agency, user_data, args.output, args.dry_run)
        if result and not args.dry_run:
            update_tracker(agency, result[0], result[1], args.custodian)

    log("Generation complete.")


if __name__ == "__main__":
    main()
