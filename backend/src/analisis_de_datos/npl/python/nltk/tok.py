#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Tokenizar es el proceso de separar oraciones o palabras
que se encuentran dentro de un texto.
"""

import nltk

# ==============================================================

#      ===========     Tokenizar en inglés     =============

#nltk.download("punkt")
#nltk.download("averaged_perceptron_tagger")

from nltk import sent_tokenize, word_tokenize, pos_tag
text = """Machine learning is the science of getting computers to act
without being explicitly programmed. In the past decade, machine learning
has given us self-driving cars, practical speech recognition, effective
web search, and a vastly improved understanding of the human genome.
Machine learning is so pervasive today that you probably use it dozens of
times a day without knowing it. Many researchers also think it is the best
way to make progress towards human-level AI. In this class, you will learn
about the most effective machine learning techniques, and gain practice
implementing them and getting them to work for yourself."""

sents = sent_tokenize(text)
tokens = word_tokenize(text)

# Clasificación de tokens por tipo (nombres, verbos, adverbios...)
tagged_tokens = pos_tag(tokens)

# Consultar información sobre un tag
nltk.help.upenn_tagset('JJ')

# ==============================================================

#     ===========     Tokenizar en español     =============

# Para tokenizar caracteres como ``¿`` o ``¡`` debemos instalar un tokenizador
#   alternativo para el español:

#nltk.download("perluniprops")
#nltk.download('nonbreaking_prefixes')

texto = """¡Hola! ¿Te funciona?"""

from nltk.tokenize.toktok import ToktokTokenizer
toktok = ToktokTokenizer()

# Tokenizar sentencias
sentencias = [ toktok.tokenize(sent) for sent in \
                   sent_tokenize(texto, language="spanish")]

# Tokenizar palabras
palabras = toktok.tokenize(texto)  # ['¡', 'Hola', '!', '¿', 'Te', 'funciona', '?']


# ==============================================================
