#include <ncurses.h>  // linkear con -lncurses al compilar

/* Para compilar este programa:
    gcc archivo.c -o ejecutable -lncurses

/* La biblioteca ncurses permite generar interfaces de usuario
    basadas en texto. */

int main() {
    // Iniciar una pantalla dentro de la terminal
    initscr();

    // Imprimir en la pantalla
    printw("¡Hola mundo con ncurses!\nPulsa una tecla para continuar");

    // Refrescar pantalla
    refresh();

    // Esperar a la pulsación de una tecla
    getch();

    // Finalizar una pantalla
    endwin();

    return 0;
}