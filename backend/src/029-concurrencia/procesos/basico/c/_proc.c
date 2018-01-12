#include <stdio.h>
#include <unistd.h>

int main() {
    // Obtener ID del proceso actual (PID)
    int pid = getpid();
    printf("ID del proceso actual: %d\n", pid);

    // Obtener ID del proceso padre (PPID)
    int ppid = getppid();
    printf("ID del proceso padre: %d\n", ppid);

    return 0;
}