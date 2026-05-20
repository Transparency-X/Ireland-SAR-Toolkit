# Ireland SAR Toolkit v2.1

> A forensic-grade toolkit for executing Subject Access Requests (SARs) under GDPR and the Data Protection Act 2018 against Irish government departments, state agencies, and public bodies.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GDPR](https://img.shields.io/badge/GDPR-Article%2015-blue.svg)](https://gdpr-info.eu/art-15-gdpr/)
[![DPC](https://img.shields.io/badge/DPC-IE-green.svg)](https://dataprotection.ie)

---


# Ireland SAR Toolkit
## One-Pager

> **The only forensic-grade, offline-first toolkit for exercising your data subject rights across the entire Irish State.**

---

## Components

| Component | Repo Link |
|---|---|
|SAR-ROI-Law-Enforcment|https://github.com/Transparency-X/SAR-ROI-Law-Enforcment

## The Problem

Ireland has **no central citizen data portal**. If you want to know what the State knows about you — from your Garda PULSE record to your HSE medical history, from your DSP welfare file to your Revenue tax data — you must:

1. Find each agency's Data Protection Officer manually
2. Draft bespoke legal requests for every body
3. Track incompatible response timelines across email, post, and portals
4. Prove evidentiary integrity if you need the data for litigation

**This toolkit solves all four problems in one offline, privacy-preserving workflow.**

---

## What It Does

| Feature | Description |
|---|---|
| **Verified DPO Directory** | Current contacts for 10+ Irish government departments and agencies |
| **Agency-Specific Templates** | Gardaí (LED/Section 89), Justice (INIS split), HSE (hospital routing), DSP, Tusla, Revenue, and more |
| **Auto-Generated Letters** | Populate one JSON config file → generate all SAR letters instantly |
| **Deadline Tracking** | Auto-calculated statutory deadlines with ICS calendar export |
| **Forensic Hashing** | SHA-256 + optional Blake3 for chain-of-custody evidence integrity |
| **DPC Complaint Auto-Drafter** | One-click escalation letters when agencies miss deadlines |
| **PII Redaction Tool** | Strip sensitive data before sharing documents with third parties |
| **Obsidian Export** | Markdown tables for personal knowledge management |
| **100% Offline** | No cloud, no API keys, no data leaves your machine |

---

## Who Needs This — Scenario Summary Table

| # | Scenario | Why It Matters | Toolkit Benefit | Time Saved |
|---|---|---|---|---|
| 1 | **Lifelong Data Audit** | You want every record the State holds on you, from birth to today | Pre-built DPO directory + batch generation across all agencies | **~15–20 hours** (researching DPOs, drafting 10+ individual letters, tracking deadlines manually) |
| 2 | **Historical Abuse Survivor** | You need Tusla / foster care records for a legal case | Tusla-specific template with National Archives guidance + forensic hashing for court admissibility | **~10–15 hours** (legal research on Tusla-specific procedures, drafting forensically sound requests, preparing evidence index) |
| 3 | **Immigration & Citizenship** | Your INIS application is delayed; you need your full file | Justice template with INIS branch split + correct DPO routing | **~6–10 hours** (navigating Justice Dept structure, finding correct INIS contact, avoiding rejection due to wrong address) |
| 4 | **Medical Negligence** | You need complete HSE records for litigation | Template explicitly requests hospital-specific DPOs, not just central HSE | **~8–12 hours** (discovering hospitals hold their own records, chasing central HSE for routing, re-sending requests) |
| 5 | **Surveillance & Harassment** | You believe you are under improper Garda monitoring | Gardaí template cites **Section 89 DPA 2018 (LED)**, not generic GDPR | **~5–8 hours** (researching LED vs GDPR distinction, correcting rejected requests, re-submitting with proper legal basis) |
| 6 | **Tax & Welfare Disputes** | Revenue or DSP claims you owe money or were overpaid | Revenue template includes PPSN + tax reference fields; correlates with DSP records | **~4–6 hours** (gathering reference numbers, formatting requests correctly, cross-referencing DSP/Revenue responses) |
| 7 | **Academic Research** | You are studying Irish public sector data practices | Standardised requests for comparative analysis + reproducible forensic hashes | **~12–18 hours** (standardising request formats across agencies, building evidence tracking system from scratch) |
| 8 | **Vulnerable Person's Advocate** | You are helping an elderly relative or person with disabilities exercise SAR rights | Single JSON config, offline execution, auto-deadline reminders, DPC complaint templates | **~10–14 hours** (repeating setup for each client, manual deadline tracking, drafting escalation letters) |

**Average time saved across all scenarios: ~8–14 hours per campaign.**

---

## Time Breakdown: Manual vs Toolkit

| Task | Manual Approach | With Toolkit | Time Saved |
|---|---|---|---|
| Research DPO contacts for 8+ agencies | 3–5 hours (web search, phone calls, outdated lists) | **2 minutes** (pre-verified directory) | ~3–5 hrs |
| Draft 8+ individual SAR letters | 4–6 hours (copy-paste, reformat, legal review) | **5 minutes** (auto-populate from JSON config) | ~4–6 hrs |
| Calculate statutory deadlines | 1–2 hours (calendar math, extension rules) | **Instant** (auto-calculated + ICS export) | ~1–2 hrs |
| Set calendar reminders | 30–60 min (manual entry per agency) | **Instant** (batch .ics generation) | ~30–60 min |
| Create evidence index for responses | 2–3 hours (spreadsheet, manual hashing) | **2 minutes** (`hash_responses.py`) | ~2–3 hrs |
| Draft DPC complaint letters | 2–3 hours (legal drafting per agency) | **2 minutes** (auto-generated from tracker) | ~2–3 hrs |
| Verify response integrity later | 1–2 hours (manual re-check) | **30 seconds** (`--verify` mode) | ~1–2 hrs |
| **TOTAL PER CAMPAIGN** | **~14–22 hours** | **~15–20 minutes** | **~13–21 hours** |

---

## The Irish Context — Competitive Comparison

| Challenge | Generic GDPR Tool | Ireland SAR Toolkit |
|---|---|---|
| No central data portal | ❌ Fails | ✅ Pre-mapped DPO directory |
| Gardaí under LED (Part 3 DPA 2018) | ❌ Uses wrong legal basis | ✅ Section 89 template |
| HSE records held by individual hospitals | ❌ Sends to central HSE only | ✅ Hospital routing guidance |
| Justice split across INIS / Prison Service / Courts | ❌ One generic letter | ✅ Branch-specific templates |
| 1-month deadline (+ 2-month extension) | ❌ Manual tracking | ✅ Auto-calc + ICS export |
| DPC complaints require structured evidence | ❌ Ad-hoc drafting | ✅ Auto-generated with hashes |
| Cloud tools risk PII leakage | ❌ SaaS dependency | ✅ 100% offline, local execution |
| Evidence integrity for litigation | ❌ No verification | ✅ SHA-256 / Blake3 + verification mode |

---

## Technical Specs

| Attribute | Detail |
|---|---|
| **Language** | Python 3.8+ |
| **Dependencies** | `blake3` (optional, for faster hashing) |
| **Runtime** | Local machine only — no cloud, no API keys |
| **Security** | `.gitignore` blocks all PII; `.dockerignore` prevents image leakage |
| **Container** | Docker + Compose with non-root user, read-only config mount |
| **Testing** | `pytest` compatible test suite |
| **Export Formats** | Markdown, CSV, ICS (calendar), PDF-ready letters |
| **License** | MIT |

---

## Quick Start

```bash
# 1. Download and enter
cd ireland-sar-toolkit

# 2. Set up (creates venv, installs deps, copies config template)
chmod +x setup.sh && ./setup.sh

# 3. Fill your details
nano config/my_details.json

# 4. Generate all SAR letters
python scripts/generate_sar.py --all --custodian "Your Name"

# 5. Track deadlines in your calendar
python scripts/ics_generator.py tracking/sar_tracker.csv output/

# 6. When responses arrive, hash them forensically
python scripts/hash_responses.py --scan responses/ --custodian "Your Name"
```

---

## Legal Foundation

- **GDPR Article 15** — Right of access (civil bodies)
- **Data Protection Act 2018, Part 3** — Law Enforcement Directive (An Garda Síochána)
- **Data Protection Act 2018, Section 91** — Right of access (public bodies)
- **Data Protection Act 2018, Section 111** — DPC complaint mechanism
- **Freedom of Information Act 2014** — Complementary regime for non-personal records

---

## The Bottom Line

> **Every other GDPR tool is generic. This one is built for Irish bureaucracy.**

If you have ever wondered *"what does the State know about me?"* — this is the most rigorous, privacy-preserving, and legally sound way to find out.

**Free. Open source. Offline. Forensic.**

---
## ⚠️ Security Warning

> **Never commit `config/my_details.json` or any PII to version control.**
> Run this toolkit **only on a local, encrypted machine**. Avoid cloud IDEs (GitHub Codespaces, Replit).

---

## Setup

### 1. Clone or Download
```bash
git clone <repository-url>
cd ireland-sar-toolkit
```

### 2. Run Setup Script
```bash
chmod +x setup.sh
./setup.sh
```

### 3. Configure Your Details
```bash
# Edit with your personal details
nano config/my_details.json
```

### 4. (Optional) Install Blake3 for Faster Hashing
```bash
pip install blake3
```

---

## Usage

### List Available Agencies
```bash
python scripts/generate_sar.py --list-agencies
```

### Generate SAR Letters
```bash
# Single agency
python scripts/generate_sar.py --agency Dept_of_Justice --output output/ --custodian "Your Name"

# All agencies
python scripts/generate_sar.py --all --output output/ --custodian "Your Name"

# Dry run (preview only)
python scripts/generate_sar.py --all --dry-run
```

### Hash Responses for Forensic Integrity
```bash
# Scan and index responses
python scripts/hash_responses.py --scan responses/ --custodian "Your Name" --output forensic/

# Verify hashes later
python scripts/hash_responses.py --verify forensic/evidence_index_YYYYMMDD.csv
```

### Export Tracker to Obsidian
```bash
python scripts/export_tracker_md.py tracking/sar_tracker.csv output/obsidian_tracker.md
```

### Generate Calendar Reminders
```bash
python scripts/ics_generator.py tracking/sar_tracker.csv output/
```

### Draft DPC Complaints
```bash
python scripts/dpc_complaint_drafter.py tracking/sar_tracker.csv "Your Name" output/
```

### Redact PII from Shared Documents
```bash
python scripts/redact.py input.md output_redacted.md
```

---

## Directory Structure
```
ireland-sar-toolkit/
├── .gitignore
├── .dockerignore
├── README.md
├── LICENSE
├── pytest.ini
├── config/
│   ├── my_details_template.json
│   └── schema.json
├── docs/
│   ├── legal_basis.md
│   ├── foi_vs_sar.md
│   └── opsec_protocol.md
├── templates/
│   ├── generic_sar.md
│   ├── garda_f20.md
│   ├── justice_sar.md
│   ├── hse_sar.md
│   ├── dsp_sar.md
│   ├── tusla_sar.md
│   ├── revenue_sar.md
│   └── dpc_complaint_template.md
├── tracking/
│   └── sar_tracker_template.csv
├── scripts/
│   ├── generate_sar.py
│   ├── hash_responses.py
│   ├── export_tracker_md.py
│   ├── ics_generator.py
│   ├── dpc_complaint_drafter.py
│   └── redact.py
├── tests/
│   ├── __init__.py
│   ├── test_generate_sar.py
│   ├── test_hash_responses.py
│   ├── test_export_tracker_md.py
│   ├── test_ics_generator.py
│   └── test_dpc_complaint_drafter.py
├── requirements.txt
├── pyproject.toml
├── setup.sh
├── Dockerfile
└── docker-compose.yml
```

---

## Master DPO Directory

| Organisation | Data Held | DPO / SAR Contact | Address | Notes |
|---|---|---|---|---|
| **An Garda Síochána** | Criminal records, PULSE, incident reports, CCTV | dataprotection@garda.ie | Data Protection Unit, 3rd Floor, 89-94 Capel Street, Dublin 1, D01 E3C6 | Use **F20 form**. LED regime applies. |
| **Dept of Justice** | Immigration, citizenship, prison policy | dataprotectioncompliance@justice.ie | DPO, 51 St Stephen's Green, Dublin 2, D02 HK52 | Immigration: also subjectaccessrequests@justice.ie |
| **Dept of Social Protection** | PPSN, welfare, child benefit, Intreo | dpo@welfare.ie | DPO, Goldsmith House, Pearse Street, Dublin 2, D02 YY17 |  |
| **HSE (Central)** | National health records, vaccination | dpo@hse.ie | National Data Protection Office, Dr Steevens Hospital, Steevens Lane, Dublin 8, D08 W2A8 | Apply to specific hospitals directly for their records |
| **Tusla** | Child protection, foster care, state care | See tusla.ie/data-protection | — | Historical records may be in National Archives |
| **Dept of Education** | School records, state exams, SEN | See gov.ie/education | — | CAO holds separate third-level data |
| **Revenue Commissioners** | Tax records, PAYE, VAT, customs | See revenue.ie | — | PPSN + tax ref required |
| **Local Authority** | Housing, planning, social housing | Search "[County] Council data protection officer" | — | Varies by council |

---

## Legal Basis Summary

| Regulation | Applies To | Key Right | Response Time |
|---|---|---|---|
| **GDPR Article 15** | Most controllers | Right of access to personal data | 1 month (+2 months extension) |
| **DPA 2018 (Part 2)** | Standard processing in Ireland | Implements GDPR | As per GDPR |
| **DPA 2018 (Part 3)** | An Garda Síochána law enforcement | Modified right of access | 1 month (broader exemptions) |
| **FOI Act 2014** | Public bodies | Access to any recorded information | 20 working days |

---

## OPSEC Protocol
1. **Never commit PII** to version control.
2. **Run locally only** (no cloud IDEs).
3. **Encrypt at rest** (LUKS, FileVault, VeraCrypt).
4. **Verify hashes** before sharing files.
5. **Use `redact.py`** to strip PII from documents before sharing.

---

## License
MIT License — See [LICENSE](LICENSE) for details.

**Maintained by:** [Your Name / Organisation]
**Last Updated:** May 2026
**DPC:** [dataprotection.ie](https://dataprotection.ie) | 21 Fitzwilliam Square South, Dublin 2, D02 RD28
