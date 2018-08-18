#!/usr/bin/sh

# Obtener IPs de la máquina actual
ip addr show

ip addr show eth0

hostname -I

# Obtener nombre del host
hostname

# Obtener todas las IPs de las máquinas conectadas
# a la red local:
nmap -sP 192.168.1.0/24

# o cambiando la máscara de subred
nmap -sP 192.168.0.0/24

