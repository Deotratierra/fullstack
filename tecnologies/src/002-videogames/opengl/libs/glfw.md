### GLFW
Es una biblioteca escrita en C destinada específicamente a OpenGL que provee las necesidades mínimas requeridaspara renderizar en la pantalla. Nos permite crear un contexto OpenGL, definir los parámetros de la ventana y manejar las entradas del usuario, que es todo lo que necesitamos.

- [Repositorio Github](https://github.com/glfw/glfw)
- [Documentación](https://www.glfw.org/docs/latest/)

#### Compilación

- [Guía oficial](https://www.glfw.org/docs/latest/compile.html)

##### Linux y X11
Antes de empezar necesitamos tener los paquetes de X11 instalados en nuestro sistema. Con el siguiente comando los instalamos si no se encuentran ya:

```bash
sudo dpkg -s xorg-dev || sudo apt-get install xorg-dev -y \
	|| sudo dpkg -s doxygen || sudo apt-get install doxygen -y
```

Una vez que tenemos las dependencias instaladas, debemos obtener el código fuente:

```bash
git clone https://github.com/glfw/glfw.git
```

Ahora podemos hacer dos tipos de compilación. Podemos compilar en el mismo directorio de github que acabamos de descargar o hacerlo en otro diferente. Las ventajas principales de hacerlo en uno diferente son:
- Puedes utilizar la misma compilación para diferentes entornos de desarrollo.
- Se aprende más, ya que ves la estructura de directorios que generas y tienes más control.

Así que vamos a generar los archivos de compilación en otro directorio. Desde el mismo directorio que hemos descargado la biblioteca, ejecutamos:

```bash
mkdir glfw-build
cd glfw-build
cmake ../glfw
```

> Puedes consultar las opciones de compilación desde [aquí](https://www.glfw.org/docs/latest/compile_guide.html#compile_compile). 

Finalmente, vamos a compilar la biblioteca:

```bash
make && sudo make install
```

> Puedes ver donde se incluyen las cabeceras en la salida del último comando. Por ejemplo, en mi sistema han sido ubicadas en `/usr/local/include/GLFW/`. La cabecera que incluiremos al compilar nuestra aplicación será el archivo `glfw3.h`, con la línea `#include <GLFW\glfw3.h>`.

