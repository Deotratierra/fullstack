#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import abc
import colorama # pip3 install colorama
colorama.init()

class Comando(metaclass=abc.ABCMeta):
    """Clase base abstracta para cada comando.
    Cada comando concreto debe implementar
    un método ejecutar() o dará un fallo:

    TypeError: Can't instantiate abstract
    class <Clase> with abstract methods ejecutar

    en cuanto la clase sea inicializada"""
    @abc.abstractmethod
    def ejecutar(self):
        pass

class Negrita(Comando):
    def __init__(self, texto):
        self.texto = texto

    def ejecutar(self):
        self.texto = colorama.Style.BRIGHT + texto

    def deshacer(self):
        self.texto = colorama.Style.NORMAL + texto

    def mostrar(self):
        print(self.texto)

class Rojo(Comando):
    def __init__(self, texto):
        self.texto = texto

    def ejecutar(self):
        self.texto = colorama.Fore.LIGHTRED_EX + texto

    def deshacer(self):
        self.texto = colorama.Fore.RESET + texto

    def mostrar(self):
        print(self.texto)

class InvocadorEditorDeTexto:
    def __init__(self):
        self._comandos = []
        self._historial = []

    def almacena(self, comando):
        self._comandos.append(comando)

    def ejecuta_todo(self):
        for comando in self._comandos:
            comando.ejecutar()
            comando.mostrar()
            self._comandos.remove(comando)
            self._historial.append(comando)

    def recibe(self, comando):
        """Receptor de comandos, almacena y ejecuta"""
        self.almacena(comando)
        self.ejecuta_todo()

    def deshacer(self):
        comando = self._historial.pop()
        comando.deshacer()
        comando.mostrar()

if __name__ == "__main__":
    texto = "Hola soy un texto en el editor"
    rojo = Rojo(texto)
    negrita = Negrita(texto)

    editorDeTexto = InvocadorEditorDeTexto()

    print(texto)
    editorDeTexto.recibe(rojo)
    editorDeTexto.recibe(negrita)
    editorDeTexto.deshacer()
    editorDeTexto.deshacer()



