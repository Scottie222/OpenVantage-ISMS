"""
Open Vantage ISMS – Scope Document Generator
ISO 27001:2022 Clause 4.3
"""
 
import os, sys
from datetime import date
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from data.ov_context import COMPANY, ISMS_SCOPE
 
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'outputs', 'reports')
os.makedirs(OUTPUT_DIR, exist_ok=True)
 
TODAY = date.today().strftime("%d %B %Y")
 
 
def generate_scope_document():
    L = [
        "# ISMS Scope Document",
        f"## {COMPANY['name']} – ISO/IEC 27001:2022",
        "",
        "| Field | Detail |",
        "|---|---|",
        "| **Document ID** | OV-ISMS-001 |",
        "| **Version** | v1.0 |",
        f"| **Date** | {TODAY} |",
        f"| **Owner** | {COMPANY['document_owner']} |",
        "| **ISO Clause** | 4.3 – Determining the scope of the ISMS |",
        "| **Classification** | CONFIDENTIAL – INTERNAL |",
        "",
        "---", "",
        "## 1. Scope Statement",
        "",
        ISMS_SCOPE["scope_statement"],
        "",
        "---", "",
        "## 2. In Scope",
        "",
    ]
    for item in ISMS_SCOPE["in_scope"]:
        L.append(f"- {item}")
    L += [
        "",
        "---", "",
        "## 3. Out of Scope",
        "",
    ]
    for item in ISMS_SCOPE["out_of_scope"]:
        L.append(f"- {item}")
    L += [
        "",
        "---", "",
        "## 4. Key Information Assets",
        "",
    ]
    for item in ISMS_SCOPE["key_assets"]:
        L.append(f"- {item}")
    L += [
        "",
        "---", "",
        "## 5. Interested Parties",
        "",
        "| Interested Party | Requirement / Expectation |",
        "|---|---|",
    ]
    for party in ISMS_SCOPE["interested_parties"]:
        parts = party.split(" — ")
        if len(parts) == 2:
            L.append(f"| {parts[0]} | {parts[1]} |")
        else:
            L.append(f"| {party} | See regulatory requirements |")
    L += [
        "",
        "---", "",
        "## 6. Regulatory Context",
        "",
    ]
    for reg in COMPANY["regulations"]:
        L.append(f"- {reg}")
    L += [
        "",
        "---", "",
        f"*{COMPANY['name']} | {COMPANY['website']} | ISMS Scope v1.0 | {TODAY}*",
    ]
 
    path = os.path.join(OUTPUT_DIR, 'OV-ISMS-001-ISMS-Scope-Document.md')
    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(L))
    print(f"  ✅ OV-ISMS-001 ISMS Scope Document → {path}")
    return path
 
 
if __name__ == "__main__":
    generate_scope_document()
 