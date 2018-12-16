# -*- coding: utf-8 -*-

"""En la morfología lingüística y la recuperación de la información,
"stemming" es el proceso para reducir las palabras inflexas
(o algunas veces derivadas) a su forma de tallo, base o raíz,
generalmente una forma de palabra escrita.

El tallo no necesita ser idéntico a la raíz morfológica de la palabra;
normalmente es suficiente que las palabras relacionadas se correspondan
con el mismo tronco, incluso si este tallo no es en sí mismo una raíz válida.

Los algoritmos para stemming han sido estudiados en informática
desde la década de 1960. Muchos motores de búsqueda tratan palabras
con el mismo tallo que los sinónimos como un tipo de expansión de consulta,
un proceso llamado "conflation".

NLTK proporciona varias interfaces de steemers famosos,
como Porter stemmer, Lancaster Stemmer, Snowball Stemmer... etc.
En NLTK, el uso de estos stemmers es muy simple.

Los diferentes steemers se basan en diferentes algoritmos que,
en NLTK, dan lugar al nombre del steemer:
"""

# Porter Steemer
from nltk.stem.porter import PorterStemmer
porter_stemmer = PorterStemmer()
porter_stemmer.stem("are")             # "are"
porter_stemmer.stem("maximum")         # "maximum"
porter_stemmer.stem("presumably")      # "presum"

# Lancaster Stemmer
from nltk.stem.lancaster import LancasterStemmer
lancaster_stemmer = LancasterStemmer()
lancaster_stemmer.stem("maximum")      # "maxim"
lancaster_stemmer.stem("presumably")   # "presum" 

# Snowball Stemmer (admite el lenguaje español)
from nltk.stem import SnowballStemmer
snowball_stemmer = SnowballStemmer("spanish")
snowball_stemmer.stem("son")           # "son"
snowball_stemmer.stem("seguridad")     # "segur"
snowball_stemmer.stem("acompañar")     # "acompañ"
