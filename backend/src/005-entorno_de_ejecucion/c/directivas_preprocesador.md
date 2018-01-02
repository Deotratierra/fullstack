## Directivas del preprocesador
Al compilar código C podemos indicarle al preprocesador cómo debe ser compilado incluyendo unas serie de directivas.

__________________________________________

### `#include`
Incluye un archivo dentro del archivo actual en tiempo de compilación: `#include <stdio.h>`

__________________________________________

### `#define`
Se utiliza para definir macros, por ejemplo:
```
#ifndef __ARCHIVO_H__
#define __ARCHIVO_H__

/*... declaraciones de funciones, etc. ...*/

#endif
```

Se utiliza comunmente junto con las directivas de compilación condicional `#ifdefp`, `#ifndef`, `#else`, `#elif` y `#endif`:

```
#ifdef WINDOWS
    ... /* código específico de Windows */
#elif defined(UNIX)
    ... /* código específico de Unix */
#else
    #error "¿ Cuál es tu Sistema Operativo ?"
#endif
```

__________________________________________

### `#error`
Con esta directiva podemos lanzar un error en tiempo de compilación: `#error "Lo siento, tu sistema operativo no está soportado todavía"`.

__________________________________________

### `#pragma`
Esta proporciona un método para que cada compilador ofrezca características específicas del equipo o del sistema operativo a la vez que conservan la compatibilidad total con los lenguajes C y C++.

Por ejemplo, la directiva `#pragma once` está diseñada para asegurar que el el archivo de cabecera que la invoca sea incluido una única vez. También podemos usar `pragma message("Mensaje al compilar este archivo")` para generar un mensaje al compilar el archivo.

#### [Lista de directivas `#pragma`](https://msdn.microsoft.com/es-es/library/d9x1s805.aspx)

__________________________________________

> Fuentes:
> - https://es.wikipedia.org/wiki/Preprocesador_de_C
> - https://es.wikipedia.org/wiki/Pragma_once