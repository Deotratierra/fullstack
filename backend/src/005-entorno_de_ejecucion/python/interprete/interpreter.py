#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Referencia:
# https://docs.python.org/3/library/sys.html

import sys, platform
from pprint import pprint as pp

# ===========================================
#           Información de tipos

# Información sobre el tipo float
pp(sys.float_info)

# Información sobre el tipo int
pp(sys.int_info)

# Mayor entero posible
pp(sys.maxsize)

# ===========================================


# Obtener la ruta de la instalación de Python
pp(sys.base_exec_prefix)

# Obtener la ruta al ejecutable de Python
pp(sys.executable)

# Flags de ejecución
pp(sys.flags)
"""
debug                   -d
inspect                 -i
interactive             -i
optimize                -O or -OO
dont_write_bytecode     -B
no_user_site            -s
no_site                 -S
ignore_environment      -E
verbose                 -v
bytes_warning           -b
quiet                   -q
hash_randomization      -R
"""

# Obtener él número de bloques de memoria
# asignados por el intérprete,
# independientemente de su tamaño
pp(sys.getallocatedblocks())

# Obtener la codificación por defecto
# usada por la implementación Unicode
pp(sys.getdefaultencoding())

# Obtener y editar el número máximo de
# recursiones permitidas:
pp(sys.getrecursionlimit())
#sys.setrecursionlimit(<num>)

# Obtener el tamaño de un objeto en bytes:
# sys.getsizeof(object[, default])

# Obtener los parámetros de implementación
# de los hashes de los objetos:
pp(sys.hash_info)
"""
width         width in bits used for hash values
modulus       prime modulus P used for numeric hash scheme
inf           hash value returned for a positive infinity
nan           hash value returned for a nan
imag          multiplier used for the imaginary part of a complex number
algorithm     name of the algorithm for hashing of str, bytes, and memoryview
hash_bits     internal output size of the hash algorithm
seed_bits     size of the seed key of the hash algorithm
"""

# Información sobre la versión
# implementada del intérprete de Python
pp(sys.implementation)
pp(platform.python_implementation())

# Consultar si el intérprete se está apagando
pp(sys.is_finalizing())

# Cadenas que aparecen en consola en el modo
# interactivo antes de las entradas,
# por defecto ">>>" y "..."
#pp(sys.ps1, sys.ps2)
# Sólo es posible obtener estas variables
# y editarlas desde el modo interactivo

# Obtener y editar cuantas instrucciones tarda el
# intérprete en realizar consultas periódicas
# tales como el cambio de hilos o los
# manejadores de señales del sistema:
pp(sys.getcheckinterval())
#sys.setcheckinterval(<num>)

# ==================================================================

# Para otras configuraciones más profundas
# consultar el módulo sysconfig:
# https://docs.python.org/3/library/sysconfig.html
