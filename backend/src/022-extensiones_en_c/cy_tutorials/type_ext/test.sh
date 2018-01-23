#!/bin/bash

function main() {
    python3 setup.py build_ext -i  # Compila

    # Ejecuta
    printf "\n=======================================================\n"
    printf "\n#####   Ejemplos gestionando atributos de clase   #####\n\n"
    printf "Lectura de atributos:\n"
    python3 -c "from punto import Punto; \
        p = Punto(3, 4, 5); \
        print('Coordenada x = %d' % p.x); \
        print('Coordenada y = %d' % p.y); \
        print('Coordenada z = %d' % p.z);"
        # Salida:
        #     Coordenada x = 3
        #     Coordenada y = 4
        #     Traceback (most recent call last):
        #         File "<string>", line 1, in <module>
        #         AttributeError: 'punto.PuntoA' object has no attribute 'z'

    printf "\nSobreescritura de atributos:\n"
    python3 -c "from punto import Punto; \
        p = Punto(3, 4, 5); \
        p.x = 13; \
        print('Coordenada x = %d' % p.x); \
        p.y = 14; \
        print('Coordenada y = %d' % p.y); \
        p.z = 15; \
        print('Coordenada z = %d' % p.z);"
        # Salida:
        #     Coordenada x = 13
        #     Traceback (most recent call last):
        #         File "<string>", line 1, in <module>
        #         AttributeError: attribute 'y' of 'punto.PuntoA' objects is not writable
    printf "\n========================================================\n"

    # Limpia
    rm punto.c *.so
    rm -Rf build/

}


if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
  main
fi
