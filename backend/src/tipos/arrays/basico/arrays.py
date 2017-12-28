#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Hay tres tipos básicos secuenciales en Python: list, tuple y range.
Estos tipos se pueden iterar. tuple y range son secuencias inmutables,
pero list puede mutar.

str también es un tipo secuencial. Todos pueden accederse a través
de sus índices.
"""

# INICIALIZACIÓN

lista1 = list()      # Mediante el tipo
lista2 = []          # Explícita
lista3 = ["uno"] # Con elementos
                     # Desde claves o valores de diccionarios
lista4 = list(dict().keys()) + list(dict().values()) # (+ para concatenar)
lista5 = list(range(10))  # De un rango numérico de 0 a 9

print(lista1 == lista2 == lista3 == lista4)  #  True

# ----------------------------------------------------

# MODIFICACIÓN

lista1.append("primero")  # Agrega un elemento al final
print(lista1)   # ["primero"]
primero = lista1.pop()    # Extrae el último elemento
print(primero)   # primero
print("primero" not in lista1)  # True

lista2.append("segundo")
lista2.insert(0, "primero") # Inserción por índice
print(lista2)  #  ['primero', 'segundo']

lista2.remove("primero") # Elimina el elemento de la lista
print(lista2)   # ["segundo"]

lista2 *= 3   # Multiplica el contenido por 3
print(lista2)  # ['segundo', 'segundo', 'segundo']

lista3.append("dos")
lista2 += lista3
print(lista2)  # ['segundo', 'segundo', 'segundo', 'uno', 'dos']

print(lista5)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

lista5 = [num + 5 for num in lista5] # Forma rápida de iterar
print(lista5)  # [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

#                       Ordenación de una lista
print(sorted(lista2)) # ['dos', 'segundo', 'segundo', 'segundo', 'uno']

# ------------------------------------------------------------

# ACCESO A SUS ELEMENTOS

print(lista5[0])  # 5
print(len(lista5)) # 10   <--- Obtener el número de elementos

print("================================================")

# =================================================================

#                 OPERACIONES ALEATORIAS
import random

# Obtener un elemento al azar
print(random.choice(lista5))  # Si está vacía la lista levanta IndexError

# Obtener un número k de elementos al azar
print(random.choices(lista5, k=5))

# Obtener un número de elementos al azar no repetidos
print(random.sample(lista5, 3))

# Alterar aleatoriamente el orden del array
random.shuffle(lista5)

# =================================================================

"""
Fuentes:
https://docs.python.org/3/library/stdtypes.html#typesseq
"""
