"""
Open Vantage ISMS – Statement of Applicability (SoA) Generator
ISO 27001:2022 | All 93 Annex A Controls
Outputs: outputs/reports/OV-SOA-001-Statement-of-Applicability.md
         outputs/reports/OV-SOA-001-Statement-of-Applicability.csv
"""
 
import os, sys, csv
from datetime import date
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from data.ov_context import COMPANY, ANNEX_A_CONTROLS
 
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'outputs', 'reports')
os.makedirs(OUTPUT_DIR, exist_ok=True)
 
TODAY    = date.today().strftime("%d %B %Y")
VERSION  = "v1.0"
STATUS   = "DRAFT – Pending CISO Approval"
 
STATUS_EMOJI = {
    "Implemented":          "✅",
    "Partially Implemented":"⚠️",
    "Not Implemented":      "❌",
    "N/A":                  "➖",
}
 
 
def generate_soa_markdown():
    applicable   = [c for c in ANNEX_A_CONTROLS if c["applicable"]]
    not_applicable = [c for c in ANNEX_A_CONTROLS if not c["applicable"]]
    implemented  = [c for c in applicable if c["status"] == "Implemented"]
    partial      = [c for c in applicable if c["status"] == "Partially Implemented"]
    not_impl     = [c for c in applicable if c["status"] == "Not Implemented"]
 
    L = [
        "# Statement of Applicability (SoA)",
        f"## {COMPANY['name']} – ISO/IEC 27001:2022",
        "",
        "| Field | Detail |",
        "|---|---|",
        "| **Document ID** | OV-SOA-001 |",
        f"| **Version** | {VERSION} |",
        f"| **Status** | {STATUS} |",
        f"| **Date** | {TODAY} |",
        f"| **Owner** | {COMPANY['document_owner']} |",
        f"| **Classification** | CONFIDENTIAL – INTERNAL |",
        "",
        "---", "",
        "## 1. Introduction",
        "",
        "This Statement of Applicability (SoA) documents Open Vantage's decisions regarding "
        "the applicability of all 93 controls in ISO/IEC 27001:2022 Annex A. For each control, "
        "this document states whether the control is applicable, provides a justification, "
        "records the current implementation status, and identifies the evidence required for "
        "certification audit.",
        "",
        "This SoA is a mandatory deliverable for ISO 27001:2022 certification (Clause 6.1.3).",
        "",
        "---", "",
        "## 2. Summary",
        "",
        "| Metric | Count |",
        "|---|---|",
        f"| **Total Annex A Controls** | 93 |",
        f"| **Applicable** | {len(applicable)} |",
        f"| **Not Applicable** | {len(not_applicable)} |",
        f"| ✅ Implemented | {len(implemented)} |",
        f"| ⚠️ Partially Implemented | {len(partial)} |",
        f"| ❌ Not Implemented | {len(not_impl)} |",
        "",
        f"**Overall Implementation Progress:** "
        f"{round((len(implemented) + len(partial) * 0.5) / len(applicable) * 100, 1)}%",
        "",
        "---", "",
    ]
 
    # Controls by theme
    themes = ["Organisational", "People", "Physical", "Technological"]
    theme_prefix = {
        "Organisational": "5",
        "People": "6",
        "Physical": "7",
        "Technological": "8",
    }
 
    for theme in themes:
        theme_controls = [c for c in ANNEX_A_CONTROLS if c["theme"] == theme]
        theme_applicable = [c for c in theme_controls if c["applicable"]]
        L += [
            f"## 3.{themes.index(theme)+1} Theme {theme_prefix[theme]}: {theme} Controls",
            "",
            f"| Control | Name | Applicable | Status | Justification |",
            "|---|---|---|---|---|",
        ]
        for c in theme_controls:
            app = "✅ Yes" if c["applicable"] else "❌ No"
            emoji = STATUS_EMOJI.get(c["status"], "")
            L.append(
                f"| **{c['id']}** | {c['control']} | {app} | "
                f"{emoji} {c['status']} | {c['justification'][:80]}... |"
                if len(c['justification']) > 80 else
                f"| **{c['id']}** | {c['control']} | {app} | "
                f"{emoji} {c['status']} | {c['justification']} |"
            )
        L += ["", "---", ""]
 
    # Evidence required for applicable controls
    L += [
        "## 4. Evidence Required for Certification Audit",
        "",
        "The following evidence must be collected and available for the ISO 27001 "
        "certification audit for all applicable controls:",
        "",
        "| Control | Evidence Required | Status |",
        "|---|---|---|",
    ]
    for c in applicable:
        emoji = STATUS_EMOJI.get(c["status"], "")
        L.append(f"| **{c['id']}** – {c['control'][:40]} | {c['evidence']} | {emoji} {c['status']} |")
 
    L += [
        "", "---", "",
        "## 5. Not Applicable Controls",
        "",
        "The following controls have been determined to be not applicable to Open Vantage "
        "and are excluded from the scope of the ISMS with justification:",
        "",
        "| Control | Name | Justification |",
        "|---|---|---|",
    ]
    for c in not_applicable:
        L.append(f"| **{c['id']}** | {c['control']} | {c['justification']} |")
 
    L += [
        "", "---", "",
        "## 6. Certification Readiness",
        "",
        f"Based on current implementation status, Open Vantage has **{len(not_impl)} controls** "
        f"that are Not Implemented and **{len(partial)} controls** that are Partially Implemented. "
        f"A remediation plan has been developed to achieve full implementation by the target "
        f"certification date of **{COMPANY['target_cert_date']}**.",
        "",
        "Priority remediation areas:",
        "1. **Logging & Monitoring** (8.15, 8.16) — SIEM deployment required",
        "2. **Vulnerability Management** (8.8) — automated scanning not yet in place",
        "3. **Security Awareness Training** (6.3) — formal programme not yet established",
        "4. **Supplier Security** (5.19, 5.20) — vendor contracts require security annexures",
        "5. **Incident Response** (5.24, 5.25, 5.26) — IR plan drafted but not tested",
        "",
        "---", "",
        f"*{COMPANY['name']} | {COMPANY['website']} | SoA Version {VERSION} | {TODAY}*",
    ]
 
    path = os.path.join(OUTPUT_DIR, 'OV-SOA-001-Statement-of-Applicability.md')
    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(L))
    print(f"  ✅ OV-SOA-001 Statement of Applicability (MD) → {path}")
    return path
 
 
def generate_soa_csv():
    path = os.path.join(OUTPUT_DIR, 'OV-SOA-001-Statement-of-Applicability.csv')
    with open(path, 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow([f"OPEN VANTAGE – ISO 27001:2022 STATEMENT OF APPLICABILITY"])
        w.writerow(["Version", VERSION, "Date", TODAY, "Status", STATUS])
        w.writerow([])
        w.writerow(["Control ID", "Theme", "Control Name", "Applicable",
                    "Justification", "Implementation Status", "Evidence Required"])
        for c in ANNEX_A_CONTROLS:
            w.writerow([
                c["id"], c["theme"], c["control"],
                "Yes" if c["applicable"] else "No",
                c["justification"], c["status"], c["evidence"]
            ])
    print(f"  ✅ OV-SOA-001 Statement of Applicability (CSV) → {path}")
    return path
 
 
def generate_all():
    print("\n📋 Generating Statement of Applicability...")
    md_path  = generate_soa_markdown()
    csv_path = generate_soa_csv()
    return md_path, csv_path
 
 
if __name__ == "__main__":
    generate_all()