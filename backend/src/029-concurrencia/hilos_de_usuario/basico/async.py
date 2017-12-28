#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Para ejecutar rutinas asíncronas en Python
podemos usar la biblioteca asyncio""" # python >= 3.5
import asyncio
from time import time

# Primero obtenemos el loop donde correrán las tareas
loop = asyncio.get_event_loop()

# Podemos preparar tareas para que se ejecuten cuando empiece el loop
# Una corrutina simple
async def tarea():
    print("Dentro de la tarea simple.")
    return await asyncio.sleep(3)

task1 = asyncio.ensure_future(tarea())
task2 = asyncio.ensure_future(tarea())
tasks = [task1, task2]

# Programamos el loop para que se ejecuten las tareas
# en cuanto empiece a correr:
#loop.call_soon(functools.partial(asyncio.wait, tasks))

try:     # Lanzamos la ejecución del bucle
    t1 = time()
    loop.run_until_complete(asyncio.wait(tasks))
except KeyboardInterrupt:
    loop.stop()
    print("Se cortó el loop en tiempo de ejecución.")
finally:
    t2 = time()
    print("Se terminaron de ejecutar las tareas")
    print("Ha tardado: %s segundos" % str(t2-t1))
