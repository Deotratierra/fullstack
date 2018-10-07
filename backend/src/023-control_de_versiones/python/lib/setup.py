#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from setuptools import setup

BASEDIR = os.path.dirname(__file__)

with open(os.path.join(BASEDIR, "requirements.txt")) as f:
    REQ = f.readlines()

with open(os.path.join(BASEDIR, "README.md"), encoding="utf-8") as f:
    DESC = f.read()


setup(
    name = 'fullstack',
    version = '1.00.005',
    url = 'https://github.com/mondeja/fullstack',
    download_url = 'https://github.com/mondeja/fullstack/archive/master.zip',
    author = 'Álvaro Mondéjar',
    author_email = 'mondejar1994@gmail.com',
    license = 'BSD License',
    description = 'Referencia de programación en español backend + frontend (múltiples lenguajes)',
    long_description = DESC,
    install_requires = REQ,
)