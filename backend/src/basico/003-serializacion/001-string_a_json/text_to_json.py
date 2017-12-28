#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Importamos el método loads del módulo json de Python
from json import loads

texto = '{"hola": "que tal"}'
print(type(texto))  #  <class 'str'>

response = loads(texto)
print(type(response))  #  <class 'dict'>

print(response["hola"]) #  que tal

