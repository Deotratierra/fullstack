#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from distutils.core import setup, Extension

# Definimos el modulo de extension
object_module = Extension('lib_c', sources=['lib_c.c'])

# Ejecutar el setup
setup(ext_modules=[object_module])