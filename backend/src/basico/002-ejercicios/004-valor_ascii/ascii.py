#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    caracter = "a"
    caracter_en_ascii = ord(caracter)
    print("El caracter '%s' en ASCII ---> %d" % (caracter, caracter_en_ascii))

    numero = 89
    numero_en_caracter = chr(numero)
    print("El número %d en caracter ---> %s" % (numero, numero_en_caracter))
