#!/bin/bash

function test() {
    printf "\n============================================="

    printf "\n     #####     demo_stdlib.pyx     #####    \n"
    printf "\n           demo_intro_stdlib()       \n"
    python3 -c "from demo_stdlib import demo_intro_stdlib; \
        demo_intro_stdlib()"

    printf "\n              demo_math()          \n"
    python3 -c "from demo_stdlib import demo_math; \
        demo_math()"

    printf "\n============================================="

    printf "\n    #####     demo_cpy_api.pyx    #####    \n"
    printf "\n            demo_version()     \n"
    python3 -c "from demo_cpy_api import demo_version; \
        demo_version()"

    printf "\n               demo_number()       \n"
    python3 -c "from demo_cpy_api import demo_number; \
        demo_number()"

    printf "\n============================================="

    printf "\n    #####     demo_libfromc.pyx    #####    \n"
    printf "\n            demo_suma_enteros()    \n"
    python3 -c "from demo_libfromc import demo_suma_enteros; \
        print(demo_suma_enteros(11, 22))"

    printf "\n=============================================\n"
}

function main() {
    python3 setup.py build_ext -i  # Compila
    test  # Ejecuta
    # Limpia
    rm demo_stdlib.c demo_cpy_api.c *.so demo_libfromc.c
    rm -Rf build/
}

if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
  main
fi

