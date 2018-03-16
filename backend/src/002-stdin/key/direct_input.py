#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from getch import getch      # pip3 install getch

# Gracias a la biblioteca getch podemos leer fácilmente
# entradas de eclado de una sola tecla en tiempo real

while True:
    print("\nPulsa la tecla S para salir")
    tecla = getch()
    print( "Has pulsado la tecla %s" % tecla)

    if tecla in ("S", "s"):
        break
