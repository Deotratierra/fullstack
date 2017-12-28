#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ============================================

# Implementación de una clase Singleton

class Singleton:
    instance = None
    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = object.__new__(cls, *args, **kwargs)
        return cls.instance


# ============================================

# Implementación de Singleton como metaclase

class MetaSingleton(type):

    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


# ============================================


class MiClase(metaclass=MetaSingleton): pass


if __name__ == "__main__":
    c1 = Singleton()
    c2 = Singleton()
    print(c1 is c2)
    print(c1 == c2)

    print()

    c3 = MiClase()
    c4 = MiClase()
    print(c1 is c2)
    print(c1 == c2)
