#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Main application router"""
import os
from pprint import pprint

from tornado.web import StaticFileHandler

class MainRouter:
    """Application router, load here
    all static files and subrouters"""
    routes = [

    ]

    def __init__(self, config):
        self.config = config

        if self.config.DEBUG:
            self.load_static_routes()
        self.load_subrouters()

        # Show routes if self.config.SHOW_ROUTES == True
        # (You can disable it in config.py)
        self.show_routes()
    
    def load_static_routes(self):
        """Load static files in development environment
        With this configuration, static files aren't cached
        ¡Use nginx in production!
        http://www.tornadoweb.org/en/stable/guide/running.html#static-files-and-aggressive-file-caching
        """
        static_routes = [
            (r"/css/(.*)", StaticFileHandler,
             {"path": os.path.join(self.config.STATIC_PATH, "css")}),
            (r"/js/(.*)", StaticFileHandler,
             {"path": os.path.join(self.config.STATIC_PATH, "js")}),
            (r"/fonts/(.*)", StaticFileHandler,
             {"path": os.path.join(self.config.STATIC_PATH, "fonts")}),

            (r"/scenes/(.*)", StaticFileHandler,
             {"path": os.path.join(self.config.BASE_DIR, "scenes")}),
        ]

        [self.routes.append(route) for route in static_routes]


    def load_subrouters(self):
        """Load subrouters for every scene"""
        from scenes.admin import AdminRouter
        from services.api import APIRouter

        subrouters = [
            AdminRouter("/admin"),
            APIRouter("/api")
        ]
        for subrouter in subrouters:
            for route in subrouter.routes:
                self.routes.append(route)

    def show_routes(self):
        """Show routes if Config.SHOW_ROUTES == True
        (You can disable it in config.py)"""
        if self.config.SHOW_ROUTES:
            print("\n=======   ROUTER   =======\n")
            for route in self.routes:
                pprint(route)
                print()
            print("=========================\n")
