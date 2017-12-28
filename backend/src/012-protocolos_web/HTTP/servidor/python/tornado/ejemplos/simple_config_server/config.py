#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, hashlib
basedir = os.path.abspath(os.path.dirname(__file__))

#from pymongo import MongoClient
from motor.motor_tornado import MotorClient

class Config(object):
    SECRET_KEY = hashlib.sha256(os.environ["COOKIE_SECRET"].encode("utf-8")).digest()
    DB = { 
        DB_NAME: MotorClient(os.environ["MONGODB_URI"] % (os.environ["MONGODB_USERNAME"], 
                                                            os.environ["MONGODB_PASSWORD"],
                                                            DB_NAME))
    }
    STATIC_PATH = os.path.join(os.path.dirname(__file__), "static/")
    TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), "pages/")

class ProductionConfig(Config):
    DEBUG = False
    PORT = os.environ["PORT"]
    HOST = "0.0.0.0"
    WEB_URL = ""
    #MAIL_HOST = "smtp.sendgrid.com"
    #SENDGRID_API_KEY = ""


class StagingConfig(Config):
    DEBUG = True
    PORT = os.environ["PORT"]
    HOST = "0.0.0.0"
    WEB_URL = ""
    #MAIL_HOST = 'smtp.sendgrid.com'
    #SENDGRID_API_KEY = ""


class DevelopmentConfig(Config):
    DEBUG = True
    PORT = os.environ["PORT"]
    HOST = "localhost"
    WEB_URL = "http://{}:{}".format(HOST, PORT)
    #MAIL_HOST = "smtp.gmail.com"
