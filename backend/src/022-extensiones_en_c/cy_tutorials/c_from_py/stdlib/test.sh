#!/bin/bash

function test() {
    # ==================================================

    printf "\n         demo_stdlib.pyx        \n"
    printf "\n#####     demo_intro_stdlib()     #####\n"
    python3 -c "from demo_stdlib import demo_intro_stdlib;demo_intro_stdlib()"

    printf "\n#####     demo_mathdemo_math()     #####\n"
    python3 -c "from demo_stdlib import demo_math;demo_math()"

    # ===================================================

    printf "\n         demo_cpy_api.pyx        \n"
    printf "\n#####     demo_version()     #####\n"
    python3 -c "from demo_cpy_api import demo_version;demo_version()"

    # ===================================================
}

function main() {
    # Compila
    python3 setup.py build_ext --inplace
    test
    rm demo_stdlib.c demo_cpy_api.c
    rm -Rf build/
}

if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
  main
fi

