#include <stdio.h>
#include <string.h>  // Necesario para las funciones str<func>()

/* Las cadenas en C no son más que arrays de caracteres (char) terminados
    en un caracter nulo ('\0'). */

int main() {
    // ==========================================================================

    // Definir una cadena usando arrays
    char hola1[5] = {'h', 'o', 'l', 'a', '\0'};  // Ambas opciones son equivalentes
    char hola2[] = "hola";

    // Recorrer una cadena
    for (int i=0; i<=strlen(hola1); i++){
        printf("%d ", hola1[i] == hola2[i]);  // 1 1 1 1 1
    }
    printf("\n");

    // Definir una cadena usando punteros
    char *hola3 = "hola";
    printf("%s\n", hola3); // hola

    // ========================================================================
    //             FUNCIONES DE MANIPULACIÓN DE CADENAS

    // Obtener el largo de una cadena
    printf("%d\n", strlen(hola1));  // 4

    // ----------------------

    // Concatenar cadenas
    printf("%s\n", strcat(hola1, hola2));  // holahola
    /* La primera cadena pasada se sobrescribe con el resultado */
    printf("hola1 = %s   hola2 = %s\n", hola1, hola2);

    // ----------------------

    // Comparar dos cadenas
    /* Devuelve 0 if ambas cadenas son la misma; menos de 0 si la primera es
    menor que la segunda y más de 0 si la primera es mayor que la segunda */
    printf("%d\n", strcmp(hola1, hola1));

    // ----------------------

    // Obtener puntero a la primera ocurrencia de un caracter en una cadena
    char *ocurrencia1;
    ocurrencia1 = strchr(hola1, 'o');
    printf("%s\n", ocurrencia1);

    // ----------------------

    // Obtener la primera ocurrencia de una cadena dentro de otra
    char *ocurrencia2;
    ocurrencia2 = strstr(hola2, hola3);
    printf("%s\n", ocurrencia2);  // hola

    if (strstr(hola2, "www")) {
    	printf("Ocurre");
    } else {
    	printf("No ocurre");
    }

    // ========================================================================

    return 0;
}

/* Fuentes:
https://www.tutorialspoint.com/cprogramming/c_strings.htm
*/