#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import argv

def rs():
    for _ in range(int(argv[1])):
        string = "Salida de emergencia"
        pattern = "Salida"
        substitution = "Entrada"
        string = string.replace(pattern, substitution)

if __name__ == "__main__":
    rs()