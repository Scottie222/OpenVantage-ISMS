#!/usr/bin/env bash
# ============================================================
#  Open Vantage ISMS – Update Status & Regenerate Documents
#
#  Marks a control as implemented/partial/not_implemented and
#  immediately regenerates all 10 ISMS output documents.
#
#  Usage:
#    chmod +x scripts/run_with_status.sh
#
#    # Mark 5.1 as implemented and regenerate
#    ./scripts/run_with_status.sh 5.1 implemented
#
#    # Mark 8.15 as partial and regenerate
#    ./scripts/run_with_status.sh 8.15 partial
#
#    # Show readiness summary only
#    ./scripts/run_with_status.sh --summary
# ============================================================

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

cd "$PROJECT_DIR"

if [ "$1" = "--summary" ]; then
  python scripts/update_control_status.py --summary
  exit 0
fi

if [ -z "$1" ] || [ -z "$2" ]; then
  echo ""
  echo "  Usage:"
  echo "    ./scripts/run_with_status.sh <control_id> <status>"
  echo ""
  echo "  Status values:  implemented | partial | not_implemented"
  echo ""
  echo "  Examples:"
  echo "    ./scripts/run_with_status.sh 5.1 implemented"
  echo "    ./scripts/run_with_status.sh 8.5 partial"
  echo "    ./scripts/run_with_status.sh --summary"
  echo ""
  exit 1
fi

CONTROL_ID="$1"
STATUS="$2"

echo ""
echo "============================================================"
echo "  Updating: $CONTROL_ID → $STATUS"
echo "============================================================"
echo ""

python scripts/update_control_status.py --control "$CONTROL_ID" --status "$STATUS"

echo ""
echo "  Regenerating ISMS documents..."
echo ""

python run_isms.py

echo ""
echo "  ✅  Done. Open outputs/ to view updated documents."
echo "  ✅  Open dashboard/isms_simulator.html to view the live dashboard."
echo ""
