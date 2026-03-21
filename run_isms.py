"""
Open Vantage ISMS Documentation Suite
ISO 27001:2022 Certification Project | Run all outputs with one command
 
Usage:
    python run_isms.py
 
Outputs:
    outputs/policies/OV-POL-001-Information-Security-Policy.md
    outputs/policies/OV-POL-002-Acceptable-Use-Policy.md
    outputs/policies/OV-POL-003-Access-Control-Policy.md
    outputs/policies/OV-POL-004-Incident-Response-Policy.md
    outputs/policies/OV-POL-005-Remote-Working-Policy.md
    outputs/policies/OV-POL-006-Data-Classification-Policy.md
    outputs/reports/OV-ISMS-001-ISMS-Scope-Document.md
    outputs/reports/OV-SOA-001-Statement-of-Applicability.md
    outputs/reports/OV-SOA-001-Statement-of-Applicability.csv
    outputs/reports/OV-GAP-001-Compliance-Gap-Report.md
"""
 
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
 
print("=" * 65)
print("  OPEN VANTAGE – ISO 27001:2022 ISMS DOCUMENTATION SUITE")
print("  Certification Project | Target: Q4 2025")
print("  openvantage.co.za | Sandton, Johannesburg")
print("=" * 65)
print()
 
print("🏢 Loading company context...")
from data.ov_context import COMPANY, ANNEX_A_CONTROLS
applicable = [c for c in ANNEX_A_CONTROLS if c["applicable"]]
not_impl   = [c for c in applicable if c["status"] == "Not Implemented"]
partial    = [c for c in applicable if c["status"] == "Partially Implemented"]
implemented = [c for c in applicable if c["status"] == "Implemented"]
print(f"   Company: {COMPANY['name']}")
print(f"   Offices: {', '.join(COMPANY['offices'])}")
print(f"   Services: {len(COMPANY['services'])} service lines")
print(f"   93 Annex A controls | {len(applicable)} applicable | "
      f"{len(not_impl)} not implemented | {len(partial)} partial | {len(implemented)} done")
print()
 
print("📄 Generating ISMS Scope Document...")
from isms_generator.generate_scope import generate_scope_document
generate_scope_document()
print()
 
print("📋 Generating Policy Documents (6 policies)...")
from isms_generator.generate_policies import generate_all_policies
generate_all_policies()
print()
 
print("📊 Generating Statement of Applicability (93 controls)...")
from isms_generator.generate_soa import generate_all as generate_soa
generate_soa()
print()
 
print("🔍 Generating Compliance Gap Report...")
from isms_generator.generate_gap_report import generate_gap_report
generate_gap_report()
print()
 
print("=" * 65)
print("  ✅ ALL ISMS DOCUMENTS GENERATED")
print("=" * 65)
print()
print("  📁 outputs/policies/")
print("     OV-POL-001 Information Security Policy")
print("     OV-POL-002 Acceptable Use Policy")
print("     OV-POL-003 Access Control Policy")
print("     OV-POL-004 Incident Response Policy")
print("     OV-POL-005 Remote Working Policy")
print("     OV-POL-006 Data Classification Policy")
print()
print("  📁 outputs/reports/")
print("     OV-ISMS-001 ISMS Scope Document")
print("     OV-SOA-001  Statement of Applicability (MD + CSV)")
print("     OV-GAP-001  Compliance Gap Report")
print()
progress = round((len(implemented) + len(partial) * 0.5) / len(applicable) * 100, 1)
print(f"  📊 CERTIFICATION READINESS: {progress}%")
print(f"     ✅ Implemented:          {len(implemented)}/{len(applicable)} controls")
print(f"     ⚠️  Partially Implemented: {len(partial)}/{len(applicable)} controls")
print(f"     ❌ Not Implemented:       {len(not_impl)}/{len(applicable)} controls")
print()
print("  🎯 Target certification date: Q4 2025")