#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from distutils.core import setup
from Cython.Build import cythonize # pip3 install cython

setup(ext_modules = cythonize("lib_cy.pyx"))

"""
Para compilar:
python3 setup.py build_ext --inplace
"""
