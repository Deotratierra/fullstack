#!/bin/sh

source ../performance.sh

VERBOSE=1
DEBUG=1
ITER=5
VALUES=("25" "50" "75" "100" "999" "9999" "99999")

function main() {
    title "Process array"
    perf_suite "rs" "${VALUES[*]}"
}

if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main
fi
