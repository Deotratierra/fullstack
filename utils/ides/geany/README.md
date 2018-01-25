## Geany

#### [Instalación por sistema operativo](https://github.com/mondeja/fullstack/tree/master/utils/ides/geany/install.md)

### Ejecutar archivos en la terminal de Geany:
Si tu versión del lenguaje o el lenguaje mismo no es aceptado por la terminal:

- Ve a Construir -> Establecer comandos de construcción y en el apartado de "Ejecutar comandos" escribes, por ejemplo: `node "%f"`.
- `node` es el comando para ejecutar el archivo (en este caso NodeJS) y  `"%f"` es la expresión regular que hace referencia al archivo que estamos ejecutando.
_______________________

##### Compilar en C++
Comando de compilación para el último estándar:
`g++ "%f" -std=c++14 -o "%e"`

>`"%e"` se refiere al ejectuable, que tomará el mismo nombre que el archivo.
