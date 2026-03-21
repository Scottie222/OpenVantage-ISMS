"""
Open Vantage ISMS – Compliance Gap Report Generator
Reads the SoA data and produces a prioritised gap report
Outputs: outputs/reports/OV-GAP-001-Compliance-Gap-Report.md
"""
 
import os, sys
from datetime import date
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from data.ov_context import COMPANY, ANNEX_A_CONTROLS
 
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'outputs', 'reports')
os.makedirs(OUTPUT_DIR, exist_ok=True)
 
TODAY   = date.today().strftime("%d %B %Y")
VERSION = "v1.0"
 
# Priority mapping — which controls are most critical for OV
PRIORITY_CONTROLS = {
    # Critical — must fix before certification audit
    "5.1":  "Critical", "5.24": "Critical", "5.25": "Critical",
    "5.26": "Critical", "6.3":  "Critical", "8.5":  "Critical",
    "8.8":  "Critical", "8.15": "Critical", "8.16": "Critical",
    "5.19": "Critical", "5.20": "Critical",
    # High — significant gap
    "5.9":  "High", "5.10": "High", "5.12": "High", "5.17": "High",
    "5.18": "High", "6.7":  "High", "8.1":  "High", "8.2":  "High",
    "8.11": "High", "8.12": "High", "8.22": "High", "8.25": "High",
    # Medium — should fix before audit
    "5.3":  "Medium", "5.7":  "Medium", "5.29": "Medium", "5.30": "Medium",
    "6.5":  "Medium", "6.8":  "Medium", "7.7":  "Medium", "7.9":  "Medium",
    "8.6":  "Medium", "8.10": "Medium", "8.18": "Medium", "8.19": "Medium",
    "8.20": "Medium", "8.23": "Medium", "8.26": "Medium", "8.30": "Medium",
}
 
PRIORITY_EMOJI = {
    "Critical": "🔴",
    "High":     "🟠",
    "Medium":   "🟡",
    "Low":      "🟢",
}
 
# Recommended actions per control
ACTIONS = {
    "5.1":  "Draft and obtain CEO approval for Information Security Policy (OV-POL-001)",
    "5.24": "Finalise and test Incident Response Policy and runbooks (OV-POL-004)",
    "5.25": "Develop incident classification procedure and triage checklist",
    "5.26": "Create IR playbooks for: ransomware, data breach, account compromise",
    "6.3":  "Implement quarterly security awareness training; run first phishing simulation",
    "8.5":  "Enforce MFA on all systems; document authentication policy",
    "8.8":  "Deploy vulnerability scanning tool (e.g. Snyk, Tenable); establish patch SLA",
    "8.15": "Deploy SIEM or centralised logging; configure retention policies",
    "8.16": "Configure automated alerting on SIEM; define monitoring thresholds",
    "5.19": "Conduct vendor risk assessments for all critical suppliers (AWS, GitHub, Slack)",
    "5.20": "Add security annexures to all vendor contracts; obtain signed DPA agreements",
    "5.9":  "Create and maintain asset register covering all systems, data and cloud resources",
    "5.10": "Draft Acceptable Use Policy; obtain signatures from all staff and contractors",
    "5.12": "Implement Data Classification Policy (OV-POL-006); label all existing assets",
    "5.17": "Implement password manager; enforce 14-character minimum; document auth policy",
    "5.18": "Schedule quarterly access reviews; document review process and outcomes",
    "6.7":  "Finalise Remote Working Policy (OV-POL-005); require VPN for all remote access",
    "8.1":  "Enrol all endpoints in MDM; enforce encryption, lock screen and remote wipe",
    "8.2":  "Deploy PAM solution; eliminate shared admin credentials",
    "8.11": "Implement data masking for all development and test environments",
    "8.12": "Deploy DLP solution; configure rules for client IP and personal data",
    "8.22": "Segregate dev, staging and production cloud environments",
    "8.25": "Document Secure SDLC; add security gates to all CI/CD pipelines",
}
 
 
def generate_gap_report():
    applicable     = [c for c in ANNEX_A_CONTROLS if c["applicable"]]
    not_impl       = [c for c in applicable if c["status"] == "Not Implemented"]
    partial        = [c for c in applicable if c["status"] == "Partially Implemented"]
    implemented    = [c for c in applicable if c["status"] == "Implemented"]
 
    # Categorise gaps by priority
    critical_gaps = [c for c in not_impl + partial
                     if PRIORITY_CONTROLS.get(c["id"]) == "Critical"]
    high_gaps     = [c for c in not_impl + partial
                     if PRIORITY_CONTROLS.get(c["id"]) == "High"]
    medium_gaps   = [c for c in not_impl + partial
                     if PRIORITY_CONTROLS.get(c["id"]) == "Medium"]
    low_gaps      = [c for c in not_impl + partial
                     if c["id"] not in PRIORITY_CONTROLS]
 
    total_gaps    = len(not_impl) + len(partial)
    progress_pct  = round((len(implemented) + len(partial) * 0.5) / len(applicable) * 100, 1)
 
    L = [
        "# ISMS Compliance Gap Report",
        f"## {COMPANY['name']} – ISO/IEC 27001:2022 Certification Readiness",
        "",
        "| Field | Detail |",
        "|---|---|",
        "| **Document ID** | OV-GAP-001 |",
        f"| **Version** | {VERSION} |",
        f"| **Date** | {TODAY} |",
        f"| **Target Certification** | {COMPANY['target_cert_date']} |",
        f"| **Owner** | {COMPANY['document_owner']} |",
        "| **Classification** | CONFIDENTIAL – INTERNAL |",
        "",
        "---", "",
        "## 1. Executive Summary",
        "",
        f"This gap report assesses Open Vantage's current ISO 27001:2022 compliance posture "
        f"ahead of the target certification date of **{COMPANY['target_cert_date']}**. "
        f"The assessment is based on the Statement of Applicability (OV-SOA-001) and covers "
        f"all {len(applicable)} applicable Annex A controls.",
        "",
        "### Current Compliance Posture",
        "",
        "| Status | Count | Percentage |",
        "|---|---|---|",
        f"| ✅ Implemented | {len(implemented)} | {round(len(implemented)/len(applicable)*100,1)}% |",
        f"| ⚠️ Partially Implemented | {len(partial)} | {round(len(partial)/len(applicable)*100,1)}% |",
        f"| ❌ Not Implemented | {len(not_impl)} | {round(len(not_impl)/len(applicable)*100,1)}% |",
        f"| **Total Applicable** | **{len(applicable)}** | **100%** |",
        "",
        f"**Overall Readiness Score: {progress_pct}%**",
        "",
        "> ⚠️ A minimum readiness score of approximately 85% is recommended before "
        "> scheduling the Stage 1 certification audit.",
        "",
        "---", "",
        "## 2. Gap Summary by Priority",
        "",
        "| Priority | Gap Count | Action Required |",
        "|---|---|---|",
        f"| 🔴 Critical | {len(critical_gaps)} | Must remediate before Stage 1 audit |",
        f"| 🟠 High | {len(high_gaps)} | Remediate before Stage 2 audit |",
        f"| 🟡 Medium | {len(medium_gaps)} | Remediate before certification |",
        f"| 🟢 Low | {len(low_gaps)} | Address within 90 days post-certification |",
        f"| **Total Gaps** | **{total_gaps}** | |",
        "",
        "---", "",
        "## 3. Critical Gaps – Immediate Action Required",
        "",
        "These gaps must be remediated before the Stage 1 audit can proceed.",
        "",
        "| Control | Name | Status | Recommended Action |",
        "|---|---|---|---|",
    ]
 
    for c in critical_gaps:
        status_emoji = "❌" if c["status"] == "Not Implemented" else "⚠️"
        action = ACTIONS.get(c["id"], "Review and implement control per ISO 27001:2022 guidance")
        L.append(f"| **{c['id']}** | {c['control'][:45]} | {status_emoji} {c['status']} | {action[:80]} |")
 
    L += [
        "", "---", "",
        "## 4. High Priority Gaps",
        "",
        "| Control | Name | Status | Recommended Action |",
        "|---|---|---|---|",
    ]
    for c in high_gaps:
        status_emoji = "❌" if c["status"] == "Not Implemented" else "⚠️"
        action = ACTIONS.get(c["id"], "Review and implement control per ISO 27001:2022 guidance")
        L.append(f"| **{c['id']}** | {c['control'][:45]} | {status_emoji} {c['status']} | {action[:80]} |")
 
    L += [
        "", "---", "",
        "## 5. Medium Priority Gaps",
        "",
        "| Control | Name | Status | Recommended Action |",
        "|---|---|---|---|",
    ]
    for c in medium_gaps:
        status_emoji = "❌" if c["status"] == "Not Implemented" else "⚠️"
        action = ACTIONS.get(c["id"], "Review and implement control per ISO 27001:2022 guidance")
        L.append(f"| **{c['id']}** | {c['control'][:45]} | {status_emoji} {c['status']} | {action[:80]} |")
 
    L += [
        "", "---", "",
        "## 6. Remediation Roadmap",
        "",
        "| Phase | Timeline | Actions |",
        "|---|---|---|",
        "| **Phase 1 – Foundation** | Month 1–2 | Information Security Policy, Asset Register, AUP, Access Control Policy, Data Classification |",
        "| **Phase 2 – Technical Controls** | Month 2–4 | MFA enforcement, EDR deployment, SIEM, vulnerability scanning, MDM enrolment |",
        "| **Phase 3 – Process & People** | Month 3–5 | Security awareness training, IR plan testing, supplier security contracts, remote working policy |",
        "| **Phase 4 – Audit Readiness** | Month 5–6 | Internal audit, management review, SoA finalisation, Stage 1 audit preparation |",
        "| **Certification** | Q4 2025 | Stage 1 and Stage 2 certification audits |",
        "",
        "---", "",
        "## 7. Regulatory Alignment",
        "",
        "| Regulation | Current Status | Priority Gaps |",
        "|---|---|---|",
        "| **POPIA (Act 4 of 2013)** | Partially compliant | Privacy policy, PAIA manual, breach notification (5.24), data deletion (8.10) |",
        "| **GDPR (Netherlands)** | Partially compliant | DPA agreements (5.20), data masking (8.11), breach notification (5.24) |",
        "| **UK GDPR** | Partially compliant | Same as GDPR — UK ICO notification procedures needed |",
        "",
        "---", "",
        f"*{COMPANY['name']} | {COMPANY['website']} | Gap Report {VERSION} | {TODAY}*",
        f"*Related: OV-SOA-001, OV-POL-001 through OV-POL-006*",
    ]
 
    path = os.path.join(OUTPUT_DIR, 'OV-GAP-001-Compliance-Gap-Report.md')
    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(L))
    print(f"  ✅ OV-GAP-001 Compliance Gap Report → {path}")
    return path
 
 
if __name__ == "__main__":
    generate_gap_report()
