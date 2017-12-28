#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""En Python, los atributos de las instancias de las clases
se guardan en un diccionariario. Esto puede ser un cuello de
botella en pequeñas clases con atributos conocidos, ya que
creando miles de instancias se gasta mucha RAM

Para evitarlo, podemos usar el método __slots__ para sólo guardar
espacio para un conjunto fijo de atributos:

http://book.pythontips.com/en/latest/__slots__magic.html

"""
class MyClass(object):
    __slots__ = ['name', 'identifier']
    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier
        self.set_up()
    #...