#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from getch import getch    # pip3 install getch

def main():
    while True:
        options = ["Opción 1", "Opción 2",
                   "Opción 3", "Salir"]
        for i, opt in enumerate(options):
            print("%d) %s" % (i+1, opt))

        print("Elige una opción: ")
        try:
            option = int(getch())
            if options[option-1] == "Salir":
                print("Hasta luego")
                break
            else:
                print("Has elegido la %s" % options[option-1])
        except (ValueError, IndexError):
            print("Opción inválida")

if __name__ == '__main__':
    main()
