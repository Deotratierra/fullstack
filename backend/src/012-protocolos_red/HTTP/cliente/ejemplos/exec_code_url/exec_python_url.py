#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from requests import get

# Ejecutar código Python a a través de una url

URL = "..."
codigo = get(URL).text

exec("python3 %s" % codigo)
