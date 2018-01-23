## Bibliotecas de C desde Python

### Biblioteca estándar
Podemos usar la biblioteca estándar de C con Cython ya que muchas funciones (si no todas) está definidas en el mismo Cython. Desde aquí puedes ver [todas las bibliotecas de C que incluye Cython](https://github.com/cython/cython/tree/master/Cython/Includes).

Tan sólo hemos de importarla tal que `from <biblioteca.cabecero> cimport <función>`.


#### <math.h>
Podemos usar también [el módulo matemático de C](https://github.com/cython/cython/blob/master/Cython/Includes/libc/math.pxd), tal y como se muestra en el ejemplo dentro de este directorio.

__________________________________________________

### CPython API
Cython también tiene un conjunto completo de declaraciones para la API de CPython. Por ejemplo, para comprobar en tiempo de compilación de C con qué versión de CPython fue compilada tu código, puedes ver el primer ejemplo.

__________________________________________________

### Enlazado dinámico
Para enlazar dinámicamente bibliotecas al compilar lo hacemos desde el archivo `setup.py` tal y como puedes ver en este directorio.

### Declaraciones externas
Si quieres acceder a código C para el cual Cython no provee una biblioteca lista para usar, debes declararlo en un archivo de extensión `.pxd`. Este tipo de archivos funcionan como los archivos de cabecero en C (`.h`) y C++ (`.hpp`). Usando `cimport` desde un archivo `pyx` a un archivo `pxd` podemos importar su contenido.

Es en los archivos `pxd` donde se realiza la el puente para que el código C pueda ser llamado desde Python. En ellos usamos las sentencias `cdef extern from <cabecero.h>` para declarar que estamos externalizando código C a nuestro archivo.

Luego debemos crear una envoltura para nuestras funciones en los archivos `pyx`, los cuales sí pueden ser directamente importados desde Python.