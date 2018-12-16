# -*- coding: utf-8 -*-

from nltk import word_tokenize, pos_tag

# ====================     Tagging en inglés     ======================

text = "Hello everybody! We're going to learn how to tag words."
tokens = word_tokenize(text)
print(pos_tag(tokens))


# ====================     Tagging en español     =====================

from nltk.corpus import cess_cat

print(cess_cat.tagged_words())
