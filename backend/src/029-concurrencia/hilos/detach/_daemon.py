#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import threading

# ========================

def contador_interminable():
    i = 1
    while True:
        print(i)
        time.sleep(1)
        i += 1

# Correr un thread en background (daemon=True)
t1 = threading.Thread(target=contador_interminable, daemon=True)

t1.start()

# Saber si un thread está en ejecución
print(t1.isAlive())   # True

# Saber si un thread corre en background
print(t1.isDaemon())  # True
