#include <ncurses.h>  // linkear con -lncurses al compilar
// ncurses ya incluye <stdio.h>

/* Para compilar este programa:
    gcc archivo.c -o ejecutable -lncurses

/* La biblioteca ncurses permite generar interfaces de usuario
    basadas en texto. Para una documentación en español bastante
    avanzada: http://ditec.um.es/~piernas/manpages-es/otros/tutorial-ncurses.html
*/

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

/* Fuentes:
http://gluc.unicauca.edu.co/index.php/Programaci%C3%B3n_con_Ncurses
*/