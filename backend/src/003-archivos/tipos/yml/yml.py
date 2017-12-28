#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import yaml   # pip3 install pyyaml

# Insertar datos en un archivo .yml

data = {
    "primero": 1,
    "segundo": dict(hola="adios")
}

with open("data.yml", "w") as outfile:
    yaml.dump(data, outfile, default_flow_style=False)

# ====================================================

# Leer datos de un archivo .yml

with open("fichero.yml", "r") as infile:
    print(yaml.load(infile))
