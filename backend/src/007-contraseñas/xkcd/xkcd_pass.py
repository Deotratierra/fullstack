#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# En sistemas estándar Linux, usamos un archivo de diccionario,
# en otras plataformas necesitamos proveer otra lista de palabras

import platform

def xcdk_password():
    if sys.platform.startswith('linux'):
        with open('/usr/share/dict/words') as f:
            words = [word.strip() for word in f]
            password = ' '.join(choice(words) for i in range(4))
        return password
    else:
        raise NotImplementedError
