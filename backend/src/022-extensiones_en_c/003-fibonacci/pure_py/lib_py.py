#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def fib(n):
    a, b = 0.0, 1.0
    for i in range(n):
        a, b = a + b, a
    return a