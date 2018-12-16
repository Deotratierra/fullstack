# -*- coding: utf-8 -*-

"""El método NLTK Lemmatization se basa en la función morphy
incorporada de WordNet. WordNet® es una gran base de datos léxica de inglés.

Los sustantivos, verbos, adjetivos y adverbios se agrupan en conjuntos
de sinónimos sintéticos (synsets), cada uno de ellos expresando
un concepto distinto. Las relaciones de síntesis están interrelacionadas
mediante relaciones conceptuales-semánticas y léxicas. La red resultante
de palabras y conceptos relacionados de forma significativa se puede navegar.

WordNet también está libre y públicamente disponible para su descarga.
La estructura de WordNet lo convierte en una herramienta útil
para la lingüística computacional y el procesamiento del lenguaje natural.

WordNet se asemeja superficialmente a un tesauro, en que agrupa las palabras
en base a sus significados. Sin embargo, hay algunas distinciones importantes.
En primer lugar, WordNet enlaza no sólo formas de palabras, cadenas de letras,
sino también sentidos específicos de palabras.

Como resultado, las palabras que se encuentran en estrecha proximidad entre sí
en la red son semánticamente desambiguadas. En segundo lugar, WordNet
etiqueta las relaciones semánticas entre palabras, mientras que
los agrupamientos de palabras en un tesauro no siguen ningún patrón
explícito que no sea la similitud de significado.
"""

from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()
wordnet_lemmatizer.lemmatize('dogs')    # 'dog'
wordnet_lemmatizer.lemmatize('are')     # 'are'
wordnet_lemmatizer.lemmatize('is')      # 'is'

# Fíjate en que los resultados de "are" y "is" no son "be",
#   es porque el argumento de tagging por defecto 
#   de ``lemmatize`` es "n" (name):

#lemmatize(word, pos="n")

# Así que hay que espicificarle que busque por verbo:
wordnet_lemmatizer.lemmatize('is', pos='v')     # ’be’


