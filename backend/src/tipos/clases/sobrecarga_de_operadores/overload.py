#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Pareja:
    def __init__(self, n1, n2):
        self.n1, self.n2 = (n1, n2)

    def __repr__(self):  # Representación
        return "%s(%r)" % (self.__class__.__name__, 
        	               self.__dict__)

    def __str__(self):  # Representación como string (print)
        return "%s(%d, %d)" % (self.__class__.__name__, 
        	                   self.n1, self.n2)

    # ===============================================

    def int_to_self(self, other):
        if isinstance(other, int): # Permite la adición de enteros
            return Pareja(other, other)
        else:
            if not isinstance(other, type(self)):
                raise NotImplementedError
            return other

    # ================================================
    #           SOBRECARGA DE OPERADORES
               
    #   Aritméticos

    def __add__(self, other):  # Suma
        other = self.int_to_self(other)
        return (self.n1 + other.n1, self.n2 + other.n2)

    def __radd__(self, other):  # Suma revertida
        other = self.int_to_self(other)
        return (self.n1 + other.n1, self.n2 + other.n2)

    def __sub__(self, other):  # Resta
        other = self.int_to_self(other)
        return (self.n1 - other.n1, self.n2 - other.n2)

    def __rsub__(self, other):  # Resta revertida
        other = self.int_to_self(other)
        return (other.n1 - self.n1, other.n2 - self.n2) # !

    def __mul__(self, other):   # Multiplicación
    	other = self.int_to_self(other)
    	return (self.n1 * other.n1, self.n2 * other.n2)

    def __rmul__(self, other):   # Multiplicación revertida
    	other = self.int_to_self(other)
    	return (self.n1 * other.n1, self.n2 * other.n2)

    # ------------------------------------------------------

    #   De comparación

    def __lt__(self, other):   # Menor que
        other = self.int_to_self(other)
        return (self.n1 + self.n2) < (other.n1 + other.n2)

    def __le__(self, other):   # Menor o igual que
    	other = self.int_to_self(other)
    	return (self.n1 + self.n2) <= (other.n1 + other.n2)

    def __eq__(self, other):   # Igual
    	other = self.int_to_self(other)  
    	return self.n1 == other.n1 and self.n2 == other.n2

    def __ne__(self, other):   # Distinto
    	other = self.int_to_self(other)  
    	return self.n1 != other.n1 or self.n2 != other.n2

    def __gt__(self, other):   # Mayor que
    	other = self.int_to_self(other)  
    	return (self.n1 + self.n2) > (other.n1 + other.n2)
 
    def __ge__(self, other):   # Mayor o igual que
    	other = self.int_to_self(other)  
    	return (self.n1 + self.n2) >= (other.n1 + other.n2)



# =============================== #
###       Inicialización        ###

pareja1 = Pareja(3, 5)     # __init__
pareja2 = Pareja(2, 7)


# =============================== #
###       Representación        ###

print(pareja1)             # __str__
print(pareja1.__repr__())  # __repr__


# =============================== #
###  Sobrecarga de operadores   ###

# Aŕitméticos
suma = pareja1 + pareja2           # __add__  
suma2 = pareja1 + 1
suma3 = 3 + pareja1                # __radd__

resta = pareja1 - pareja2          # __sub__
resta2 = pareja1 - 2
resta3 = 2 - pareja1               # __rsub__

multiplicacion = pareja1 * pareja2 # __mul__
multiplicacion2 = pareja1 * 3
multiplicacion3 = 3 * pareja1      # __rmul__

# ----------------------------------------------

# De comparación
menor_que =       pareja1 <  pareja2    # __lt__
menor_igual_que = pareja1 <= pareja2    # __le__
igual =           pareja1 == pareja2    # __eq__
distinto =        pareja1 != pareja2    # __ne__
mayor_que =       pareja1 >  pareja2    # __gt__
mayor_igual_que = pareja1 >= pareja2    # __ge__


"""
Fuentes:
https://docs.python.org/3/reference/datamodel.html#special-method-names
https://stackoverflow.com/questions/1436703/difference-between-str-and-repr-in-python
"""