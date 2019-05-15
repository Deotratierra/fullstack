#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Ejemplo del patrón adaptador en Python.
  - `SpanishPerson`: es el cliente.
  - `EnglishTranslater`: es el adaptador.
  - `EnglishPerson`: es la intefaz que necesita ser adaptada.
"""

class SpanishPerson(metaclass=abc.ABCMeta):
    """Define la interfaz de dominio específico que usa el cliente
    dentro del constructor, ya que esta clase está pensada como un
    cliente para un cliente específico.
    """

    def __init__(self):
        self._adaptee = EnglishPerson()

    def spanish_greet(self, greeting="Hola"):
        """Saludamos un un hola a la persona inglesa.
        """
        print("Persona española:", greeting)
        return self._adaptee.greet(greeting)


class EnglishTranslater(SpanishPerson):
    """Adapta la interfaz que necesita adaptarse a la interfaz ``SpanishPerson``"""
    spanish_to_english = {
        "Hola": "Hello",
        "Adiós": "Goodbye",
        "No te entiendo": "I dont understand you"
    }
    english_to_spanish = {
        "Hello": "Hola",
        "Goodbye": "Adiós",
        "I dont understand you": "No te entiendo"
    }

    def spanish_greet(self, greeting="Hola"):
        """Envía una petición a la interfaz y traduce
        la respuesta al español.
        """
        print("Persona española:", greeting)
        greeting = self.spanish_to_english[greeting]

        print("Traductor español-inglés:", greeting)
        answer = self._adaptee.greet(greeting)
        print("Persona inglesa:", answer)
        answer = self.english_to_spanish[answer]
        return answer


class EnglishPerson:
    """Interfaz de necesita ser adaptada."""

    def greet(self, greeting):
        """Devuelve un saludo en inglés."""
        if greeting == "Hello":
            return "Hello"
        elif greeting == "Goodbye":
            return "Goodbye"
        else:
            return "I dont understand you"


def main():
    target = SpanishPerson()
    print("Persona inglesa:", target.spanish_greet())
    print()
    adapter = EnglishTranslater()
    print("Respuesta del traductor:", adapter.spanish_greet())


if __name__ == "__main__":
    main()

"""
> Fuentes:

- https://sourcemaking.com/design_patterns/adapter
"""
