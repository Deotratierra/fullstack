#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from distutils.core import setup
from Cython.Build import cythonize # pip3 install cython

# Podemos cythonizar mediante globs
#ext_modules = "*.pyx"

# Lo anterior sería equivalente a:
from distutils.extension import Extension
ext_modules = [
    Extension("punto",
              sources=["punto.pyx"],
    ),
]

setup(ext_modules=cythonize(ext_modules))

"""
Para compilar:
python3 setup.py build_ext -i
"""
