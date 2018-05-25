#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# =============================================

lista = [1, 2, 3]

# Las siguientes estructuras son equivalentes:

for elemento in lista:
    print(elemento)

# ---------------------------------------------

iterador = iter(lista)

while True:
    try:  # También:  iterador.__next__()
        elemento = next(iterador)
        print(elemento)
    except StopIteration:
        break

# ===============================================================

#####     iter()     #####

# Podemos crear iteradores a medida, desde una lista, una clase...

lista6 = ["a", "e", "i", "o", "u"]

iterador = iter(lista6) # Creamos un iterador de una lista

print(next(iterador)) # a
print(next(iterador)) # e
print(next(iterador)) # i
                      # ...

class Rango:
    """ Clase minimalista de la función range()"""
    def __init__(self, min, max):
        self.min = min - 1  # Comienzo de la iteración
        self.max = max      # Final de la iteración

    def __iter__(self):   # Se llama cuando se crea un iter(Rango)
        self.num = self.min
        return self

    def __next__(self):
        if self.num >= self.max:
            raise StopIteration
        self.num += 1
        return self.num

rang = Rango(3, 4)
rang = iter(rang)

try:
    print(next(rang)) # 3
    print(next(rang)) # 4
    print(next(rang)) # raises StopIteration
except StopIteration:
    pass

print(list(rang)) # [3, 4]

"""
A la función iter se le puede pasar un centinela (sentinel)
como segundo parámetro. En el siguiente ejemplo, cuando
lleguemos a una línea en el archivo que sea == '' el iterador
lanzará una StopIteration
"""

with open('fichero.txt') as fp:
    for line in iter(fp.readline, ''):
        processLine(line)

# ===============================================================

    #####     UNA CLASE ITERADORA     #####

class Invertir:
    """Recorre los caracteres de una cadena
    de texto desde el último al primero"""
    def __init__(self, cadena):
        self.cadena = cadena
        self.puntero = len(cadena)

    def __iter__(self):
        return self

    def __next__(self):
        if self.puntero == 0:
            raise(StopIteration)
        self.puntero = self.puntero - 1
        return(self.cadena[self.puntero])

cadena_invertida = Invertir("Hola")

for caracter in cadena_invertida:
    print(caracter, end=" ")      #  a l o H
print("\n")

# ===============================================================

# itertools
# https://docs.python.org/3/library/itertools.html

import itertools

#         Iteradores infinitos

# itertools.count(start, step)
#   Itera por todos los números empezando por
#   el indicado en el parámetro 'start' y va
#   saltando de uno a otro según la diferencia
#   indicada en el parámetro 'step'.
for i in itertools.count(10, 2):  # start, step
    print(i, end=",")    # 10,12,14,16,18,20,
    if i >= 20:
        print("")
        break

# itertols.cycle(iterable)
#   Itera a través de los elementos de un iterable
#   comenzando siempre de nuevo por el principio
#   al llegar al final
word = "XYZ"
turns = 0
for ch in itertools.cycle(word):
    print(ch, end="-")  # X-Y-Z-X-Y-Z-X-Y-Z-
    if ch == word[-1]:
        turns += 1

    if turns >= 3:
        print("")
        break

# itertools.repeat(elem[, times])
#   Devuelve el mismo elemento el número de veces
#   indicado en el parámetro opcional 'times'.
#   Si no se especifica lo devuelve infinitamente.
for elem in itertools.repeat("HOLA", 3):
    print(elem, end="-")   # HOLA-HOLA-HOLA-
print("")

# ----------------------------------------------


"""
Fuentes:
https://www.programiz.com/python-programming/methods/built-in/iter
"""
