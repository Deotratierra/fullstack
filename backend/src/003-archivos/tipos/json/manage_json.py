#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json

# Parsear formato json
with open("fichero.json", "r") as fichero:
    json_parsed = json.loads(fichero.read())

# Escribir ficheros en json
with open("fichero2.json", "w") as fichero:
    fichero.write(json.dumps(json_parsed))

# Comenta para ver el nuevo fichero creado:
os.remove("fichero2.json")

# Podemos crear codificadores y descodificadores personalizados:
# https://docs.python.org/3/library/json.html
