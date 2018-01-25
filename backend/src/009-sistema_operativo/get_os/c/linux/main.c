#include <stdio.h>
#include <sys/utsname.h>

/* Para obtener información sobre el sistema operativo
en Linux utilizamos la función uname(), toma la dirección de memoria
de una estructura utsname y donde guarda la información.

http://man7.org/linux/man-pages/man2/uname.2.html

Para una lista completa de los campos devueltos por uname en cada
sistema operativo, consultar: https://en.wikipedia.org/wiki/Uname
*/

int main() {
    struct utsname unameData;
    int ok;

    ok = uname(&unameData);
    if (ok == -1) {
        printf("Ocurrió un error en la función uname().\n");
    } else {
        printf("Sistema operativo: %s\n", unameData.sysname);
        printf("Lanzamiento: %s\n", unameData.release);
        printf("Versión: %s\n", unameData.version);
    }

    return 0;
}



/* Fuentes:
https://stackoverflow.com/questions/3596310/c-how-to-use-the-function-uname
https://stackoverflow.com/questions/6315666/c-get-linux-distribution-name-version
*/