#!/usr/bin/env python3
"""
ics_generator.py
Reads tracker CSV and generates .ics calendar files for Day-14 and Day-30 deadlines.
Usage: python ics_generator.py <tracker.csv> [output_dir]
"""

import csv
import os
import sys
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo


def escape_ics(text):
    if not text:
        return ""
    return text.replace("\\", "\\\\").replace(";", "\\;").replace(",", "\\,").replace("\n", "\\n")


def create_event(uid, summary, start_date, description):
    dtstart = start_date.strftime("%Y%m%d")
    return "\n".join([
        "BEGIN:VEVENT",
        f"UID:{uid}",
        f"SUMMARY:{escape_ics(summary)}",
        f"DTSTART;VALUE=DATE:{dtstart}",
        f"DTEND;VALUE=DATE:{dtstart}",
        f"DESCRIPTION:{escape_ics(description)}",
        "BEGIN:VALARM",
        "ACTION:DISPLAY",
        "DESCRIPTION:Reminder",
        "TRIGGER:-P1D",
        "END:VALARM",
        "END:VEVENT"
    ])


def generate_ics(tracker_path, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    events = []
    dublin_tz = ZoneInfo("Europe/Dublin")
    uid_counter = 0

    with open(tracker_path, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if not row.get("Agency"):
                continue

            agency = row["Agency"]
            sent_str = row.get("Date_Sent", "")
            if not sent_str:
                continue

            try:
                sent_date = datetime.strptime(sent_str, "%Y-%m-%d").replace(tzinfo=dublin_tz)
            except ValueError:
                continue

            uid_counter += 1
            d14 = sent_date + timedelta(days=14)
            events.append(create_event(
                f"sar-{agency}-d14-{d14.strftime('%Y%m%d')}-{uid_counter:04d}@ireland-sar-toolkit",
                f"SAR Reminder: {agency}",
                d14,
                f"Follow-up if no acknowledgement for SAR to {agency}"
            ))

            uid_counter += 1
            d30 = sent_date + timedelta(days=30)
            events.append(create_event(
                f"sar-{agency}-d30-{d30.strftime('%Y%m%d')}-{uid_counter:04d}@ireland-sar-toolkit",
                f"SAR DEADLINE: {agency}",
                d30,
                f"Statutory deadline for {agency} response. Escalate to DPC if missed."
            ))

    if not events:
        print("No valid tracker entries found.")
        return

    ics_content = "\n".join([
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        "PRODID:-//Ireland SAR Toolkit//EN",
        "CALSCALE:GREGORIAN",
        "METHOD:PUBLISH",
        "\n".join(events),
        "END:VCALENDAR"
    ])

    out_path = os.path.join(out_dir, "sar_deadlines.ics")
    with open(out_path, "w") as f:
        f.write(ics_content)

    print(f"Calendar file generated: {out_path}")
    print("Import into Google Calendar, Outlook, or Apple Calendar.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python ics_generator.py <tracker.csv> [output_dir]")
        sys.exit(1)
    generate_ics(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else "output")
