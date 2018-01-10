## Criptografía asimétrica
También llamada criptografía de clave pública o criptografía de dos claves1​, es el método criptográfico que usa un par de claves para el envío de mensajes. Las dos claves pertenecen a la misma persona que ha enviado el mensaje. Una clave es pública y se puede entregar a cualquier persona, la otra clave es privada y el propietario debe guardarla de modo que nadie tenga acceso a ella. Además, los métodos criptográficos garantizan que esa pareja de claves sólo se puede generar una vez, de modo que se puede asumir que no es posible que dos personas hayan obtenido casualmente la misma pareja de claves.

### Cómo funciona
Imagina que dos personas (`A` y `B`) quieren intercambiar información de forma segura. Estas dos personas utilizan dos claves cada una, una pública y otra privada, las cuales llamaremos `A pública`, `B privada`... Cada clave pública ha sido generada a partir de la clave privada, por lo que los mensajes cifrados con una clave pública sólo pueden ser descifrados con su correspondiente clave privada.

Para conseguir el intercambio seguro deben seguir los siguientes pasos:
1. `A` le envía a `B` la `A pública` y `B` le envía a `A` la `B pública`.
2. `A` cifra con `B pública` su mensaje y se lo envía a `B`.
3. `B` descifra el mensaje con `B privada` y puede leerlo.
4. Ahora `A` cifra un mensaje con `A privada` y lo envía a `B`.
5. `B` descifra el mensaje con `A pública`. Esto le garantiza que el remitente del mensaje es realmente `A`.

Esto es básicamente el funcionamiento de la criptografía asimétrica. Se trata de cifrar tu mensaje con la clave pública de tu destinatario para que el contenido sea seguro y certificar el origen de tus mensajes con tu clave privada para que los demás puedan compararlo con tu clave pública, aseverando que realmente eres tú el destinatario.

Todo esto depende de que las claves privadas sean absolutamente secretas. El administrador de sistemas debe encargarse de gestionarlas, particularmente en lo que respecta a nivel de permisos en el servidor: `chmod 400` ó `chmod 500` (ver apartado de [permisos](https://github.com/mondeja/fullstack/tree/master/backend/src/046-sistema_operativo/permisos).
