# -*- coding: utf-8 -*-

"""
Script que, dada una ruta de formato de archivo de imagen
  pasada como primer parámetro, construye un gráfico de
  torta donde muestra el número de archivos clasificados
  por lenguaje que existen dentro de las carpetas `backend`
  y `frontend` del proyecto y lo guarda en la ruta.
"""

import os
import sys
import json
import subprocess

import matplotlib
if os.environ.get("DISPLAY", None) is None:
    matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Porcentaje mínimo de archivos del total
#   para que un lenguaje sea incluido en el gŕafico
MIN_PERCENTAGE_TO_SHOW_LANGUAGE = 0.1

def main():
    # Obtenemos el número de archivos por cada lenguaje
    process = subprocess.Popen(
        ["bash", "scripts/stats/recopile_stats.sh"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    stats_by_language = json.loads(stdout.decode("utf-8"))

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
        "go": "Golang",
        "php": "PHP",
        "java": "Java",
    }

    total = sum(stats_by_language.values())

    labels, sizes, explode = ([], [], [])
    exploded = False
    for lang, files in stats_by_language.items():
        perc = 100/total*files
        if perc > MIN_PERCENTAGE_TO_SHOW_LANGUAGE:
            sizes.append(files)
            labels.append(labels_map[lang])
            if not exploded:  # Explode al azar
                explode.append(0.1)
                exploded = True
            else:
                explode.append(0)

    def format_percentage(perc):
        return "{perc:.2f}%".format(perc=perc)

    fig, ax = plt.subplots()
    ax.pie(
        sizes,
        explode=explode,
        labels=labels,
        autopct=format_percentage,
        shadow=True,
        startangle=90,
        labeldistance=1.2,
        radius=1.5,
    )
    fig.figsize = (16, 8)

    # "equal" asegura que el gráfico pie se dibuja como un círculo
    ax.axis('equal', bbox_inches='tight')
    ax.set_title("Número de archivos por lenguaje\n")

    labels = [
        "%s = %d" % (ext, n_files) for ext, n_files \
            in stats_by_language.items()
    ]
    legend = ax.legend(labels=labels)

    plt.savefig(sys.argv[1])
    plt.close(fig)

if __name__ == "__main__":
    main()
