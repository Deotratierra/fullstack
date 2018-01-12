#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from multiprocessing import Pool

def exp2(x):
    return x*x

# Creamos una psicina con 5 procesos como máximo
with Pool(5) as pool:
    print(pool.map(exp2, [1, 2, 3])) # [1, 4, 9]

# ==============================================

import os
from multiprocessing import Process

def hola(nombre):
    print("Hola %s" % nombre)
    # Obtener el pid del proceso padre
    print(os.getppid())
    # Obtener el pid del proceso
    print(os.getpid())

# Creación de un proceso con argumentos
proceso = Process(target=hola, args=("Paco",))

# Lanzar un proceso 
proceso.start()

# Esperar a que termine un proceso
proceso.join()

# ==============================================

"""
Fuente:
https://docs.python.org/3/library/multiprocessing.html
"""

