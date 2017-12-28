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

with open('mydata.txt') as fp:
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
print("")

# ===============================================================

"""
Fuentes:
https://www.programiz.com/python-programming/methods/built-in/iter
"""
