#!/bin/bash

function show_files() {
    echo "----> Estos son los archivos que existen en el directorio:"
    ls
    echo
}

function main() {
    show_files

    echo "Del archivo libpitagoras.c creamos libpitagoras.o"
    # De la biblioteca creamos un archivo objeto (.o), independiente de su posicion
    echo ">> gcc -c -fPIC libpitagoras.c"
    gcc -c -fPIC libpitagoras.c

    # Los nombres de las bibliotecas empiezan con lib para que gcc
    # los reconozca como bibliotecas

    show_files

    echo "Del archivo objeto creamos libpitagoras.so enlazando el cabecero math.h"
    # Del archivo objeto creamos un archivo objeto compartido (.so = shared object)
    echo ">> gcc -shared -o libpitagoras.so libpitagoras.o -lm"
    gcc -shared -o libpitagoras.so libpitagoras.o -lm  # Con -shared creamos el .so
    # y con -l linkeamos a una bibilioteca

    show_files

    echo "Compilamos el ejecutable enlazando al archivo objeto compartido"
    echo ">> gcc -o mainpi main.c -L. -lpitagoras"
    # Con L indicamos en qué directorio se encuentra el archivo objeto compartido,
    # en este caso un . ya que se encuentra en el directorio actual
    # y con -l enlazamos a la biblioteca (no neceitamos incluir lib*...)
    gcc -o mainpi mainpi.c -L. -lpitagoras

    show_files

    echo "Copiamos el archivo objeto compartido a un lugar donde pueda ser encontrado"
    echo ">> sudo cp libpitagoras.so /lib/libpitagoras.so"
    sudo cp libpitagoras.so /lib/libpitagoras.so
    echo

    echo "Comprobamos las bibliotecas dinámicas que necesita el ejecutable:"
    echo ">> ldd mainpi"
    # Con ldd podemos comprobar cuales son las dependencias de un archivo ejecutable
    ldd mainpi
    echo

    echo "Ejecutamos el código:"
    ./mainpi

    echo
    echo "Limpiamos el directorio ya que esto es una prueba."
    echo ">> sudo rm *.so *.o mainpi /lib/libpitagoras.so"
    sudo rm *.so *.o mainpi /lib/libpitagoras.so

    show_files
}


if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
  main
fi
