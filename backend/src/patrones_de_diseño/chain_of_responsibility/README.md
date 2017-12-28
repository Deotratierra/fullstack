## Cadena de responsabilidad
Es un patrón de comportamiento que evita acoplar el emisor de una petición a su receptor dando a más de un objeto la posibilidad de responder a una petición. Para ello, se encadenan los receptores y pasa la petición a través de la cadena hasta que esta es procesada por algún objeto.

### Ejemplos de uso
#### Botón de ayuda desacoplado
Imagina un botón de ayuda <kbd>?</kbd> en una interfaz gráfica. El usuario puede solicitar la ayuda en cualquier parte de la interfaz y la ayuda depende de la parte de la interfaz donde se haya solicitado, así como de su contexto. Si no existe información de ayuda específica para esa parte, el sistema debería mostrar un mensaje de ayuda más general sobre el contexto en el que se encuentra. El problema es que el botón de ayuda no conoce explícitamente al objeto que inicializa la petición.

Usando la cadena de responsabilidad, todos los objetos comparten una clase `ManejadorDeAyuda()` que va reenviando la petición a través de todos ellos hasta que una subclase tenga implementada una función que gestione la petición de ayuda. Las subclases pueden redefinir esta operación para proporcionar ayuda en determinadas circunstancias; en caso contrario usarán la implementación predeterminada para reenviar la petición.

### Aplicabilidad
Este patrón requiere un amplio coste de memoria, ya que va guardando todos los objetos por los que pasa y, en muchas situaciones, hay que valorar otra posible forma de solucionar el problema sin un coste computacional tan alto.

Este patrón debe usarse cuando:
- Hay más de un objeto que puede manejar una petición, y el manejador no se conoce a priori, si no que debería determinarse automáticamente.
- Se quiere enviar una petición a un objeto sin especificar explícitamente el receptor.
- El conjunto de objetos que pueden tratar una petición debería ser especificado dinámicamente.

>Fuentes:
- https://es.wikipedia.org/wiki/Cadena_de_responsabilidad
- https://sourcemaking.com/design_patterns/chain_of_responsibility
