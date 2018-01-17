#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket

# ===================================================
#                 Información local

# Obtener host local
local_host = socket.gethostname()
print(local_host)# debian

# Obtener dirección IP local
print(socket.gethostbyname(local_host))  # 127.0.1.1

# Obtener IP local de forma completa:
def local_ip():
    """Get local IP host address"""
    return [l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] \
        if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), s.getsockname()[0],  \
        s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0]

# ===================================================
#                 Información remota

# Obtener IP de un host remoto
remote_host = "www.github.com"

try:
    print("Dirección IP de %s: %s" % (remote_host, socket.gethostbyname(remote_host)))
except socket.error:
    print("%s: %s" % (remote_host, socket.error))


# ===================================================
