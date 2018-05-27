#!/usr/bin/ruby

# Importamos el módulo json de Ruby
require "json"

# Parsear el contenido de un archivo JSON
archivo = File.read('fichero.json')

puts archivo["py"]  # py

# --------------------------------

# Parsear cadena de texto JSON
texto = '{"hola": "que tal"}'
puts texto.class  #  String

response = JSON.parse(texto)
puts response.class  #  Hash

puts response["hola"]  # que tal

