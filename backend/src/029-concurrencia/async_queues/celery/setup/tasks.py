# -*- coding: utf-8 -*-

"""Este script crea una aplicación de Celery que espera
a que le lleguen tareas y las va ejecutando."""

# Para lanzar este script ejecutamos:
# celery -A tasks worker -l info

# ===========================================================

from celery import Celery   # pip3 install celery

# Creamos una aplicación de Celery
app = Celery('tasks',
	         broker='redis://localhost:6379/0',  # 6379 es el puerto por defecto de Redis
	         backend='redis://localhost:6379/0') # puedes comprobar que está corriendo ejecutando:
                                               #    redis-cli ping

# Creamos las tareas
@app.task
def multiplicar(x, y):
    return x * y
