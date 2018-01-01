#!/bin/bash

#####     CONCURRENCIA EN BASH     #####

:'
Al lanzar un proceso en segundo plano en Bash
se pierde la posibilidad de leer datos desde la terminal
pero conserva la salida estándar y la salida de errores.

Normalmente al inciar un proceso en segundo plano
se le asigna como salida estándar un fichero especial
que se encuentra en /dev/null, que descarta todo lo que
recibe, la información enviada ahí no se puede recuperar
de ninguna manera.
'

# Para ejecutar un proceso en segundo plano
# (agregar & al final del comando):
ls > /dev/null &

# También podemos redirigirlo hacia un archivo
# escribiendo en el la salida con >>
ls > /dev/null >> log.text &
# Si no existe el archivo se crea automáticamente


# ------------------------------------------------

# Poner un proceso en segundo plano
:'
Podemos ejecutar un proceso, presionar Ctrl+Z antes
de que acabe para pararlo y ejecutar inmediatamente bg,
lo cual evía el proceso a segundo plano
'

# ------------------------------------------------

# Observar los procesos en segundo plano
:'
Con el comando jobs podemos comprobar los procesos
que se están ejecutando actualmente en segundo plano

Opciones:
    -l -> muestra información detallada del estado
            en el que se encuentran los procesos.
    -p -> muestra el ID de los procesos sin mostrar
            el estado en el que se encuentran.
    -s -> muestra sólo los procesos parados.
    -r -> sólo los procesos que están ejecutándose.
'

# Poner un proceso en primer plano
fg <numero_de_trabajo>

# ============================================================

# Ejecutar en otra pantalla de Bash
:'
Si por ejemplo queremos ejecutar un servidor
y un cliente en la misma consola, podemos usar el
comando screen para cambiar de la pantalla del cliente
a la del servidor a placer.

Simplemente ejecutamos screen, lo cual nos moverá
a otra "pantalla" dentro de la misma consola.
Entonces ejecutamos el proceso y presionamos Ctrl+A, D
Esto nos sacará de la pantalla y volveremos al cliente.

Para volver a la pantalla ejecutamos screen -rD
Si tenemos varias pantallas ejecutamos screen <numero_de_pantalla>
'

# ------------------------------------------------

