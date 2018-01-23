#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# IMPORTACIÓN DE MÓDULOS:
import modulo  # <---- Módulo completo
from modulo import funcion  #  <---- Función del modulo

# Le damos otro nombre a la función al importarla
from modulo import funcion as otro_nombre_para_la_funcion

# Para importarlo todo de un módulo:
from modulo_variables import * # <---- Variables: UNO, DOS

# ======================================================

# IMPORTACIÓN DE MÓDULOS DENTRO DE PAQUETES:
from paquete.modulo import funcion as funcion_del_paquete

# La siguiente importación es posible gracias al archivo
# paquete/__init__.py
from paquete import funcion as funcion_del_paquete_con__init__

# ======================================================

import sys

# Consultar los módulos que han sido importados:
print(sys.modules)

# Obtener la lista de rutas donde el intérprete
# de Python busca para importar módulos
print(sys.path)


if __name__ == "__main__":
    modulo.funcion()
    funcion()
    otro_nombre_para_la_funcion()

    print(UNO, DOS, "(Estas variables vienen del import *)")

    print("------------------------")

    funcion_del_paquete()
    funcion_del_paquete_con__init__()






