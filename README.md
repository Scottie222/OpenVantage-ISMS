# Open Vantage – ISO 27001:2022 ISMS Documentation Suite

A Python-based ISMS documentation generator and interactive audit simulator built for **Open Vantage (Pty) Ltd**, a South African software development and AI company preparing for ISO 27001:2022 certification.

**Website:** https://openvantage.co.za &nbsp;·&nbsp; **Location:** Sandton, Johannesburg

---

## Overview

Open Vantage provides full-cycle software development, AI services and augmented talent to enterprise clients including Howdens, Ctrack and Omnia. Two enterprise clients have included ISO 27001:2022 certification as a contractual requirement in upcoming renewals, triggering this ISMS project.

Open Vantage operates across three jurisdictions simultaneously:

| Jurisdiction | Regulation |
|---|---|
| 🇿🇦 South Africa (HQ) | POPIA (Act 4 of 2013) |
| 🇳🇱 Netherlands | GDPR (EU Regulation 2016/679) |
| 🇬🇧 United Kingdom | UK GDPR and Data Protection Act 2018 |

---

## Live Simulator

**Open the ISMS Audit Simulator: https://scottie222.github.io/OpenVantage-ISMS/dashboard/isms_simulator.html**

Toggle all 91 ISO 27001:2022 Annex A controls and watch the certification readiness score update in real time. Includes live charts, priority gap breakdown, change log, and CSV export.

---

## What This Tool Does

Generates 10 complete ISMS documents from a single command, tracks control implementation status, and provides an interactive browser-based audit simulator showing live certification readiness.

```bash
python run_isms.py
```

---

## Project Structure

```
OpenVantage-ISMS/
├── data/
│   ├── __init__.py
│   └── ov_context.py
│
├── isms_generator/
│   ├── __init__.py
│   ├── generate_scope.py
│   ├── generate_policies.py
│   ├── generate_soa.py
│   └── generate_gap_report.py
│
├── dashboard/
│   └── isms_simulator.html
│
├── scripts/
│   ├── update_control_status.py
│   ├── generate_simulator.py
│   ├── open_simulator.sh
│   ├── run_with_status.sh
│   └── bulk_update_example.csv
│
├── outputs/
│   ├── policies/
│   └── reports/
│
├── run_isms.py
├── requirements.txt
└── README.md
```

---

## Usage

### Generate all documents
```bash
python run_isms.py
```

### Open the audit simulator
```bash
# Windows
start dashboard\isms_simulator.html

# Mac / Linux
open dashboard/isms_simulator.html
```

### Update a control status
```bash
python scripts/update_control_status.py --control 8.15 --status implemented
python scripts/update_control_status.py --control 6.3 --status partial
python scripts/update_control_status.py --control 5.1 --status not_implemented
```

### View readiness summary
```bash
python scripts/update_control_status.py --summary
```

### Filter controls
```bash
python scripts/update_control_status.py --list critical
python scripts/update_control_status.py --list high
python scripts/update_control_status.py --list partial
```

### Bulk update from CSV
```bash
python scripts/update_control_status.py --bulk scripts/bulk_update_example.csv
```

### Update and regenerate in one step
```bash
python scripts/update_control_status.py --control 5.1 --status implemented --regenerate
```

---

## Generated Documents

### Policies

| Document | Description | ISO Clause |
|---|---|---|
| OV-POL-001 | Information Security Policy | 5.2, A.5.1 |
| OV-POL-002 | Acceptable Use Policy | A.5.10 |
| OV-POL-003 | Access Control Policy | A.5.15–5.18 |
| OV-POL-004 | Incident Response Policy | A.5.24–5.26 |
| OV-POL-005 | Remote Working Policy | A.6.7 |
| OV-POL-006 | Data Classification Policy | A.5.12–5.13 |

### Reports

| Document | Description | ISO Clause |
|---|---|---|
| OV-ISMS-001 | ISMS Scope Document | 4.3 |
| OV-SOA-001 | Statement of Applicability (MD + CSV) | 6.1.3 |
| OV-GAP-001 | Compliance Gap Report | 9.1, 10.2 |

---

## Score Calculation

```
Readiness = (Implemented × 1.0 + Partially Implemented × 0.5) ÷ 91
```

A minimum score of 85% is recommended before scheduling a Stage 1 certification audit.

---

## Remediation Roadmap

| Phase | Timeline | Focus |
|---|---|---|
| Phase 1 – Foundation | Month 1–2 | Policies, asset register, data classification |
| Phase 2 – Technical | Month 2–4 | MFA, EDR, SIEM, vulnerability scanning, MDM |
| Phase 3 – Process & People | Month 3–5 | Training, IR testing, supplier contracts |
| Phase 4 – Audit Readiness | Month 5–6 | Internal audit, management review, Stage 1 prep |
| Certification | Q4 2025 | Stage 1 and Stage 2 certification audits |

---

## Regulatory Coverage

| Regulation | Jurisdiction |
|---|---|
| POPIA (Act 4 of 2013) | South Africa |
| GDPR (EU 2016/679) | Netherlands |
| UK GDPR / DPA 2018 | United Kingdom |
| ECTA (Act 25 of 2002) | South Africa |

---

## Related Projects

- [StandardBank-Risk-Assessment](https://github.com/Scottie222/StandardBank-Risk-Assessment)
- [GRC-Controls-Lab](https://github.com/Scottie222/GRC-Controls-Lab)
- [POPIA-GDPR-Compliance-Tracker](https://github.com/Scottie222/POPIA-GDPR-Compliance-Tracker)
