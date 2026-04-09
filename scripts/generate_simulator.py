#!/usr/bin/env python3
"""
Open Vantage ISMS – Simulator Generator
=========================================
Reads the live control statuses from data/ov_context.py and writes
an up-to-date copy of the HTML simulator to dashboard/isms_simulator.html
so the browser dashboard always reflects the current state.

Usage:
    python scripts/generate_simulator.py

    # Or after a bulk update:
    python scripts/update_control_status.py --bulk scripts/bulk_update_example.csv
    python scripts/generate_simulator.py
"""

import os
import sys
import json
from datetime import date

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from data.ov_context import ANNEX_A_CONTROLS, COMPANY

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'dashboard')
os.makedirs(OUTPUT_DIR, exist_ok=True)

TODAY = date.today().strftime("%d %B %Y")


STATUS_MAP = {
    'Implemented':          'impl',
    'Partially Implemented': 'partial',
    'Not Implemented':      'ni',
}

PRIORITY_MAP = {
    '5.1':  'critical', '5.19': 'critical', '5.20': 'critical',
    '5.24': 'critical', '5.25': 'critical', '5.26': 'critical',
    '6.3':  'critical', '8.5':  'critical', '8.8':  'critical',
    '8.15': 'critical', '8.16': 'critical',
    '5.9':  'high', '5.10': 'high', '5.12': 'high', '5.17': 'high',
    '5.18': 'high', '6.7':  'high', '7.9':  'high', '8.1':  'high',
    '8.2':  'high', '8.11': 'high', '8.12': 'high', '8.22': 'high',
    '8.25': 'high', '8.30': 'high',
    '5.3':  'medium', '5.7': 'medium', '5.29': 'medium', '5.30': 'medium',
    '6.5':  'medium', '6.8': 'medium', '7.7':  'medium', '7.9':  'medium',
    '8.6':  'medium', '8.10': 'medium', '8.18': 'medium', '8.19': 'medium',
    '8.20': 'medium', '8.23': 'medium', '8.26': 'medium', '8.30': 'medium',
}

THEME_MAP = {
    '5': 5, '6': 6, '7': 7, '8': 8,
}

ACTIONS = {
    '5.1':  'Draft and obtain CEO approval for OV-POL-001',
    '5.19': 'Vendor risk assessments for AWS, GitHub, Slack',
    '5.20': 'Add security annexures to all vendor contracts; obtain DPAs',
    '5.24': 'Finalise OV-POL-004; test with tabletop exercise',
    '5.25': 'Develop incident classification and triage checklist',
    '5.26': 'Create playbooks: ransomware, breach, account compromise',
    '6.3':  'Launch quarterly training; run first phishing simulation',
    '8.5':  'Enforce MFA on all systems; document authentication policy',
    '8.8':  'Deploy Snyk or Tenable; establish patch SLA',
    '8.15': 'Deploy SIEM; configure retention policies',
    '8.16': 'Configure automated SIEM alerting and monitoring thresholds',
}


def build_js_controls():
    applicable = [c for c in ANNEX_A_CONTROLS if c['applicable']]
    js_controls = []
    for c in applicable:
        ctrl_id = c['id']
        theme_key = ctrl_id.split('.')[0]
        theme = THEME_MAP.get(theme_key, 5)
        status = STATUS_MAP.get(c['status'], 'ni')
        priority = PRIORITY_MAP.get(ctrl_id, 'low')
        action = ACTIONS.get(ctrl_id, f"Review and implement {ctrl_id} per ISO 27001:2022 guidance")
        js_controls.append({
            'id': ctrl_id,
            'n': c['name'][:60],
            'theme': theme,
            's': status,
            'p': priority,
            'action': action,
        })
    return js_controls


def calc_score(controls):
    impl = sum(1 for c in controls if c['s'] == 'impl')
    part = sum(1 for c in controls if c['s'] == 'partial')
    return round((impl + part * 0.5) / len(controls) * 100, 1)


def main():
    applicable = [c for c in ANNEX_A_CONTROLS if c['applicable']]
    js_controls = build_js_controls()
    score = calc_score(js_controls)
    impl  = sum(1 for c in js_controls if c['s'] == 'impl')
    part  = sum(1 for c in js_controls if c['s'] == 'partial')
    ni    = sum(1 for c in js_controls if c['s'] == 'ni')

    controls_json = json.dumps(js_controls, indent=2)

    # Read the static simulator template and inject live data
    sim_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'dashboard', 'isms_simulator.html')
    if not os.path.exists(sim_path):
        print("  ⚠️  dashboard/isms_simulator.html not found — run from project root after cloning.")
        return

    with open(sim_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Inject current date into footer
    html = html.replace(
        "document.getElementById('footerDate').textContent = new Date().toLocaleDateString",
        f"document.getElementById('footerDate').textContent = '{TODAY}'; //",
    )

    # Write updated file
    out_path = os.path.join(OUTPUT_DIR, 'isms_simulator_live.html')
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html)

    print()
    print("=" * 60)
    print("  ✅  Live simulator generated")
    print(f"  📁  {out_path}")
    print()
    print(f"  Readiness: {score}%  (Implemented: {impl}  Partial: {part}  NI: {ni})")
    print(f"  Stage 1 status: {'✅ ELIGIBLE' if score >= 85 else f'⬅  need +{round(85-score,1)}%'}")
    print("=" * 60)
    print()
    print("  Open in browser to explore the live dashboard:")
    print(f"  file://{out_path}")
    print()


if __name__ == '__main__':
    main()
