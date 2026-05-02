#!/usr/bin/env python3
"""
redact.py
Auto-redacts PII (PPSN, email, phone, addresses) from text files.

Usage: python redact.py <input_file> <output_file>
"""

import re
import sys


def redact_ppsn(text):
    return re.sub(r"\b\d{7}[A-Z]{1,2}\b", "[REDACTED-PPSN]", text)


def redact_email(text):
    return re.sub(
        r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
        "[REDACTED-EMAIL]",
        text
    )


def redact_phone(text):
    # Irish phone formats: +353 1 234 5678, 087 123 4567, (01) 234 5678
    return re.sub(
        r"\b(?:\+353|0)[\s\-]?[1-9]\d{0,2}[\s\-]?\d{2,3}[\s\-]?\d{2,4}\b",
        "[REDACTED-PHONE]",
        text
    )


def redact_address(text):
    # Enhanced pattern for Irish addresses
    # Matches: "123 Street Name", "Apt 5, Building Name", "Co. Dublin", "Dublin 2"
    patterns = [
        # Eircode: A65 F4E2, D02 XY31
        r"\b[A-Z]\d{2}\s?[A-Z0-9]{4}\b",
        # "Co. Dublin", "Co Cork"
        r"\bCo\.?\s+[A-Z][a-z]+\b",
        # "Dublin 2", "Cork City"
        r"\b(?:Dublin|Cork|Galway|Limerick|Waterford|Kilkenny)\s+\d?\b",
        # Street numbers with names
        r"\b\d+[A-Za-z]?\s+[A-Z][a-zA-Z\s]+(?:Street|Road|Avenue|Lane|Drive|Crescent|Place|Square|Terrace|Park|Way|Close|Grove|Heights|Mews|Court|Gardens|Green|Grove|Hill|Mount|Quay|Walk)\b",
        # "Apartment 5", "Flat 2B", "Unit 3"
        r"\b(?:Apartment|Flat|Unit|Suite|Room|Floor|Level)\s*\d+[A-Z]?\b",
    ]
    for pattern in patterns:
        text = re.sub(pattern, "[REDACTED-ADDRESS]", text, flags=re.IGNORECASE)
    return text


def redact_file(input_path, output_path):
    with open(input_path, "r") as f:
        text = f.read()

    text = redact_ppsn(text)
    text = redact_email(text)
    text = redact_phone(text)
    text = redact_address(text)

    with open(output_path, "w") as f:
        f.write(text)

    print(f"Redacted file written to: {output_path}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python redact.py <input_file> <output_file>")
        sys.exit(1)
    redact_file(sys.argv[1], sys.argv[2])
