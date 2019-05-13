## Jerarquía de clases en Qt

Qt usa la herencia, especialmente en el módulo de Widgets. El siguiente gráfico muestra algunas de esas herencias:

![Algunas herencias de clases en Qt](class-hierarchy.jpg)

``QObject`` es la clase más básica en Qt. La mayoría de las clases en Qt heredan de esta. ``QObject`` provee algunas capacidades poderosas como:

- **Nombre de objeto**: puedes establecerle un nombre, como cadena a cualquier objeto y buscar objetos por nombres.
- **Sistema de parentesco**: puedes crear elementos que heredan de otros, como por ejemplo ventanas que heredan de la clase ``QWidget``.
- **Señales y slots**: Puedes comunicar el objeto con otros por medio de señales y reaccionar a eventos en cualquier objeto.
- **Propiedades**: los objetos tienen propiedades que funcionan como *getters* y *setters*. Si una propiedad, pongamos por ejemplo, tiene el nombre ``text``, podemos establecer un nuevo texto con el método ``object.setText("Nuevo texto")`` y obtener el valor de la propiedad con ``object.getText()``.

Todos los widgets (un widget es cualquier elemento de la interfaz) pueden responder a eventos y heredan de la clase ``QObject``. El widget más básico es el ``QWidget``, que contiene la mayoría de propiedades usadas para describir a una ventana, como posición (``position``) y tamaño (``size``), cursor del mouse, tooltips, etc. Esta herencia está diseñada para facilitar la adminsitración de propiedades.