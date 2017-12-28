#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import getpass

# Preguntar al usuario por una contraseña
# sin mostrar la introducción en pantalla:
hola = getpass.getpass(prompt="Contraseña: ")

# Obtener el usuario del sistema
# Chequea las varables de entorno
# LOGNAME, USER, LNAME y USERNAME, en orden
# y retorna el primer valor que no es una
# cadena vacía.
# Si ninguno está activado, retorna el nombre
# de usuario de la base de datos de contraseñas
# en sistemas que soportan el módulo pwd,
# si no, LEVANTA UNA EXCEPCIÓN
user = getpass.getuser()

# Fuente:
# https://docs.python.org/3/library/getpass.html

# Código fuente:
# https://github.com/python/cpython/blob/3.6/Lib/getpass.py
