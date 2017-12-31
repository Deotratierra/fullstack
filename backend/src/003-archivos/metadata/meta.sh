#!/bin/bash

ARCHIVO=meta.py
DIRECTORIO=.


# Obtener tamaño de un archivo
stat -c%s $ARCHIVO

# Obtener tamaño de un un directorio
du -sb $DIRECTORIO | cut -f1
du -h $DIRECTORIO # Incluye el tamaño de los directorios

# Obtener fecha de la última modificación de un archivo
stat -c %y $ARCHIVO | cut -d "." -f1
stat -c %Y $ARCHIVO # En unix timestamps

# Obtener atributos de metadatos de un archivo
stat $ARCHIVO


: '
Fuentes:
https://stackoverflow.com/questions/16661982/check-folder-size-in-bash
https://stackoverflow.com/questions/16391208/print-a-files-last-modified-date-in-bash
'
