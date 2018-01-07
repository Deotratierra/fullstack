#!bin/bash

# Declaramos un array asociativo (hash o diccionario)
# con todas las carpetas y modulos...
declare -A IMPLEMENTACIONES_PY=( ["cython"]="lib_cy" ["manual"]="lib_c" ["pure_py"]="lib_py")
# y otro para guardar los resultados de rendimiento
declare -A RESULTADOS

compilar() {
  for impl in ${!IMPLEMENTACIONES_PY[@]}
  do
    cd $impl
    if [ $impl != "pure_py" ];  # La implementación en puro Python no necesita ser compilada
    then  # Implementaciones que necesitan compilación
      python3 setup.py -q build_ext --inplace
    fi
    cd ..
  done
}

testear() {
  for impl in ${!IMPLEMENTACIONES_PY[@]}
  do
    cd $impl
    # Medir el rendimiento de cada implementación
    CODE="import timeit;print(timeit.timeit('${IMPLEMENTACIONES_PY[$impl]}.summa(100)', \
              setup='import ${IMPLEMENTACIONES_PY[$impl]}', number=10000))"
    # Guardar el resultado
    RESULTADOS[$impl]=$(python3 -c "$CODE")
    cd ..
  done
}

limpiar() {
  # Borar todos los archivos compilados
  for impl in ${!IMPLEMENTACIONES_PY[@]}
  do
    cd $impl
    rm -Rf build __pycache__
    if [ $impl = "cython" ];
    then
      rm lib_cy.c
    fi
    cd ..
  done
}

mostrar_resultados() {
  # Mostrar el rendimiento de las diferentes implementaciones
  for key in "${!RESULTADOS[@]}";
  do
    printf "%-10s -> %-10s\n" $key ${RESULTADOS[$key]}
  done
}


if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
  compilar
  testear
  limpiar
  mostrar_resultados
fi
