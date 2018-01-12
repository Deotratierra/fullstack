## Señales
Las señales es un mecanismo que provee el kernel para que los procesos se intercomuniquen. Existe un número predeterminado de señales (normalmente 32) disponibles. También interrumpen procesos para corregir situaciones anormales. Tienen significados predefinidos, algunas pueden ser programadas. A estas se les refiere como manejadoras de señales (signal handlers).

Muchas de las señales son usadas para proveer información a los procesos desde el kernel. Un programa puede decirle al kernel que desea ignorar una señal en particular. Si esta señal no es capturada o ignorada, la acción por defecto tomará lugar cuando el proceso la recibe. Dos señales jamás podrán ser ignoradas o atrapadas que son: STOP y KILL.

Cada señal está determinada por un número en el sistema, pero en los programas se suelen llamar por sus nombres.

### Comportamiento
Las señales son asíncronas, es decir, cuando un programa recibe una señal, esta se procesa inmediatamente sin finalizar la función, ni siquiera la línea
de código actual.

Para cada señal hay un comportamiento por defecto que determina qué le pasa al proceso si el programa no especifica algún otro comportamiento. Si un el programa usa un manejador de señal, la ejecución actual del programa se detiene, el manejador es ejecutado y cuando el manejador retorna el programa continua desde el punto donde paró.

#### Ejemplos de señales
> Para ver la lista de todas las señales posibles definidas en el sistema puedes consultar la cabecera de C `/usr/include/bits/signum.h` o `/usr/include/x86_64-linux-gnu/bits/signum.h` (u otra localización en tu sistema).

El sistema Linux envía señales a los procesos para responder a condiciones específicas. Por ejemplo, las señales `SIGBUS` (error de bus), `SIGSEGV` (violación de segmento) y `SIGFPE` (excepción de punto flotante) pueden ser enviadas a un proceso que intenta realizar una operación ilegal. La disposición por defecto de esas señales es terminar el proceso y producir un archivo de núcleo.

Un proceso también puede enviar una señal a otro. Un uso común de este mecanismo es terminar un proceso enviándole una señal `SIGTERM` o `SIGKILL`.

> Diferencia entre `SIGTERM` y `SIGKILL`:
> - `SIGTERM`: pide al proceso terminarse. El proceso puede ignorar la petición enmascarando o ignorando la señal.
> - `SIGKILL`: siempre termina el proceso inmediatamente porque no se puede enmascarar o ignorar.

Otro uso común es enviar un comando a un programa corriendo actualmente, para lo cual hay dos señales reservadas: `SIGUSR1` y `SIGUSR2`. La señal `SIGHUP` es usada a veces para esto, comunmente para levantar un programa inactivo o hacer que relea sus archivos de configuración.

Cuando el usuario pulsa `Ctrl+C` en la consola, se envía la señal `SIGINT` al proceso. Cuando se llama a la función `abort()` desde C, se envía la señal `SIGABRT`


### Limitaciones
Ya que las señales son asíncronas, un programa puede estar en un estado frágil cuando se procesa una señal y mientras la función manejadora de señal se ejecuta. Evita el realizar operaciones de entrada o salida de datos y el llamar a funciones del sistema desde las señales.

Un manejador de señal debe realiar el mínimo trabajo necesario para responder a la señal y luego retornar el control al programa principal o terminarlo. En la mayoría de los casos, esto consiste simplemente en grabar el hecho de que ocurrió una señal.

Puede ocurrir que el programa recibe otra señal cuando se esté manejando una. Esto es lo que se llama una condición de carrera y puede ser muy difícil de diagnosticar y depurar. Por lo tanto **debes ser muy cuidadoso con lo que hace tu programa en un manejador de señal**.


