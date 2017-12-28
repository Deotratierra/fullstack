#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from requests import get       # pip3 install requests
from bs4 import BeautifulSoup  # pip3 install bs4
from pprint import pprint as pp

# https://www.crummy.com/software/BeautifulSoup/bs4/doc/

html_doc = "<div><h4>Hola Mundo</h4></div>"
url = "https://www.sport.es/es/resultados/la-liga/estadisticas/"

# ===============   Cargar documentos   ====================

# Cargar un documento html
soup = BeautifulSoup(html_doc, "html.parser")

# Mostrar HTML de forma leíble
print(soup.prettify())

# Cargar una página web
soup = BeautifulSoup(get(url).content, "html.parser")


# ===============   Comandos básicos   =====================

# Obtener todo el texto de una página
soup.get_text()

# Obtener el título
print(soup.title)  # <title>Estadisticas - Liga Santander - 2017-2018</title>

# Contenido de una etiqueta
print(soup.title.string)  # Estadisticas - Liga Santander - 2017-2018

# Nombre de una etiqueta
print(soup.title.name)    # title

# Buscar todos los elementos de un tipo
soup.find_all("a")

# Buscar por clase
soup.find_all(class_="clase")

# Buscar por identificador
soup.find(id="identificador")

# Acceder a los valores del atributo de un elemento
print(soup.find("button")["class"])  # ['icon-lupa']

# Acceder a todos los atributos de un elemento con sus valores
print(soup.find("button").attrs)     # {'type': 'submit', 'class': ['icon-lupa']}


# ===============   Navegando el árbol de elementos   ==================

# Acceder a los elementos dentro de una etiqueta en una lista
soup.head.contents

# Acceder a los elementos dentro de una etiqueta con un generador
pp(soup.head.children)  # <list_iterator object at ... >

"""Los métodos anteriores sólo acceden a los hijos directos,
para acceder a todo el árbol de hijos usamos: """
pp(soup.head.descendants)  # <generator object descendants at ... >

# ---------------------------------------------

# Acceder al padre
print(soup.title.parent.name)  # head

# Acceder a los padres recursivamente
pp(soup.title.parents)   # <generator object parents at ... >

# ---------------------------------------------

# Acceder al hermano siguiente
soup.title.next_sibling

# Acceder al hermano anterior
soup.title.previous_sibling

