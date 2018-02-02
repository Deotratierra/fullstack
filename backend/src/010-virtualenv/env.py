#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Documentación de referencia:
# https://virtualenv.pypa.io/en/stable/reference/

# Instalar virtualenv
pip3 install virtualenv


#============================================================

# Iniciar un entorno virtual:
virtualenv nombre_del_entorno

#     Indicando la versión de Python:
virtualenv nombre_del_entorno -p /ruta/al/ejecutable/python.major.minor

# -----------------------

# Para desactivar el entorno virtual
deactivate

# Eliminar un entorno virtual
rm -Rf nombre_del_entorno

#============================================================