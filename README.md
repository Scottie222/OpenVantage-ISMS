# Open Vantage – ISO 27001:2022 ISMS Documentation Suite

A Python-based ISMS documentation generator built for **Open Vantage (Pty) Ltd**, a South African software development and AI company preparing for **ISO 27001:2022 certification for the first time**.

**Website:** https://openvantage.co.za | **Location:** Sandton, Johannesburg

---

## Why Open Vantage Needs ISO 27001

Open Vantage provides full-cycle software development, AI services and augmented talent to enterprise clients including Howdens, Ctrack and Omnia. Two enterprise clients have included **ISO 27001:2022 certification as a contractual requirement** in upcoming renewals, triggering this ISMS project.

Open Vantage operates across **three jurisdictions** simultaneously:
- 🇿🇦 **South Africa** — subject to POPIA (Act 4 of 2013)
- 🇳🇱 **Netherlands** — subject to GDPR (EU Regulation 2016/679)
- 🇬🇧 **United Kingdom** — subject to UK GDPR and Data Protection Act 2018

As a company that builds security products (Proof — physical security management, YardLink — access control), ISO 27001 certification is both a **client requirement and a credibility imperative**.

---

## What This Tool Generates

Running `python run_isms.py` produces **10 complete ISMS documents** from a single command:

### Policy Documents (6 policies)

| Document ID | Policy | ISO 27001 Clause |
|---|---|---|
| OV-POL-001 | Information Security Policy | 5.2, Annex A 5.1 |
| OV-POL-002 | Acceptable Use Policy | Annex A 5.10 |
| OV-POL-003 | Access Control Policy | Annex A 5.15, 5.16, 5.17, 5.18 |
| OV-POL-004 | Incident Response Policy | Annex A 5.24, 5.25, 5.26 |
| OV-POL-005 | Remote Working Policy | Annex A 6.7 |
| OV-POL-006 | Data Classification Policy | Annex A 5.12, 5.13 |

### ISMS Reports (4 documents)

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
| **Overall Readiness** | **18.1%** | Target: 85% before Stage 1 audit |

### Top Critical Gaps

| Control | Gap | Priority |
|---|---|---|
| 5.1 | Information Security Policy not approved | 🔴 Critical |
| 5.24 | Incident Response Plan not tested | 🔴 Critical |
| 6.3 | No security awareness training programme | 🔴 Critical |
| 8.8 | No vulnerability scanning tool deployed | 🔴 Critical |
| 8.15 | No SIEM or centralised logging | 🔴 Critical |
| 5.19 | Vendor risk assessments not conducted | 🔴 Critical |

---

## Project Structure

```
OpenVantage-ISMS/
├── data/
│   ├── __init__.py
│   └── ov_context.py          # Company profile, ISMS scope, all 93 Annex A controls
├── isms_generator/
│   ├── __init__.py
│   ├── generate_scope.py      # ISMS Scope Document (ISO 27001 Clause 4.3)
│   ├── generate_policies.py   # 6 policy documents
│   ├── generate_soa.py        # Statement of Applicability (93 controls)
│   └── generate_gap_report.py # Compliance gap report with remediation roadmap
├── outputs/
│   ├── policies/              # 6 generated policy documents
│   └/  reports/               # Scope, SoA, Gap Report
├── run_isms.py                # Single-command runner
├── requirements.txt
└── README.md
```

---

## How to Run

```bash
python run_isms.py
```

No additional packages required, pure Python standard library only.

---

## ISO 27001:2022 Alignment

| Clause | Requirement | Implementation |
|---|---|---|
| 4.3 | Determine ISMS scope | OV-ISMS-001 Scope Document |
| 5.2 | Information security policy | OV-POL-001 |
| 6.1.3 | Statement of Applicability | OV-SOA-001 (93 controls) |
| 9.1 | Monitoring and measurement | OV-GAP-001 Gap Report |
| 10.2 | Continual improvement | Remediation roadmap in gap report |

---

## Regulatory Compliance Coverage

| Regulation | Relevance | Documents Addressing It |
|---|---|---|
| **POPIA (Act 4 of 2013)** | SA HQ — personal data of employees and clients | POL-001, POL-004, POL-006, SOA-001 |
| **GDPR (EU 2016/679)** | Netherlands office operations | POL-001, POL-004, POL-005, SOA-001 |
| **UK GDPR / DPA 2018** | UK office operations | POL-001, POL-004, SOA-001 |
| **ECTA (Act 25 of 2002)** | Electronic communications compliance | POL-002, SOA-001 |

---

## Remediation Roadmap

| Phase | Timeline | Focus |
|---|---|---|
| Phase 1 – Foundation | Month 1–2 | Policies, Asset Register, AUP, Data Classification |
| Phase 2 – Technical | Month 2–4 | MFA, EDR, SIEM, vulnerability scanning, MDM |
| Phase 3 – Process & People | Month 3–5 | Awareness training, IR testing, supplier contracts |
| Phase 4 – Audit Readiness | Month 5–6 | Internal audit, management review, Stage 1 prep |
| **Certification** | **Q4 2025** | Stage 1 and Stage 2 certification audits |

---

## Related Projects

- [StandardBank-Risk-Assessment](https://github.com/Scottie222/StandardBank-Risk-Assessment) — ISO 27001 Risk Assessment (Experian breach 2020)
- [GRC-Controls-Lab](https://github.com/Scottie222/GRC-Controls-Lab) — ISO 27001 & NIST CSF control implementation
- [POPIA-GDPR-Compliance-Tracker](https://github.com/Scottie222/POPIA-GDPR-Compliance-Tracker) — Automated POPIA/GDPR compliance scoring
