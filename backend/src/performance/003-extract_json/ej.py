#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import argv
from json import loads

STRING='{"clave": "valor 1", "num": 2}'

def ej():
    return loads(STRING)[argv[1]]

if __name__ == '__main__':
    ej()