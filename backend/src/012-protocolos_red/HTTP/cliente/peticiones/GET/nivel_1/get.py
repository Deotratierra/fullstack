#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from json import loads

URL = "https://min-api.cryptocompare.com/stats"

# ==================================================

# ------ SÍNCRONA --------------------------------  urllib
# https://docs.python.org/2/library/urllib.html#examples
from urllib.request import urlopen

def urllib_GET(url):
    try:
        data = urlopen(url)
    except Exception as e:
        print(e)
    else:
        status = data.getcode()
        if status != 200:
            print("Error en la petición GET síncrona con requests.")
            print("Status code == %d" % response.status_code)
        #return loads(response.read())  #  <-- En JSON
        response = data.read()
        data.close()
        return response

# ==================================================

# ------ SÍNCRONA --------------------------------  requests
# pip3 install requests
# http://docs.python-requests.org/en/master/

from requests import get

def requests_GET(url):
    try:
        response = get(url) #  <-- Biblioteca requests
    except Exception as e:
        print(e)
    else:
        if response.status_code != 200:
            print("Error en la petición GET síncrona con requests.")
            print("Status code == %d" % response.status_code)
        return response.text
        #return response.json()  #  <-- En JSON

# ==================================================

# ------ SÍNCRONA ----------------------------------  pycurl
# Implementación a bajo nivel
# pip3 install pycurl
# http://pycurl.io/docs/latest/quickstart.html

import pycurl
from io import BytesIO

def pycurl_GET(url):
    buffer = BytesIO()
    c = pycurl.Curl()
    c.setopt(c.URL, url)
    c.setopt(c.WRITEDATA, buffer)
    try:
        c.perform()
    except Exception as e:
        print(e)
    else:
        status = c.getinfo(c.RESPONSE_CODE)
        c.close()
        body = buffer.getvalue()
        response = body.decode('utf-8')
        if status != 200:
            print("Error en la petición GET síncrona con pycurl.")
            print("Status code == %d" % status)
        #return loads(response)  # <---- En JSON
        return response

# ==================================================

# ------ ASÍNCRONA ---- (Python >= 3.5) ------------  aiohttp
# pip3 install aiohttp
# http://aiohttp.readthedocs.io/en/stable/client.html
# https://docs.python.org/3/library/asyncio.html

from aiohttp import ClientSession
import asyncio

async def async_GET(url):
    try:
        async with ClientSession() as session:
            async with session.get(url) as response:
                if response.status != 200:
                    print("Error en la petición GET asíncrona con aiohttp.")
                    print("Status code == %d" % response.status)
                #response = await response.json() #  <-- En JSON
                response = await response.text()
                print(response)
                return response
    except Exception as e:
        print(e)

# ==================================================

if __name__ == "__main__":
    # Peticiones síncronas
    print(urllib_GET(URL))
    print(requests_GET(URL))
    print(pycurl_GET(URL))

    # Petición asíncrona
    loop = asyncio.get_event_loop()
    loop.run_until_complete(async_GET(URL))
