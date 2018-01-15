#include <stdio.h>

/* ========================================================================
                          ####   struct   ####
   El concepto más parecido a un array asociativo en C son las estructuras.
    Estas solventan los problemas de agrupación de datos o construcción
    de tipos nuevos a partir de otros más primitivos. Son el objeto más
    parecido a una clase en C.
   Los miembros de una estructura ocupan diferentes espacios de memoria.

   ------------------------------------------------------------------------
                          ####   union   ####
   En cambio, en las uniones, los miembros ocupan la misma área de memoria.
    El tamaño de una unión es el tamaño de su miembro de mayor tamaño.
   Si modificamos un miembro de una union, los demás cambian y, a veces,
    de maneras impredecibles. También se limitan en que no podemos acceder
    a sus diferentes miembros al mismo tiempo.

   ------------------------------------------------------------------------
                          ####   enum   ####
   Es una estructura definida con constantes de tipo entero. Los miembros
    de la misma sólo pueden almacenar constantes de tipo entero y si son
    inicializados sin valor van tomando los valores: 0, 1, 2, ... n

  =========================================================================
   */


int main() {
    // ================================================================
    //                    ####   struct   ####
    // Declaración de estructura:
    struct Estructura_tipo_1 { // Nombre de este tipo de estructuras
        int miembro1;
        double miembro2;
        unsigned char miembro3[8];
    } estructura1;  // Instancia de la estructura (se puede omitir de la declaración)

    /* Es una convención (buena práctica) declarar el nombre de las estructuras
        con el primer caracter en mayúsucula */

    // Si se omite la instanciación de una estructura al declararla, se declararía así:
    //struct Estructura_tipo_1 estructura1.

    // -----------------------------------------------------
    /* Para no tener que estar declarando siempre "struct Estructura_tipo_1" al crear
        nuevas estructuras de ese tipo, podemos definirlas de otra forma: */

    typedef struct {  // Definimos un nuevo tipo
        int miembro1;
        double miembro2;
        unsigned char miembro3[8];
    } Estructura_tipo_2;  // Aquí el nombre de la estructura vendría abajo

    // Para instanciar
    Estructura_tipo_2 estructura2;

    // -------------------------------------------------------------------

    // Acceder a los valores
    estructura2.miembro2 = 3.1416;

    printf("Estructura2.miembro2 = %f\n", estructura2.miembro2);

    // ===================================================================


    // ===================================================================
    //                       ####   union   ####
    // Aspecto de una union
    union {
      int i;
      double d;
    } u;

    /* Por lo demás, las uniones funcionan igual que las estructuras */

    // ===================================================================

    // ===================================================================
    //                       ####   enum   ####
    
    // Inicialización automática de enumeradores
    enum Boolean {
        FALSE,  // 0
        TRUE    // 1
    };

    // Inicialización por valores
    enum Hexaedro {
		VERTICE = 8,
		LADOS = 12,
		CARAS = 6
	};

	// ===================================================================

    return 0;
}

/* Fuentes:
https://es.wikibooks.org/wiki/Programaci%C3%B3n_en_C/Estructuras_y_Uniones
*/
