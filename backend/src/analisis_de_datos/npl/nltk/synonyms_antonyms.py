# -*- coding: utf-8 -

"""WordNet es una base de datos creada para el procesamiento 
del lenguaje natural. Incluye grupos de sinónimos y una 
breve definición. Gracias a WordNet, podemos obtener
sinónimos y antónimos en varios idiomas, junto a las
definiciones de cada acepción y ejemplos de uso.
"""

from nltk.corpus import wordnet

# =======================================================

word = "light"

#                  Sinónimos en inglés

synonyms = []
for meaning in wordnet.synsets(word):
    # Imprimimos la acepción y su definición
    #print("%s: %s" % (meaning, meaning.definition()))
    
    # Aquí, la letra que aparece detrás del carácter ``.``
    #   indica el tipo de palabra que es la acepción.
    #   Por ejemplo, ``v`` es un verbo (ver ``tagging.py``).

    # Buscamos los sinónimos
    for lemma in meaning.lemmas():
        lemma_name = lemma.name()
        if lemma_name not in synonyms:
            synonyms.append(lemma_name)
print("Synonyms of '%s':" % word)
print(synonyms, end="\n\n")

#    ------------------------------------------------

#                  Antónimos en inglés

antonyms = []
for meaning in wordnet.synsets(word):
    for lemma in meaning.lemmas():
        lemma_antonyms = lemma.antonyms()
        for lemma_antonym in lemma_antonyms:
            antonym = lemma_antonym.name()
            if antonym not in antonyms:
                antonyms.append(antonym)
print("Antonyms of '%s':" % word)
print(antonyms, end="\n\n")

# =======================================================

# También podemos obtener los sinónimos de una palabra en
#   otro idioma (desde el inglés). Veamos cómo obtener los
#   sinónimos de la palabra anterior en español:

synonyms = []
for meaning in wordnet.synsets(word):
    for lemma_name in meaning.lemma_names("spa"):
        if lemma_name not in synonyms:
            synonyms.append(lemma_name)
print("Sinónimos de '%s' en español:" % word)
print(synonyms)

# =======================================================
