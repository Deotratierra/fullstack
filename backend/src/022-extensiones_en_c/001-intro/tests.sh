#!bin/bash

# Declaramos un array asociativo (hash o diccionario)
# con todas las carpetas y modulos...
declare -A IMPLEMENTACIONES_PY=( ["cython"]="lib_cy" ["manual"]="lib_c" ["pure_py"]="lib_py" ["ctypes"]="lib_ctypes")
# y otro para guardar los resultados de rendimiento
declare -A RESULTADOS

compilar() {
  if [ $impl = "ctypes" ];
  then  # Compilación de la implementación con ctypes
    gcc -Wall -O3 -shared lib_c.c -o lib_c.so
    export LD_LIBRARY_PATH=$PWD
  else  # Compilaciones cython y con la API de C/Python
    python3 setup.py -q build_ext --inplace
  fi
}

testear() {
  # Medir el rendimiento de cada implementación
  CODE="import timeit;from decimal import Decimal; \
            print(round(Decimal(timeit.timeit('${IMPLEMENTACIONES_PY[$impl]}.summa(100)', \
            setup='import ${IMPLEMENTACIONES_PY[$impl]}', number=10000)*1000), 10))"
  # Guardar el resultado
  RESULTADOS[$impl]=$(python3 -c "$CODE")
}

limpiar() {
  # Borar todos los archivos compilados
  rm -Rf build __pycache__
  case $impl in
  "cython")
    rm lib_cy.c
    ;;
  "ctypes")
    rm lib_c.so
    ;;
  esac
}

mostrar_resultados() {
  # Mostrar el rendimiento de las diferentes implementaciones
  echo
  for key in "${!RESULTADOS[@]}";
  do
    printf "%-8s ->   %13s ms\n" $key ${RESULTADOS[$key]}
  done
}


main() {
  for impl in ${!IMPLEMENTACIONES_PY[@]}
  do
    cd $impl
    if [ $impl != "pure_py" ];  # La implementación en puro Python no necesita ser compilada
    then
      compilar
    fi
    testear
    limpiar
    cd ..
  done
  mostrar_resultados
}

if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
  main
fi
