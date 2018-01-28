#ifdef __APPLE__

#include <stdio.h>
#include <sys/sysctl.h>

/* Correpondencia entre las versiones del sistema operativo
    y los lanzamientos de OSX:

16.x.x  macOS 10.12.x Sierra
15.x.x  OS X  10.11.x El Capitan
14.x.x  OS X  10.10.x Yosemite
13.x.x  OS X  10.9.x  Mavericks
12.x.x  OS X  10.8.x  Mountain Lion
11.x.x  OS X  10.7.x  Lion
10.x.x  OS X  10.6.x  Snow Leopard
 9.x.x  OS X  10.5.x  Leopard
 8.x.x  OS X  10.4.x  Tiger
 7.x.x  OS X  10.3.x  Panther
 6.x.x  OS X  10.2.x  Jaguar
 5.x    OS X  10.1.x  Puma
*/

int main() {
    char version[8];
    size_t size = sizeof(version);

    int ret = sysctlbyname("kern.osrelease", version, &size, NULL, 0);
    if (ret == -1) {
        printf("Ocurrió un error obteniendo la versión del sistema operativo.\n");
    } else {
        printf("Versión del sistema operativo: %s\n", version);
    }

    return 0;
}

#endif /* __APPLE__ */
