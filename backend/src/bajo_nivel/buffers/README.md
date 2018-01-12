## Búffers de datos
Un buffer es una memoria en la que se almacenan los datos de manera temporal para ser procesados. Se utiliza cuando los datos llegan a mayor velocidad de los que podemos procesar, o cuando llegan de manera irregular o esporádica. Los sistemas de entrada de teclado o la reproducción de vídeos en internet utilizan buffers de datos.

### Origen de la palabra
La palabra "buffer" en inglés significa amortiguador, regulador, tope...

Desde la época de los vaqueros y los inicios de la aviación los encargados de los sistemas de reparto y entregas descubrieron que podían ahorrarse mucho tiempo si en lugar de hacer que los mensajeros se detuvieran para entregar la mercancía colocaban uno de esos grandes colchones donde podían dejar caer los paquetes sin detenerse. De ese modo no era necesario dejar a alguien en la puerta esperando al mensajero y los empleados podían ir con toda calma y a una hora predeterminada a revisar estos buffers para ver si había llegado algún paquete. Un sistema muy parecido se utilizó en algunas fábricas y bodegas de muchos pisos en los que dejaban caer los productos por una especie de pozo vertical en cuyo fondo había un cojín y una pequeña puerta por la que se podían entregar los productos. En la actualidad las máquinas expendedoras automáticas usan buffers en los que dejan caer tanto el cambio en monedas como la mercancía de modo que el cliente no tenga que poner la mano y esperar a que estos caigan. Otro ejemplo mas sencillo es el viejo buzón de correos en el que el cartero puede dejar documentos y los habitantes pueden ir a revisarlos al regresar a su casa.

### Problemas en los buffers
Cuando queremos obtener datos y el buffer está vacío se denomina **underflow** y cuando queremos insertar datos pero el buffer está lleno se denomina **overflow**.

El Underflow es mas peligroso de lo que suena en ciertas aplicaciones como por ejemplo la grabación de datos en medios físicos como los discos. Si ocurre un buffer underflow la pieza puede quedar arruinada o en el caso de audio y video en tiempo real la comunicación puede presentar cortes. Es por eso que cada que se va a tener acceso al buffer ya sea para leer o escribir datos en él es necesario verificar que no van a ocurrir ninguna de estas dos condiciones. Pues si no se hace esta prueba no solo puede haber pérdidas de datos entrantes o cortes en el flujo de información sino que en casos de buffers muy mal diseñados puede haber problemas de sobreescritura que acaben por afectar otros datos importantes del programa y en casos muy dramáticos causar un fallo de protección de memoria o una caida completa del sistema.

### Consejos al crear buffers
Lo recomendable es que los buffers siempre deben tener un tamaño que sea una potencia de 2.
