#include <stdio.h>

// DECLARACIÓN DE FUNCIONES
void printbinchar(char character);


int main() {
    printf("%d", intBits());


    return 0;
}

// ==================================================================================

//                               FUNCIONES ÚTILES

/**
 * //  --------------  Imprimir un caracter en binario  ----------------
 * @param character caracter a imprimir en binario
 *
 * Fuente:
 * https://stackoverflow.com/questions/18327439/printing-binary-representation-of-a-char-in-c
 *
 * Explicación:
 *    Proceso:
 *        Imagina que pasas a la función el caracter 'a' (97, 0b0110000)
 *        En cada iteración aplicamos las siguientes operaciones:
 *            1. Asignación a la izquierda (significa exponenciar al ²
 *                el número de veces que le pasamos como argumento).
 *                En la segunda iteración tendríamos (194, 0b11000010).
 *                En la primera tendríamos 97 ya que es i=0.
 *            2. Operación & (AND) con la constante 0x80 (128, 0b10000000)
 *                11000010  = 194
 *              & 10000000  = 128    Sólo hay dos soluciones posibles, 0 ó 128
 *              ----------
 *                10000000  = 0x80  = 128
 *            3. Ahora negamos dos veces !! para convertir 128 en 1 y 0 en 0
 *
 *    Funcionamiento:
 *        log(128, 2) = 7  <->  2⁷ = 128  <->  el bit de orden más alto en
 *        128 es el 7º bit.
 *        Este 7º bit funciona como un lector de todos los bits que le vamos
 *        pasando del número que vamos exponenciando.
 *        Esta técnica es básicamente coger los bits del número y mandarlos
 *        a la izquierda donde vamos leyéndolos al hacer la operación AND
 *        como si tuviéramos un lector láser. Se denomina enmascaramiento.
 * Mas información: https://en.wikipedia.org/wiki/Bitwise_operations_in_C
 */
void printbinchar(char ch) {
    int i;
    //printf("DEBUG: 0x80 = %d\n", 0x80);
    for (i = 0; i < 8; i++) {
        // DEBUG para entender qué hace el código
        //printf("DEBUG: (ch << i) == %d\n", (ch << i));
        //printf("DEBUG: (ch << i) & 0x80 == %d\n", (ch << i) & 0x80);
        //printf("DEBUG: !!((ch << i) & 0x80) == %d\n", !!((ch << i) & 0x80));

        printf("%d", !!((ch << i) & 0x80));
    }
    printf("\n");
}

// ------------------------------------------------------------------------



/* Fuentes:

FUNCIONES:
https://stackoverflow.com/questions/18327439/printing-binary-representation-of-a-char-in-c
*/
