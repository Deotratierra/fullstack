#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# AVISO: NO EJECUTABLE

import os
# https://docs.python.org/3/library/os.html

# Obtener el directorio actual
path = os.getcwd()

# Saber si se puede acceder a un archivo o directorio
os.access(<path>, modo_de_acceso) # El segundo parámetro es el modo de acceder ("r" == lectura)

# Cambiar de directorio de trabajo
os.chdir(<path>)

# Cambiar al directorio de trabajo raíz
os.chroot()

# Cambiar los permisos de un archivo o directorio
os.chmod(<path>, permisos)

# Cambiar el propietario de un archivo o directorio
os.chown(<path>, permisos)

# Crear un directorio
os.mkdir(<path>[, modo])

# Crear directorios recursivamente
os.mkdirs(<path>[, modo])

# Eliminar un archivo
os.remove(<path>)

# Eliminar un directorio
os.rmdir(<path>)

# Eliminar directorios recursivamente
os.removedirs(<path>)
#Renombrar un archivo
os.rename(<path_actual>, <nuevo_path>)

#Crear un enlace simbólico
os.symlink(<path>, nombre_destino)

# ----------------------------------------------

# Directorio del archivo actual
os.path.abspath(os.path.dirname(__file__))

# Unir paths añadiendo "/" ó "\" entre ellos
os.path.join(<path>, [,paths])

# Ruta absoluta
os.path.abspath(<path>)

# Directorio base
os.path.basename(<path>)

# Saber si una ruta existe
os.path.exists(<path>)

# Conocer último acceso a un directorio
os.path.getatime(<path>)

# Conocer tamaño del directorio
os.path.getsize(<path>)

# Saber si una ruta es absoluta
os.path.isabs(<path>)

# Saber si una ruta es un archivo
os.path.isfile(<path>)

# Saber si una ruta es un directorio
os.path.isdir(<path>)

# Saber si una ruta es un enlace simbólico
os.path.islink(<path>)

# Saber si una ruta es un punto de montaje
os.path.ismount(<path>)

# ------------------------------------------------

# Recorrer árbol de directorios
os.walk(top[, topdown=True[, onerror=None[, followlinks=False]]])
# Ejemplo:
for root, dirs, files in os.walk(".", topdown=False):
   for name in files:
      print(os.path.join(root, name))
   for name in dirs:
      print(os.path.join(root, name))

# ------------------------------------------------

# Agregar modulo al path para importarlo globalmente
import sys
sys.path.append("<path_al_modulo>.py")

# Fuente:
# http://librosweb.es/libro/python/capitulo_10/modulos_de_sistema.html