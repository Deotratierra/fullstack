#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    /* Obtener el número de pulsos de reloj desde que se inició el proceso

    Los pulsos de reloj son unidades que usan los dispositivos electrónicos para
    medir el tiempo. Para los ordenadores personales, los pulsos de reloj generalmente
    se refieren al reloj principal del sistema, el cual corre a 66 MHz. Esto significa
    que hay 66 millones de pulsos (o ciclos) de reloj por segundo. */
    clock_t pulsos;  // clock_t es el tipo que retorna clock()
    pulsos = clock();
    printf("Pulsos de reloj desde el comienzo del proceso: %d\n", pulsos);
    /* Para calcular la relación entre los pulsos de reloj y los segundos reales,
        podemos dividir el tiempo retornado por clock entre la variable
        CLOCKS_PER_SEC que nos provee esta biblioteca. */
    clock_t equiv_segundos;
    equiv_segundos = ((double)pulsos)/CLOCKS_PER_SEC;
    printf("Tiempo usado por la CPU en seg = %f (%d µs).\n\n",
        equiv_segundos, equiv_segundos*1000000);

    // --------------------------------------------------------------------------

    /* Obtener el tiempo actual en unix timestamps con la función time().

    Ver protocolos para la especificación de tiempos: https://tools.ietf.org/html/rfc868
     */
    time_t actual_unix_timestamps_1;
    actual_unix_timestamps_1 = time(NULL); // time() permite pasar un argumento por referencia
    // donde guardar el resultado o nulo y que lo devuelva. Lo siguiente es equivalente:
    // time(&actual_unix_timestamps_1);

    if (actual_unix_timestamps_1 == (time_t)-1) { // Casting a -1
        printf("Ocurrió un fallo obteniendo el tiempo en unix_timestamps.\n");
        exit(1);
    } else {
        printf("Tiempo actual en unix timestamps: %d\n\n", actual_unix_timestamps_1);
    }

    // --------------------------------------------------------------------------

    /* Convertir de unix timestamps a cadena de caracteres en formato leíble
    mediante la función ctime() */
    char* tiempo_en_cadena;
    tiempo_en_cadena = ctime(&actual_unix_timestamps_1);
    if (tiempo_en_cadena == NULL) {
        printf("Ocurrió un error convirtiendo de unix timestamps a formato leíble.\n");
        exit(1);
    } else {
        printf("Fecha actual del PC en formato leíble: %s\n", tiempo_en_cadena);
    }


    // ===============================================================================

    /* Para trabajar con fechas el cabecero <time.h> provee la estructura tm, la cual
        contiene los siguientes campos:
        int    tm_sec   seconds [0,61]
        int    tm_min   minutes [0,59]
        int    tm_hour  hour [0,23]
        int    tm_mday  day of month [1,31]
        int    tm_mon   month of year [0,11]
        int    tm_year  years since 1900
        int    tm_wday  day of week [0,6] (Sunday = 0)
        int    tm_yday  day of year [0,365]
        int    tm_isdst daylight savings flag

    Los miembros de la estructura significan lo siguiente:
       tm_sec   El número de segundos después del minuto, normalmente
                 en el rango de 0 a 59, pero pueden subir a 60 para permitir
                 saltos de segundos.
       tm_min    El número de minutos después de la hora, en el rango de 0 a 59.
       tm_hour   El número de horas pasada medianoche, en el rango de 0 a 23.
       tm_mday   El día del mes, en el rango de 1 a 31.
       tm_mon    El número de meses desde enero, en el rango de 0 a 11.
       tm_year   El número de años desde 1900.
       tm_wday   El número de días desde el domingo, en el rango de 0 a 6.
       tm_yday   El número de días desde el 1 de Enero, en el rango de 0 a 365.
       tm_isdst  Una bandera que indica si el horario de verano está en el momento
                  descrito. El valor es positivo si está en horario de verano,
                  cero si no y negativo si la información no está disponible.

    Para inicializar una estructura de este tipo podemos seguir los siguientes pasos:
    */
    time_t tiempo_en_crudo;  // Variable donde guardaremos el tiempo en crudo
    struct tm* estructura_de_fecha;  // Puntero a la estructura
    char buffer[32];

    time(&tiempo_en_crudo);  // Guardamos el tiempo en unix_timestamps
    // Pasamos el tiempo en unix_timestamps a la función localtime() y nos devuelve
    // la estructura tm
    estructura_de_fecha = localtime(&tiempo_en_crudo);

    /* Con la función strftime() (string from time) formateamos la fecha a nuestro
        gusto. Como primer parámetro le pasamos la cadena donde se guardará la fecha
        formateada como cadena de caracteres, como segundo el tamaño, como tercero
        las claves para el formateo y como cuarto la estructura de fecha tm. */
    strftime(buffer, 32, "%d/%m/%Y", estructura_de_fecha);

    printf("Hoy es %s.\n", buffer);


    // =========================================================================
    /*
    struct tm tiempo_1;

    time_t actual_unix_timestamps_2;
    actual_unix_timestamps_2 = mktime(tiempo_en_cadena);
    if (actual_unix_timestamps_2 == (time_t)-1) {
        printf("Ocurrió un error convirtiendo de formato leíble a unix timestamps.\n");
    } else {
        printf("Fecha actual en unix_timestamps: %d\n", actual_unix_timestamps_2);
    }
    */




    return 0;
}

/* Fuentes:
https://en.wikipedia.org/wiki/C_date_and_time_functions
https://www.tutorialspoint.com/c_standard_library/c_function_clock.htm
http://pubs.opengroup.org/onlinepubs/7908799/xsh/time.h.html
https://www.webopedia.com/TERM/C/clock_tick.html
https://stackoverflow.com/questions/13658756/example-of-tm-use
https://www.daniweb.com/programming/software-development/threads/335282/struct-tm
*/