#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ===============================================

"""En C, definimos una estructura de datos para
guardar una persona con un mail de la siguiente forma:

struct Persona {
    char[32] nombre;
    int edad;
}

struct *Persona crearPersona(char* nombre, int edad)
{
    struct Persona* persona = malloc(sizeof(struct Persona));
    strcpy(persona.nombre, nombre);
    persona.edad = edad;
    return persona;
}

Sin embargo Python es un lenguaje orientado a objetos,
por lo que no tenemos estructuras de datos como en C:
"""

# Creación de una clase en Python
class Persona:
	def __init__(self, nombre, edad):
		self.nombre = nombre
		self.edad = edad

persona1 = Persona("Álvaro", 24)

print(persona1.nombre) # Álvaro

# --------------------------------------------------

# Creación programática de una clase en Python
class Persona: pass

persona2 = Persona

persona2.nombre = "Álvaro"
print(persona2.nombre) # Álvaro

#print(persona2.edad)
# AttributeError: type object 'Persona' has no attribute 'edad'

persona2.edad = 24
print(persona2.edad) # 24

# ===============================================


