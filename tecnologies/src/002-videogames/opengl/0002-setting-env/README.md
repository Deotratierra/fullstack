## Preparando el entorno

Para crear gráficos, lo primero que necesitamos es crear un contexto OpenGL y una ventan para dibujar en ella. Sin embargo, esa operaración depende del sistema operativo y OpenGL intenta a propósito abstraerse de esas operaciones. Esos significa que tenemos que crear una ventana, definir un contexto y manejar las entradas del usuario por nosotros mismos.

Por suerte, hay unas cuantas bibliotecas que proveen estas funcionalidades, algunas dirigidas a OpenGL. Esas bibliotecas nos salvan el trabajo específico de cada sistema operativo y nos dan una ventana y un contexto OpenGL en el que renderizar. Algunas de las más populares son [GLUT (The OpenGL Utility Toolkit)](https://www.opengl.org/resources/libraries/glut/), [SDL (Simple DirectMedia Layer)](https://www.libsdl.org/), [SFML (Simple and Fast Multimedia Library)](https://www.sfml-dev.org/) y [GLFW](https://www.glfw.org/).

### Bibliotecas OpenGL
- [GLFW](https://github.com/mondeja/fullstack/blob/master/tecnologies/src/002-videogames/opengl/libs/glfw.md)

### GLAD
Dado que OpenGL es un estándar / especificación, depende del fabricante del controlador implementar la especificación en un controlador compatible con una tarjeta gráfica específica. Dado que hay muchas versiones diferentes de controladores OpenGL, la localización de la mayoría de funciones no se conoce en tiempo de compilación y necesita ser consultada en tiempo de ejecución. Es entonces tarea del desarrollador obtener la localización de las funciones que necesita y almacenarlas en punteros a las funciones para usarlos más tarde. Obtener las localizaciones es una tarea dependiente del sistema operativo.

[GLAD](https://github.com/Dav1dde/glad) es una biblioteca de código abierto que administra todo este engorroso trabajo. GLAD tiene una configuración de instalación algo diferente a la mayoría de bibliotecas de código abierto. Usando un [servicio web](https://glad.dav1d.de/) podemos indicarle a GLAD para que versión de OpenGL vamos a desarrollar y carga todas las funciones relevantes de OpenGL de acuerdo a esa versión.

Para ello vamos a ir al servicio web y generaremos los archivos indicando las siguientes opciones:

- Language: `C/C++`
- Specification: `OpenGL`
- Profile: `Core`
- API -> gl: `Version 4.6`

Marcamos la casilla `Generate a Loader` y hacemos click en el botón generar.

> También podemos abrir el servicio con estas opciones marcadas accediendo desde [este enlace](http://glad.dav1d.de/#profile=core&specification=gl&api=gl%3D4.6&api=gles1%3Dnone&api=gles2%3Dnone&api=glsc2%3Dnone&language=c&loader=on)

Descargamos el zip, lo descomprimimos y movemos los directorios `glad/` y `KHR/` ubicados dentro del directorio `include/` a la carpeta `include/` del sistema (en mi caso, en Debian, `/usr/include`). Comprueba antes que no existen estos directorios ya creados y:

```bash
sudo cp -r glad/include/glad /usr/include/glad
sudo cp -r glad/include/KHR /usr/include/KHR
```

Para incluir GLAD en nuestra compilación, podemos incluir el header `glad.h`:

```c
#include <glad/glad.h> 
```

> Como paso final, podemos comprobar si tenemos correctamente configurado el entorno para trabajar con el siguiente comando (desde este directorio):

```bash
g++ -lGL -lX11 -lpthread -lXrandr -lXi -ldl test-glad-glfw-compile.cpp \
	-o test-glad-glfw-compile && \
	./test-glad-glfw-compile && \
	rm test-glad-glfw-compile
```


#### Fuentes:
- [LearnOpenGL - Creating a window](https://learnopengl.com/Getting-started/Creating-a-window)