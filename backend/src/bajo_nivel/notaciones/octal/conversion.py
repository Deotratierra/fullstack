#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":

    # =========================================

    # Conversión de decimal a octal
    oct_num = oct(81)
    print(oct_num)        # 0o121
    print(type(oct_num))  # <class 'str'>

    # --------------------------------

    # Conversión de octal a decimal
    dec_num = int(0o121)
    print(dec_num)        # 81
    print(type(dec_num))  # <class 'int'>

    # --------------------------------

    # Conversión de octal a binario
    bin_num = bin(0o121)
    print(bin_num)        # 0b1010001
    print(type(bin_num))  # <class 'str'>

    # --------------------------------

    # Conversión de octal a hexadecimal
    hex_num = hex(0o121)
    print(hex_num)        # 0x51
    print(type(hex_num))  # <class 'str'>

    # =========================================
