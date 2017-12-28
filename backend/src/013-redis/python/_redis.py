#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import redis   # pip3 install redis
# Aquí está la documentación:
# https://pypi.python.org/pypi/redis

# Es conveniente instalar tambien hiredis:
# pip3 install hiredis


rdb = redis.StrictRedis(host="localhost", port=6379, db=0)

rdb.set("foo", "bar")

# La respuesta viene en formato bytes
response = rdb.get("foo")
print(response.decode())

# Abre en otra consola redis-cli y ejecuta
# monitor antes de correr este script
