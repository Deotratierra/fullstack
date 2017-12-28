#!/usr/bin/env python3
# -*- coding: utf-8 -*-

a = ["elem1"]
b = [2, 1, [3, [4, 5], 6], 7, [8]]

def flatten(l, source=None):
    source = list(source) if isinstance(a, (list, tuple)) else []
    for i in l:
        if isinstance(i, (list, tuple)):
            source = flatten(i, source)
        else:
            source.append(i)
    return source

print(flatten(b, a))
