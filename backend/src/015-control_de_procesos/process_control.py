#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import signal
import psutil  # pip3 install psutil
# http://psutil.readthedocs.io/en/latest/

# Objetos Process de la biblioteca psutil:
# http://psutil.readthedocs.io/en/latest/#psutil.Process

# Obtener los procesos corriendo por objetos Process
procesos = [proc for proc in psutil.process_iter()]

# Obtener los procesos corriendo por pid
PIDS = psutil.pids()

# Saber si un proceso existe por pid
psutil.pid_exists(PIDS[0])

# Matar un proceso por pid
os.kill(pid, signal.SIGKILL)

# Esperar que terminen una lista de procesos
psutil.wait_procs(procs, timeout=30)

