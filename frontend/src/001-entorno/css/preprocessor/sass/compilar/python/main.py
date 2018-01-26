#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sass  # pip3 install libsass

ORIGEN = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__),
	         os.pardir)), "example.scss")
DESTINO = os.path.join(os.path.dirname(__file__), "example.css")


# Leemos el archivo origen
with open(ORIGEN, "r") as scss:
    scss_content = scss.read()

# Compilamos el código
css_content = sass.compile(string=scss_content,
	                       output_style='compressed')  # Estilo minificado

# Lo guardamos en el archivo de destino
with open(DESTINO, "w") as css:
    css.write(css_content)
