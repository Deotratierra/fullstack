## Tipado en Cython
En Cython, las variables no tipadas se comportan exactament igual que las variables de Python. Para tipar estáticamente en Cython debemos usar la palabra reservada `cdef` seguida del tipo y el nombre de la variable. Por ejemplo:

```
cdef int i
cdef long j
cdef float k
```

Como en C, también podemos declarar varias variables a la vez además de proveer valores inciales:
```
cdef int i, j, k
cdef double pi = 3.1416
```

Otra manera de declarar variables es indentarlas todas en un bloque `cdef` tal que:
```
cdef:
   int i, j, k
   float a, b = 45.4
```

> La palabra clave reservada en C `static` se usa para declarar variables cuya vida se extiende a la vida completa del programa. **No es una palabra clave válida en Cython**.

Podemos declarar cualquier tipo de variable que soporte C. La siguiente tabla muestra algunos ejemplos para las expresiones en C más comunes:

Tipo de C                                | Cython `cdef` statement
-----------------------------------------|------------------------------------
Pointers                                 | `cdef int *p`<br> `cdef void **buf`
Arrays asignados en forma de pila        | `cdef int arr[10]`<br>`cdef double points[20][30]`
Tipos definidos con `typedef`            | `cdef size_t len`
Tipos compuestos (estructuras y uniones) | `cdef tm time_struct`<br>`cdef int_short_union_t hi_lo_bytes`
Punteros de funciones                    | `cdef void (*f)(int, double)`

_________________________

### Inferencia de tipos C en Cython
Podemos escribir funciones con variables de C sin definir la expresión `cdef` si importamos cython con `cimport cython` y decoramos la función con `@cython.infer_types(True)`.

Esto hace que Cython tipe las variables automáticamente, convirtiendo las variables a simple vista puramente pythónicas en variables de C. [Puedes ver un ejemplo en este mismo directorio](https://github.com/mondeja/fullstack/tree/master/backend/src/022-extensiones_en_c/cy_tutorials/types/inferencia.pyx).

_________________________

### Conversión entre tipado estático y dinámico
Cython permite asignaciones entre variables estática y dinámicamente tipadas. Esta mezcla de tipada es una característica muy poderosa que usaremos en numoerosas ocasiones: nos permite usar objetos dinámicos de Python para la mayoría de nuestro código y convertirlos fácilmente en variables estáticamente tipadas de C análogas para las partes de nuestro código en las que el rendimiento es importante. Por ejemplo:

```
cdef int a, b, c
# ... Diferentes cálculos usando las variables anteriores ...
tuple_of_ints = (a, b, c)
```

Este ejemplo funciona porque existe una obvia correspondencia entre los enteros de C y los de Python, así que Python puede transformarlo automáticamente. Este ejemplo no funcionaría si las variables fueran, por ejemplo, punteros de C.

#### Correspondencia de tipos entre C y Python
Tipo de Python    |  Tipo de C
------------------|-------------------
`bool`            | `bint`
`int`<br>`long`   | `unsigned char`<br>`unsigned short`<br>`unsigned int`<br>`unsigned long`<br>`unsigned long long`
`float`           | `float`<br>`double`<br>`long double`
`complex`         | `float complex`<br>`double complex`
`bytes`<br>`str`<br>`unicode`| `char *`<br>`std::string` (C++)
`dict`            | `struct`

##### bint
El tipo `bint` entero booleano es un `int` a nivel de C que es convertido de y hacia un `bool` de Python.

##### Conversiones entre tipos integrales y desbordamiento
Cuando convierte tipos integrales de Python a C, Cython genera código que comproba el desbordamiento. Si el tipo de C no puede representar al entero de Python, se levanta el error en tiempo de ejecución `OverflowError`.

##### Conversiones entre tipos de punto flotante
Un `float` de Python es almacenado como un `double` de C. La conversión de un `float` de Python en un `float` de C puede ser truncada a `0.0`, a `∞` o a `-∞`, de acuerdo a las reglas de conversión del [estándar IEEE para aritmética en coma flotante 754](https://es.wikipedia.org/wiki/IEEE_coma_flotante).

##### complex
El tipo `complex` de Python es alamacenado en C commo una estructua de dos `double`.

Cython posee los tipos a nivel de C `float complex` y `double complex`, que corresponden al tipo `complex` de Python. Estos tienen la misma interfaz que el `complex` de Python, pero usando operaciones eficientes a nivel C, los cuales incluyen los atributos `real` e `imag` para acceder a los componentes real e imaginario, el método `conjugate()` para crear la conjugación compleja de un número y operaciones eficientes para la suma, resta, multiplicación y división.

El tipo a nivel C `complex` es compatible con el tipo `_Complex` de [la clase `std::complex`](http://en.cppreference.com/w/cpp/numeric/complex) de la biblioteca estándar C99 de C++.

##### bytes
El tipo de Python `bytes` se convierte automáticamente a `char *` (C) o a `std::string` (C++).

##### str y unicode
Las directivas de compilador `c_string_type` y `c_string_encoding` necesitan ser establecidas para permitir a los tipos `str` o `unicode` ser convertidos hacia y desde `char *` o `std::string`.

_________________________

### Variables estáticas con los tipos de Python
Es posible usar `cdef` para declarar variables estáticas con un tipo de Python. Podemos hacerlo para los tipos nativos de Python como `list`, `tuple` y `dict`; extensiones de tipos como los arrays de Numpy; y muchos otros...

No todos los tipos de Python pueden ser declarados estáticamente. Necesitan estar implementados en C y Cython debe tener acceso a su declaración. Los tipos nativos de Python cumplen esas características y su declaración es tan simple como:

```
cdef list particulas, particulas_modificadas
cdef dict nombres_desde_particulas
cdef str pname
cdef set particulas_unicas
```

Las variables en el ejemplo anterior son objetos de Python completos. Cython las declara como punteros de C apuntando a estructuras embebidas en Python. Pueden ser usadas como variables de Python ordinarias, pero están constreñidas a su tipo declarado:

```
# ...Inicialización del ejemplo anterior...
particulas = list(nombres_desde_particulas.keys())
otras_particulas = particles  # Podemos declarar de ellas variables dinámicas
del otras_particulas[0]
```

Aquí eliminar el elemento `0` por medio de la variable `otras_particulas` lo eliminará de la lista `particulas`, ya que está haciendo referencia a`**la misma lista**.

#### Lista de tipos embebidos de Python soportados por Cython
- `type`, `object`
- `bool`
- `complex`
- `basestring`, `str`, `unicode`, `bytes`, `bytearray`
- `list`, `tuple`, `dict`, `set`, `frozenset`
- `array`
- `slice`
- `date`, `time`, `datetime`, `timedelta`, `tzinfo`

_________________________

> Fuentes:
> - Kurt W. Smith - Cython, una guía para programadores de Python (Editorial O'Reilly)