#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ===============================================

        #####     GENERADORES     #####

def gen_primos():
    """Generador de números primos."""

    contador = 1
    lista_primos=[]

    while True:
        es_primo = True
        contador += 1
        for primo in lista_primos:
            if contador % primo == 0:
                es_primo = False
                break
        if es_primo:
            lista_primos.append(contador)
            yield contador

generador = gen_primos()

print("Generar los 10 primeros números primos")
for primo in range(10):
    print(next(generador))

# ===============================================
