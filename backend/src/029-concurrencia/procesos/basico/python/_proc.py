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


print()
# ==============================================

"""Podemos crear un proceso como una clase"""

class Proceso(Process):
    def __init__(self, arg1):
        super(Proceso, self).__init__()
        self.arg1 = arg1

    # Dentro de esta método irá el código que ejecutará
    def run(self):
        msg_schema = "Hola soy un proceso desde clase con argumento %r, my PID es %d"
        print(msg_schema % (self.arg1, os.getpid()))

p = Proceso(True)
p.start()
p.join()


"""
Fuentes:
https://docs.python.org/3/library/multiprocessing.html
"""

