#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Lanzar una tarea en background con Tornado"""

import tornado.ioloop
import tornado.web
import functools
from time import sleep

loop = tornado.ioloop.IOLoop.current()

def terminar_conexion(self):
    self.write("Terminada la conexión")

# ==========================================================

class TareaSinArgumentos(tornado.web.RequestHandler):
    def get(self):
        loop.spawn_callback(self.tarea)  # Sin argumentos

        terminar_conexion(self)

    def tarea(self):
        sleep(3) # El callback se muestra con retraso
        # cuando la conexión ya ha sido devuelta
        print("Tarea sin argumentos")

class TareaConArgumentos(tornado.web.RequestHandler):
    def get(self):
        # Con argumentos
        tarea = functools.partial(self.tarea_con_argumentos,
        	                      "ARGUMENTO", 2, False)
        loop.spawn_callback(tarea)

        terminar_conexion(self)

    def tarea_con_argumentos(self, *args):
        sleep(2)
        print("Tarea con argumentos:", args)

# ===========================================================

def make_app():
    return tornado.web.Application([
        (r"/tarea", TareaSinArgumentos),
        (r"/tarea_con_argumentos", TareaConArgumentos)
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888, address="localhost")
    loop.start()


# Se produce un delay entre el retorno de la petición
# y la impresión en el servidor
"""
>>> from requests import get
>>> get("http://localhost:8888/tarea").text
'Terminada la conexión'
>>> get("http://localhost:8888/tarea_con_argumentos").text
'Terminada la conexión'
"""