#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import platform

print(platform.architecture())

# Obtener la arquitectura en bits (32/64)
def bits_arch():  # Esta función es más segura
    if sys.maxsize > 2**32:
        return 64
    else:
        return 32

