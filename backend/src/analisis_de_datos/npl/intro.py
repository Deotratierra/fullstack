# -*- coding: utf-8 -*-

import nltk   # pip3 install -U nltk

"""Además de la librería también es necesario
descargar una serie de ficheros y diccionarios con patrones
para varios tipos de estructuras gramaticales llamados “corporas”,
dichos ficheros se instalan de forma independiente por medio de un
gestor de descargas que puede iniciarse utilizando el modulo nltk
#nltk.download()

Invocando a “download” se abre una ventana en la que se pueden
gestionar todos los ficheros “corpora” en diferentes categorías.

Si no se abre, podemos descargar los paquetes populares ejecutando
nltk.download("popular")

Los corpus principales que se suelen utilizar en el procesamiento
de texto son conocidos como “gutenberg”, el cual incluye una selección
de 18 textos del proyecto Gutenberg (http://www.gutenberg.org/)
y contiene más de 1.5 millones de palabras.
Para consultar los textos de gutenberg incluidos en el corpus de NLTK:
"""

from nltk.corpus import gutenberg as gut
#print(gut.fileids())

texto = 'shakespeare-hamlet.txt'

# Contar número de palabras en un texto
num_tokens = len(gut.words(texto))
# Token: Se trata de la unidad más simple de procesamiento
#   y representa una palabra en el texto.

# Contar número de caracteres
num_caracteres = len(gut.raw(texto))

# Contar número de sentencias
num_sents = len(gut.sents(texto))
# Una sentencia comprende las palabras de punto a punto
#   en las lenguas occidentales.

# ---------------------------------------------------------------

#                  Insertar un texto propio

from nltk.corpus import PlaintextCorpusReader

#wordlists = PlaintextCorpusReader('/home/adastra/Escritorio/textos', '.*')
#wordlists.words('prueba.txt')

