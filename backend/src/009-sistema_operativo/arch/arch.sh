#!/bin/bash

# ======================================

# Obtener la arquitectura en bits
bits_arch() {
  if [ `uname -m` == 'x86_64' ]; then
    BITS_ARCH=64
  else
    BITS_ARCH=32
  fi
}

bits_arch
echo $BITS_ARCH

# --------------------------------

# Otra forma
bits_arch2() {
  if [ `getconf LONG_BIT` = "64" ]
  then
    BITS_ARCH=64
  else
    BITS_ARCH=32
  fi
}

bits_arch2
echo $BITS_ARCH

# ========================================


