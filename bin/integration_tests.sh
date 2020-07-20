#!/usr/bin/env bash
[[ "$TRACE" ]] && set -x
set -eu -o pipefail

cd /app/serverless
python -m pytest ../tests/integration/
