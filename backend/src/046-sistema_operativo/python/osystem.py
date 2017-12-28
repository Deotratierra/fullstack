#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

# Obtener la codificación del sistema operativo
sys.getfilesystemencoding()

# Obtener la plataforma
sys.platform
"""
if sys.platform.startswith('freebsd'):
    # Código específico de FreeBSD aquí...
elif sys.platform.startswith('linux'):
    # Código específico de Linux aquí...
elif sys.platform.startswith('win32'):
    # Código específico de Windows aquí...
elif sys.platform.startswith('cygwin'):
    # Código específico de Windows/Cygwin aquí...
elif sys.platform.startswith('darwin'):
    # Código específico de Mac OS X aquí...
else:
    # Plataforma desconocida
"""

import platform

# Obtener la arquitectura en bits de la plataforma
is_64bits = sys.maxsize > 2**32

# Obtiene el tipo de máquina ('i386', 'x86_64'...)
platform.machine()

# Retorna el nombre del ordenador en la red
platform.node()

# Retorna la plataforma, versión, arquitectura,
# version... en un formato leíble para humanos
platform.platform()

# Obtiene la versión de lanzamiento del sistema
platform.release()

# Fuentes:
# https://docs.python.org/3/library/sys.html
# https://docs.python.org/3/library/platform.html

# =============================================

#    Rendimiento y utilización del sistema

import datetime
import psutil   # http://psutil.readthedocs.io/en/latest/

# Número de CPUs
psutil.cpu_count()

# Porcentaje de uso
psutil.cpu_percent()

# Porcentaje de uso por CPU
psutil.cpu_percent(percpu=True)

# Uso de memoria
psutil.virtual_memory()

# Particiones de discos duros
particiones = psutil.disk_partitions()

# Uso de discos duros (hay que pasarle un path de punto de montaje)
psutil.disk_usage(particiones[0].mountpoint)

# Información sobre la temperatura del sistema (actual, más alta, crítica...)
psutil.sensors_temperatures()  # Sólo funciona en Linux

# Información de los ventiladores
psutil.sensors_fans()          # Sólo funciona en Linux

# Información de la batería
psutil.sensors_battery()

# Último arranque del sistema
psutil.boot_time()  # En unix timestamps
#print(datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S"))

# Información sobre los usuarios
print(psutil.users())

# ===========================================