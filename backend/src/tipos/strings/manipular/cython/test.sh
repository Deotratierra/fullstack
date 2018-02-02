#!/bin/sh


function test_cadena_c_desde_py()
{
  python3 -c "from str import cadena_c; \
    s = cadena_c(); \
    print(s, type(s));"
}

function test_cadena_py_desde_c()
{
  python3 -c "from str import cadena_py_desde_c; \
    cadena_py_desde_c();"
}



function main()
{
  make
  printf "\n# ==========   Testeando las cadenas de C desde Python   ========== #\n"

  test_cadena_c_desde_py
  test_cadena_py_desde_c



  printf "\n# ================================================================== #\n"
  make clean
}


if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
  main
fi
