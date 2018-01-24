## Compilar según sistemas operativos y versiones

La web [Macros predefinidas por sistema operativo](https://sourceforge.net/p/predef/wiki/OperatingSystems/) tiene un completo listado de las macros definidas en cada sistema operativo junto a las diferentes versiones.

En el siguiente listado sólo se incluyen los sistemas operativos más importantes (sin número de versión).

______________________________________

### Unix
- `#ifdef unix`      // Estamos en Unix
- `#ifdef __unix`
- `#ifdef __unix__`

______________________________________

### Linux
- `#ifdef __linux__`  // Estamos en un sistema basado en el kernel de Linux

> Obtener todas las macros predefinidas: `gcc -dM -E - </dev/null`

### Android
- `#ifdef __ANDROID__`  // Estamos en Android

______________________________________

### Windows
- `#ifdef _WIN32`   // Estamos en Windows 32 bits ó 64 bits
- `#ifdef _WIN64`   // Estamos en Windows 64 bits

> Obtener todas las macros predefinidas: `gcc -dM -E - <NUL:`

#### [CygWin](https://en.wikipedia.org/wiki/Cygwin)
- `#ifdef __CYGWIN__`  // Estamos en CygWin

#### [MS-DOS](https://en.wikipedia.org/wiki/MS-DOS)
- `#ifdef __MS_DOS__` // Estamos en MS-DOS

______________________________________

### MacOS
- `#ifdef __APPLE__`  // Estamos en Apple MacOSX
- `#ifdef __MACH__`

### [iOS](https://es.wikipedia.org/wiki/IOS)
- ``    // Estamos en Apple iOS


______________________________________

### [BSD](https://en.wikipedia.org/wiki/Berkeley_Software_Distribution)
- `#ifdef __FreeBSD__`  // Estamos en [FreeBSD](https://es.wikipedia.org/wiki/FreeBSD)
- `#ifdef __NetBSD__`   // Estamos en [NetBSD](https://es.wikipedia.org/wiki/NetBSD)
- `#ifdef __OpenBSD__`  // Estamos en [OpenBSD](https://es.wikipedia.org/wiki/OpenBSD)

______________________________________

### Solaris/SunOS
```
#if defined(sun) || defined(__sun)
# if defined(__SVR4) || defined(__svr4__)
/* Estamos en Solaris */
# else
/* Estamos en SunOS */
# endif
#endif
```
______________________________________


> Fuentes:
> - https://stackoverflow.com/questions/142508/how-do-i-check-os-with-a-preprocessor-directive