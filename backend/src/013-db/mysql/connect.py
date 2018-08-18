#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# sudo apt-get install python-mysqldb
# sudo apt-get install python3-dev libmysqlclient-dev
# pip3 install mysqlclient
from sqlalchemy import *

USER = "root"
PASSWORD = ""
HOST = "localhost"
PORT = 3306
DATABASE_NAME = ""

URL = "mysql://%s:%s@%s:%d/%s?charset=utf8" % (USER, PASSWORD, HOST, PORT, DATABASE_NAME)
engine = create_engine(URL, pool_recycle=PORT)

with engine.connect() as db:
    print(db)

"""
Fuente:
https://es.stackoverflow.com/questions/34346/como-conectarme-con-sqlalchemy-a-una-basededatos
"""
