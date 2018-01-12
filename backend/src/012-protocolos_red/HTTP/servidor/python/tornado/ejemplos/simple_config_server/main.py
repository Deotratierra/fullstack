#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Modelo de una configuración compleja en tornado,
con certificados SSL, cookies XSRF y más...

Esta implementación no recoge ninguna clase de petición.
"""

from tornado.ioloop import IOLoop
from tornado.web import Application
from tornado.httpserver import HTTPServer
from tornado.options import parse_command_line

# Cargar diferentes tipos de configuración mediante variable de entorno
exec('from config import %s as config' % os.environ['APP_SETTINGS'])
from router import handlers    # Router en un archivo aparte

class App(Application):
    def __init__(self):
        settings =  {"debug": config.DEBUG,
            "static_path": config.STATIC_PATH,
            "cookie_secret": config.SECRET_KEY,
            "login_url": "/login",
            "template_path": config.TEMPLATE_PATH,
            "db": config.DB,
            "host": config.HOST,
            "port": config.PORT,
            "xsrf_cookies": True,
            "web_url": config.WEB_URL}
        ssl_options = {"certfile": "certificado.crt", 
                       "keyfile": "clave.key"}
        super(App, self).__init__(handlers, **settings, 
                                  ssl_options=ssl_options)


if __name__ == '__main__':
    parse_command_line()
    http_server = HTTPServer(App())
    http_server.listen(config.PORT, address=config.HOST)

    msg = "Servidor escuchando en http://{}:{}"
    print(msg.format(config.HOST, config.PORT))
    try:
        IOLoop.current().start()
    except KeyboardInterrupt:
        verboser("\nCerrando el servidor...")
