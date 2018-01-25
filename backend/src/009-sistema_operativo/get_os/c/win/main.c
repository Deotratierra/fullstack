#include <stdio.h>
#include "get_os.h"

/* Compilación:
gcc main.c get_os.c -o main
*/

int main() {
    double num;
    char* name;

    num = os_version_num();
    name = os_version_name(num);

    printf("Numero de version: %f\n", num);
    printf("Nombre de version: %s\n", name);
}
