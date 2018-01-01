## Señales
Las señales es un mecanismo que provee el kernel para que los procesos se intercomuniquen. Existe un número predeterminado de señales (normalmente 32) disponibles. También interrumpen procesos para corregir situaciones anormales. Tienen significados predefinidos, algunas pueden ser programadas. A estas se les refiere como manejadoras de señales (signal handlers).

Muchas de las señales son usadas para proveer información a los procesos desde el kernel. Un programa puede decirle al kernel que desea ignorar una señal en particular. Si esta señal no es capturada o ignorada, la acción por defecto tomará lugar cuando el proceso la recibe. Dos señales jamás podrán ser ignoradas o atrapas que son: STOP y KILL.

El uso de señales es un método de alto nivel para interrumpir la ejecución de un proceso. Administradores de sistemas a menudo utilizan señales para eliminar procesos.