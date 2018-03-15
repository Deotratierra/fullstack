#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from sys import argv

from setuptools import setup
from setuptools.extension import Extension

from Cython.Build import cythonize

filename = argv[2]
del argv[2]

os.rename("%s.pyx" % filename, "cy%s.pyx" % filename)

setup(
    name = filename,
    ext_modules = cythonize(
        Extension("cy%s" % filename, ["cy%s.pyx" % filename])
    )
)

