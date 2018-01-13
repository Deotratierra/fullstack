#include <stdio.h>
#include <limits.h> /* SHRT_MIN, SHRT_MAX, USHRT_MAX, INT_MIN, INT_MAX,
                       UINT_MAX, LONG_MIN, LONG_MAX, ULONG_MAX */

/*
SHRT_MIN 	-32768 	Defines the minimum value for a short int.
SHRT_MAX 	+32767 	Defines the maximum value for a short int.
USHRT_MAX 	65535 	Defines the maximum value for an unsigned short int.
INT_MIN 	-2147483648 	Defines the minimum value for an int.
INT_MAX 	+2147483647 	Defines the maximum value for an int.
UINT_MAX 	4294967295 	Defines the maximum value for an unsigned int.
LONG_MIN 	-9223372036854775808 	Defines the minimum value for a long int.
LONG_MAX 	+9223372036854775807 	Defines the maximum value for a long int.
ULONG_MAX 	18446744073709551615 	Defines the maximum value for an unsigned long int.
*/

/* Los enteros son el tipo de dato más primitivo en C.
    Se usan para representar cualquier variable discreta.
   Se pueden declaran con signo o sin signo. En caso
    de que no se declare se define con signo.

   El entero que menos espacio ocupa es el tipo char,
    pero no se tocará en esta sección (ver apartado Caracteres)
    */

int main() {
    // ===========================================================
    //                          short
    /* El tipo signed short toma un rango de 0 a 65535 y el
        unsigned short desde -32768 a 32767. */

    unsigned short corto = 500;
    ushort tambien_asi;

    // -----------------------------------------------------

    //                          int
    int entero = 9;
    uint entero_sin_signo;

    // -----------------------------------------------------------

    //                          long
    long largo = 3372036854775807;
    ulong mas_largo;

    // -----------------------------------------------------------


    // ===========================================================

    //                      Límites

    // ¿Qué pasa si intentamos forzarlo un tipo sin signo a negativo?
    corto -= 1000;
    printf("%d\n", corto);  // 65036
    // Vuelve a sus valores más altos, siguiendo un esquema circular.

    // -----------------------------------------------------------

    /* Dentro del cabecero <limits.h> se encuentran las macros
        que nos indican directamente los límites de los rangos de
        las variables de tipo entero */
    printf("SHRT_MIN = %d (valor mínimo de short)\n", SHRT_MIN);            // -32768
    printf("SHRT_MAX = %d (valor máximo de short)\n", SHRT_MAX);            // 32767
    printf("USHRT_MAX = %d (valor máximo de unsigned short)\n", USHRT_MAX); // 65535

    printf("INT_MIN = %d (valor mínimo de int)\n", INT_MIN);                // -2147483648
    printf("INT_MAX = %d (valor máximo de int)\n", INT_MAX);                // 2147483647
    printf("UINT_MAX = %d (valor máximo de unsigned int)\n", UINT_MAX);     // 4294967295

    printf("LONG_MIN = %d (valor mínimo de long)\n", LONG_MIN);             // -9223372036854775808
    printf("LONG_MAX = %d (valor máximo de long)\n", LONG_MAX);             // 9223372036854775807
    printf("ULONG_MAX = %d (valor máximo de unsigned long)\n", ULONG_MAX);  // 18446744073709551615

    return 0;
}
