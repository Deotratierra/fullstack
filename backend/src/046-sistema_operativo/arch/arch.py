#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

# Obtener la arquitectura en bits (32/64)
def bits_arch()
    if sys.maxsize > 2**32:
        return 64
    else:
        return 32

