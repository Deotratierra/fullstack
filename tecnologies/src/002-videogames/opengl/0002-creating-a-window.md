## Creando una ventana

Para crear gráficos, lo primero que necesitamos es crear un contexto OpenGL y una ventan para dibujar en ella. Sin embargo, esa operaración depende del sistema operativo y OpenGL intenta a propósito abstraerse de esas operaciones. Esos significa que tenemos que crear una ventana, definir un contexto y manejar las entradas del usuario por nosotros mismos.

Por suerte, hay unas cuantas bibliotecas que proveen estas funcionalidades, algunas dirigidas a OpenGL. Esas bibliotecas nos salvan el trabajo específico de cada sistema operativo y nos dan una ventana y un contexto OpenGL en el que renderizar. Algunas de las más populares son [GLUT (The OpenGL Utility Toolkit)](https://www.opengl.org/resources/libraries/glut/), [SDL (Simple DirectMedia Layer)](https://www.libsdl.org/), [SFML (Simple and Fast Multimedia Library)](https://www.sfml-dev.org/) y [GLFW](https://www.glfw.org/).

### Tutoriales de bibliotecas OpenGL
- [GLFW](https://github.com/mondeja/fullstack/blob/master/tecnologies/src/002-videogames/opengl/libs/glfw.md)


#### Fuentes:
- [LearnOpenGL - Creating a window](https://learnopengl.com/Getting-started/Creating-a-window)