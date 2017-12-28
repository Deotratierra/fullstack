#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import abc

class Operacion(metaclass=abc.ABCMeta):
    """Define una operación en dos pasos
    abstractos que cada subclase concretará"""

    # Método plantilla
    def ejecutar(self):
        self.suboperacion_1()
        self.suboperacion_2()

    @abc.abstractmethod
    def suboperacion_1(self):
        pass

    @abc.abstractmethod
    def suboperacion_2(self):
        pass

class OperacionConcreta(Operacion):
    """Implementa las operaciones
    para seguir los pasos del algoritmo
    específicos para esta subclase"""

    def suboperacion_1(self):
        print("Primer paso en la operación")

    def suboperacion_2(self):
        print("Segundo paso en la operación")

if __name__ == "__main__":
    operacion_concreta = OperacionConcreta()
    operacion_concreta.ejecutar()
