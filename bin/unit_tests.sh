#!/usr/bin/env bash
[[ "$TRACE" ]] && set -x
set -eu -o pipefail

TEST_RESULTS="/tmp/test_results"

# This value is percent of 100
CODE_COVERAGE_MINIMUM=25

pwd

python -m pytest -c ../setup.cfg

# If the test above fails, then we don't need to check coverage
# we can just bail here
if [ "$?" -ne 0 ]; then
    python -m pytest -vv
    exit $?
fi

mkdir -p ${TEST_RESULTS}/pytest/ || true

python -m pytest \
       -c ../setup.cfg \
       --cov-config=.coveragerc \
       --cov=. \
       --cov-fail-under=$CODE_COVERAGE_MINIMUM \
       --junitxml=${TEST_RESULTS}/pytest/results.xml
