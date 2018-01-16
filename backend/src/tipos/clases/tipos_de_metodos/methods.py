#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import abc

class Base:
    __metaclass__ = abc.ABCMeta

    _propiedad2 = "Soy otra "

    @classmethod         # Cualquier instancia de Ejemplo,
    @abc.abstractmethod  # tiene que implementar el método
    def abstracto(cls):  # abstracto o se lanzará un
    	return cls._propiedad2  # TypeError al instanciarla

class Ejemplo(Base):
    _propiedad = "Soy una propiedad"

    # Constructor
    def __init__(self, *args, **kwargs):
        self._atributo = "Soy un atributo"


    def normal(self, *args, **kwargs):
        print("¡No te olvides de self!")

    @property
    def propiedad(self, *args, **kwargs):
        return self._propiedad

    @staticmethod    
    def estatico(*args, **kwargs):
        print("¡No tengo relación con la clase!")

    @classmethod
    def de_clase(cls, *args, **kwargs):
        print("Recibo la clase como primer parámetro")
        print("Puedes llamarme sin instanciar la clase:")
        print(">>> Ejemplo.de_clase()")

    def abstracto(self, *args, **kwargs):
    	print( "Te obligo a implementarme" )
    	print( super(Ejemplo, self).abstracto() + "propiedad" )


# Acceso a propiedades (son parte de la clase):
print(Ejemplo._propiedad) # Soy una propiedad

# Constructor
ej = Ejemplo(1, 2, 3, cuarto="cuatro")

# Acceso a atributos (propias de la instancia):
print(ej._atributo) # Soy un atributo

# Método normal
ej.normal()  # ¡No te olvides de self!

# Método con @property
print(ej.propiedad) # Soy una propiedad

# Método estático
Ejemplo.estatico(), ej.estatico # ¡No tengo relación con la clase!

# Método de clase
Ejemplo.de_clase() # Recibo la clase como primer parámetro
                   # Puedes llamarme sin instanciar la clase:
                   # >>> Ejemplo.de_clase()

# Método abstracto
ej.abstracto()    # Te obligo a implementarme
                  # Soy otra propiedad
