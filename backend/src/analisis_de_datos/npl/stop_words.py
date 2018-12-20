# -*- coding: utf-8 -*-

# Las "stop words" (en inglés) son aquellas palabras que
#   deseamos ignorar comúnmente cuando estamos analizando
#   textos, como por ejemplo, los determinantes, las
#   preposiciones, los pronombres y algunos verbos,
#   ya que no nos dicen nada acerca del contenido.

# ==========================================================

# Para consultar las stop words que vienen icorporadas en
#   NLTK para varios idiomas, podemos usar lo siguiente:
from nltk.corpus import stopwords
 
print(stopwords.words("english"))
print(stopwords.words("spanish"))

# ------------------------------------------------------

# Para eliminar estas palabras de un texto, podemos filtrarlo
#   de la siguiente forma:
from nltk.tokenize.toktok import ToktokTokenizer
toktok = ToktokTokenizer()

text = """Esto es un texto de ejemplo, del cual vamos a filtrar
las palabras que no nos interesan para poder analizarlo mejor."""

# Lo tokenizamos
tokens = toktok.tokenize(text)

# Filtramos las palabras no deseadas
clean_tokens = list(
    filter(lambda token: token not in stopwords.words("spanish"), tokens))
# ['Esto', 'texto', 'ejemplo', ',', 'vamos', 'filtrar', 'palabras',
#  'interesan', 'poder', 'analizarlo', 'mejor', '.']

# ==========================================================
