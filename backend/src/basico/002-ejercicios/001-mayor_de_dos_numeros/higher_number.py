#!/usr/bin/env python3
# -*- coding: utf-8 -*-

num1, num2 = (3, 5) # Asignación múltiple

def mayor(a, b):
    if a >= b:
        return a
    else:
        return b


print(mayor(num1, num2))

'''
Más fácil:

max(num1, num2)
'''

