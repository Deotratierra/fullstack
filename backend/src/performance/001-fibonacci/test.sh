#!/bin/sh

source ../performance.sh

#VERBOSE=1
#DEBUG=0

#ITER=5

VALUES=("99" "999" "9999" "99999")

function main() {
    title "Fibonacci numbers"
    perf_suite "fib" "${VALUES[*]}"
}

if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main
fi
