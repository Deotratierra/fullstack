#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pymongo import MongoClient # pip3 install pymongo

USER, PASSWORD = ("", "")
HOST, PORT = ("", "")
DATABASE_NAME = ""

URI = "mongodb://%s:%s@%s:%d/%s" + (USER, PASSWORD, HOST, PORT, DATABASE_NAME)

mongo = MongoClient(URI)
db = mongo[DATABASE_NAME]

"""
Modelo de ruta en mlab.com:

mongodb://<dbuser>:<dbpassword>@ds119395.mlab.com:19395/<dbname>

------------------------------------------------

Ejemplo de conexión para la ruta anterior:

USER, PASSWORD = (<dbuser>, <dbpassword>)
HOST, PORT = ("ds119395.mlab.com", 19395)
DATABASE_NAME = <dbname>
"""


