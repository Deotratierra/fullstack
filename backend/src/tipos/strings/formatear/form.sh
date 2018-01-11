#!/bin/bash

# Para formatear cadenas en Bash usamos printf()
# printf() está implementado en muchos lenguajes de programación
# así que mejor saber manejarla al 100%

# Referencia: https://es.wikipedia.org/wiki/Printf
# Comandos: http://wiki.bash-hackers.org/commands/builtin/printf

# ===============================================================

NUMERO=9
CADENA="cadena de ejemplo"

# Justificación:

printf "<%d> no está justificado.\n" $NUMERO
printf "<%5d> está justificado a la derecha.\n" $NUMERO
printf "<%-5d> El signo - significa justificación a la izquierda.\n" $NUMERO
printf "\n"
printf "'%s' no está justificada.\n" "$CADENA"
printf "'%20s' está justificada a la derecha.\n" "$CADENA"
printf "'%-20s' está justificada a la izquierda con un signo -\n" "$CADENA"

# ===============================================================
