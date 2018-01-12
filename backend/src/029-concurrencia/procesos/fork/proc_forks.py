#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Para una explicación detallada del funcionamiento ver ejemplo en C"""

import os

if __name__ == "__main__":
    print("El proceso principal del programa es %d" % os.getpid())

    # Crear una bifurcación (fork)
    child_pid = os.fork()
    if child_pid != 0:
        print("Este es el proceso padre (PID: %d)" % os.getpid())
        print("El ID del proceso hijo es %d" % child_pid)
    else:
        print("Este es el proceso hijo (PID: %d)" % os.getpid())
        print("La variable child_pid desde el proceso hijo es %d" % child_pid)  # 0
