#!/bin/bash

: '
Para colorear las salidas en Bash, se usan las secuencias de escape ANSI.
Estas secuencias son a menudo representadas con los caracteres "^[" o "<Esc>",
seguida de otros caracteres. En Bash, el caracter <Esc> se puede obtener
mediante las sintaxis: "\e", "\033" y "x1B".

Para eliminar todos los atributos de formateo se usa: \e[0m
Es útil colocarlo al final de cada sentencia, así los atributos no
seguiran afectando a todo el aspecto de la terminal.

Para parsear las secuencias de escape al mostrar caracteres en Bash se usa:
echo -e

Ejemplos:
'
echo -e "Normal \e[1mNegrita\e[0m"

echo -e "\e[38;5;11m¡\e[38;5;33mHola \e[38;5;199mmundo \e[38;5;118mcoloreado\e[38;5;11m!\e[0m"

: '
Lista completa de secuencias de formateo
https://misc.flogisoft.com/bash/tip_colors_and_formatting
'