#include <stdio.h>

/*                      ENUM en C
Un tipo de datos enumerado es una manera de asociar nombres a números, y,
    por consiguiente de ofrecer más significado a alguien que lea el código.
    La palabra reservada enum (de C) enumera automáticamente cualquier lista
    de identificadores que se le pase, asignándoles valores de 0, 1, 2... etc.
    Se pueden declarar variables enum (que se representan siempre como valores
    enteros.

Un tipo enumerado se declara como un struct. Si sus valores son inicializados
    (siempre a enteros), el siguiente valor no inicializado toma el siguiente
    valor al anterior: */
enum Posicion {
    ganador = 1,
    secundon,   // == 2
    perdedor   // == 3
};

int main(int argc, char const *argv[]) {
    /* Los tipos enumerados son útiles cuando se quiere poder seguir la pista
        de alguna característica: */
    enum Posicion participante;

    participante = ganador;
    printf("El participante quedo en la posición número %d\n", participante);

    /* También son útiles cuando se quiere operar con BANDERAS (FLAGS),
        pueden realizar operaciones interesantes a nivel de bits ya que estamos
        hablando con números enteros (ver fuente 2). */

	return 0;
}

/* Fuentes:
http://arco.esi.uclm.es/~david.villa/pensar_en_C++/vol1/ch03s08s03.html
https://www.programiz.com/c-programming/c-enumeration
*/
