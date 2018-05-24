#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ===============================================

class Persona:
	def __init__(self, nombre, email):
		self.nombre = nombre
		self.email = email

persona1 = Persona("Álvaro", "mondejar1994@gmail.com")

print(persona1.nombre) # Álvaro

# ===============================================

class Persona: pass

persona2 = Persona

persona2.nombre = "Álvaro"
print(persona2.nombre) # Álvaro

# ===============================================