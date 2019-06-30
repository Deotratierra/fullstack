## ¿Qué es OpenGL?

OpenGL, a primera vista, puede parecer una API que provee un gran conjunto de funciones que podemos usar para manipular gŕaficos e imágenes. Sin embargo, OpenGL por sí mismo no es una API, sino una **especificación**, desarrollada y mantenida por el [Grupo Khronos](https://www.khronos.org/).

La especificación OpenGL define exactamente cual debe ser el resultado y la salida de cada función y cómo debe funcionar. Luego, depende de los desarrolladores que implementan la especificación encontrar una solución de cómo implementarla apropiadamente. Debido a que las diferentes versiones de la especificación OpenGL no nos aportan detalles de implementación, las versiones de OpenGL desarrolladas actualmente permiten diferentes implementaciones.

Los desarrolladores de las bibliotecas OpenGL trabajan usualmente para empresas de producción de tarjetas gráficas. Cada tarjeta gráfica que compras soporta versiones específicas de OpenGL, que son las versiones de OpenGL desarrolladas explícitamente para esa serie de tarjetas. Esto significa que siempre que OpenGL se comporte de manera inadecuada, es debido a fallos de las empresas que producen las tarjetas gráficas (o quien sea que esté desarrollando/manteniendo la biblioteca).

> Para encontrar la última versión de la especificación de OpenGL, simplemente googlea `opengl spec` y busca la última versión.

## Modo *Core-profile* vs modo *inmediato*

### Modo *inmediato*
Antiguamente, usar OpenGl significaba desarrollar en *modo inmediato* (inmediate mode), a veces referido como *fixed function pipeline*. Este era un método fácil para dibujar gráficos, pero no era nada eficiente. Seguramente, si quieres aprender a usar esta biblioteca en algún lenguaje, encontrarás el típico ejemplo de modo inmediato usando funciones como `glBegin`, `glEnd` con un `glVertex` por ahí en medio. Este modo quedó obsoleto desde la versión 3.3 de OpenGL. 

La razón principal por la que el modo inmediato no es nada óptimo es que **enlaza directamente el flujo de ejecución de la tarjeta gráfica con el flujo de tu programa**. El driver no puede decirle a la GPU que que empiece a renderizar antes de la llamada a `glEnd` porque no sabe cuando terminarás de enviarle datos (hasta la llegada a `glEnd`).

### Modo *Core-profile*
Cuando usamos el modo *core-profile*, OpenGL nos obliga a usar prácticas modernas. Si en cualquier parte del código intentamos llamar a una de las funciones obsoletas, OpenGL levanta un error y para de dibujar. La ventaja de aprender la aproximación moderna es que es muy flexible y eficiente, pero desafortunadamente es más dificil de aprender, ya que es una forma de programar de más bajo nivel.

Como el modo *Core-profile* se añadió a partir de la versión 3.3 de OpenGL, debes entender que las versiones posteriores sólo añaden funciones de utilidad, así que si buscas tutoriales para aprender, asegúrate que parten, al menos, de esta versión.

> Cuando usas funciones añadidas en la versión más reciente de OpenGL (las cuales no tienen compatibilidad hacia atrás), sólo las tarjetas gráficas más modernas serán capaces de ejecutar tu aplicación. Por esto, usualmente la mayoría de desarrolladores eligen versiones menores de OpenGL y habilitan opcionalmente funcionalidades de versiones superiores.

## Extensiones


> Fuentes:
    - [LearnOpenGl - Getting Started](https://learnopengl.com/Getting-started/OpenGL)
    - [StackOverflow - What does inmediate mode mean in OpenGL?](https://stackoverflow.com/questions/6733934/what-does-immediate-mode-mean-in-opengl)