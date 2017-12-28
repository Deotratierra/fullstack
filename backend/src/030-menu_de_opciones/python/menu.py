#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Plantilla de jerarquía de menús anidados
para el scripting a través de menús de opciones"""

from sys import exit
from getch import getch # pip3 install getch

# =============================================================================

#####     FUNCIONES PARA COLOREAR LAS SALIDAS     #####

def separator():
    print("\n_______________________________________________________________\n")

from colorama import Back, Fore, Style, init
init(autoreset=True)

def success(message):
    """Mensaje de éxito"""
    print("\n" + Back.LIGHTGREEN_EX + Fore.BLUE + Style.BRIGHT + "  " + message + "  ")

def fail(message):
    """Mensaje de error"""
    print("\n" + Back.RED + Fore.YELLOW + Style.BRIGHT + "  " + message + "  ")

def warning(message):
    """Mensaje de advertencia"""
    print("\n" + Back.LIGHTRED_EX + Fore.YELLOW + Style.BRIGHT + str(message) + "\n")

def title(message):
    """Título"""
    print(Back.LIGHTBLUE_EX + Fore.LIGHTWHITE_EX + Style.BRIGHT + " " + str(message) + " ")

def head(message):
    """Cabecero"""
    print(Back.LIGHTWHITE_EX + Fore.BLUE + Style.BRIGHT + "    " + str(message) + "    ")

def op(message):
    print(Back.LIGHTYELLOW_EX + Fore.RED + Style.BRIGHT + ' ' + str(message) + ' ')


# ===================================================================================

def exiting():
    """Salida del programa"""
    success("¡Hasta la próxima!")
    print("")
    exit(0)

class Menu(object):
    """Clase base para construir un menú con Submenus
    asociados en una jerarquía de padre e hijos,
    con una opción de volver al menú padre desde
    cada submenú"""

    # Opción de salida del programa (opción impresa, función, [módulo])
    EXIT_PROGRAM = ('Salir del programa', 'exiting')
    # Ruta que usarán los submenús para buscar imports
    BASE_IMPORT = None
    # Ancho de caracteres
    CHARS_WIDTH = 53
    TITLE_CHARS_WIDTH = CHARS_WIDTH - 6

    def _build_main_menu(self):
        """Construye el menu

        Returns:
            dict: Número del menú con su título y una clase
                asociada -> `{'1': (Titulo, Clase)}`
        """
        response = {}
        for enum, info in enumerate(self.MENU):
            response[str(enum + 1)] = info
        response[str(len(response) + 1)] = self.EXIT_PROGRAM
        return response

    def _show_menu(self, menu):
        """Impresión del menú ordenado numéricamente

        Args: 
            menu (dict): Número de cada elemento del menú
                asociado a su nombre
        """
        nums = menu.keys() # Cogemos los números en str

        list_nums = []     # Creamos una lista de ints ordenada
        for n in nums:
            list_nums.append(int(n))
        list_nums.sort()
        for num in list_nums: # Imprimimos cada campo del menú
            printer = "%d. " % num
            printer += menu[str(num)][0]
            if len(printer) < self.CHARS_WIDTH:
                for space in range(self.CHARS_WIDTH - len(printer)):
                    printer += " "
            title(printer)

    def _show_menu_title(self):
        """Muestra el nombre del menú"""
        print("")
        _menu_title = self.MENU_TITLE
        if len(_menu_title) < self.TITLE_CHARS_WIDTH - len(_menu_title):
            after = False
            for space in range(self.TITLE_CHARS_WIDTH - len(_menu_title)):
                if not after:
                    _menu_title = " " + _menu_title
                    after = True
                else:
                    _menu_title += " "
                    after = False
        head(_menu_title)

    def _main_menu(self):
        """Menú, función que se ejecuta para elegir opciones"""
        self._show_menu_title()
        _menu = self._build_main_menu() # Obtenemos el menú
        self._show_menu(_menu) # Lo imprimimos ordenado
        error = True  # Por si pulsamos teclas erróneas
        arch = None   # Módulo desde donde importar el Submenú
        while error == True:
            try:
                if len(_menu.keys()) < 10:   # Si el menú tiene menos de 10 opciones
                    option = getch()       # Seleccionamos opción con getch()
                else:                    # Si no lo hacemos con input()
                    option = input("Introduce un número y pulsa ENTER: ")
                try:
                    tit, cls, arch = _menu[str(option)] # Titulo clase archivo
                except ValueError:  # No hay módulo desde donde importar
                    tit, cls = _menu[str(option)]
            except KeyError: # Este error se produce cuando
                pass         # pulsamos una tecla no válida
            else:
                error = False

        if arch:
            if self.BASE_IMPORT:
                template_import = "from " + self.BASE_IMPORT + ".{} import {}"
            else:
                template_import = "from {} import {}"
            exec(template_import.format(arch, cls))    # Importamos el módulo de la clase

        if cls[0].isupper():
        # Comprobamos si la clase comienza por mayúscula
            eval(cls + "().run()") # Ejecutamos la clase elegida
        # Si empieza por minúscula es una función
        else:
            eval(cls + "()") # Se ejecuta la función
            self._main_menu() # Cuando acaba, debemos volver al menú

    def run(self):
        self._main_menu()

class SubMenu(Menu):
    """La clase submenú añade una función para volver al menú
    padre. En la propiedad BACK_TO_MAIN añadimos
    (opción impresa, función/Clase, [módulo])"""
    BACK_TO_MAIN = ("Volver al menú principal", "MainMenu", "menu")

    # Sustituye esta función del objeto Menu agregando el nuevo campo
    def _build_main_menu(self): # Construye el menú
        response = {}
        for enum, info in enumerate(self.MENU):
            response[str(enum + 1)] = info   # Tupla:
        response[str(len(response) + 1)] = self.BACK_TO_MAIN
        return response      #         título, clase/función, modulo

# ========================================================================

# ========================================================================

# MENÚ DE EJEMPLO

def funcion_de_ejemplo():
    """Función de ejemplo, cuando se ejecuta
    vuelve al menú donde que estábamos"""
    print("\nHola soy una función de ejemplo.")

class SubMenu1(SubMenu):
    MENU_TITLE = "SUBMENÚ"
    MENU = (
            ("Ejecutar función en otro módulo", 'funcion_de_ejemplo_en_otro_modulo', 'modulo'),
           )

class MainMenu(Menu):
    """Menú principal de ejemplo"""

    # Título del menú
    MENU_TITLE = "-[ MENÚ PRINCIPAL ]-"

    # Estructura de submenús (Título, función/Clase, [módulo])
    # Si la clase empieza en minúscula significa que es una función
    # que se ejecutará, si no es un submenú
    MENU = (
            ("Ejecutar función en el mismo módulo", "funcion_de_ejemplo"),
            ("Submenú de ejemplo", "SubMenu1"),
           )

if __name__ == "__main__":
    menu = MainMenu()
    menu.run()
