#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ===================================================================+
#        Generar un número al azar criptográficamente seguro

# Para ello podemos usar el módulo estándar de Python secrets, pero sólo
import secrets  # está disponible en la bibilioteca estándar desde la versión 3.6
# https://docs.python.org/3/library/secrets.html
import hashlib

import bitcoin.core.key as key

def is_valid(num):
    return num > 0x1 and num < 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364140

# ---------------------------------------------------------------------------

# Opción 1:
#     Generamos un número de 256 bits al azar usando los mecanismos
#     de generación de aleatoriedad del sistema operativo

# Generamos un número de 256 bits de aleatoriedad
rand_bytes_num = secrets.randbits(256)
print("Generamos un número de 256 bits de aleatoriedad.\nNum: %d\nHex: %x" % \
	      (rand_bytes_num, rand_bytes_num) )

# Comprobamos si es un número válido (num > 0 and num < 1.158 * 1077)
print("¿Es un número válido? %s" % ("SI" if is_valid(rand_bytes_num) else "NO"))

# ---------------------------------------------------------------------------

# Opción 2:
#     


#k = key.CECKey()
#k.set_privkey(secure_rand_bytes)
#print(k.get_pubkey())

#print(hashlib.sha256(secure_rand_bytes).digest())