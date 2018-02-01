## El preprocesador de Cython
Cython provee la palabra reservada `DEF` para crear macros, equivalente a [`#define` in C](https://github.com/mondeja/fullstack/tree/master/backend/src/005-entorno_de_ejecucion/c/preprocessor):

```
DEF E = 2.718281828459045
DEF PI = 3.141592653589793

long cdef area_circulo(long R):
    return PI*R**2
```

Las constantes `DEF` se resuelven en tiempo de compilación y están restringidas a tipos simples. Pueden estar hechas de integrales literales, números de coma flotante, cadenas, variables `DEF` predefinidas, llamadas a un conjunto de funciones predefinidas o expresiones involucrando esos tipos y otras variables `DEF`.

Todos los tipos de constantes y funciones que podemos usar en declaraciones `DEF`:

Tipo | Opciones
-----|----------
Constants | `None`, `True`, `False`
Funciones embebidas | `abs`, `chr`, `cmp`, `divmod`,<br>`enumerate`, `hash`, `hex`, `len`,<br>`map`, `max`, `min`, `oct`, `ord`,<br>`pow`, `range`,
`reduce`, `repr`,<br>`round`, `sum`, `xrange`, `zip`
Tipos embebidos | `bool`, `complex`, `dict`, `float`, `int`,<br>`list`, `long`, `slice`, `str`, `tuple`

> Recuerda que el lado derecho de una declaración `DEF` debe en última instancia evaluar a un objeto `int`,  `float` o `str`. El compilador de Cython dará un error si no se cumple esta regla.

#### Condicionales en tiempo de compilación
Para evaluar condicionales en tiempo de compilación usamos las directivas `IF`, `ELIF` y `ELSE`.


### Obtener información del sistema en la compilación
[Al igual que hacemos en C](https://github.com/mondeja/fullstack/tree/master/backend/src/005-entorno_de_ejecucion/c/preprocessor/get_os.md), podemos obtener información sobre el sistema operativo en tiempo de compilación, con la ventaja de usar la biblioteca estándar de Python desde Cython, la cual nos proporciona la información desde todas las plataformas de la misma forma.

Variable `DEF` predefinida | Significado
---------------------------|-----------------------------
`UNAME_SYSNAME`            | Nombre del sistema operativo
`UNAME_RELEASE`            | Lanzamiento del sistema operativo
`UNAME VERSION`            | Versión del sistema operativo
`UNAME_MACHINE`            | Nombre del hardware de la máquina
`UNAME_NODENAME`           | Nombre del nodo en la red

Ejemplo:
```
IF UNAME_SYSNAME == "Windows":
# ...Estamos en Windows...
ELIF UNAME_SYSNAME == "Darwin":
# ...Estamos en Mac...
ELIF UNAME_SYSNAME == "Linux":
# ...Estamos en Linux...
ELSE:
# ...Estamos en otro sistema operativo...
```

