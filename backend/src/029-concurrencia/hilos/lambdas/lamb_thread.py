#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import threading

workers = []

for i in range(1, 6):
    workers.append(
        threading.Thread(target=lambda arg: print("Dentro del hilo número %d" % arg),
                         args=[i])
    )

# Los hilos se ejecutan de forma ordenada
for t in workers:
    t.start()
