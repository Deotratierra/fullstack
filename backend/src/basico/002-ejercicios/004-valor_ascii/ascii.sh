#!/bin/bash

chr() {
  [ "$1" -lt 256 ] || return 1
  printf "\\$(printf '%03o' "$1")"
}

ord() {
  LC_CTYPE=C printf '%d' "'$1"
}

if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    ord f
    echo 
    chr 97
fi

# Fuente:
# http://mywiki.wooledge.org/BashFAQ/071
