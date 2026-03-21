Open Vantage – ISO 27001:2022 ISMS Documentation Suite
A Python-based ISMS documentation generator built for Open Vantage (Pty) Ltd — a South African software development and AI company preparing for ISO 27001:2022 certification for the first time.
Website: https://openvantage.co.za | Location: Sandton, Johannesburg

Why Open Vantage Needs ISO 27001
Open Vantage provides full-cycle software development, AI services and augmented talent to enterprise clients including Howdens, Ctrack and Omnia. Two enterprise clients have included ISO 27001:2022 certification as a contractual requirement in upcoming renewals — triggering this ISMS project.
Open Vantage operates across three jurisdictions simultaneously:

🇿🇦 South Africa — subject to POPIA (Act 4 of 2013)
🇳🇱 Netherlands — subject to GDPR (EU Regulation 2016/679)
🇬🇧 United Kingdom — subject to UK GDPR and Data Protection Act 2018

As a company that builds security products (Proof — physical security management, YardLink — access control), ISO 27001 certification is both a client requirement and a credibility imperative.

What This Tool Generates
Running python run_isms.py produces 10 complete ISMS documents from a single command:
Policy Documents (6 policies)
Document IDPolicyISO 27001 ClauseOV-POL-001Information Security Policy5.2, Annex A 5.1OV-POL-002Acceptable Use PolicyAnnex A 5.10OV-POL-003Access Control PolicyAnnex A 5.15, 5.16, 5.17, 5.18OV-POL-004Incident Response PolicyAnnex A 5.24, 5.25, 5.26OV-POL-005Remote Working PolicyAnnex A 6.7OV-POL-006Data Classification PolicyAnnex A 5.12, 5.13
ISMS Reports (4 documents)
Document IDReportISO 27001 ClauseOV-ISMS-001ISMS Scope Document4.3OV-SOA-001Statement of Applicability (MD)6.1.3OV-SOA-001Statement of Applicability (CSV)6.1.3OV-GAP-001Compliance Gap Report9.1, 10.2

Current Certification Readiness
StatusControlsPercentage✅ Implemented0 / 910%⚠️ Partially Implemented33 / 9136%❌ Not Implemented58 / 9164%Overall Readiness18.1%Target: 85% before Stage 1 audit
Top Critical Gaps
ControlGapPriority5.1Information Security Policy not approved🔴 Critical5.24Incident Response Plan not tested🔴 Critical6.3No security awareness training programme🔴 Critical8.8No vulnerability scanning tool deployed🔴 Critical8.15No SIEM or centralised logging🔴 Critical5.19Vendor risk assessments not conducted🔴 Critical

Project Structure
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

How to Run
bashpython run_isms.py
No additional packages required — pure Python standard library only.