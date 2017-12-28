#!/usr/bin/env python3
# -*- coding: utf-8 -*-

sentencias = [
    "abcdefGHIJKLMNopqrstuvwxyz",
    "abcdefGHIJKLwNopqrstuvwxyz",
    "Texto de ejemplo",
    "The quick brown fox jumps over the lazy dog",
]

abecedario_ingles = "abcdefghijklmnopqrstuvwxyz"

def pangrama(string):
    letras = []
    for letra in string.replace(" ", ""): # Eliminamos espacios
        letra = letra.lower()  # Convertimos a minúsculas
        if letra not in letras:
            if letra in abecedario_ingles:
                letras.append(letra)
    if len(letras) == len(abecedario_ingles):
        return True
    return False
    
for s in sentencias:
    print(pangrama(s))
    
