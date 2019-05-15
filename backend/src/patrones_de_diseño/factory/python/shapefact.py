#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Fuente:
# http://python-3-patterns-idioms-test.readthedocs.io/en/latest/Factory.html

import random

class Shape(object):
    # Creación basada en el nombre de la clase:
    @staticmethod
    def factory(shape_type):
        try:
            return eval(shape_type + "()")
        except NameError as e:
            print("Bad shape creation: %s" % shape_type)
            print(e)

        #if type == "Circle": return Circle()
        #if type == "Square": return Square()
        #raise Exception("Bad shape creation: " + type)

class Circle(Shape):
    def draw(self): print("Circle.draw")
    def erase(self): print("Circle.erase")

class Square(Shape):
    def draw(self): print("Square.draw")
    def erase(self): print("Square.erase")

# Genera los nombres de clase al azar:
def shapeNameGen(n):
    types = Shape.__subclasses__()
            #[<class '__main__.Circle'>, 
            # <class '__main__.Square'>]
    for i in range(n):
        yield random.choice(types).__name__

shapes = \
  [ Shape.factory(i) for i in shapeNameGen(7)]

for shape in shapes:
    shape.draw()
    shape.erase()