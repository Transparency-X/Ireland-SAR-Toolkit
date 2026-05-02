# Ireland SAR Toolkit v2.1

> A forensic-grade toolkit for executing Subject Access Requests (SARs) under GDPR and the Data Protection Act 2018 against Irish government departments, state agencies, and public bodies.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GDPR](https://img.shields.io/badge/GDPR-Article%2015-blue.svg)](https://gdpr-info.eu/art-15-gdpr/)
[![DPC](https://img.shields.io/badge/DPC-IE-green.svg)](https://dataprotection.ie)

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
