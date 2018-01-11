#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import hashlib

FILEDIR = os.path.dirname(__file__)

# ===============================================

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
