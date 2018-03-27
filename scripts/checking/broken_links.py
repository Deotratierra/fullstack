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
import json
import asyncio

import aiohttp
from tqdm import tqdm

global URLS_DOWN
URLS_DOWN = []

async def fetch(url, session, progress_bar):
    """Fetch a url, using specified ClientSession."""
    _url = list(url.keys())[0]
    try:
        async with session.get(_url, timeout=5) as response:
            resp = response.status
    except Exception as e:
        resp = 404
    finally:
        progress_bar.update(1)
        if resp == 404:
            URLS_DOWN.append(url)
        return (resp, url)

async def fetch_all(urls, progress_bar):
    """Launch requests for all web pages."""
    tasks = []
    async with aiohttp.ClientSession() as session:
        for url in urls:
            task = asyncio.ensure_future(
                fetch(url, session, progress_bar)
            )
            tasks.append(task) # create list of tasks
        responses = await asyncio.gather(*tasks)
    return responses

def main():
    # Obtenemos todas las urls recopiladas
    with open(sys.argv[1], "r", encoding="utf-8") as urls_file:
        all_urls = json.loads(urls_file.read())



    # Instanciamos barra de progreso y loop
    progress_bar = tqdm(
        desc="Checking %d urls" % len(all_urls),
        total=len(all_urls)
    )
    loop = asyncio.get_event_loop()

    # Checkeamos todas las urls en busca de links caídos:
    future = asyncio.ensure_future(
        fetch_all(all_urls, progress_bar)
    )
    loop.run_until_complete(future)

    from pprint import pprint
    pprint(URLS_DOWN)

    """
    for url in tqdm(all_urls):
        for stop in stops:
            if stop in url:
                continue
        url, filename = (list(url.keys())[0], list(url.values())[0])
        if not check_url(url, filename):  # Si encontramos un link caido
            urls_down.append({url: filename})
    """

    # Guardamos las urls caidas en un archivo JSON pasado como 2º argumento
    with open(sys.argv[2], "w", encoding="utf-8") as broken_urls_file:
        broken_urls_file.write(json.dumps(URLS_DOWN, indent=4))
    return sys.exit(0)


if __name__ == "__main__":
    main()
