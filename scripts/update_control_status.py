#!/usr/bin/env python3
"""
Open Vantage ISMS – Control Status Updater
==========================================
Update one or more Annex A control statuses directly from the command line.
Changes are written to data/ov_context.py and the readiness score is
recalculated instantly.

Usage
-----
    # Show current status of a control
    python scripts/update_control_status.py --show 5.1

    # Mark a control as Implemented
    python scripts/update_control_status.py --control 5.1 --status implemented

    # Mark as Partially Implemented
    python scripts/update_control_status.py --control 8.5 --status partial

    # Mark as Not Implemented (rollback)
    python scripts/update_control_status.py --control 8.15 --status not_implemented

    # Bulk update from a CSV file (id,status per line)
    python scripts/update_control_status.py --bulk scripts/bulk_update_example.csv

    # Show full readiness summary
    python scripts/update_control_status.py --summary

    # List all controls with a specific status
    python scripts/update_control_status.py --list critical

    # List controls by priority
    python scripts/update_control_status.py --list high

    # After updating, regenerate all outputs
    python scripts/update_control_status.py --control 5.1 --status implemented --regenerate
"""

import sys
import os
import re
import argparse
import csv
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from data.ov_context import ANNEX_A_CONTROLS

CONTEXT_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'ov_context.py')

STATUS_MAP = {
    'implemented':     'Implemented',
    'impl':            'Implemented',
    'done':            'Implemented',
    'partial':         'Partially Implemented',
    'partially':       'Partially Implemented',
    'not_implemented': 'Not Implemented',
    'ni':              'Not Implemented',
    'not':             'Not Implemented',
}

STATUS_LABELS = {
    'Implemented':          '✅ Implemented',
    'Partially Implemented':'⚠️  Partially Implemented',
    'Not Implemented':      '❌ Not Implemented',
}

PRIORITY_MAP = {
    '5.1':'critical','5.19':'critical','5.20':'critical','5.24':'critical',
    '5.25':'critical','5.26':'critical','6.3':'critical','8.5':'critical',
    '8.8':'critical','8.15':'critical','8.16':'critical',
    '5.9':'high','5.10':'high','5.12':'high','5.17':'high','5.18':'high',
    '6.7':'high','7.9':'high','8.1':'high','8.2':'high','8.11':'high',
    '8.12':'high','8.22':'high','8.25':'high','8.30':'high',
    '5.3':'medium','5.7':'medium','5.29':'medium','5.30':'medium',
    '6.5':'medium','6.8':'medium','7.7':'medium','8.6':'medium',
    '8.10':'medium','8.18':'medium','8.19':'medium','8.20':'medium',
    '8.23':'medium','8.26':'medium',
}

PRIORITY_COLORS = {
    'critical': '\033[91m',   # red
    'high':     '\033[93m',   # yellow
    'medium':   '\033[94m',   # blue
    'low':      '\033[92m',   # green
}
RESET  = '\033[0m'
BOLD   = '\033[1m'
GREEN  = '\033[92m'
RED    = '\033[91m'
YELLOW = '\033[93m'
BLUE   = '\033[94m'
GREY   = '\033[90m'


def calc_score(controls):
    applicable = [c for c in controls if c['applicable']]
    if not applicable:
        return 0.0
    impl    = sum(1 for c in applicable if c['status'] == 'Implemented')
    partial = sum(1 for c in applicable if c['status'] == 'Partially Implemented')
    return round((impl + partial * 0.5) / len(applicable) * 100, 1)


def find_control(control_id):
    for c in ANNEX_A_CONTROLS:
        if c['id'] == control_id:
            return c
    return None


def print_control(c):
    p = PRIORITY_MAP.get(c['id'], 'low')
    color = PRIORITY_COLORS.get(p, '')
    print(f"\n  {BOLD}Control {c['id']}{RESET} — {c.get('control', c.get('name', ''))}")
    print(f"  Theme    : {c.get('theme', 'Annex A')}")
    print(f"  Priority : {color}{p.upper()}{RESET}")
    print(f"  Status   : {STATUS_LABELS.get(c['status'], c['status'])}")
    print(f"  Applicable: {'Yes' if c['applicable'] else 'No (excluded)'}\n")


def update_status_in_file(control_id, new_status):
    """
    Rewrites the status field for a given control_id in ov_context.py.
    Matches lines of the form:  "status": "...",
    within the control's dict block.
    """
    with open(CONTEXT_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    # Build a pattern that matches the control block and its status line
    # We look for the id field followed (eventually) by the status field within the same dict
    pattern = (
        r'(\{[^{}]*?"id"\s*:\s*"' + re.escape(control_id) + r'"'
        r'[^{}]*?"status"\s*:\s*")'
        r'[^"]*'
        r'(")'
    )
    replacement = r'\g<1>' + new_status + r'\g<2>'
    new_content, count = re.subn(pattern, replacement, content, flags=re.DOTALL)

    if count == 0:
        # Fallback: try alternate ordering (status before id)
        pattern2 = (
            r'(\{[^{}]*?"status"\s*:\s*")'
            r'[^"]*'
            r'("[^{}]*?"id"\s*:\s*"' + re.escape(control_id) + r'")'
        )
        replacement2 = r'\g<1>' + new_status + r'\g<3>'
        new_content, count = re.subn(pattern2, replacement2, content, flags=re.DOTALL)

    if count == 0:
        return False

    with open(CONTEXT_FILE, 'w', encoding='utf-8') as f:
        f.write(new_content)
    return True


def print_summary(controls):
    applicable  = [c for c in controls if c['applicable']]
    impl        = [c for c in applicable if c['status'] == 'Implemented']
    partial     = [c for c in applicable if c['status'] == 'Partially Implemented']
    ni          = [c for c in applicable if c['status'] == 'Not Implemented']
    not_appl    = [c for c in controls if not c['applicable']]
    score       = calc_score(controls)
    score_color = GREEN if score >= 85 else (YELLOW if score >= 50 else RED)

    print(f"\n{'='*60}")
    print(f"  {BOLD}OPEN VANTAGE – ISO 27001:2022 READINESS SUMMARY{RESET}")
    print(f"{'='*60}")
    print(f"  Total Annex A controls : 93")
    print(f"  Applicable             : {len(applicable)}")
    print(f"  Not Applicable         : {len(not_appl)}")
    print(f"")
    print(f"  {GREEN}✅ Implemented          : {len(impl):3d} / {len(applicable)}{RESET}")
    print(f"  {YELLOW}⚠️  Partially Implemented: {len(partial):3d} / {len(applicable)}{RESET}")
    print(f"  {RED}❌ Not Implemented       : {len(ni):3d} / {len(applicable)}{RESET}")
    print(f"")
    print(f"  {BOLD}Readiness Score : {score_color}{score}%{RESET}")
    print(f"  Stage 1 target  : 85.0%  {'  ✅ ELIGIBLE' if score >= 85 else f'  ⬅  need +{round(85-score,1)}%'}")
    print(f"{'='*60}")

    # Priority breakdown
    crit_open = [c for c in ni + partial if PRIORITY_MAP.get(c['id'],'low') == 'critical']
    high_open = [c for c in ni + partial if PRIORITY_MAP.get(c['id'],'low') == 'high']
    med_open  = [c for c in ni + partial if PRIORITY_MAP.get(c['id'],'low') == 'medium']
    low_open  = [c for c in ni + partial if PRIORITY_MAP.get(c['id'],'low') == 'low']

    print(f"\n  {BOLD}Open gaps by priority:{RESET}")
    print(f"  {RED}🔴 Critical : {len(crit_open)}{RESET}")
    print(f"  {YELLOW}🟠 High     : {len(high_open)}{RESET}")
    print(f"  {BLUE}🟡 Medium   : {len(med_open)}{RESET}")
    print(f"  {GREEN}🟢 Low      : {len(low_open)}{RESET}")
    print()

    if crit_open:
        print(f"  {BOLD}{RED}Critical gaps remaining:{RESET}")
        for c in crit_open:
            print(f"    {GREY}{c['id']:<6}{RESET} {c.get('control', c.get('name', ''))}  [{STATUS_LABELS.get(c['status'], c['status'])}]")
    print()


def list_controls(controls, filter_by):
    """List controls matching a priority or status filter."""
    filter_by = filter_by.lower()

    # Priority filter
    if filter_by in ('critical', 'high', 'medium', 'low'):
        matches = [c for c in controls if c['applicable'] and PRIORITY_MAP.get(c['id'],'low') == filter_by]
        label = filter_by.upper()
    elif filter_by in ('implemented', 'impl', 'done'):
        matches = [c for c in controls if c['applicable'] and c['status'] == 'Implemented']
        label = 'IMPLEMENTED'
    elif filter_by in ('partial', 'partially'):
        matches = [c for c in controls if c['applicable'] and c['status'] == 'Partially Implemented']
        label = 'PARTIALLY IMPLEMENTED'
    elif filter_by in ('ni', 'not_implemented', 'gaps'):
        matches = [c for c in controls if c['applicable'] and c['status'] == 'Not Implemented']
        label = 'NOT IMPLEMENTED'
    else:
        print(f"{RED}Unknown filter: '{filter_by}'{RESET}")
        print("Valid filters: critical, high, medium, low, implemented, partial, ni")
        return

    print(f"\n  {BOLD}{label} controls ({len(matches)}):{RESET}")
    print(f"  {'ID':<8} {'Name':<50} {'Status'}")
    print(f"  {'-'*8} {'-'*50} {'-'*25}")
    for c in matches:
        p = PRIORITY_MAP.get(c['id'], 'low')
        pc = PRIORITY_COLORS.get(p, '')
        status_icon = '✅' if c['status']=='Implemented' else ('⚠️ ' if c['status']=='Partially Implemented' else '❌')
        print(f"  {pc}{c['id']:<8}{RESET} {c.get('control', c.get('name', '')):<50} {status_icon} {c['status']}")
    print()


def bulk_update(csv_path, controls):
    if not os.path.exists(csv_path):
        print(f"{RED}CSV file not found: {csv_path}{RESET}")
        return

    updated = []
    errors  = []

    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row_num, row in enumerate(reader, 1):
            if not row or row[0].startswith('#'):
                continue
            if len(row) < 2:
                errors.append(f"  Row {row_num}: malformed — expected 'id,status'")
                continue
            ctrl_id  = row[0].strip()
            status_raw = row[1].strip().lower()
            if status_raw not in STATUS_MAP:
                errors.append(f"  Row {row_num}: unknown status '{status_raw}' for {ctrl_id}")
                continue
            new_status = STATUS_MAP[status_raw]
            ctrl = find_control(ctrl_id)
            if not ctrl:
                errors.append(f"  Row {row_num}: control '{ctrl_id}' not found")
                continue
            old_status = ctrl['status']
            if old_status == new_status:
                continue
            success = update_status_in_file(ctrl_id, new_status)
            if success:
                ctrl['status'] = new_status
                updated.append((ctrl_id, ctrl.get('control', ctrl.get('name','')), old_status, new_status))
            else:
                errors.append(f"  {ctrl_id}: file update failed")

    if updated:
        print(f"\n  {GREEN}{BOLD}Bulk update — {len(updated)} controls updated:{RESET}")
        for ctrl_id, name, old, new in updated:
            print(f"  {GREY}{ctrl_id:<8}{RESET} {name[:48]:<48}  {old} → {BOLD}{new}{RESET}")

    if errors:
        print(f"\n  {RED}Errors ({len(errors)}):{RESET}")
        for e in errors:
            print(e)

    if not updated and not errors:
        print(f"\n  {YELLOW}No changes — all controls already at target status.{RESET}")

    return updated


def main():
    parser = argparse.ArgumentParser(
        description='Open Vantage ISMS — Control Status Updater',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python scripts/update_control_status.py --summary
  python scripts/update_control_status.py --show 8.5
  python scripts/update_control_status.py --control 5.1 --status implemented
  python scripts/update_control_status.py --control 8.15 --status partial
  python scripts/update_control_status.py --list critical
  python scripts/update_control_status.py --bulk scripts/bulk_update_example.csv
  python scripts/update_control_status.py --control 5.1 --status implemented --regenerate
        """
    )
    parser.add_argument('--control',    metavar='ID',     help='Control ID to update (e.g. 5.1, 8.15)')
    parser.add_argument('--status',     metavar='STATUS', help='New status: implemented | partial | not_implemented')
    parser.add_argument('--show',       metavar='ID',     help='Show current status of a control')
    parser.add_argument('--summary',    action='store_true', help='Print full readiness summary')
    parser.add_argument('--list',       metavar='FILTER', help='List controls: critical|high|medium|low|implemented|partial|ni')
    parser.add_argument('--bulk',       metavar='CSV',    help='Bulk update from CSV file (id,status per line)')
    parser.add_argument('--regenerate', action='store_true', help='Regenerate all ISMS outputs after update')
    args = parser.parse_args()

    if not any(vars(args).values()):
        parser.print_help()
        return

    if args.summary:
        print_summary(ANNEX_A_CONTROLS)
        return

    if args.show:
        ctrl = find_control(args.show)
        if ctrl:
            print_control(ctrl)
        else:
            print(f"{RED}Control '{args.show}' not found.{RESET}")
        return

    if args.list:
        list_controls(ANNEX_A_CONTROLS, args.list)
        return

    if args.bulk:
        updated = bulk_update(args.bulk, ANNEX_A_CONTROLS)
        if updated:
            print_summary(ANNEX_A_CONTROLS)
            if args.regenerate:
                _regenerate()
        return

    if args.control and args.status:
        status_raw = args.status.lower()
        if status_raw not in STATUS_MAP:
            print(f"{RED}Unknown status '{args.status}'.{RESET}")
            print(f"Valid values: {', '.join(set(STATUS_MAP.keys()))}")
            return

        ctrl = find_control(args.control)
        if not ctrl:
            print(f"{RED}Control '{args.control}' not found.{RESET}")
            return

        new_status = STATUS_MAP[status_raw]
        old_status = ctrl['status']

        if old_status == new_status:
            print(f"\n  {YELLOW}No change — {args.control} is already '{new_status}'.{RESET}\n")
            return

        before_score = calc_score(ANNEX_A_CONTROLS)
        success = update_status_in_file(args.control, new_status)

        if success:
            ctrl['status'] = new_status
            after_score = calc_score(ANNEX_A_CONTROLS)
            delta = round(after_score - before_score, 1)
            delta_str = (f"{GREEN}+{delta}%{RESET}" if delta > 0 else
                         (f"{RED}{delta}%{RESET}" if delta < 0 else f"{GREY}no change{RESET}"))

            print(f"\n  {GREEN}{BOLD}✅ Updated:{RESET}  {args.control} — {ctrl.get('control', ctrl.get('name',''))}")
            print(f"  Old status : {STATUS_LABELS.get(old_status, old_status)}")
            print(f"  New status : {STATUS_LABELS.get(new_status, new_status)}")
            print(f"  Score      : {before_score}%  →  {after_score}%  ({delta_str})")
            print(f"  Timestamp  : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

            if args.regenerate:
                _regenerate()
        else:
            print(f"\n  {RED}❌ Failed to update {args.control} in ov_context.py.{RESET}")
            print(f"  Make sure the control ID and file format are correct.\n")
        return

    if args.control and not args.status:
        ctrl = find_control(args.control)
        if ctrl:
            print_control(ctrl)
        else:
            print(f"{RED}Control '{args.control}' not found.{RESET}")
        return

    parser.print_help()


def _regenerate():
    print(f"\n  {BLUE}Regenerating ISMS documents...{RESET}\n")
    os.chdir(os.path.dirname(os.path.dirname(__file__)))
    os.system('python run_isms.py')


if __name__ == '__main__':
    main()
