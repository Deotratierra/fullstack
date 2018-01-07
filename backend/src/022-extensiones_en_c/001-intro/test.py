#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
from timeit import timeit

# Modulos y directorios correspondientes
IMPLEMENTACIONES = [
    ("pure_py", "pure_py"),
    ("lib_cy", "cython"),
    ("lib_c", "manual")
]

def test_impl(module, directory):
    os.chdir(directory)
    print("\n%s\n" % os.getcwd())
    rendimiento = timeit("%s.summa(100)" % module,
    	                 setup="import %s" % module,
    	                 number=10000 )
    os.chdir("..")

def tests():
    response = []
    for impl_details in IMPLEMENTACIONES:
        response.append(test_impl(*impl_details))
    return response  #(py, cy, c)

if __name__ == "__main__":
    print(tests())
    sys.exit(0)
