# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web

# Reenviando el puerto 80 al 8001 en el router
PORT = 8001

# 0.0.0.0 A la red externa
ADDRESS = "0.0.0.0"

class BaseAPIRequestHandler(tornado.web.RequestHandler):
    """Base handler for all API requests"""
    @property
    def request_arguments(self):
        """Return all arguments of a request in a dict"""
        response = {}
        for key in self.request.arguments:
            value = self.get_argument(key)
            if value != "":
                response[key] = value
        return response

class MainHandler(BaseAPIRequestHandler):
    def post(self):
        args = self.request_arguments
        if args["id"]:
            print("Llego una petición POST con el id '%s'." % args["id"])
        return self.write("OK\n")

class TestHandler(BaseAPIRequestHandler):
    def get(self):
        return self.write("OK\n")

def make_app():
    return tornado.web.Application([
        (r"/log", MainHandler),
        (r"/", TestHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(PORT, address=ADDRESS)
    tornado.ioloop.IOLoop.current().start()

