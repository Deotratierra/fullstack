#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Server configuration file"""

import os
import sys
import hashlib
from motor.motor_tornado import MotorClient

class Config:
    """Main class configuration, 
    persistent along multiples environments"""
    SECRET_KEY = hashlib.sha256(os.environ["COOKIE_SECRET"].encode("utf-8")).digest()


    BASE_DIR = os.path.dirname(__file__)
    LOGS_DIR = os.path.join(BASE_DIR, "log")
    STATIC_PATH = os.path.join(os.path.dirname(BASE_DIR), "build", "static")

    GLOBAL_MODULES = [
        # Folders to append to system path for easy python imports
        os.path.join(BASE_DIR, "global_modules")
    ]

    WATCH = {
        "extensions": ["html", "css", "js", "scss", "jade", "py"],
        "folders": [
            os.path.join(os.path.dirname(BASE_DIR), "src"),
        ],
        "hook_command": "gulp build", # False to not to add hook function
        "debug": False,  # To see files watching or not
    }


    SHOW_ROUTES = True

    DATABASES = {
        "main": {
            "name": os.environ.get("DATABASE_1_NAME", ""),
            "user": os.environ.get("DATABASE_1_USER", ""),
            "password": os.environ.get("DATABASE_1_PASSWORD", ""),
            "host": os.environ.get("DATABASE_1_HOST", ""),
            "port": os.environ.get("DATABASE_1_PORT", ""),
            "uri_schema": os.environ.get("DATABASE_1_URI_SCHEMA", "")
        }
    }
    
    XSRF = True
    SSL = {
        "enabled": False,
        "certfile": None,
        "keyfile": None
    }

    def __init__(self):
        self.DB = self.mongodb_uri_builder(self.DATABASES)

    def mongodb_uri_builder(self, databases):
        """MongoDB uri builder"""
        database_names = list(databases.keys())
        for db in database_names:
            settings = databases[db]
            db_uri = settings["uri_schema"] % (settings["user"],
                                           settings["password"],
                                           settings["host"],
                                           settings["port"],
                                           settings["name"])
            databases[db] = MotorClient(db_uri)[settings["name"]]
        return databases


class DevelopmentConfig(Config):
    """Development configuration class"""
    DEBUG = True
    SERVER_HOST = "localhost"
    SERVER_PORT = int(os.environ["SERVER_PORT"])
    DOMAIN = "http://{}:{}".format(SERVER_HOST, SERVER_PORT)

    def __init__(self):
        super(DevelopmentConfig, self).__init__()


class StagingConfig(Config):
    """Staging configuration class"""
    DEBUG = True
    SERVER_HOST = "0.0.0.0"
    SERVER_PORT = int(os.environ["SERVER_PORT"])
    DOMAIN = "http://{}:{}".format(SERVER_HOST, SERVER_PORT)

    def __init__(self):
        super(StagingConfig, self).__init__()


class ProductionConfig(Config):
    """Production configuration class"""
    DEBUG = False
    SERVER_HOST = "0.0.0.0"
    SERVER_PORT = int(os.environ["SERVER_PORT"])
    DOMAIN = "http://{}:{}".format(SERVER_HOST, SERVER_PORT)
    
    def __init__(self):
        super(ProductionConfig, self).__init__()


# Environments configs mapping
ENVIRONMENTS = {
    "development": DevelopmentConfig,
    "stage": StagingConfig,
    "production": ProductionConfig
}


# ======    GLOBAL MODULES   =======

for path in Config.GLOBAL_MODULES:
    sys.path.append(path)

# ==================================
