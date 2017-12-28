#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def permute(lista):
    perms = [[]]
    for elem in lista:
        new_perms = []
        for perm in perms:
            print(perm, elem)
            for i in range(len(perm)+1):
                new_perms.append(perm[:i] + [elem] + perm[i:])
                #print(perm[:i] + [elem] + perm[i:])
        perms = new_perms
    return perms

def permutations(lista):
    n = len(lista)
    response = n
    for mul in range(1, n):
        response = mul*response
    return response


test = ["h", "o", "l"]
print(test)
print(permute(test))

print(permutations(test))
