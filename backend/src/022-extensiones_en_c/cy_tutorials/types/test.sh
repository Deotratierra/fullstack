#!/bin/sh

function main() {
  # Construcción
  make

  # Tests
  python3 -c "from timeit import timeit; \
    t = timeit('funcion_inferida(10)', setup='from inferencia import funcion_inferida'); \
    print('Función con tipos inferidos: %f' % t); \
    t = timeit('funcion_no_inferida(10)', setup='from inferencia import funcion_no_inferida'); \
    print('Función sin tipos inferidos: %f' %t);"

  # Limpieza
  make clean

}

if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
  main
fi
