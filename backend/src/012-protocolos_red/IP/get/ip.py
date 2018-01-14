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

# ===================================================
#                 Información remota

# Obtener IP de un host remoto
remote_host = "www.github.com"

try:
    print("Dirección IP de %s: %s" % (remote_host, socket.gethostbyname(remote_host)))
except socket.error:
    print("%s: %s" % (remote_host, socket.error))


# ===================================================