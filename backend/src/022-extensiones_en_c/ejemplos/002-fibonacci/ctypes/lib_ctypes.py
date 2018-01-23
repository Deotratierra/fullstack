#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import ctypes as c

# Wrapper a la biblioteca creada en C
dll = c.cdll.LoadLibrary("lib_c.so")

def fib(x):
    return dll.cfib(x)
