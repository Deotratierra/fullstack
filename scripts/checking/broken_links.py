#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""El siguiente script realiza la siguiente tarea:
    - Abre un archivo cuya ruta es pasada como primer parámetro y
        cuyo contenido consta de la siguiente estructura:

            [
                {"https://docs.python.org/3/library/argparse.html": "/home/mondeja/Escritorio/fullstack/backend/src/020-pasar_argumentos/args_parser.py"},
                {"...": "..."},
                ...
             ]

        Son urls acompañadas de un archivo, en el cual se encuentran escritas.
    - Comprueba el código que devuelve cada URL. Si el código no es 200,
        imprime el código de error, la URL y el archivo donde se encuentra,
        la guarda como url caída.
    - Guarda todas las URLs caídas en un archivo JSON cuya ruta es pasada como 2º argumento.
"""


import os
import sys
import re
import json
from pprint import pprint
from requests import get
from tqdm import tqdm

def check_url(url, filename):
    broken, status, attempts = (False, 404, 5)
    first_url = url
    def fetch(url):
        try:
            status = get(url).status_code
        except Exception as error:
            return 200
        else:
            return status

    passing_status = (200, 403)
    while status not in passing_status and not broken:
        if attempts < 1:
            broken = True
        else:
            status = fetch(url)
            attempts -= 1
            url = url[:-1]

    if broken:
        print("\nERROR: Status code: %d - URL: %s - FILE: %s\n" \
                % (status, first_url, filename))
        return False
    return True

def main():
    # Obtenemos todas las urls recopiladas
    with open(sys.argv[1], "r", encoding="utf-8") as urls_file:
        all_urls = json.loads(urls_file.read())

    # Checkeamos todas las urls en busca de links caídos:
    urls_down = []
    stops = [
        "\t", "\n"
    ]
    print("Checking %d urls" % len(all_urls))
    for url in tqdm(all_urls):
        for stop in stops:
            if stop in url:
                continue
        url, filename = (list(url.keys())[0], list(url.values())[0])
        if not check_url(url, filename):  # Si encontramos un link caido
            urls_down.append({url: filename})

    # Guardamos las urls caidas en un archivo JSON pasado como 2º argumento
    with open(sys.argv[2], "w", encoding="utf-8") as broken_urls_file:
        broken_urls_file.write(json.dumps(urls_down, indent=4))
    return sys.exit(0)


if __name__ == "__main__":
    main()
