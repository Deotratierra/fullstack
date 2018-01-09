#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    name = input("Escribe tu nombre: ")
    print("Bienvenid@ a mi documentación, %s." % name)
    # Otra opción
    #print("Bienvenid@ al curso {}".format(name))

'''
Si hemos ejecutado directamente este archivo
archivo, __name__ será igual a __main__.

Si hemos importado este archivo desde otro,
__name__ != "__main__"  así que no se ejecutará la función main()

Para más información:
https://es.stackoverflow.com/questions/32165/qu%C3%A9-es-if-name-main
'''

if __name__ == '__main__':
    main()
