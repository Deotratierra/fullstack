#include <stdio.h>
#include <ctype.h>  // Funciones para clasificación de caracteres
#include <limits.h> // CHAR_BIT, SCHAR_MIN, SCHAR_MAX, UCHAR_MAX


// CARACTERES EN C //

/* El tipo char es un tipo básico en C. Por defecto, char se refiere a
    signed char, el cual opcupa un rango de -128 a 127. E tipo unsigned char
    ocupa el rango de 0 a 255.

   Estos se representan mediante la tabla de caracteres ASCII:
    http://www.elcodigoascii.com.ar/caracteres-ascii-control/caracter-nulo-codigo-ascii-0.html
    También puedes ver la tabla ejecutando: man ascii
   Hay determinados caracteres en la tabla ASCII como \n (nueva línea),
    \t (tabulador) ó \0 (caracter nulo) que no se muestran por pantalla,
    si no que sirven para propósitos específicos.
*/

// DECLARACIÓN DE FUNCIONES:

void printbinchar(char character);

int main() {

	// ==================================================================

    //                Declaración y representación
    /* Los caracteres deben ir entre comillas simples y se componen de una letra. */

    char c = 'c';
    printf("Representación como caracter: %c\nValor numérico: %d\n", c, c);

    /* No es lo mismo que una cadena, por lo que si ejecutamos printf("%s", c)
        se producirá una violación de segmento.*/

    // ---------------------------------------------------------

    //                         Tamaño
    /* Internamente se representan como una secuencia binaria de 8 bits (1 byte).
    Debido a que 2⁸ = 256, la tabla de caracteres ASCII extendida se compone
    de 256 valores con los que se representan los caracteres occidentales. */

    printf("Tamaño de char: %d bytes\n", sizeof(char)); // 1

    // El tamaño de los caracteres puede variar
    printf("Tamaño de 'z': %d bytes\n", sizeof('z'));

    // ---------------------------------------------------------

    //                  Promoción de enteros
    /* Realmente char sería un entero, pero de un tipo especial que C reconoce
        como caracter y aplica la conversión ASCII. Por ello también se puede utilizar
        para representar números pequeños, con la ventaja de que ocupa sólo un byte.
       Entonces, podemos realizar operaciones numéricas con los caracteres de acuerdo
        a su naturaleza de números enteros: */

    int suma;
    char a;

    suma = c + 3;
    printf("De char a int  ->  c + 3 = %d\n", suma);

    a = c - 2;
    printf("De int a char  ->  c - 2 = %c\n", a);

    printf("Comparación  ->  a < c = %d\n", a < c); // Es verdadero

    // -------------------------------------------------------------------

    //                        Límites
    /* Si hemos dicho al principio que el tipo signed char ocupa un rango de
    -128 a 127, ¿qué pasaría si intentamos ir a los márgenes? Probemos: */

    signed char x = '}';                  //        125 = }
                                          //        126 = ~
    while (x > 124 || x < -125) {         //        127 =
        printf("%d = %c\n", x, x);        //        -128 = �
        x++;                              //        -127 = �
    }                                     //        -126 = �

    /* Si incrementamos el valor del caracter a través de un bucle y llegamos
        a 127, el siguiente es -128. Esta es una diferencia fundamental con las
        variantes de tipos enteros.

       Si realizamos la misma operación con el tipo unsigned char, veremos
        que sucede lo mismo en los límites 0 y 255:
    */
    unsigned char y = 253;                //         253 = �
                                          //         254 = �
    while (y > 252 || y < 3) {            //         255 = �
        printf("%d = %c\n", y, y);        //         0 =
        y++;                              //         1 =
    }                                     //         2 =

    /* Los tipos char podemos usarlos para operar con números pequeños,
        siempre que no toquemos estos límites */

    // ----------------------------------------------------------------

    /* El cabecero <limits.h> determina propiedades de varios tipos de variables.
        Pueden servirnos para saber los rangos de estos límites. */
    printf("CHAR_BIT = %d (número de bits en char)\n", CHAR_BIT);          // 8
    printf("SCHAR_MIN = %d (valor mínimo de signed char)\n", SCHAR_MIN);   // -128
    printf("SCHAR_MAX = %d (valor máximo de unsigned char)\n", SCHAR_MAX); // 127
    printf("UCHAR_MAX = %d (valor máximo de unsigned char)\n", UCHAR_MAX); // 255

    // ====================================================================

    //              Rutinas de clasificación de caracteres

    /*
    int islower(ch);          Dentro del cabecero <ctype.h> existen varias
    int isupper(ch);              funciones útiles para clasificar caracteres.
    int isalpha(ch);
    int isascii(ch);          Las siguientes funciones indican el tipo de caracter.
    int isblank(ch);              Las que devuelven enteros son booleanos
    int iscntrl(ch);              (1 True, 0 False).
    int isdigit(ch);
    int isgraph(ch);          Para más información ejecutar: man <nombre_de_funcion>
	int isalnum(ch);
	int isprint(ch);
	int ispunct(ch);
	int isspace(ch);
	int isxdigit(ch);
	char tolower(ch);
	char toupper(ch);
	*/

    // -------------------------------------------------------------------

    //                 Leer la entrada por teclado
    char inserted;

    printf("Inserta el caracter 'a': ");
    inserted = getchar();

    if (inserted == 'a') {  // Al compararlo SIEMPRE COMILLAS SIMPLES
        printf("Has insertado el caracter correcto.\n");
    } else {
        printf("No has insertado el caracter correcto, si no '%c'.\n", inserted);
    }

    // ==================================================================


    return 0;
}

// ======================================================================================

//                               FUNCIONES ÚTILES

/**
 * --------------  Imprimir un caracter en binario  ----------------
 * @param character caracter a imprimir en binario
 *
 * Fuente:
 * https://stackoverflow.com/questions/18327439/printing-binary-representation-of-a-char-in-c
 * Para entender esta función ver el apartado  Bajo nivel -> bits
 */
void printbinchar(char ch) {
    int i;
    for (i = 0; i < 8; i++) {
        printf("%d", !!((ch << i) & 0x80));
    }
    printf("\n");
}

// =====================================================================================


/* Fuentes:

http://www2.elo.utfsm.cl/~lsb/elo311/clases/apuntes_c/chars.pdf
https://gsamaras.wordpress.com/code/negative-ascii-codes/
https://stackoverflow.com/questions/2172943/size-of-character-a-in-c-c
https://www.cs.swarthmore.edu/~newhall/unixhelp/C_chars.html
https://www.tutorialspoint.com/c_standard_library/limits_h.htm

FUNCIONES:
https://stackoverflow.com/questions/18327439/printing-binary-representation-of-a-char-in-c
*/
