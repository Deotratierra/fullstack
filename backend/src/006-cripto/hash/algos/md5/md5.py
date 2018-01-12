#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
FILEDIR = os.path.dirname(__file__)

# ==========================================================================

import hashlib
# https://docs.python.org/3/library/hashlib.html

# Comprobar si podemos usar md5
print("md5" in hashlib.algorithms_available)

# Obtener el hash de un archivo (abrimos en binario)
with open(os.path.join(FILEDIR, "archivo.txt"), "rb") as arch:
    content = arch.read()
    hash1 = hashlib.md5(content)  # La función md5 toma el buffer en binario

# Obtener los bytes del hash
print(hash1.digest_size) # 16

# Obtener el hash en hexadecimal
print(hash1.hexdigest())

# Obtener el hash en binario
print(hash1.digest())

# -------------------------------------------------------------

# Comprobar si el archivo ha sido cambiado
with open(os.path.join(FILEDIR, "archivo.txt"), "rb") as arch:
    content = arch.read()
    hash2 = hashlib.md5(content)  # La función md5 toma el buffer en binario

# Atención, no comparar los objetos Hash porque
# siempre evaluarán como diferentes en las comparaciones
if hash1.digest() != hash2.digest():
    print("El archivo ha sido modificado")
else:
    print("El archivo no ha sido modificado")

# ==========================================================================

# Esta implementación en más lenta al estar orientada a objetos

from Crypto.Hash import MD5  # pip3 install pycrypto
# http://pythonhosted.org/pycrypto/Crypto.Hash.MD5.MD5Hash-class.html

# Crear un hash md5
hash3 = MD5.new(content)

# Obtener el hash en hexadecimal
print(hash3.hexdigest())

# Obtener el hash en binario
print(hash3.digest())

# ============================================================================

# Prueba de rendimiento

NUMBER = 1000

from timeit import timeit
_hashlib = timeit("content=b'345390238';hash = md5(content);hash.hexdigest()",
                setup="from hashlib import md5", number=NUMBER)

_pycrypto = timeit("content=b'345390238';hash = MD5.new(content);hash.hexdigest()",
                setup="from Crypto.Hash import MD5", number=NUMBER)

print("\nhashlib: %10f s\npycrypto: %9f s" % (_hashlib, _pycrypto))

# ============================================================================
