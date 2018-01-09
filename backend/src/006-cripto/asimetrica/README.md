## Criptografía asimétrica
También llamada criptografía de clave pública o criptografía de dos claves1​, es el método criptográfico que usa un par de claves para el envío de mensajes. Las dos claves pertenecen a la misma persona que ha enviado el mensaje. Una clave es pública y se puede entregar a cualquier persona, la otra clave es privada y el propietario debe guardarla de modo que nadie tenga acceso a ella. Además, los métodos criptográficos garantizan que esa pareja de claves sólo se puede generar una vez, de modo que se puede asumir que no es posible que dos personas hayan obtenido casualmente la misma pareja de claves.

Imagina que dos personas (`A` y `B`) quieren intercambiar información de forma segura. Estas dos personas utilizan dos claves cada una, una pública y otra privada, las cuales llamaremos `A pública`, `B privada`...
Para conseguir el intercambio seguro deben seguir los siguientes pasos:
1. `A` le envía a `B` la `A pública` y `B` le envía a `A` la `B pública`.
2. `A` cifra con `B pública`