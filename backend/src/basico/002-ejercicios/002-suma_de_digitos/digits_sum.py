#!/usr/bin/env python3
# -*- coding: utf-8 -*-

num1 = 4511
num2 = 369301

def digits_sum(number):
    response, total = ("", 0)
    while number != 0:
        rest = number % 10
        response += str(rest)
        total += rest
        number = int(number/10)
        if number > 0:
        	response += " + "
    response += " = " + str(total)
    return response

print(digits_sum(num1))
print(digits_sum(num2))
