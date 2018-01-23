## Bibliotecas de C desde Python

### Biblioteca estándar
Podemos usar la biblioteca estándar de C con Cython ya que muchas funciones (si no todas) está definidas en el mismo Cython. Desde aquí puedes ver [todas las bibliotecas de C que incluye Cython](https://github.com/cython/cython/tree/master/Cython/Includes).

Tan sólo hemos de importarla tal que `from <biblioteca.cabecero> cimport <función>`.


#### <math.h>
Podemos usar también [el módulo matemático de C](https://github.com/cython/cython/blob/master/Cython/Includes/libc/math.pxd), tal y como se muestra en el ejemplo dentro de este directorio.

__________________________________________________

### CPython API
Cython también tiene un conjunto completo de declaraciones para la API de CPython. Por ejemplo, para comprobar en tiempo de compilación de C con qué versión de CPython fue compilada tu código, puedes ver el primer ejemplo.
