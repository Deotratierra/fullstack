#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# La siguiente es una implementación simple
# del patrón memento. En una situación real
# sería más recomendable guardar el estado de la
# clase completa con todos sus atributos con la
# bilioteca estándar copy, función deepcopy(),
# o la función loads() de la bilioteca pickle
# (ver fuentes)

#import copy


class Originador:
    def __init__(self, estado_inicial):
        print("Estado inicial:", estado_inicial)
        self._estado = estado_inicial

    class Memento:
        def __init__(self, m_estado):
            self.m_estado = m_estado

        def retroceder_estado(self):
            return self.m_estado
    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, valor):
        print("Cambio de estado: %s -> %s" % (self.estado, valor))
        self._estado = valor

    @estado.getter
    def estado(self):
        return self._estado

    def guardar_estado(self):
        print("Guardando estado:", self.estado)
        return self.Memento(self.estado)

    def retroceder_estado(self, memento):
        self.estado = memento.retroceder_estado()
        print("Retrocediendo a:", self.estado)


"""python3 -i memento.py

>>> orig = Originador("Estado 1")
Estado inicial: Estado 1
>>> orig.estado
'Estado 1'
>>> orig.estado = "Estado 2"
Cambio de estado: Estado 1 -> Estado 2
>>> orig.estado
'Estado 2'
>>> estado_guardado = orig.guardar_estado()
Guardando estado: Estado 2
>>> orig.estado = "Estado 3"
Cambio de estado: Estado 2 -> Estado 3
>>> orig.retroceder_estado(estado_guardado)
Cambio de estado: Estado 3 -> Estado 2
Retrocediendo a: Estado 2
>>> orig.estado
'Estado 2'

"""


# Fuentes:
# https://gist.github.com/fabiobatalha/5404977
# https://sourcemaking.com/design_patterns/memento/python/1
