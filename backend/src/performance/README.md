## Tests de rendimiento entre lenguajes

> Entra a un directorio y ejecuta `bash test.sh` para lanzar la comparación de rendimiento para ese ejemplo. La suite puede controlarse estableciendo las variables:
- `ITER`: Número de veces que se repite la llamada.
- `VERBOSE`: Muestra avisos de ejecución.
- `DEBUG`: Añade advertencias de debug.
- `LANGS_OFF`: Admite una cadena de extensiones de archivo separados por comas. Los archivos con esa extensión no serán ejecutados.
- Si preparas tu script para parsarle un argumento, puedes pasar un array desde el archivo `test.sh` (mira los ejemplos).

### `performance.sh`

#### Lenguajes soportados:
| Nombre     | Extensión | Compilación | Ejecución | Limpieza  |
|:----------:|:---------:|:-----------:|:---------:|:---------:|
| Python     |    py     |             | python3...|           |
| Golang     |    go     | go build ...|  ./...    |  rm ...   |
| Cython     |    pyx    |     \*1     | python3...|  rm ...   |
| Javascript |    js     |             | node ...  |           |
| Ruby       |    rb     |             | ruby ...  |           |
|     C      |     c     |   gcc ...   |  ./...    |  rm ...   |
|     C++    |    cpp    |   g++ ...   |  ./...    |  rm ...   |
|   Bash     |     sh    |             | bash ...  |           |

\*1. Con Cython hay que crear un archivo llamado cy_<nombre_de_tu_archivo> desde el cual ejecutamos la biblioteca C que se compila automáticamente. El script de instalación se encuentra en la carpeta `setup/pyx`.

> Todos los resultados de los tests se guardan en el archivo `.json`.

____________________________________________

### Ejemplos de tests de performance entre lenguajes de programación

- [Fibonacci](https://github.com/mondeja/fullstack/tree/master/backend/src/performance/001-fibonacci) (c, cpp, py, cy, js, rb, go, sh)
- [Reemplazo de subcadena](https://github.com/mondeja/fullstack/tree/master/backend/src/performance/001-fibonacci) (c, cpp, py, js, rb, go, sh)
