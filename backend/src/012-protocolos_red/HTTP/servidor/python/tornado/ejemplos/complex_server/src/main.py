#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Server starter module"""

from tornado.httpserver import HTTPServer

from utils.printers import verboser, success

from app import App

def main():
    """Starter function"""
    application = App()
    http_server = HTTPServer(application)

    http_server.listen(application.server_port, address=application.server_host)
    success("Server listening at %s:%d" % (
    	   application.server_host, application.server_port))

    try:
        application.start()
    except KeyboardInterrupt:
        verboser("\nStopping server...")
        application.loop.stop()


if __name__ == "__main__":
    verboser("Starting server...")
    main()
