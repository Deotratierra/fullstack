#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Para lanzarlo:

python3 main.py
"""

# pip3 install tornado
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888, address="localhost")
    tornado.ioloop.IOLoop.current().start()
