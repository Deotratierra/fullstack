## Make
Los archivos `Makefile` ayudan a escribir comandos de compilación, limpieza, testeo... para los proyectos en C, do una forma simple.

> Instalar Make en Linux: `sudo apt-get install make`

### Sintaxis
- **Variables**: simplemente añadimos el nombre de la variable seguido de un símbolo `=` y su valor -> `NOMBRE_DE_VARIABLE=valor`. Luego podemos reutilizarlas siguiendo la sintáxis `$(NOMBRE_DE_VARIABLE)`.
- **Tareas**: podemos simplificar la compilación (cuando tenemos muchos archivos que dependen unos de otros) estableciendo tareas. Las tareas se ejecutan mediante `make nombre_de_tarea`, excepto la primera tarea definida en el archivo que puede ejecutarse con `make`. Para crear tareas escribimos
```make
nombre_de_tarea: <archivos_de_destino>
    <comando1>
    <comando2>
    ...
```


> Fuentes:
> - https://hernandis.me/2017/03/20/como-hacer-un-makefile.html
> - http://www.calcifer.org/documentos/make/ejemplo.html