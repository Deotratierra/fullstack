## [Máscaras de red](https://es.wikipedia.org/wiki/M%C3%A1scara_de_red)
La dirección `192.168.0.XXX` se utiliza para identificar y comunicarnos con los ordenadores que se ubican dentro de la red local. Todas las peticiones que se realizan a direcciones que empiezan en `192.` se canalizan hacia la red local, prefijo que puede extenderse siguiendo la especificación de la submáscara de red.

> Las submáscaras de red no son más que una forma de delimitar cuántos equipos y cuántas redes pueden configurarse en una red local.

Suponte que tienes una máscara de red `255.255.255.0`. Esto realmente te está indicando que las direcciones IP que envías están siendo enmascaradas por 3 números binarios de la forma `1111 1111` (8 en total) y un número `0000 0000`. Es decir, es lo mismo que `11111111.11111111.11111111.00000000` en binario.

>En este directorio tienes un script en Python (`masking.py`) que simula la forma en la que se comportan las máscaras de red mediante la técnica del enmascaramiento de bits por operadores lógicos `&` (AND).

Básicamente indica la cantidad de grupos que deben coincidir tu petición de IP con los de la IP local para que el router te envíe afuera o intente conectar con otro equipo en la red `192.168.1....`. Los números `255.25......` no son más que indicar 8 unos ó 8 ceros, "o pasa o no pasa", o se enmascara o no.

De otra forma: "En resumen, la máscara lo que determina es qué paquetes que circulan por la LAN se aceptan por algún ordenador de la LAN o qué paquetes han de salir fuera de la LAN (por el router). De esta manera, si se escribe en el navegador una dirección IP: 182.23.112.9, el equipo enviará la petición web, ftp, etc, directamente a la dirección especificada por la puerta de enlace (es decir, el router). Ningún equipo de la subred (LAN) atenderá estos paquetes por no estar dentro de su subred (LAN)" (extraído de Wikipedia).
