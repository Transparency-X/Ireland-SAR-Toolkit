# Ireland SAR Toolkit 🇮🇪
> A forensic-grade toolkit for executing Subject Access Requests (SARs) under GDPR and the Data Protection Act 2018 against Irish government departments, state agencies, and public bodies.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GDPR](https://img.shields.io/badge/GDPR-Article%2015-blue.svg)](https://gdpr-info.eu/art-15-gdpr/)
[![DPC](https://img.shields.io/badge/DPC-IE-green.svg)](https://dataprotection.ie)

---

## Overview

There is **no central database** for personal data held by the Irish State.  
This repository provides verified DPO contacts, request templates, tracking tools, and evidentiary protocols to systematically extract your data from birth to present across all relevant controllers.

**Status:** Active development  
**Jurisdiction:** Republic of Ireland (ROI)  
**Legal Basis:** Article 15 GDPR, Section 91 Data Protection Act 2018, Part 3 LED (An Garda Síochána)

---

## Features

### Current (v1.0)
| Feature | Description |
|---|---|
| **Verified DPO Directory** | Current contact details for 10+ government departments and agencies |
| **Agency-Specific Templates** | Tailored SAR letters for Gardaí (F20), Justice, HSE, DSP, Tusla, Revenue, Local Authorities |
| **LED Compliance** | Correct protocol for law enforcement data (An Garda Síochána) under Part 3 DPA 2018 |
| **FOI Crossover Guide** | When to use SAR vs. Freedom of Information Act 2014 |
| **Deadline Tracker** | Markdown/CSV tracking sheet with statutory deadlines and escalation triggers |
| **Evidentiary Protocol** | SHA-256 hashing, PDF/A archival, chain-of-custody indexing for legal proceedings |
| **Escalation Templates** | Day-14 reminder letters and DPC complaint drafts |

---

## Directory Structure

```
ireland-sar-toolkit/
├── README.md
├── LICENSE
├── docs/
│   ├── legal_basis.md              # GDPR Art 15, DPA 2018, LED analysis
│   ├── foi_vs_sar.md               # Strategic comparison
│   └── redaction_guide.md          # How to challenge unlawful redactions
├── templates/
│   ├── generic_sar.md              # Master template for any department
│   ├── garda_f20.md                # An Garda Síochána F20 guidance
│   ├── justice_sar.md              # Dept of Justice (immigration + general)
│   ├── hse_sar.md                  # HSE central + hospital-specific
│   ├── dsp_sar.md                  # Dept of Social Protection
│   ├── tusla_sar.md                # Tusla Child and Family Agency
│   ├── revenue_sar.md              # Revenue Commissioners
│   └── local_authority_sar.md      # Template for county/city councils
├── tracking/
│   ├── sar_tracker.csv             # Master tracking spreadsheet
│   └── sar_tracker_template.md     # Printable markdown version
├── escalation/
│   ├── day_14_reminder.md
│   ├── day_30_dpc_complaint.md
│   └── dpc_complaint_template.md
└── forensic/
    ├── evidence_protocol.md        # Scanning, hashing, indexing SOP
    └── index_template.csv          # Document index with SHA-256 column
```

---

## Quick Start

### 1. Prepare Your Identity Kit
Before sending any request, gather:
- Current passport or driving licence (photocopy)
- Utility bill dated within last 6 months
- List of **all previous Irish addresses** with dates
- Your PPS Number

### 2. Select Your Targets
Use the [DPO Directory](#master-dpo-directory) below to identify which bodies hold your data.

### 3. Send Requests
- **An Garda Síochána:** Complete the [F20 form](https://www.garda.ie/en/about-us/our-departments/offices-of-the-garda-commissioner/data-protection-unit/) and post to Capel Street.
- **All others:** Use the relevant template from `/templates/` and email or post to the DPO.

### 4. Track & Escalate
Import `/tracking/sar_tracker.csv` into your preferred spreadsheet app. Set calendar reminders for:
- **Day 14:** Send reminder if no acknowledgement
- **Day 30:** Deadline for response (or notification of extension)
- **Day 90:** Final deadline if extension invoked

### 5. Handle Responses Forensically
Follow `/forensic/evidence_protocol.md` to scan, hash, and index all responses.

---

## Master DPO Directory

| Organisation | Data Held | DPO / SAR Contact | Address | Notes |
|---|---|---|---|---|
| **An Garda Síochána** | Criminal records, PULSE, incident reports, CCTV | dataprotection@garda.ie | Data Protection Unit, 3rd Floor, 89-94 Capel Street, Dublin 1, D01 E3C6 | Use **F20 form**. LED regime applies. |
| **Dept of Justice** | Immigration, citizenship, prison policy | dataprotectioncompliance@justice.ie | DPO, 51 St Stephen's Green, Dublin 2, D02 HK52 | Immigration: also subjectaccessrequests@justice.ie |
| **Dept of Social Protection** | PPSN, welfare, child benefit, Intreo | dpo@welfare.ie | DPO, Goldsmith House, Pearse Street, Dublin 2, D02 YY17 |  |
| **HSE (Central)** | National health records, vaccination | dpo@hse.ie | National Data Protection Office, Dr Steevens Hospital, Steevens Lane, Dublin 8, D08 W2A8 | Apply to specific hospitals directly for their records |
| **Tusla** | Child protection, foster care, state care | See [tusla.ie/data-protection](https://www.tusla.ie) | — | Historical records may be in National Archives |
| **Dept of Education** | School records, state exams, SEN | See [gov.ie/education](https://www.gov.ie) | — | CAO holds separate third-level data |
| **Revenue Commissioners** | Tax records, PAYE, VAT, customs | See [revenue.ie](https://www.revenue.ie) | — | PPSN + tax ref required |
| **Local Authority** | Housing, planning, social housing | Search "[County] Council data protection officer" | — | Varies by council |
| **Irish Prison Service** | Prison records, detention data | Via Dept of Justice or [irishprisons.ie](https://www.irishprisons.ie) | — | If applicable |
| **Property Registration Authority** | Property ownership, titles | See [pra.ie](https://www.pra.ie) | — | Residential history verification |

---

## Legal Basis Summary

| Regulation | Applies To | Key Right | Exemptions |
|---|---|---|---|
| **GDPR Article 15** | Most public/private bodies | Right of access to personal data | Manifestly unfounded/excessive requests |
| **Data Protection Act 2018 (Part 2)** | Standard processing in Ireland | Implements GDPR | As per GDPR |
| **Data Protection Act 2018 (Part 3)** | An Garda Síochána law enforcement data | Modified right of access | Broader: ongoing investigations, national security, endangerment |
| **FOI Act 2014** | Public bodies | Access to any recorded information | Personal info of others, deliberative processes |

---

## Roadmap

### v1.1 — Template Expansion (Q2 2026)
- [ ] Add templates for **CAO**, **Land Registry**, **National Archives**, and **RTB** (Residential Tenancies Board)
- [ ] Add **Northern Ireland crossover guide** (UK GDPR / DPA 2018 UK) for cross-border residents
- [ ] Add **Irish language (Gaeilge) versions** of all templates
- [ ] Add **plain English** simplified templates for accessibility

### v1.2 — Automation Tools (Q3 2026)
- [ ] Python script: `generate_sar.py` — CLI tool to auto-populate templates from a JSON config
- [ ] Python script: `hash_responses.py` — Batch SHA-256 hashing and indexing of scanned PDFs
- [ ] CSV-to-ICS converter: Generate calendar reminders from `sar_tracker.csv`
- [ ] Markdown-to-PDF renderer for all templates

### v1.3 — Tracking & Dashboard (Q4 2026)
- [ ] Streamlit dashboard for visual SAR campaign management
- [ ] Deadline countdown with auto-escalation flagging
- [ ] Document upload portal with automatic hashing
- [ ] Export to Obsidian-compatible markdown for personal knowledge management

### v2.0 — Jurisdiction Expansion (2027)
- [ ] **UK module:** England & Wales, Scotland, Northern Ireland SAR protocols
- [ ] **EU module:** Template for cross-border SARs (Art 15 + Art 56 GDPR)
- [ ] **FOI module:** Dedicated FOI request templates and tracking for Irish public bodies

### v2.1 — Legal Intelligence (2027)
- [ ] DPC decision tracker: Database of published DPC SAR-related determinations
- [ ] Redaction challenge guide: Template letters to challenge excessive redactions
- [ ] Judicial review primer: When and how to escalate to the High Court

### v3.0 — Forensic Integration (Future)
- [ ] Integration with chain-of-custody logging standards
- [ ] Timestamped evidence packaging (RFC 3161 timestamping)
- [ ] Automated correlation mapping across multiple agency responses
- [ ] Export to legal brief format (Law Society / FLAC compatible)

---

## Contributing

Contributions welcome. Priority areas:
- Verified DPO contact updates
- New agency templates
- Legal accuracy reviews
- Translation to Irish (Gaeilge)

Please open an issue before submitting major changes.

---

## Disclaimer

This toolkit is provided for **informational and educational purposes** only. It does not constitute legal advice. For complex cases involving criminal records, immigration status, or litigation, consult a solicitor or contact **FLAC** (Free Legal Advice Centres) at [flac.ie](https://www.flac.ie).

---

## License

MIT License — See [LICENSE](LICENSE) for details.

---

**Maintained by:** Transparency-X  
**Last Updated:** May 2026  
**Data Protection Commission:** [dataprotection.ie](https://dataprotection.ie) | 21 Fitzwilliam Square South, Dublin 2, D02 RD28
