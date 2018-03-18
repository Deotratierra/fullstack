#!/bin/sh

source ../performance.sh

VERBOSE=0
DEBUG=1
ITER=15
VALUES=("clave" "num")

function main() {
    title "Extract JSON value from dict string"
    perf_suite "ej" "${VALUES[*]}"
}

if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main
fi
