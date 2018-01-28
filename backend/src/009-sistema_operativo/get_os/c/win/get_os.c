#ifdef _WIN32
#include <windows.h>
#include "get_os.h"

/**
 * Obtener la versión de Windows
 * Devuelve el número de versión del sistema.
 * Correspondencia entre números y nombres:
 *      Windows 10             : 10.0
 *      Windows 8.1            : 6.3
 *      Windows 8.0            : 6.2
 *      Windows 7              : 6.1
 *      Windows Vista          : 6.0
 * @return Número de versión
 **/
double os_version_num() {
    OSVERSIONINFOEX info;
    ZeroMemory(&info, sizeof(OSVERSIONINFOEX));
    info.dwOSVersionInfoSize = sizeof(OSVERSIONINFOEX);
    GetVersionEx((LPOSVERSIONINFO)&info);

    double version;
    version = info.dwMajorVersion
            + (info.dwMinorVersion / 10.0);

    return version;
}

/**
 * Obtiene el nombre de versión de Windows
 * a partir del número-
 * @param  num Número de versión
 * @return     Nombre de la versión
 */
void os_version_name(double num) {
    if (num == 6.0) {
        return "Vista";
    } else if (num == 6.1) {
        return "7";
    } else if (num == 6.2) {
        return "8.0";
    } else if (num == 6.3) {
        return "8.1";
    } else if (num == 10.0) {
        return "10";
    } else {
        return ""; // Desconocida
    }
}

#endif /* _WIN32 */

/* Fuentes:
https://stackoverflow.com/questions/29944745/get-osversion-in-windows-using-c
*/
