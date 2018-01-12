#include <stdlib.h>

/* La función system de la biblioteca estandar de C
    provee una fácil forma de ejecutar un comando shell
    desde un programa C.
   Devuelve el valor de retorno del comando. Si la shell
    misma no puede ejecutarse, devuelve 127 y si ocurre otro
    error devuelve -1.
*/

int main() {
    int valor_de_retorno;
    valor_de_retorno = system("ls -l");
    return valor_de_retorno;
}
