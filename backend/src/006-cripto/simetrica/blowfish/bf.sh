#!/bin/bash

# Demostración de uso del algoritmo Blowfish con OpenSSL
echo "Cifrar información:"
openssl bf -e -in info.txt -out info.enc.bf

echo
echo "Descifrando información:"
openssl enc -bf -d -in info.enc.bf -out info_descifrada.txt
