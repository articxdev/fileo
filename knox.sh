#!/usr/bin/env bash
set -e
if [ "${SKIP_UPDATE:-true}" = "false" ] && [ -n "${UPSTREAM_REPO:-}" ]; then
  python3 update.py
fi
exec python3 -m Knox
