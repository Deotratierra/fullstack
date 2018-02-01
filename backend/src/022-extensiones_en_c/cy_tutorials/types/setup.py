#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from distutils.core import setup
from Cython.Build import cythonize

from distutils.extension import Extension
ext_modules = [
    Extension("inferencia",
              sources=["inferencia.pyx"],
    ),
]

setup(ext_modules=cythonize(ext_modules))

"""
Para compilar:
python3 setup.py build_ext -i
"""
