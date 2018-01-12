#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web
from tornado.web import asynchronous
from tornado.httpclient import AsyncHTTPClient

# http://www.tornadoweb.org/en/stable/gen.html

# Gracias a tornado.gen podemos simplificar el uso de corrutinas en tornado
import tornado.gen

url = "https://www.google.com"
urls_list = ["https://steemit.com/@mondeja",
             "http://www.tornadoweb.org/en/stable/gen.html",
             "https://www.google.com",
             "https://github.com/mondeja"]

# ===========================================================================

# Interfaz estándar para realizar una petición asíncrona
class ManejadorAsincrono(tornado.web.RequestHandler):
    @asynchronous
    def get(self):
        cliente_HTTP = AsyncHTTPClient()
        response = cliente_HTTP.fetch(url, callback=self.on_fetch)
        print(response)  # <tornado.concurrent.Future object at 0x7f71f6a4be80>

    def on_fetch(self, response):
        return self.finish("Número de caracteres: %d" % len(response.body))

# Interfaz basada en generador
class GeneradorManejadorAsincrono(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def get(self):
        cliente_HTTP = AsyncHTTPClient()
        response = yield cliente_HTTP.fetch(url) # Resultado del futuro
        return self.finish("Número de caracteres: %d" % len(response.body))

# ===========================================================================

# Podemos usar yield con varias corrutinas a la vez
class GeneradorManejadorAsincronoMultiple(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def get(self):
        cliente_HTTP = AsyncHTTPClient()
        # Todas las llamadas detrás de yield corren en paralelo
        response1, response2 = yield [cliente_HTTP.fetch(urls_list[0]),
        	                          cliente_HTTP.fetch(urls_list[1])]
        response_dict = yield dict(response3=cliente_HTTP.fetch(urls_list[2]),
        	                       response4=cliente_HTTP.fetch(urls_list[3])
        	                       )
        response = (len(response1.body), len(response2.body),
        	        len(response_dict["response3"].body),
        	        len(response_dict["response4"].body))
        print(response)
        return self.finish("Números de caracteres: %d, %d, %d, %d" % response)


def make_app():
    return tornado.web.Application([
        (r"/callback_estandar", ManejadorAsincrono),
        (r"/callback_con_generador", GeneradorManejadorAsincrono),
        (r"/callback_con_generador_multiple", GeneradorManejadorAsincronoMultiple),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888, address="localhost")
    loop = tornado.ioloop.IOLoop.current()
    loop.start()


"""
>>> from requests import get
>>> get("http://localhost:8888/callback_estandar").text
'Número de caracteres: 47177'
>>> get("http://localhost:8888/callback_con_generador").text
'Número de caracteres: 47183'
>>> get("http://localhost:8888/callback_con_generador_multiple").text
'Números de caracteres: 382107, 66922, 47189, 84878'
"""