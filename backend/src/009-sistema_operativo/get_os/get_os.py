#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

# Obtener la plataforma
sys.platform

if sys.platform.startswith('freebsd'):
    print("Estamos en FreeBSD")
elif sys.platform.startswith('linux'):
    print("Estamos en Linux")
elif sys.platform.startswith('win32'):
    print("Estamos en Windows32")
elif sys.platform.startswith('cygwin'):
    # https://es.wikipedia.org/wiki/Cygwin
    print("Estamos en Windows/Cygwin")
elif sys.platform.startswith('darwin'):
    print("Estamos en MacOSX")
else:
    print("No tengo ni idea de dónde estamos, pero quizás esto te ayude: %s" % sys.platform)




