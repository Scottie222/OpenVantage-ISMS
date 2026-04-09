# Open Vantage – ISO 27001:2022 ISMS Documentation Suite

A Python-based ISMS documentation generator and **interactive audit simulator** built for **Open Vantage (Pty) Ltd**, a South African software development and AI company preparing for ISO 27001:2022 certification.

**Website:** https://openvantage.co.za &nbsp;·&nbsp; **Location:** Sandton, Johannesburg

---

## Why Open Vantage Needs ISO 27001

Open Vantage provides full-cycle software development, AI services and augmented talent to enterprise clients including Howdens, Ctrack and Omnia. Two enterprise clients have included **ISO 27001:2022 certification as a contractual requirement** in upcoming renewals, triggering this ISMS project.

Open Vantage operates across **three jurisdictions** simultaneously:

| Jurisdiction | Regulation |
|---|---|
| 🇿🇦 South Africa (HQ) | POPIA (Act 4 of 2013) |
| 🇳🇱 Netherlands | GDPR (EU Regulation 2016/679) |
| 🇬🇧 United Kingdom | UK GDPR and Data Protection Act 2018 |

---

## What This Tool Does

### 1. Generates 10 ISMS documents from one command
```bash
python run_isms.py
```

### 2. Opens an interactive audit simulator in your browser
```bash
./scripts/open_simulator.sh
# or just open: dashboard/isms_simulator.html
```

### 3. Updates individual control statuses from the CLI
```bash
python scripts/update_control_status.py --control 5.1 --status implemented
```

### 4. Shows your live readiness score at any time
```bash
python scripts/update_control_status.py --summary
```

---

## Project Structure

```
OpenVantage-ISMS/
├── data/
│   ├── __init__.py
│   └── ov_context.py                   # Company profile, ISMS scope, all 93 Annex A controls
│                                        # ← EDIT THIS FILE to update control statuses
│
├── isms_generator/
│   ├── __init__.py
│   ├── generate_scope.py               # ISMS Scope Document (ISO 27001 Clause 4.3)
│   ├── generate_policies.py            # 6 policy documents
│   ├── generate_soa.py                 # Statement of Applicability (93 controls)
│   └── generate_gap_report.py          # Compliance gap report with remediation roadmap
│
├── dashboard/
│   └── isms_simulator.html             # ← Interactive audit simulator (open in browser)
│
├── scripts/
│   ├── update_control_status.py        # ← CLI tool: update control statuses
│   ├── generate_simulator.py           # Regenerates simulator from live ov_context.py data
│   ├── open_simulator.sh               # One-click launcher: opens simulator in browser
│   ├── run_with_status.sh              # Update a control + regenerate documents in one step
│   └── bulk_update_example.csv         # Example bulk update input file
│
├── outputs/
│   ├── policies/                       # 6 generated policy documents (.md)
│   └── reports/                        # Scope, SoA (MD + CSV), Gap Report
│
├── run_isms.py                         # Single-command document generator
├── requirements.txt
└── README.md
```

---

## Step-by-Step: How to Use This Tool

### Step 1 — Clone and generate documents

```bash
git clone https://github.com/Scottie222/OpenVantage-ISMS.git
cd OpenVantage-ISMS
python run_isms.py
```

This generates all 10 ISMS documents into `outputs/`.

---

### Step 2 — Open the audit simulator

```bash
# Mac / Linux
./scripts/open_simulator.sh

# Or open directly in any browser
open dashboard/isms_simulator.html       # Mac
xdg-open dashboard/isms_simulator.html  # Linux
start dashboard/isms_simulator.html     # Windows
```

The simulator shows:
- Live readiness score (recalculates as you click)
- All 91 applicable Annex A controls grouped by theme
- Three-button status toggle per control: `Not Implemented` → `Partial` → `Implemented`
- Score formula breakdown (Implemented × 1.0 + Partial × 0.5 ÷ 91)
- Colour-coded stage readiness indicator (red < 50% → amber 50–84% → green ≥ 85%)
- Theme-level progress bars (Themes 5, 6, 7, 8)
- Critical gaps table with checkbox quick-resolve
- Full change log with timestamps
- Export snapshot button (downloads current state as CSV)
- Filter controls by: All / Critical / High / Not Implemented / Partial / Implemented
- Search bar to find any control by ID or name

---

### Step 3 — Update a control status from the terminal

Once you have actually implemented a control (e.g. deployed SIEM for 8.15), update it:

```bash
python scripts/update_control_status.py --control 8.15 --status implemented
python scripts/update_control_status.py --summary
```

Output example:
```
  ✅ Updated:  8.15 — Logging
  Old status : ❌ Not Implemented
  New status : ✅ Implemented
  Score      : 18.1%  →  19.7%  (+1.6%)
  Timestamp  : 2026-04-09 14:32:01
```

---

### Step 4 — Update a control and regenerate all documents at once

```bash
./scripts/run_with_status.sh 5.1 implemented
```

This runs the status update **and** `python run_isms.py` in one step, so all 10 documents reflect the new status.

---

### Step 5 — Bulk update multiple controls

Edit `scripts/bulk_update_example.csv`:

```csv
# control_id,status
5.1,implemented
5.10,implemented
8.5,partial
8.15,partial
```

Then run:

```bash
python scripts/update_control_status.py --bulk scripts/bulk_update_example.csv
python run_isms.py
```

---

### Step 6 — Check specific controls

```bash
python scripts/update_control_status.py --show 8.5        # Show one control
python scripts/update_control_status.py --list critical   # All critical gaps
python scripts/update_control_status.py --list partial    # All partial controls
python scripts/update_control_status.py --list high       # All high-priority gaps
```

---

### Step 7 — Refresh the simulator after CLI updates

```bash
python scripts/generate_simulator.py
# then open: dashboard/isms_simulator_live.html
```

---

## Generated Documents

### Policy Documents (6)

| Document ID | Policy | ISO 27001 Clause |
|---|---|---|
| OV-POL-001 | Information Security Policy | 5.2, Annex A 5.1 |
| OV-POL-002 | Acceptable Use Policy | Annex A 5.10 |
| OV-POL-003 | Access Control Policy | Annex A 5.15, 5.16, 5.17, 5.18 |
| OV-POL-004 | Incident Response Policy | Annex A 5.24, 5.25, 5.26 |
| OV-POL-005 | Remote Working Policy | Annex A 6.7 |
| OV-POL-006 | Data Classification Policy | Annex A 5.12, 5.13 |

### ISMS Reports (4)

| Document ID | Report | ISO 27001 Clause |
|---|---|---|
| OV-ISMS-001 | ISMS Scope Document | 4.3 |
| OV-SOA-001 | Statement of Applicability (MD) | 6.1.3 |
| OV-SOA-001 | Statement of Applicability (CSV) | 6.1.3 |
| OV-GAP-001 | Compliance Gap Report | 9.1, 10.2 |

---

## Current Certification Readiness

| Status | Controls | Percentage |
|---|---|---|
| ✅ Implemented | 0 / 91 | 0% |
| ⚠️ Partially Implemented | 33 / 91 | 36% |
| ❌ Not Implemented | 58 / 91 | 64% |
| **Overall Readiness** | **18.1%** | Target: ≥ 85% before Stage 1 audit |

### Top Critical Gaps

| Control | Gap | Priority |
|---|---|---|
| 5.1 | Information Security Policy not approved | 🔴 Critical |
| 5.24 | Incident Response Plan not tested | 🔴 Critical |
| 6.3 | No security awareness training programme | 🔴 Critical |
| 8.5 | MFA not fully enforced | 🔴 Critical |
| 8.8 | No vulnerability scanning tool deployed | 🔴 Critical |
| 8.15 | No SIEM or centralised logging | 🔴 Critical |
| 8.16 | No automated monitoring or alerting | 🔴 Critical |
| 5.19 | Vendor risk assessments not conducted | 🔴 Critical |

> To update any of these: `python scripts/update_control_status.py --control <id> --status <status>`

---

## How the Score Is Calculated

```
Readiness Score = (Implemented × 1.0 + Partially Implemented × 0.5) ÷ 91
```

| If you implement... | Score impact |
|---|---|
| 1 fully implemented control | +1.1% |
| 1 partially implemented control | +0.5% |
| All 11 critical controls (NI → Impl) | +12.1% |
| All 11 critical + 12 high (NI → Impl) | +25.3% |

---

## Remediation Roadmap

| Phase | Timeline | Focus | Score Gain (est.) |
|---|---|---|---|
| Phase 1 – Foundation | Month 1–2 | Policies, Asset Register, AUP, Data Classification | +11% |
| Phase 2 – Technical | Month 2–4 | MFA, EDR, SIEM, vulnerability scanning, MDM | +22% |
| Phase 3 – Process & People | Month 3–5 | Awareness training, IR testing, supplier contracts | +20% |
| Phase 4 – Audit Readiness | Month 5–6 | Internal audit, management review, Stage 1 prep | +14% |
| **Certification** | **Q4 2025** | Stage 1 and Stage 2 certification audits | **85%+** |

---

## All Available Commands

```bash
# ── Document generation ───────────────────────────────────────────────────────
python run_isms.py

# ── Simulator ────────────────────────────────────────────────────────────────
./scripts/open_simulator.sh
python scripts/generate_simulator.py

# ── Control status (single) ──────────────────────────────────────────────────
python scripts/update_control_status.py --summary
python scripts/update_control_status.py --show 8.5
python scripts/update_control_status.py --control 5.1 --status implemented
python scripts/update_control_status.py --control 8.15 --status partial
python scripts/update_control_status.py --control 5.24 --status not_implemented

# ── Control status (list / filter) ───────────────────────────────────────────
python scripts/update_control_status.py --list critical
python scripts/update_control_status.py --list high
python scripts/update_control_status.py --list partial
python scripts/update_control_status.py --list implemented

# ── Bulk update ───────────────────────────────────────────────────────────────
python scripts/update_control_status.py --bulk scripts/bulk_update_example.csv

# ── Update + regenerate in one step ─────────────────────────────────────────
./scripts/run_with_status.sh 5.1 implemented
python scripts/update_control_status.py --control 5.1 --status implemented --regenerate
```

---

## ISO 27001:2022 Alignment

| Clause | Requirement | Implementation |
|---|---|---|
| 4.3 | Determine ISMS scope | OV-ISMS-001 Scope Document |
| 5.2 | Information security policy | OV-POL-001 |
| 6.1.3 | Statement of Applicability | OV-SOA-001 (93 controls) |
| 9.1 | Monitoring and measurement | OV-GAP-001 Gap Report + Simulator |
| 10.2 | Continual improvement | Remediation roadmap in gap report |

---

## Regulatory Compliance Coverage

| Regulation | Relevance | Documents |
|---|---|---|
| **POPIA (Act 4 of 2013)** | SA HQ — personal data of employees and clients | POL-001, POL-004, POL-006, SOA-001 |
| **GDPR (EU 2016/679)** | Netherlands office operations | POL-001, POL-004, POL-005, SOA-001 |
| **UK GDPR / DPA 2018** | UK office operations | POL-001, POL-004, SOA-001 |
| **ECTA (Act 25 of 2002)** | Electronic communications compliance | POL-002, SOA-001 |

---

## Related Projects

- [StandardBank-Risk-Assessment](https://github.com/Scottie222/StandardBank-Risk-Assessment) — ISO 27001 Risk Assessment (Experian breach 2020)
- [GRC-Controls-Lab](https://github.com/Scottie222/GRC-Controls-Lab) — ISO 27001 & NIST CSF control implementation
- [POPIA-GDPR-Compliance-Tracker](https://github.com/Scottie222/POPIA-GDPR-Compliance-Tracker) — Automated POPIA/GDPR compliance scoring
