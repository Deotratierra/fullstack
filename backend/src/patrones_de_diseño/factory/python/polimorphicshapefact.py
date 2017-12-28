#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

class ShapeFactory:
    factories = {}

    @staticmethod
    def createShape(id):
        # Si no está la fabrica del objeto entre
        # las fábricas creadas
        if not id in ShapeFactory.factories:
            ShapeFactory.factories[id] = \
              eval(id + '.Factory()') # La insertamos
              # Por ejemplo:  Circle.Factory()
        return ShapeFactory.factories[id].create()
        # Creamos el objeto desde su fábrica interna

class Shape(object): pass

class Circle(Shape):
    def draw(self): print("Circle.draw")
    def erase(self): print("Circle.erase")
    class Factory:  # Las fácricas son individuales por objeto
        def create(self): return Circle()

class Square(Shape):
    def draw(self):
        print("Square.draw")
    def erase(self):
        print("Square.erase")
    class Factory:
        def create(self): return Square()

def shapeNameGen(n):
    types = Shape.__subclasses__()
    for i in range(n):
        yield random.choice(types).__name__

shapes = [ ShapeFactory.createShape(i)
           for i in shapeNameGen(7) ]

for shape in shapes:
    shape.draw()
    shape.erase()

""" python3 -i polimorphicshapefact.py

>>> ShapeFactory.factories
{'Square': <__main__.Square.Factory object at 0x7f2ab389a9e8>, 
 'Circle': <__main__.Circle.Factory object at 0x7f2ab37fa898>}
"""
