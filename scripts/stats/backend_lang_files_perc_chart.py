#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import json
from subprocess import Popen, PIPE
import shlex


import matplotlib
if os.environ.get("DISPLAY", "") == "":
    matplotlib.use("Agg")
import matplotlib.pyplot as plt


"""
Este script necesita de un una ruta como primer parámetro
donde guardar el gráfico resultante
"""

# Obtenemos el número de archivos por cada lenguaje
process = Popen(shlex.split("bash scripts/stats/recopile_stats.sh"), stdout=PIPE, stderr=PIPE)
stdout, stderr = process.communicate()
stats = json.loads(stdout.decode("utf-8"))

# Constuimos el mapa de etiquetas
labels_map = {
    "py": "Python",
    "ipynb": "IPythonNotebook",
    "js": "NodeJS",
    "rb": "Ruby",
    "cpp": "C++",
    "c": "C",
    "sh": "Bash",
    "tex": "LaTeX",
    "cy": "Cython",
}

total = sum(stats.values())

labels, sizes, explode = ([], [], [])
exploded = False
for lang, files in stats.items():
    perc = 100/total*files
    if perc > 0.4:
        sizes.append(files)
        labels.append(labels_map[lang])
        if not exploded:  # Explode al azar
            explode.append(0.1)
            exploded = True
        else:
            explode.append(0)

def pct(perc):
    return "{perc:.2f}%".format(perc=perc)

fig, ax = plt.subplots()
ax.pie(sizes, explode=explode, labels=labels, autopct=pct,
        shadow=True, startangle=90, labeldistance=1.2, radius=1.5,
)
# "equal" asegura que el gráfico pie se dibuja como un círculo
ax.axis('equal', bbox_inches='tight')
ax.set_title("Número de archivos por lenguaje\n")
legend = ax.legend(labels=["%s = %d" % (ext, f) for ext, f in stats.items()])

plt.savefig(sys.argv[1])
plt.close(fig)
