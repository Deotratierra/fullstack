#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Función definida en código Python,
# sólo es posible llamarla desde Python
def py_interpreted_factorial(n):
    """Calcula el factorial del número pasado como parámetro."""
    if n <= 1:
        return 1
    return n * py_interpreted_factorial(n-1)
