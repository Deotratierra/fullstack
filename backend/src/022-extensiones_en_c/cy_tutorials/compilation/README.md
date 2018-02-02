## Compilación en Cython
El código Cython se compila en dos pasos:
1. Cython compila un archivo `.pyx` a un archivo `.c`.
2. Un compilador de C compila el archivo `.c` a un archivo `.so` (Unix) o `.pyd` (Windows).

### Compilando módulos directamente
Podemos compilar un módulo directamente desde línea de comandos ejecutando `cythonize modulo.pyx`. Este comando acepta [patrones glob](https://github.com/mondeja/fullstack/tree/master/backend/src/003-archivos/globs) como `**/*.pyx`.

Podemos pasar diferentes opciones al compilador, para verlas todas ejecuta `cythonize -h`. Aquí hay una lista con las más comunes:

- `-i`: Sinónimo de `--inplace`. Construye los módulos usando `distutils` reemplazándolos por los ya instalados.
- `-b`: Sinónimo de `--build`. Construye los módulos usando `distutils`.
- `-j <N>`: Construye los módulos en `N` número de procesos paralelos.
- `-f`: Fuerza a la recompilación.
- `-a`: Genera una página HTML anotada para los archivos del código fuente. Esta página es especialmente útil para ver la correspondencia entre el código Cython y el C compilado.

