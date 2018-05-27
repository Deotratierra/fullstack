#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json

path = "fichero.json"

# Parsear formato json
with open(path, "r") as fichero:
    json_parsed = json.loads(fichero.read())

# Escribir ficheros en json
with open(path, "w") as fichero:
    fichero.write(json.dumps(json_parsed))

# Comenta para ver el nuevo fichero creado:
os.remove(path)

# -----------------------------------------

# Parsear cadenas de texto JSON
texto = '{"hola": "que tal"}'
print(type(texto))  #  <class 'str'>

response = loads(texto)
print(type(response))  #  <class 'dict'>

print(response["hola"]) #  que tal

# ----------------------------------------

# Podemos crear codificadores y decodificadores personalizados:
# https://docs.python.org/3/library/json.html
