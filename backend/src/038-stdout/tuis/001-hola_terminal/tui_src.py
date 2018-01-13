#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import curses

if __name__ == "__main__":
	# Iniciar una pantalla dentro de la terminal
	term_scr = curses.initscr()

	# Imprimir en la pantalla
	term_scr.addstr("¡Hola mundo con curses en Python!\nPulsa una tecla para continuar")

	# Refrescar la pantalla
	term_scr.refresh()

	# Obtener la pulsación de una tecla
	term_scr.getkey()

	# Finalizar una pantalla
	curses.endwin()
