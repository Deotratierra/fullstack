## Debugging en Bash

### [Comando set](set_command.sh)
Usando el comando `set` al principio de un script podemos añadir verbosidad a su ejecución.

- `set -x`: Cada línea de código ejecutada aparecerá precedida de un carácter `+` si se ejecuta en la misma shell o 2 (`++`) si se ejecuta en una subshell.

### [Niveles de debugging](debug_levels.sh)
Podemos establecer una variable al principio del script que determine el nivel de debug. Luego con la sentencia `test $debug -gt 0 && echo <mensaje>` imprimos las sentencias de debugging. Esta sentencia significa "testea que la variable `debug` es mayor que 0, si es así imprime `<mensaje>`".

### [Código de estado de la última ejecución](status_code.sh)
Cada vez que ejecutamos un comando en la consola, esta guarda el código de estado de la ejecución en la variable `$?`. Así que si ejecutamos algo que provoca un error y, seguidamente `echo $?` veremos en la salida el número `1`.

Podemos crear una función que muestre la salida del último comando en un script ([ver ejemplo](status_code.sh)).

> Fuente: Expert Shell Scripting - Ron Peters