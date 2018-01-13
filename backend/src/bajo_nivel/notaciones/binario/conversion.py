#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":

    # =========================================

    # Conversión de decimal a binario
    bin_num = bin(81)
    print(bin_num)        # 0b1010001
    print(type(bin_num))  # <class 'str'>

    # --------------------------------

    # Conversión de binario a decimal
    dec_num = int("0b1010001", 2)
    print(dec_num)        # 81
    print(type(dec_num))  # <class 'int'>

    # --------------------------------

    # Conversión de binario a octal
    oct_num = oct(int("0b1010001", 2))
    print(oct_num)        # 0o121
    print(type(oct_num))  # <class 'str'>

    # --------------------------------

    # Conversión de binario a hexadecimal
    hex_num = hex(int("0b1010001", 2))
    print(hex_num)        # 0x51
    print(type(hex_num))  # <class 'str'>

    # =========================================

