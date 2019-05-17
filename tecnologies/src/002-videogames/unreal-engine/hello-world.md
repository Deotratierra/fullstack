## Hola Mundo en Unreal Engine 4

Para esta demostración, vamos a imprimir ``¡Hola Mundo en UE4!`` justo cuando comience el juego. Para ello seguimos los siguientes pasos:

1. Creamos un nuevo proyecto usando la plantilla de 3ª persona.
2. Vamos a ``Blueprints`` -> ``Abrir blueprint del nivel``
3. Agregamos el nodo ``BeginPlay``, que es el evento que se ejecuta cuando el actor empieza a jugar.
4. Agregamos el nodo ``Imprimir cadena`` (o ``Print String``), indicamos el texto ``¡Hola Mundo en UE4!``.
5. Conectamos los nodos de forma de la salida de ``BeginPlay`` se conecte con la entrada de ``Print String``.

Si le damos a reproducir, veremos que aparecerá el mensaje en pantalla. Puedes controlar el color y la duración de la impresión, entre otros parámetros, desde el nodo ``Print String``.
