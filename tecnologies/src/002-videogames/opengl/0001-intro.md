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
OpenGL soporta extensiones. Una vez que una compañía deesarrolla una nueva técnica una gran optimización en el renderizado, normalmente se encuentra en una extensión implementada en los controladores. Si el hardware en el que se ejecuta una aplicación soporta una extensión el desarrollador puede usar la funcionalidad provista por la extensión para un dibujo más avanzado o eficiente. De esta forma, el desarrollador puede seguir usando esas nuevas técnicas de renderizado sin tener que esperar a que OpenGL incluya estas funcionalidades en futuras versiones, simplemente compruba si la es soportada por la tarjeta gráfica. Usualmente, cuando una extensión es popular o muy útil, se vuelve parte de las versiones futuras de OpenGL.

```c
if(GL_ARB_extension_name)
{
    // Haz estas cosas geniales, ya que el hardware lo soporta
}
else
{
    // La extensión no está soportada, hazlo de la forma antigua
}
```

## Máquina de estados
OpenGL es por sí mismo una gran [**máquina de estados**](https://es.wikipedia.org/wiki/M%C3%A1quina_de_estados). El estado actual de la ejecución de OpenGL es comúnmente denominado el **contexto** OpenGL. Cuando usamos OpenGL, a menudo cambiamos su estado definiendo algunas opciones, manipulando algunos buffers y renderizando usando el contexto actual.

Cuando trabajamos con OpenGL nos encontramos con muchas funciones de cambio de estado que alteran el contexto y otras funciones de uso de estado, que realizan operaciones basadas en el estado actual de OpenGL. Mientras tengas en cuenta que OpenGL es básicamente una gran máquina de estados, la mayoría de sus funcionalidades cobrarán sentido.

## Objetos
Las bibliotecas OpenGL están escritas en C y permiten muchas derivaciones de las mismas en otros lenguajes, pero en su núcleo se mantiene como una biblioteca C. Ya que la mayoría de construcciones en C no se pueden traducir bien a otros lenguajes de más alto nivel, OpenGL se desarrolló tomando en cuenta bastantes abstracciones. Una de ellas son los *objetos* en OpenGL.

Un objeto en OpenGL es una colección de opciones que representan un subconjunto de un estado de OpenGL. Por ejemplo, podríamos tener un objeto que representara la configuración de la ventana de dibujo; podríamos entonces definir su tamaño, cuantos colores soporta, y así sucesivamente. Uno podría visualizar un objeto como un `struct` de C:

```c
struct object_name {
    float  option1;
    int    option2;
    char[] name;
};
```

Donde quiera que usemos objetos veremos algo parecido a esto (con el objeto del contexto OpenGL visualizado como un gran `struct`):

```c
// El estado de OpenGL
struct OpenGL_Context {
  	...
  	object_name* object_Window_Target;
  	...  	
};

```

```c
// Creamos el objeto
unsigned int objectId = 0;
glGenObject(1, &objectId);
// Enlazamos el objeto un contexto
glBindObject(GL_WINDOW_TARGET, objectId);
// Definimos opciones del objeto enlazado actualmente a GL_WINDOW_TARGET
glSetObjectOption(GL_WINDOW_TARGET, GL_OPTION_WINDOW_WIDTH, 800);
glSetObjectOption(GL_WINDOW_TARGET, GL_OPTION_WINDOW_HEIGHT, 600);
// Volvemos a establecer el contexto a su estado original
glBindObject(GL_WINDOW_TARGET, 0);

```

Esta pieza de código es un flujo de trabajo que verás frecuentemente al trabajar con OpenGL. Primero creamos un objetos y almacenamos una referencia al mismo como un identificador (los datos reales del objeto son almacenados entre bastidores). Entonces enlazamos el objeto a la ubicación donde se encuentra el contexto (el objeto de la ubicación de la ventana destino del ejemplo está definida como `GL_WINDOW_TARGET`). Lo siguiente que hacemos es establcer las opciones de la ventana y finalmente desenlazamos el objeto definiendo el identificador del objeto de la ventana destino a `0`. Las opciones establecidas que establecimos son almacenadas en el objeto referenciado por la variable `objectId` y restauradas cuando volvamos a enlazarlo a `GL_WINDOW_TARGET`.

Lo mejor de usar estos objetos es que podemos definir más de un objeto en nuestra aplicación, establecer sus opciones y cuando empecemos una operación que haga uso de un estado de OpenGL, enlazamos el objeto con la configuración definida. Por ejemplo, hay objetos que actuan como contenedores de objetos para datos de modelos 3D (una casa o un personaje) y cuando queremos dibujar uno de ellos, enlazamos el objeto que contiene los datos del modelo que queremos dibujar. Tener varios objetos nos permite especificar muchos modelos y cuando queremos dibujar uno de ellos, simplemente enlazamos el objeto correspondiente antes de dibujarlo sin tener que definir todas sus opciones de nuevo.

#### Fuentes:
- [LearnOpenGL - Getting Started](https://learnopengl.com/Getting-started/OpenGL)
- [StackOverflow - What does inmediate mode mean in OpenGL?](https://stackoverflow.com/questions/6733934/what-does-immediate-mode-mean-in-opengl)
