#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import kivy
kivy.require('1.10.0') # Reemplaza con tu versión actual de Kivy

from kivy.app import App

"""El módulo uix es el lugar donde se encuentran los paquetes
que contienen los elementos de la interfaz de usuario"""
from kivy.uix.label import Label

""" Todas las aplicaciones con Kivy comienzan en una clase
    que hereda de App, la cual se encuentra en el módulo kivy.app
"""
class MiAplicacion(App):
    """La función build() se encarga de inicializar la aplicación y devuelve
    el widget raíz (en este caso una simple etiqueta): """
    def build(self):
    	# Para crear una etiqueta usamos la clase Label()
        return Label(text='¡Hola mundo desde Kivy!')

if __name__ == '__main__':
    # Para ejecutar la aplicación llamamos al método run de la clase App
    MiAplicacion().run()
