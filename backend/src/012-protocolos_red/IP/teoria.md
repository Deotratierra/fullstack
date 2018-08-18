## Direcciones IP
Una dirección IP es un número que identifica, de manera lógica y jerárquica, a una Interfaz en red (elemento de comunicación/conexión) de un dispositivo (computadora, tableta, portátil, smartphone) que utilice el protocolo IP o (Internet Protocol).

_________________________________

### Como funciona
#### En redes locales (LAN)
Las IPs se distribuyen por el router de forma dinámica (lo más común por defecto) o estática.

>Desde aquí puedes entender [qué son y cómo funcionan las submáscaras de red](https://github.com/mondeja/fullstack/tree/master/backend/src/012-protocolos_red/IP/subnet_masks).

#### En internet
Cada nodo de internet tiene una dirección pública, la cual es mostrada al interactuar con otros, aunque existen procedimientos para evitar mostrala.

_________________________________

### Versiones de IP

#### IPv4
> Cantidad total de direcciones: `256⁴ = 4,294,967,296`

Una dirección IPv4 es un número de 32 bits formado por cuatro octetos (números de 8 bits) en una notación decimal, separados por puntos. La notación decimal de un octeto tiene `2⁸ = 256` posibilidades. Ya que nosotros empezamos a contar desde el 0, los posibles valores de un octeto en una dirección IP van de 0 a 255.

> Ejemplos de direcciones IPv4: `192.168.0.1`, `66.228.118.51`, `173.194.33.16`

_________________________________

#### IPv6
> Cantidad total de direcciones: `2¹²⁸ = 340,282,366,920,938,463,463,374,607,431,768,211,456`

Las direcciones IPv6 están basadas en 128 bits. Usando la misma matemática anterior, nosotros tenemos 2 elevado a la 128va potencia para encontrar el total de direcciones IPv6 totales, mismo que se mencionó anteriormente. Ya que el espacio en IPv6 es mucho mas extenso que el IPv4 sería muy difícil definir el espacio con notación decimal... se tendría 2 elevado a la 32va potencia en cada sección.

>Ejemplo de dirección IPv6: `2607:f0d0:4545:3:200:f8ff:fe21:67cf`

IPv6 está compuesto por ocho secciones de 16 bits, separadas por dos puntos (:). Ya que cada sección es de 16 bits, tenemos 2 elevado a la 16 de variaciones (las cuales son 65,536 distintas posibilidades). Usando números decimales de 0 a 65,535, tendríamos representada una dirección bastante larga. Las direcciones IPv6 están expresadas con notación hexadecimal (16 diferentes caracteres: 0-9 y a-f).

> IPv6 se diseñó para afrontar el crecimiento de número de IPs en internet en las futuras generaciones, ya que cada dirección de internet debe tener una IP única.