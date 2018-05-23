#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import hashlib

class BasicBlock:
    """Crea un bloque básico con 3 campos como
    atributos de clase: ``timestamp``, ``prev_hash`` y ``hash``.

    :param prev_block: Inserta aquí el bloque previo en la cadena
        para definir el valor del atributo ``prev_hash`` como
        el valor del atributo ``hash`` del bloque pasado como argumento.
    :param seal: Sella el bloque al momento de instanciarlo,
        definiendo los atributos ``timestamp`` y ``hash``.
        El sellado en tiempo de instanciación no tendría mucho
        sentido en una red real.

    :type optional prev_block: :py:class:`BasicBlock`. As default ``None``.
    :type optional seal: bool. As default ``False``.
    """
    def __init__(self, prev_block=None, seal=False):
        self.timestamp = None
        self.prev_hash = None
        self.hash = None

        if prev_block:
            self.link(prev_block)
        if seal:
            self.seal()

    def __get_hash(self):
        """Devuelve un hash SHA256 del bloque, usando
        los atributos de instancia ``prev_hash`` y ``timestamp``
        """
        return hashlib.sha256(
            bytearray(
                str(self.prev_hash) + str(self.timestamp), "utf-8"
            )
        ).hexdigest()

    def link(self, block):
        """Enlaza el bloque de la instancia actual
        con un bloque anterior pasado como argumento.
        El hash del bloque anterior será definido
        en el atributo ``prev_hash`` de esta instancia.

        :param block: Bloque anterior al que enlazar.
        :type block: :py:class:`BasicBlock`
        """
        self.prev_hash = block.hash

    def seal(self):
        """Sella el bloque, lo cual implica establecer
        la marca de tiempo en segundos Unix como valor
        del atributo ``timestamp`` de la clase y el hash
        del bloque como valor del atributo ``hash``.
        """
        self.timestamp = time.time()
        self.hash = self.__get_hash()


""" $ python3 -i block.py

>>> b1 = BasicBlock()
>>> b1.seal()
>>> b1.__dict__
{'timestamp': 1527095147.9904575, 'prev_hash': None, 'hash': '9db55a5ddc74f339585e664a1b11955638ce17005cf8013ec8e9ea8b5c3517a8'}
>>>
>>> b2 = BasicBlock()
>>> b2.seal()
>>> b2.link(b1)
>>> b2.__dict__
{'timestamp': 1527095229.062442, 'prev_hash': '9db55a5ddc74f339585e664a1b11955638ce17005cf8013ec8e9ea8b5c3517a8', 'hash': 'f3029d915150a7bcec618426d10f9c5f6c66c2368e0791e5d57ecd3d03ebf6a9'}
>>> b2.prev_hash == b1.hash
True

"""
