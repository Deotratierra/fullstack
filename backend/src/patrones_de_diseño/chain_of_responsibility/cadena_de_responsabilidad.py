#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#####     Código servidor     #####

class Evento:
    def __init__(self, nombre):
        self.nombre = nombre

class Manejador:
    """Base de la interfaz del manejador"""

    def __init__(self, sucesor=None):
        self._sucesor = sucesor

    def manejar(self, evento):
        # Obtenemos el método que manejará el evento
        manejador = "manejar_" + evento.nombre

        # Si el manejador tiene el método que
        # puede manejar el evento...
        if hasattr(self, manejador):
            metodo = getattr(self, manejador)
            metodo(evento)

        # Este es un detalle de implementación y no es
        # estrictamente necesario, añade un soporte a todos
        # los manejadores (por ejemplo, cazar a todos los
        # eventos no soportados)
        elif hasattr(self, "manejar_por_defecto"):
            self.manejar_por_defecto(evento)

        # Pasa al próximo manejador en la cadena
        # si este existe
        elif self._sucesor:
            self._sucesor.manejar(evento)

# Manejadores concretos
class FinalDeCadena(Manejador):
    def manejar_cierre(self, evento):
        print("FinalDeCadena:", evento.nombre)

    def manejar_por_defecto(self, evento):
        print("Defecto:", evento.nombre)

class MitadDeCadena(Manejador):
    def manejar_hacer(self, evento):
        print("MitadDeCadena:", evento.nombre)

class PrincipioDeCadena(Manejador):
    def manejar_accion(self, evento):
        print("PrincioDeCadena:", evento.nombre)

# ===================================================

#####     Código cliente     #####

# Manejadores                        # Métodos soportados

final = FinalDeCadena()              # [cierre, por_defecto]
mitad = MitadDeCadena(final)         # [cierre, por_defecto, hacer]
principio = PrincipioDeCadena(mitad) # [cierre, por_defecto, hacer, accion]

# ^^^^^^
# Construimos la cadena de forma que el principio
# pueda manejar todos los eventos soportados,
# ya que hereda de todos los manejadores

eventoHacer = Evento("hacer")
eventoAccion = Evento("accion")
eventoCierre = Evento("cierre")
eventoNulo = Evento("nulo")

if __name__ == "__main__":
    print("")

    # Pasamos los eventos al principio de la cadena
    print("Debe imprimir PrincioDeCadena: accion")
    principio.manejar(eventoAccion)

    print("\n-----------------------\n")

    print("Debe imprimir MitadDeCadena: hacer")
    principio.manejar(eventoHacer)

    print("\n-----------------------\n")

    print("Debe imprimir FinalDeCadena: cierre")
    principio.manejar(eventoCierre)

    print("\n-----------------------\n")

    print("Debe imprimir Defecto: nulo")
    principio.manejar(eventoNulo)

# Fuente:
# https://github.com/Skookum/design-patterns/blob/master/patterns/chain-of-responsibility/chain-of-responsibility.py