#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

class Shape(object):
    pass

def factory(type):
    class Circle(Shape):
        def draw(self): print("Circle.draw")
        def erase(self): print("Circle.erase")

    class Square(Shape):
        def draw(self): print("Square.draw")
        def erase(self): print("Square.erase")

    try:
        return eval(type + "()")
    except NameError as e:
        print("Bad shape creation: " + type)
        print(e)

def shapeNameGen(n):
    for i in range(n):
        yield factory(random.choice(["Circle", "Square"]))

# Circle() # Not defined

for shape in shapeNameGen(7):
    shape.draw()
    shape.erase()