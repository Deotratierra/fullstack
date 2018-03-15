#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import argv
from cyfib import fib

if __name__ == "__main__":
    arg = int(argv[1])
    fib(arg)
