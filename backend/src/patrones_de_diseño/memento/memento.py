#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
La siguiente es una implementación simple
  del patrón memento. En una situación real
  sería más recomendable guardar el estado de la
  clase completa con todos sus atributos con la
  bilioteca estándar copy, función deepcopy(),
  o la función loads() de la bilioteca pickle (ver fuentes)
"""
#import copy

class Originador:
    def __init__(self, estado_inicial):
        print("Estado inicial:", estado_inicial)
        self._estado = estado_inicial

    class Memento:
        """Esta implementación guarda el estado
        anterior del objeto dentro de la clase, para
        además proveer un método para volver al estado
        que tenía la clase antes de guardarlo.
        """
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

# ---------------------------------------------

import pickle

class OriginadorBasadoEnPickle:
    def __init__(self, a=5, b=10):
        self.a = a
        self.b = b

    def set_memento(self, memento):
        previous_state = pickle.loads(memento)

        # Eliminamos los atributos de la
        #  instancia (self.a y self.b)
        vars(self).clear()
        # Los actualizamos con el estado previo
        vars(self).update(previous_state)

    def create_memento(self):
        # Devolvemos una representación en bytes
        #   de los atributos de la instancia
        return pickle.dumps(vars(self))

"""python3 -i memento.py

>>> originator = OriginadorBasadoEnPickle()
>>> memento = originator.create_memento()

>>> memento
b'\x80\x03}q\x00(X\x01\x00\x00\x00bq\x01K\nX\x01\x00\x00\x00aq\x02K\x05u.'

>>> originator.a = 2
>>> originator.b = 3

>>> originator.set_memento(memento)
>>> originator.a
5
>>> originator.b
10
"""


# Fuentes:
# https://gist.github.com/fabiobatalha/5404977
# https://sourcemaking.com/design_patterns/memento/python/1
