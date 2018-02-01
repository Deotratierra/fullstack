#!/bin/sh

function main() {
  # Construcción
  make

  # Tests
  printf "\n======   Comparación de rendimiento de funciones   ======\n"
  python3 -c "from timeit import timeit; \
    t = timeit('py_interpreted_factorial(900)', setup='from funciones_py import py_interpreted_factorial', number=1); \
    print('Función Python interpretada: %f' % t); \
     t = timeit('py_compiled_factorial_not_typed(900)', setup='from funciones_cy import py_compiled_factorial_not_typed', number=1); \
    print('Función Python compilada sin tipado: %f' %t); \
     t = timeit('py_compiled_factorial_typed(900)', setup='from funciones_cy import py_compiled_factorial_typed', number=1); \
    print('Función Python compilada con tipado (con resursion absurda): %f' %t); \
    t = timeit('envoltura_c_factorial(900)', setup='from funciones_cy import envoltura_c_factorial', number=1); \
    print('Función C envuelta manualmente: %f' %t); \
    t = timeit('c_py_factorial(900)', setup='from funciones_cy import c_py_factorial', number=1); \
    print('Función C encuelta automáticamente: %f' %t);"
  printf "=========================================================\n\n"

  # Limpieza
  make clean

}

if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
  main
fi
