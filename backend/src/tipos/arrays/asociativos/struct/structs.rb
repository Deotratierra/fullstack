#!/usr/bin/ruby

# ==================================================

# Struct constante (no permite añadir nuevos campos)
Persona = Struct.new(:nombre, :email)

persona1 = Persona.new("Álvaro", "mondejar1994@gmail.com")
puts persona1.nombre # Álvaro

# ==================================================
 
require "ostruct"

# OpenStruct (permite añadir nuevos campos)
persona2 = OpenStruct.new

persona2.nombre = "Álvaro"
puts persona2.nombre # Álvaro

# ==================================================
# 
# =begin
# Fuentes:
# http://robdodson.me/ruby-objects-and-dot-syntax/
# =end