# -*- coding: utf-8 -*-

"""En cualquier documento de texto, hay ciertos términos
que representan entidades específicas que son más informativas
y tienen un contexto único. Esas entidades son conocidas como
entidades nombradas ("named entities" en inglés), las cuales
refieren a términos que representan objetos del mundo real,
como lugares, personas, organizaciones... etc, que son señalizadas
comúnmente por nombres propios.

El reconocimiento de entidades nombradas (NER, por sus siglas
en inglés) es una técnica usada en extracción de información
para identificar y segmentar las entidades nombradas y clasificarlas
o categorizarlas bajo varias clases predefinidas.
"""

"""Spacy es una biblioteca de modelos de reconocimiento de entidades
nombradas, entrenados con el corpus de OntoNotes5. Es más potente que
NLTK en este campo, así que vamos a demostrar su potencial.

Antes debemos instalar ``spacy`` y descargar los modelos:

   sudo python3 -m pip install spacy
   sudo python3 -m spacy download en
   sudo python3 -m spacy download es

Más información:
- https://spacy.io/usage/models
"""

from pprint import pprint

# ==============================================================

#         Reconocimiento de entidades nombradas en inglés

import en_core_web_sm
# https://spacy.io/models/en

text = "Jordan Bernt Peterson (born June 12, 1962) is a Canadian" \
     + " clinical psychologist and a professor of psychology at" \
     + " the University of Toronto."

nlp = en_core_web_sm.load()
document = nlp(text)
entities = [(ent.text, ent.label_) for ent in document.ents]
pprint(entities)

# --------------------------------------------------------------

#       Reconocimiento de entidades nombradas en español

import es_core_news_sm
# https://spacy.io/models/es

text = "Jordan Bernt Peterson (nacido en 1962) es un psicólogo" \
     + " clínico, crítico cultural y profesor de psicología" \
     + " canadiense que imparte clases en la Universidad de Toronto."

nlp = es_core_news_sm.load()
document = nlp(text)
entities = [(ent.text, ent.label_) for ent in document.ents]
pprint(entities)

# ==============================================================
