#!/bin/bash

: '
Para generar contraseñas seguras siguiendo unos parámetros
podemos usar el programa pwgen:
sudo apt-get install pwgen

Para usarlo:
pwgen [-opciones] <longitud_en_caracteres> <número_de_contraseñas>
'

# Generar una contraseña de 15 caracteres
C1=$(pwgen 15 1)
echo $C1

: '
-0, –no-numerals: No incluye números en las contraseñas generadas.
-A, –no-capitalize: No incluye letras mayúsculas en las contraseñas generadas.
-B, –ambiguous: No incluye ningún caracter que pueda llamar a confusión (como el 1 y la l , O y 0)
-y, –symbols: Inserta en la contraseña generada al menos un caracter especial (como *$=!?% …)
-n, –numerals: Inserta al menos un número en la contraseña generada.
-s, –secure: Genera una contraseña totalmente aleatoria, muy difícil de memorizar.
'

# 3 contraseñas seguras con un símbolo y al menos un número
C2=$(pwgen -snyB 20 3)
echo $C2
