#!/usr/bin/env python3
# -*- coding: utf-8 -*-

a = [1,2,3,4,5,6,7,8,9]

def circular_selector(int_list, skip):
    skip = skip - 1
    idx = 0
    len_list = len(int_list)
    while len_list > 0:
        idx = (skip + idx) % len_list
        yield int_list.pop(idx)
        len_list -= 1

print([a for a in circular_selector(a,3)])






