#!/bin/sh

set -x

echo -n "¿Puedes escribir de memoria los dispositivos conectados? s/n: "
read answer
answer=`echo $answer | tr [a-z] [A-Z]`

if [ $answer = s ]; then
    echo "¡Wow, debes ser un auténtico friki!"
else
    echo "Yo tampoco puedo, esto es sólo un ejemplo de script Bash"
fi