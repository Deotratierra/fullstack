#!/bin/sh

function fib() {
    a=1
    b=0
    let n="$1"
    for i in $(seq 1 $n); do
        tmp=$a
        a=$(($a + $b))
        b=$tmp
    done
    ret=$a
}


if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    fib $1
    printf "$ret\n"
fi