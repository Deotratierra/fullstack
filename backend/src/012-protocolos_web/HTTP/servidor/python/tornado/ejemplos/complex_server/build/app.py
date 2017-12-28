#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""App main module for server"""

import os
import sys
from pprint import pprint

from tornado.web import Application
from tornado.ioloop import IOLoop
import tornado.options

from config import ENVIRONMENTS as environments
from router import MainRouter as Router
from watcher import AutoreloadWatcher
from logger import Logger

class App(Application):
    """Main application class"""
    config = environments[os.environ["APP_SETTINGS"]]() # Config __init__

    def __init__(self):
        self.loop = IOLoop.current()
        self.router = Router(self.config)
        self.watcher = AutoreloadWatcher(self.config)
        self.logger = Logger(self.config, self.loop)
        
        # ========================================

        #   Application attrs
        self.db = self.config.DB   # Databases global access
        self.server_host = self.config.SERVER_HOST
        self.server_port = self.config.SERVER_PORT
        self.domain = self.config.DOMAIN

        # =============   SETTINGS   ==============

        self.settings = {
            "debug": self.config.DEBUG,
            "cookie_secret": self.config.SECRET_KEY,
            "xsrf_cookies": self.config.XSRF,
        }

        ssl_options = {
            "certfile": self.config.SSL["certfile"],
            "keyfile": self.config.SSL["keyfile"]
        } if self.config.SSL["enabled"] else None
        
        if self.config.DEBUG: self.show_settings()

        # =========================================

        super(App, self).__init__(self.router.routes, **self.settings,
                                  ssl_options=ssl_options)

    def start(self):
        """Start application method"""
        self.logger.schedule_loggers_filename_updates()
        return self.loop.start()   

    def show_settings(self):
        """Function to log and show settings before start server"""
        ignore_keys = ["DB", "DEBUG", "SECRET_KEY"]
        show_config = {}
        all_settings = self.settings
        config_settings = {key: getattr(self.config, key) \
            for key in dir(self.config) if not callable(getattr(self.config, key))}
        all_settings.update(config_settings)
        for key, value in all_settings.items():
            if "__" not in key and key not in ignore_keys:
                show_config[key] = value

        self.logger.general.debug("App started with configuration: %s", 
                                  str(show_config))

        if self.config.DEBUG:
            legend = "  (Tornado settings in lowercase)"
            print("\n=========   APP SETTINGS   ========== %s" % legend)
            pprint(show_config)
            print("=====================================\n")

    
