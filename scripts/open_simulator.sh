#!/usr/bin/env bash
# ============================================================
#  Open Vantage ISMS – Simulator Launcher
#  Opens the interactive HTML audit simulator in your browser.
#
#  Usage:
#    chmod +x scripts/open_simulator.sh
#    ./scripts/open_simulator.sh
# ============================================================

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
SIMULATOR="$PROJECT_DIR/dashboard/isms_simulator.html"

if [ ! -f "$SIMULATOR" ]; then
  echo "❌  Simulator not found at: $SIMULATOR"
  echo "   Run: git pull  (to ensure dashboard/ is present)"
  exit 1
fi

echo "============================================================"
echo "  OPEN VANTAGE – ISMS AUDIT SIMULATOR"
echo "  ISO 27001:2022 | Interactive Readiness Dashboard"
echo "============================================================"
echo ""
echo "  Opening: $SIMULATOR"
echo ""

# Detect OS and open accordingly
case "$OSTYPE" in
  darwin*)   open "$SIMULATOR" ;;
  linux*)
    if command -v xdg-open &>/dev/null; then
      xdg-open "$SIMULATOR"
    elif command -v gnome-open &>/dev/null; then
      gnome-open "$SIMULATOR"
    else
      echo "  Cannot auto-open. Please open manually:"
      echo "  file://$SIMULATOR"
    fi
    ;;
  msys*|cygwin*|win32*)
    start "$SIMULATOR" ;;
  *)
    echo "  Unknown OS. Please open manually:"
    echo "  file://$SIMULATOR"
    ;;
esac

echo "  ✅  Simulator launched"
echo ""
echo "  Tip: After updating control statuses, run:"
echo "  python scripts/update_control_status.py --summary"
echo ""
