#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import abc

class Contexto:
    """Mantiene una instancia de una
    subclase EstadoConcreto que define
    el estado actual"""
    def __init__(self, estado):
        self._estado = estado

    def peticion(self):
        self._estado.manejar()

class Estado(metaclass=abc.ABCMeta):
    """Interfaz para encapsular el comportamiento
    asociado a un estado particular del contexto"""

    @abc.abstractmethod
    def manejar(self):
        print("Manejador por defecto")

class EstadoConcretoA(Estado):
    def manejar(self):
        print("Manejador de %s" % self.__class__.__name__)

class EstadoConcretoB(Estado):
    def manejar(self):
        print("Manejador de %s" % self.__class__.__name__)


if __name__ == "__main__":
    estado_concreto_A = EstadoConcretoA()
    contexto = Contexto(estado_concreto_A)
    contexto.peticion()
