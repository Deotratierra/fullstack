#!/usr/bin/ruby

# Importamos el módulo json de Ruby
require "json"

texto = '{"hola": "que tal"}'
puts texto.class  #  String

response = JSON.parse(texto)
puts response.class  #  Hash

puts response["hola"]  # que tal

