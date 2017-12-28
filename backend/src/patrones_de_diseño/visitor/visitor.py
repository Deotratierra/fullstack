#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Demostración del patrón visitor en Python3"""

import random

class NoModificable: pass

# Las superclases de Flor no pueden ser modificadas:
class Flor(NoModificable):
    def aceptar(self, visitante): # Visitor (nombre en inglés del patrón)
        visitante.visitar(self)
    def polinizar(self, polinizador):
        print(self, "polinizado por", polinizador)
    def depredar(self, depredador):
        print(self, "depredado por", depredador)
    def __str__(self):
        return self.__class__.__name__

class Gladiolo(Flor): pass
class Tulipan(Flor): pass
class Crisantemo(Flor): pass

class Visitante:
    def __str__(self):
        return self.__class__.__name__

class Insecto(Visitante): pass
class Polinizador(Insecto): pass
class Depredador(Insecto): pass


class Abeja(Polinizador):
    def visitar(self, flor):
        flor.polinizar(self)

class Mosquito(Polinizador):
    def visitar(self, flor):
        flor.polinizar(self)

class Gusano(Depredador):
    def visitar(self, flor):
        flor.depredar(self)


def flowerGen(n):
    flores = Flor.__subclasses__()
    for i in range(n):
        yield random.choice(flores)()

abeja = Abeja()
mosquito = Mosquito()
gusano = Gusano()

for flor in flowerGen(10):
    flor.aceptar(abeja)
    flor.aceptar(mosquito)
    flor.aceptar(gusano)
