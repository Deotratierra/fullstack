#ifndef __GET_OS__
#define __GET_OS__

#ifdef _WIN32  /* Windows */
#include<windows.h>
#define OS "Windows"

/** Obtener la versión de Windows
 *  Devuelve el número de versión del sistema.
 *  Correspondencia entre números y nombres:
 *      Windows 10             : 10.0
 *      Windows 8.1            : 6.3
 *      Windows 8.0            : 6.2
 *      Windows 7              : 6.1
 *      Windows Vista          : 6.0
 **/
double get_os_version() {
    OSVERSIONINFOEX info;
    ZeroMemory(&info, sizeof(OSVERSIONINFOEX));
    info.dwOSVersionInfoSize = sizeof(OSVERSIONINFOEX);
    GetVersionEx((LPOSVERSIONINFO)&info);

    float version;
    version = info.dwMajorVersion 
            + (info.dwMinorVersion / 10.0);

    return version;
}

#endif /* Windows */

#endif /* __GET_OS__ */

/* Fuentes:
https://stackoverflow.com/questions/29944745/get-osversion-in-windows-using-c
*/
