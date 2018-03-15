#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import argv

def fib(n):
    a, b = 0, 1
    for i in range(n+1):
        a, b = a + b, a
    return a

if __name__ == "__main__":
    arg = int(argv[1])
    fib(arg)