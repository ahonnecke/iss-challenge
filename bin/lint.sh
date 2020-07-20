#!/usr/bin/env bash
[[ "$TRACE" ]] && set -x
set -u -o pipefail

ARTIFACTS="/tmp/artifacts"

#Work in docker *or* in circleCI
cd ~/repo/serverless/ || cd /app/serverless/
pipenv run pre-commit run --all-files
