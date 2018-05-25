#!/usr/bin/env python3
# -*- coding: utf-8 -*-

IP = "192.168.1.11"
MASKS = ["255.0.0.0", "255.255.0.0", "255.255.255.0"]

def ip_to_bin(address):
    """Toma una dirección IPv4 como string
    y la devuelve como string en binario.

    Por ejemplo, le pasamos "255.255.0.0" y
    devuelve "11111111.11111111.00000000.00000000"
    """
    groups = address.split(".")
    response = []
    for group in groups:
        str_group = str(bin(int(group))).split("b")[1]
        for _ in range(len(str_group), 8):
            str_group += "0"
        response.append(str_group)
    return ".".join(response)

def masking(address, mask):
    """Pasa una dirección IP y una máscara de subred
    y enmascara la parte de la dirección IP que corresponde
    a 0 en números binarios en la máscara.
    """
    b_addr, b_mask = ( ip_to_bin(address).split("."),
    	               ip_to_bin(mask).split(".") )
    response = []
    for addr_group, mask_group in zip(b_addr, b_mask):
        masked = (int(addr_group, 2) & int(mask_group, 2))
        if masked == 0:
            masked = "XXX"
        response.append(str(masked))
    return ".".join(response)




if __name__ == '__main__':
    print("\nIP de ejemplo: %s" % IP)
    for MASK in MASKS:
        masked = masking(IP, MASK)
        print("Máscara de subred: %15s | Resultado tras enmascaramiento: %15s" % (MASK, masked))
    print()
