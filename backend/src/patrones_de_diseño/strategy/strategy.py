#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import abc

class Contexto:
    """Interfaz de interés para los clientes"""
    def __init__(self, estrategia):
       self._estrategia = estrategia

    def ejecutar(self):
       self._estrategia.algoritmo()

class Estrategia(metaclass=abc.ABCMeta):
    """Declaramos una interfaz común a todos
    los algoritmos soportados. El Contexto usa
    esta interfaz para llamar al algoritmo
    definido en EstrategiaConcreta"""

    @abc.abstractmethod  # Método abstracto
    def algoritmo(self):
        print("Algoritmo por defecto")

class EstrategiaConcretaA(Estrategia):
    def algoritmo(self):
        print("Algoritmo de", self.__class__.__name__)

class EstrategiaConcretaB(Estrategia):
    def algoritmo(self):
        print("Algoritmo de", self.__class__.__name__)


if __name__ == "__main__":
    estrategia_concreta_A = EstrategiaConcretaA()
    contexto = Contexto(estrategia_concreta_A)
    contexto.ejecutar()


"""
  Fuentes:
https://sourcemaking.com/design_patterns/strategy/python/1
https://stackoverflow.com/questions/963965/how-to-write-strategy-pattern-in-python-differently-than-example-in-wikipedia
"""
