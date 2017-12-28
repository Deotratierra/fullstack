#!usr/bin/bash

# En unix, los comandos bash pueden canalizar en tuberías
# las salidas de los comandos hacia el siguiente,
# permitiendo operar sobre la información antes de ser devuelta.

# Para crear tuberías agregamos el caracter | entre comandos

# Por ejemplo, cuando ejecutamos el siguiente comando
# para obtener el número de CPUs de nuestro ordenador:

cat /proc/cpuinfo | grep processor | wc -l

# realmente estamos ejecutando, en el siguiente orden:
cat /proc/cpuinfo
# lo que devuelve información sobre las CPUs,

grep processor

# grep es un comando que nos permite buscar, dentro de los archivos,
# las líneas que coinciden con el patrón especificado.
# En este caso indicamos que nos devuelva la parte de procesadores,
# que son 4 líneas, cada una indicando uno de ellos

wc -l
# wc es una abreviatura de word count y sirve para saber el número
# de palabras que componen los archivos, pero en este caso,
# con el parámetro -l indicamos que nos devuelva el número de líneas
# que componen el archivo en la tubería.

# Como en Unix todo es un archivo, pues lo que nos devuelven los
# streams que generan las tuberías son archivos.

# Fuentes:
# https://enavas.blogspot.com.es/2008/04/el-shell-de-linux-comando-grep.html
# https://es.wikipedia.org/wiki/Wc_(Unix)
