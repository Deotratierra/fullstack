## Ctypes
Es parte de la biblioteca estándar de Python y nos permite usar los tipos de C en Python, así como cargar bibliotecas de enlace dinámico ([`so` en Linux](http://www.lopeztorrijos.com/tutoriales/linux/gestionar-software/bibliotecas-compartidas) y [`.dll` en Windows](https://es.wikipedia.org/wiki/Biblioteca_de_enlace_din%C3%A1mico)).

### Envolver código C en Python
Como puedes ver en el ejemplo de este directorio, podemos crear código C y envolverlo desde Python. Esto requiere de la compilación de una biblioteca como dinámica, que puede hacerse en gcc para Linux con el comando `gcc -Wall -O3 -shared lib_c.c -o lib_c.so`. No debemos olvidar que debemos agregar el directorio en el que se encuentra la biblioteca a la variable `LD_LIBRARY_PATH`, así que desde su interior ejecutamos `export LD_LIBRARY_PATH=$PWD`.

> Fuentes:
> - https://stackoverflow.com/questions/1099981/why-cant-python-find-shared-objects-that-are-in-directories-in-sys-path
> - http://icaza23.blogspot.com.es/2013/07/acceso-una-dll-con-python.html
> - http://www.dreamincode.net/forums/topic/252650-making-importing-and-using-a-c-library-in-python-linux-version/