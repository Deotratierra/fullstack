#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import queue
# https://docs.python.org/3/library/queue.html

# ====================================================================


# Creación de una cola FIFO
qfifo = queue.Queue(maxsize=10) # Si el tamaño máximo es 0 o menor, es infinita

# Insertar un elemento en la cola
qfifo.put("hola")  # Se le puede pasar un timeout par aque bloquee hasya que haya espacio

# Obtener un elemento de la cola
print(qfifo.get())  # hola

# Saber el tamaño de la cola
print(qfifo.qsize()) # 0

# Saber si la cola está llena
print(qfifo.full()) # False

# Saber si la cola está vacía
print(qfifo.empty()) # True

print()

# ===================================================================

"""
Las colas en Python son especialmente útiles en programación de hilos,
cuando la información debe ser intercambiada de forma segura entre
múltiples hilos.
Por ello las clases del módulo queue implementan métodos especiales para
trabajar con tareas:
"""

# Saber si la última tarea de la cola ha sido procesada
#qfifo.task_done()  # Levanta ValueError si se llama más veces que elementos contiene

# Bloquear hasta que todos los elementos de la cola han sido procesados
#qfifo.join()

# ===================================================================

# Ejemplo

import os
import signal
import threading
from random import randint

def procesar(elem):
    return elem**3

def trabajador():  # Siempre lo verás como "worker()"
    while True:
        elem = qfifo.get()
        if elem == None:
            break
        resultado = procesar(elem)
        resultados.append(resultado)
        qfifo.task_done()  # Bloquea hasta que el elemento ha sido procesado

num_trabajadores = 1
resultados = []

hilos = []
for i in range(num_trabajadores):
    hilo = threading.Thread(target=trabajador)
    hilo.start()
    hilos.append(hilo)

# Agregamos números al azar a la cola
for num in range(30):
    qfifo.put(randint(0, 100))

# Detiene los trabajadores
for i in range(num_trabajadores):
    qfifo.put(None)
for hilo in hilos:
    hilo.join()

print(resultados)

# Los hilos no mueren, el programa se queda abierto

# =================================================================
