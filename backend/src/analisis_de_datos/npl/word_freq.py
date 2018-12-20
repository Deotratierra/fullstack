# -*- coding: utf-8 -*-

# ==========================================================

#  Calcular la frecuencia de palabras en un texto

import nltk

text = """Esto es un texto de ejemplo en el cual
me basaré para calcular la frecuencia de las palabras.
La frecuencia que aparecen las palabras en un texto
nos proporciona una base de información general que
podríamos usar para saber de qué trata.
"""

# Primero tokenizamos el texto usando un tokenizador
#   para el lenguaje castellano

from nltk.tokenize.toktok import ToktokTokenizer
toktok = ToktokTokenizer()

# Tokenizamos el texto
tokens = toktok.tokenize(text)
#print(tokens)

# Obtenemos el conteo del número de apariciones
#   de cada token en el texto
freq = nltk.FreqDist(tokens)
for word, appearances in freq.items():
    print("%s -> %d" % (word, appearances))

# Para comprobar la frecuencia de aparición de una palabra
#   podemos usar el método ``freq``:
print(freq.freq("texto"))  # 0.046511627906976744

# Imprimir de la más a la menos frecuente
print(freq.most_common())

# ==========================================================
