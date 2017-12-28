#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from timeit import timeit

py = timeit("lib_py.summa(100)", setup="import lib_py", number=10000)
cy = timeit("lib_cy.summa(100)", setup="import lib_cy", number=10000)

print(py, cy)
print("Cython es %f veces más rápido" % float(py/cy))
