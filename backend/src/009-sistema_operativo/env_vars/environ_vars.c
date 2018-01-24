#include <stdio.h>
#include <stdlib.h>  // getenv()

int main() {
	// Obtener una variable de entorno
    char* ENV_PATH;
    ENV_PATH = getenv("PATH");
    if (ENV_PATH != NULL) {
        printf("%s\n", ENV_PATH);
    }

    return 0;
}