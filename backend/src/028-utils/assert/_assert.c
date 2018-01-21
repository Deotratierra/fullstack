#include <stdio.h>
#include <assert.h>  // Hay que incluir este cabecero para utilizar aserciones

int main() {
    // Las aserciones en C no lanzan ninguna excepción, por
    // lo que no pueden ser cazadas. En su lugar, producen un
    // aborto en el código.
    assert(1 + 2 == 3);

    return 0;
}
