#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv

# ===============================================================

#####   CREAR ARCHIVOS CSV   #####

headers = ["campo1", "campo2", "campo3"]

with open("fichero.csv", "w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, 
                        fieldnames=headers,
                        restval=' ',
                        quoting=csv.QUOTE_NONNUMERIC)
    # QUOTE_NONNUMERIC convierte todos los campos numéricos en tipo float

    writer.writeheader() # Write header

    insercion = {"campo1": "hola", "campo2": 8, "campo3": "valorfinal"}
    writer.writerow(insercion)

# ===============================================================

#####   LEER ARCHIVOS CSV   #####

with open("fichero.csv", "r", newline="") as csvfile:
    reader = csv.DictReader(csvfile, quoting=csv.QUOTE_NONNUMERIC)

    print(reader.fieldnames)

    for row in reader:  #  ['campo1', 'campo2', 'campo3']
        print(row) # OrderedDict([('campo1', 'hola'), ('campo2', '8'), ('campo3', 'valorfinal')])

# ===============================================================

"""
Fuente:
https://docs.python.org/3/library/csv.html
"""