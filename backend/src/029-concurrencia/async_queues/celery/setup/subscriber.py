# -*- coding: utf-8 -*-

from celery import Celery   # pip3 install celery

# Creamos una aplicación de Celery para la conexión
app = Celery('tasks',
	         broker='redis://localhost:6379/0',  # 6379 es el puerto por defecto de Redis
	         backend='redis://localhost:6379/0') # puedes comprobar que está corriendo ejecutando:
                                                 #    redis-cli ping

if __name__ == "__main__":
    # Lanzamos tareas a la aplicación
    promise = app.send_task('tasks.multiplicar', args=[2, 2])

    # Obtenemos los resultados
    print(promise.get())   # 4
