#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from re import findall
from urllib.request import urlopen
from urllib.parse import urlencode


key = os.environ["PASTEBIN_PRIVATE_KEY"]


# Todas las llamadas a la API se realizan a través de la misma URL:
url = "https://pastebin.com/api/api_post.php"
# Sólo hay que cambiar el parámetro ``option`` de la función para cambiar
# de comando a usar.

def GET(url, data=None):
    if data:
        req = urlopen(url, data.encode())
    else:
        req = urlopen(url)
    return req.read().decode()

def pastebin(content=None, privacy="unlisted", language="python",
	         option="paste", expire=None, **kwargs):
    """Conecta con Pastebin para realizar alguna acción.

    Args:
        content (str, optional): Content of the paste if ``option == "paste"``.
            As default, ``None``.
        option (str, optional): Select the action that you want to performs in
            pastebin API. Valid actions are ``"paste"``, ``"delete"`` y ``"list"``.
            As default ``"paste"``.
        privacy (str, optional): Select between ``"public"``, ``"unlisted"`` or
            ``"private"`` if ``option == "paste"``. As default ``"unlisted"``.
        language (str, optional): Syntax highlighting language used if
            ``option == "paste"``. See ``languages`` function to retrieve all
            posible languages programatically. As default == ``"python"``.
        expire (str, optional): Time until paste expiration if ``option == "paste"``.
            As default ``None``.
    """
    if option == "paste" and content == None:
        raise ValueError("You can't make a paste without content.")

    if not privacy:
        privacy = "unlisted"

    privacy = dict(public=0, unlisted=1, private=2)[privacy]

    parms = {"api_option":        option,
             "api_dev_key":       key}
    if expire:
        parms["api_paste_expire_date"] = expire
    if option == "paste":
        parms["api_paste_code"] = content
        parms["api_paste_private"] = privacy
        parms["api_paste_format"] = language
    else:
        parms.update(kwargs)

    data = urlencode(parms)
    res = GET(url, data=data)
    return res

def languages():
    url = "https://pastebin.com/api"
    res = GET(url)
    searchs = findall(r'(\w+\s=\s\w+)', res)

    stops = ['href = location', 'e9 = new', 'e9 = new',
             'public = 0', 'unlisted = 1', 'private = 2',
              'N = Never', '10M = 10', '1H = 1', '1D = 1',
              '1W = 1', '2W = 2', '1M = 1', '6M = 6', '1Y = 1',
              '0 = Public', '1 = Unlisted', '2 = Private',
              'e9 = new', 'snackbar = true']
    response = {}
    for search in searchs:
        if search not in stops:
            _s = search.split(" = ")
            response[_s[0]] = _s[1]
    return response
