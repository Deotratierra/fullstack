#include <stdio.h>
#include <ctype.h>  // toupper()

int main() {
    // Para seleccionar opciones tipo SI o NO debemos utilizar lo siguente:
    int seleccion_valida = 0;
    char sn;

    while (seleccion_valida == 0) {
        printf("\n¿Te gusta esta documentación? S/N: ");
        scanf(" %c", &sn);

        // Pasamos la variable a mayúscula
        sn = toupper(sn);

        // Las cadenas 'S' y 'N' deben ir con comillas simples
        if ( (sn == 'S') || (sn == 'N') ) {
            seleccion_valida = 1;
        } else {
            printf("Opción inválida.\n");
            continue;
        }

        if (sn == 'S') {
            printf("¡Me alegro!\n");
        } else {
            printf("Está en proceso. Si tienes alguna sugerencia comunícamela.\n");
        }
    }

    return 0;
}