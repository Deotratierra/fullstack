#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    # ==========================================

    # Conversión de decimal a hexadecimal
    hex_num = hex(250)
    print(hex_num)         # 0xfa
    print(type(hex_num))   # <class 'str'>

    # ------------------------------------------

    # Conversión de hexadecimal a decimal
    dec_num = int(0xfa)
    print(dec_num)        # 250
    print(type(dec_num))  # <class 'int'>

    # ------------------------------------------

    # Conversión de hexadecimal a binario
    bin_num = bin(0xfa)
    print(bin_num)        # 0b11111010
    print(type(bin_num))  # <class 'str'>

    # ------------------------------------------

    # Conversión de hexadecimal a octal
    oct_num = oct(0xfa)
    print(oct_num)        # 0o372
    print(type(oct_num))  # <class 'str'>

    # ==========================================




