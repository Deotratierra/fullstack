## Cython
La ventaja más usual de [Cython](https://es.wikipedia.org/wiki/Cython) es que podemos escribir Python con el tipado estático de C para optimizar considerablemente el código.

En esta introducción vamos a ver un ejemplo de cómo optimizar el código añadiendo un par de variables estáticamente tipadas.

> Instrucciones de compilación: `python3 setup.py build_ext --inplace`

### Flujo de trabajo básico
Para trabajar con Cython, primero creamos un archivo con la extensión `.pyx`. En este archivo escribimos código Cython. En el ejemplo puedes ver que la función se define mediante `cpdef` y las variables se definen antes de la ejecución añadiéndole el tipado al estilo C: `cdef int`.

### El archivo de instalación
En el archivo `setup.py` simplemente incluimos el código `.pyx` como un módulo externo a través de la función `cythonize` de Cython.

Si compilamos veremos que se crea un archivo con la extensión `.c`, entonces ya podemos importar el archivo `.pyx` como si fuera un módulo de Python. Este funciona como una envoltura para el código C generado en la compilación.

Ahora ya podemos ejecutar el archivo `test.py` y ver la abismal diferencia de rendimiento entre el código Python y el mismo en Cython.

#### Ejecutar sin instalacíón
Si tu módulo no requiere de bibliotecas extra o una compilación especial puedes usar el módulo `pyximport` que viene con Cython, con el cual no necesitas de archivo de instalación para importar los archivos `.pyx`.

- [Ver ejemplo](https://github.com/mondeja/fullstack/tree/master/backend/src/022-extensiones_en_c/ejemplos/001-intro/cython/sin_instalar)

>Fuente:
- https://www.youtube.com/watch?v=mXuEoqK4bEc