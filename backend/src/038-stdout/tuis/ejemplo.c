#include <ncurses.h>
#include <string.h>

/* El funcionamiento de ncurses se basa en moverse a través de las
    lineas y columnas de la pantalla donde queremos ir imprimiendo
    las salidas. La función mvprintw() mueve el cursor hasta unas
    coordenadas antes de imprimir la salida en pantalla y la función
    printw() simplemente muestra la salida en las coordenadas actuales.
   Para obtener el número de filas y columnas en pantalla usamos
    la función getmaxyx().
*/

int main() {
    char msg[] = "Mensaje en el centro de la pantalla";
    int lineas, columnas;

    initscr();

    // Obtener el número de lineas y columnas de la pantalla
    /* La variable stdscr se refiere a la pantalla actual */
    getmaxyx(stdscr, lineas, columnas);

    // Imprimir en el centro de la pantalla.
    /* Esta función imprime el mensaje pasado como tercer parámetro
        en las coordenadas de la pantalla (lineas y columnas)
        pasadas como primer y segundo parámetros respectivamente */
    mvprintw(lineas/2, (columnas-strlen(msg))/2, "%s", msg);

    // Imprimir en la parte baja de la pantalla (penúltima fila)
    mvprintw(lineas-2, 0,
    	     "Esta pantalla tiene %d lineas y %d columnas.\n",
    	     lineas, columnas);

    printw("Prueba a redimensionar tu ventana (si es posible) y vuelve a correr el programa.");

    refresh();
    getch();
    endwin();

    return 0;
}
