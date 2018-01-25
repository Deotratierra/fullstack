#include <stdio.h>
#include <sys/sysinfo.h>

int main() {
    printf("Número de procesadores\n");
    printf("  Configurados: %2d\n", get_nprocs_conf());
    printf("  Disponibles: %3d\n", get_nprocs());

    return 0;
}
