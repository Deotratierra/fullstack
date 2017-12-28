#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import threading

# =====================================

def contador():
    for i in range(1, 6):
        print(i)
        time.sleep(1)

# Crear hilos
t1 = threading.Thread(target=contador)
t2 = threading.Thread(target=contador)

# Iniciar la ejecución
t1.start()
t2.start()

# Esperar a que se ejecuten los hilos
t1.join()
t2.join()

print("Fin de la ejecución")

# =====================================

# Obtener el hilo actual
actual = threading.current_thread()

# Obtener el hilo principal
principal = threading.main_thread()

# Lista con los hilos activos
hilos = threading.enumerate()

# Número de hilos activos
threading.active_count() # 1

# Identificador del hilo actual
threading.get_ident()

# ====================================

# Fuente:
# https://docs.python.org/3/library/threading.html
