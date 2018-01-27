#include <stdio.h>
#include <stdlib.h> // exit()
#include <ctype.h>  // toupper()

int max_enemigos_muertos(void* _matriz, int filas, int columnas);

int muertos_columna(void* _matriz, int i, int j, int columnas);
int muertos_fila(void* _matriz, int i, int filas, int j, int columnas);

int main() {
    // ===========================================================
    // El usuario genera la matriz del tablero de juego

    int filas, columnas, s_in, respuesta;
    char seleccion_valida = 0, celda_vacia = 0, sel;

    // El usuario define el número de filas y columnas
    while (seleccion_valida == 0) {
        printf("Introduce el número de filas de la matriz: ");
        s_in = scanf("%d", &filas);

        if (s_in != 1) {
            printf("Por favor, introduce un número.\n");
            exit(1);
        } else if (filas == 0) {
            printf("Una matriz con %d filas no es posible.\n", filas);
            exit(1);
        } else {
            seleccion_valida = 1;
        }
    }
    seleccion_valida = 0;

    while (seleccion_valida == 0) {
        printf("Introduce el número de columnas de la matriz: ");
        s_in = scanf("%d", &columnas);

        if (s_in != 1) {
            printf("Por favor, introduce un número.\n");
            exit(1);
        } else if (columnas == 0) {
            printf("Una matriz con %d columnas no es posible.\n", filas);
            exit(1);
        } else {
            seleccion_valida = 1;
        }
    }
    seleccion_valida = 0;

    // Creamos la matriz
    char matriz[filas][columnas];

    printf("Ahora vas a crear el campo de juego.\n");
    printf("Leyenda:\n\tEnemigo = E\n\tMuro = M\n\tCelda vacía = -\n");

    // El usuario rellena la matriz
    for (int i=0; i<filas; i++) {
        for (int j=0; j<columnas; j++) {
            while (seleccion_valida == 0) {
                printf("Introduce el valor para matriz[%d][%d]: ", i, j);
	            s_in = scanf(" %c", &sel);
	            sel = toupper(sel);
	            if ( (sel == 'E') || (sel == 'M') || (sel == '-') ) {
                    seleccion_valida = 1;
                    matriz[i][j] = sel;
                    if (sel == '-') {
                        celda_vacia = 1;
                    }
	            } else {
	                printf("El caracter %c no es válido.\n", sel);
	            }
            }
            seleccion_valida = 0;
        }
    }
    printf("\nHas terminado de definir el tablero:\n");


    // Mostramos la matriz generada
    for (int i=0; i<filas; i++) {
        for (int j=0; j<columnas; j++) {
             printf("%c ", matriz[i][j]);
        }
        printf("\n");
    }
    printf("\n");

    if (celda_vacia == 0) {
        printf("Debido a que no has colocado ninguna celda vacía, ");
        printf("no puedes poner la bomba.\n");
        respuesta = 0;
    } else {
        // Calculamos el máximo de muertos posibles con para el tablero
        respuesta = max_enemigos_muertos(matriz, filas, columnas);
    }

    printf("El máximo número de muertos posibles para el tablero es: %d\n",
    	   respuesta);

    return 0;
}


/**
 * Calcula el máximo de enemigos muertos según las reglas del juego.
 * @param  _matriz  Matriz del tablero de juego
 * @param  filas    Número de filas en el tablero
 * @param  columnas Número de columnas en el tablero
 * @return          Máximo de enemigos muertos posibles poniendo una bomba
 */
int max_enemigos_muertos(void* _matriz, int filas, int columnas) {
    if (filas == 0) {
    	printf("El número de filas no puede ser 0.\n");
    	return 0;
    }
    if (columnas == 0) {
    	printf("El número de columnas no puede ser 0.\n");
    	return 0;
    }

    char (*matriz)[columnas] = _matriz; // Casting a matriz de caracteres

    int enemigos_columna = 0;
    int enemigos_fila[filas];
    int maximo_muertos = 0;
    int muertos_bomba_aqui;

    for (int i=0; i<filas; i++) {
        enemigos_fila[i] = 0;
        for (int j=0; j<columnas; j++) {

            if ( (j == 0) || (matriz[i][j-1] == 'W') ) {
                enemigos_columna = muertos_columna(matriz, i, j, columnas);
            }
            if ( (i == 0) || (matriz[i-1][j] == 'W') ) {
                enemigos_fila[j] = muertos_fila(matriz, i, filas, j, columnas);
            }

            if (matriz[i][j] == '-') {
                muertos_bomba_aqui = enemigos_columna + enemigos_fila[j];
                if (maximo_muertos < muertos_bomba_aqui) {
                    maximo_muertos = muertos_bomba_aqui;
                }
            }
        }
    }
    return maximo_muertos;
}

/**
 * Calcula los enemigos muertos en una columna
 * @param  _matriz   Matriz original
 * @param  i        Número de i a comprobar
 * @param  j        Número de j a comprobar
 * @param  columnas Columnas de la matriz
 * @return          Número de enemigos muertos en la fila
 */
int muertos_columna(void* _matriz, int i, int j, int columnas) {
    int enemigos = 0;
    char (*matriz)[columnas] = _matriz;
    while ( (j < columnas) && (matriz[i][j] != 'M') ) {
        if (matriz[i][j] == 'E') {
            enemigos++;
        }
        j++;
    }
    return enemigos;
}

/**
 * Calcula los enemigos muertos en una columna
 * @param  _matriz   Matriz original
 * @param  i        Número de fila a comprobar
 * @param  filas    Filas en la matriz
 * @param  j        Número de columna a comprobar
 * @return          Número de enemigos muertos en la columna
 */
int muertos_fila(void* _matriz, int i, int filas, int j, int columnas) {
    int enemigos = 0;
    char (*matriz)[columnas] = _matriz;
    while ( (i < filas) && (matriz[i][j] != 'M') ) {
        if (matriz[i][j] == 'E') {
            enemigos++;
        }
        i++;
    }
    return enemigos;
}

/* Fuentes:
https://www.lawebdelprogramador.com/foros/C-Visual-C/499652-Matriz-por-referencia.html
https://stackoverflow.com/questions/18661702/passing-matrix-as-a-parameter-in-function
*/
