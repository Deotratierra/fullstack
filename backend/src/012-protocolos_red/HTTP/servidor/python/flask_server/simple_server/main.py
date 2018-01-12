#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Para lanzar el servidor (host 127.0.0.1, port 5000):

export FLASK_APP=simple_server.py
flask run

----------------------------------------------------

Abajo podemos configurar afitrión y puerto, para lanzarlo:

python3 simple_server.py
"""

# pip3 install Flask
from flask import Flask
app = Flask(__name__)


@app.route("/")  # Ruteo mediante decoradores
def hello_world():
    return "Hola mundo en Flask!"

if __name__ == '__main__':
    app.run(host='localhost', port=8765)

"""
Referencia:
http://flask.pocoo.org/docs/0.12/api/
"""
