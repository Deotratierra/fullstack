#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def longest_non_repeat(s):
    start, maxlen = 0, 0
    used_char = {} # Guardamos los caracteres usados con su posición
    for i, char in enumerate(s):
    	# Si ya hemos usado el caracter antes
        if char in used_char and start <= used_char[char]:
            start = used_char[char] + 1 # Marcamos comienzo
        else: # Si no, comprobamos si restando al índice 
            # actual el del comienzo de la subcadena
            # obtenemos un nuevo largo máximo
            maxlen = max(maxlen, i-start+1)
        used_char[char] = i # Añadimos/actualizamos el caracter con índice
    return maxlen

a = "abcabcdefbb"
print(a)
print(longest_non_repeat(a)) # 6