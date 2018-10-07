## Make
Los archivos `Makefile` ayudan a escribir comandos de compilación, limpieza, testeo... para los proyectos en C, do una forma simple. Aunque también pueden servir para cualquier tipo de tareas del sistema ya que proveen comandos de consola más cortos para un conjunto de ellos.

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

#### Conflictos de nombres
Imagina que tienes un archivo `Makefile` así:
```
all:
    mkdir clean

clean:
    rm -rf all
```

Make podría confundirse ya que los objetivos de algunos comandos apuntan a un archivo que también es un comando del `Makefile`.

Para eliminar estos conflictos usamos el objetivo `.PHONY`. El archivo quedaría así:
```
.PHONY: all clean

all:
    mkdir clean

clean:
    rm -Rf all
```

Con la directiva `.PHONY` indicamos a Make que los comandos que le pasamos a la directiva son comandos del `Makefile`, así que es buena práctica comenzar el `Makefile` definiéndola. Incluso en proyectos largos, es mejor especificar ``.PHONY: <nombre_de_tarea>`` delante de cada una para no perderse entre tantas.

_______________________________________


> Fuentes:
> - https://hernandis.me/2017/03/20/como-hacer-un-makefile.html
> - http://www.calcifer.org/documentos/make/ejemplo.html
> - https://stackoverflow.com/questions/2145590/what-is-the-purpose-of-phony-in-a-makefile