#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

num = float(input("Introduce un número: "))
print("")

# Raíz cuadrada
calc = math.sqrt(num)
print("\tRaíz cuadrada = %.2f" % calc)

# Próximo entero hacia arriba
calc = math.ceil(num)  # 6
print("\tPróximo entero hacia arriba = %.2f" % calc)

# Próximo entero hacia abajo
calc = math.floor(num)
print("\tPróximo entero hacia abajo = %.2f" % calc)

# Valor absoluto
calc = math.fabs(num)
print("\tValor absoluto = %.2f" % calc)

# Factorial (sólo acepta enteros)
calc = math.factorial(num)
print("\tFactorial = %.2f" % calc)

# Logaritmo natural
calc = math.log(num)
print("\tLogaritmo natural = %.2f" % calc)

# Logaritmo en base 10
calc = math.log10(num)
print("\tLogaritmo en base 10 = %.2f" % calc)

"""
Fuentes:
https://docs.python.org/3.1/library/math.html
"""
