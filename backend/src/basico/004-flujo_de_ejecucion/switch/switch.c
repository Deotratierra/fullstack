#include <stdio.h>


/* La instrucción switch en C sigue la siguiente sintaxis:
    -------------------------------------------------------
    switch(variable/expresión) {

        case constante-expresion:
            <Código para este caso>;
            break;  // opcional

        case constant-expression:
            <Código para este caso>;
            break;  // opcional

        // Puedes escribir cualquier número de sentencias case

        // Si ninguna se cumple, la siguiente por defecto:
        default:  // opcional
            <Código para este caso>;
    }
    ------------------------------------------------------

Funciona de la siguiente forma: cuando se cumple un caso, sejecutan
    todos las sentencias definidas por debajo de este. Para prevenir
    que la ejecución continúe hacia abajo, debemos indicar break.

Esta instrucción no permite utilizar tipos no nativos, por lo tanto,
    no puedes incluir en la variable a analizar un array, por ejemplo.
    Switch está pensado para sentencias de bajo nivel, números o bytes
    como caracteres.
*/

int main() {

	// Comparando caracteres con switch
    char caracter = 'C';

    switch(caracter) {
        case 'A':
            printf("Buena nota\n");
            break;
        case 'B':
            printf("Nota media\n");
            break;
        case 'C':  // Especificamos varios casos para el mismo código
        case 'D':
            printf("Mala nota\n");  // Esta sería la ejecutada
            break;  // Sin este break también imprime "Muy mala nota"
        default:
            printf("Muy mala nota\n");
    }

    return 0;
}

/* Fuentes:
https://stackoverflow.com/questions/4480788/c-c-switch-case-with-string
*/