#!/bin/sh

debug=1

test $debug -gt 0 && echo "El debug está activado"
echo -n "¿Puedes escribir de memoria los dispositivos conectados? s/n: "
read answer

test $debug -gt 0 && echo "La respuesta es $answer"

answer=`echo $answer | tr [a-z] [A-Z]`
if [ $answer = S ]; then
    echo "¡Wow, debes ser un auténtico friki!"
else
    echo "Yo tampoco puedo, esto es sólo un ejemplo de script Bash."
fi