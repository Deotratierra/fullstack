#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""El siguiente script realiza lo siguientes pasos:
    - Itera por todos los archivos de un árbol de directorios. La ruta
        del directorio padre es pasada como primer parámetro.
    - Abre cada uno de los archivos y extrae todas las URLs que contienen.
    - Guarda todas las urls junto con la ruta respectiva del archivo en el
        el cual han sido encontradas.

Notas:
    El proceso de extracción de URLs de archivos es una tarea complicada,
        debido a que a menudo no podemos saber dónde acaba o empieza una URL.
        Por ejemplo, si escribimos código markdown, una url tendrá la estructura:
            [Nombre del link a mostrar](https://proveedor.com/ruta)

    Construyendo una expresión regular completa podemos solucionar el problema,
        sin embargo es posible que siempre encontremos estructuras condicionales
        o urls que no merecen la pena tomar en cuenta.

    Por ello, en el script se incluyen dos listas IGNORE_URLS (ignora ciertas urls)
        e IGNORE_FILENAMES (ignora ciertos archivos donde buscar urls).
    Si ello no resulta, existe la función conditional_cleaner(), la cual podemos
        editar para añadir otras condiciones fácilmente.

"""

import os
import sys
import re
import json
from tqdm import tqdm

# ================================================================

# Urls a ignorar
IGNORE_URLS = [
    "https://github.com/user/repository/archive/branch.zip",
    "https://raw.github.com/gdsmith/jquery-easing/master/LICENSE",
    "https://github.com/VodkaBears/Remodal/blob/master/src/jquery.remodal.js",
    "https://github.com/<usuario>/<repositorio>/archive/<branch>.zip",
    "https://<usuario>:<contrase",
    "https://github.com/krallin/tini/releases/download/$",
    "https://<usuario>:<contrase\u00f1a>@github.com/<usuario>/<repositorio>.git".
    "https://www.python.org/ftp/python/<NUMERO.DE.VERSI\u00d3N>/<nombre_del_archivo_comprimido_con_patch>.tgz",
]

# Proveedores a ignorar (https://www.PROVEEDOR.com)
IGNORE_PROVIDERS = [
    "milanuncios",
    "localhost",
    "git-lfs",
    "googleapis"
]

# Nombres de archivo a ignorar
# (sólo nombres, no hace falta la ruta completa)
IGNORE_FILENAMES = [
    "bootstrap.min.js.map",
    "main.js",
    "materialize.js",
    "materialize.css",
    "axios.min.map",
]

REGEX = r"http[s]?://(?:[a-zA-Z]|[áéíóúÁÉÍÓÚñÑ]|[0-9]|[$-_@.&+]|[!*\(\),])+"

def conditional_cleaner(url, filename):
    if url.count(")") > url.count("("):
        for _ in range( url.count(")") - url.count("(") ):
            if url[-1] == ")":
                url = url[:-1]
    return (url, filename)

# ================================================================


def get_all_files(root):
    """Obtener todos los archivos recursivamente desde
    un directorio padre pasado como parámetro"""
    response = []
    for root, dirs, files in os.walk(root, topdown=False):
        for name in files:
           response.append(os.path.join(os.path.abspath(root), name))
    return response

def extract_urls(content, filename):
    """Extraer todas las urls de un archivo"""
    urls = re.findall(REGEX, content)

    def clean(url):
        # Al final de las urls muchas tienen caracteres no deseados
        stops = [".", ":", "\n", "\t", ",", "'"]

        for _ in range(len(stops)*3):
            for stop in stops:
                if url[-len(stop)] == stop:
                    url = url[:-len(stop)]

        hard_stops = [r"\n", r"\t"]
        for stop in hard_stops:
            url = re.sub(stop, "", url)

        return url

    output = []
    for url in urls:
        ignore = False
        url = clean(url)
        if url == "" or url in IGNORE_URLS or  \
            os.path.basename(filename) in IGNORE_FILENAMES:
            continue
        for provider in IGNORE_PROVIDERS:
            if provider in url:
                ignore = True
        if not ignore:
            url, filename = conditional_cleaner(url, filename)
            output.append({url: filename})

    return output

def main():
    # Extraemos todas las urls de todos los archivos
    all_urls = []
    for f in tqdm(get_all_files(sys.argv[1])):
        with open(f, "r", encoding="utf-8") as f:
            try:
                content = str(f.read())
            except UnicodeDecodeError as error:
                pass
            else:
                all_urls += extract_urls(content, f.name)

    with open(sys.argv[2], "w", encoding="utf-8") as urls_file:
        urls_file.write(json.dumps(all_urls))


if __name__ == "__main__":
    main()
