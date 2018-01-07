#!/bin/bash

# ======================================

# Obtener la arquitectura en bits
bits_arch() {
  if [ `uname -m` == 'x86_64' ]; then
    return 64
  else
    return 32
  fi
}

bits_arch
echo $?

# --------------------------------

# Otra forma
bits_arch2() {
  if [ `getconf LONG_BIT` = "64" ]
  then
    return 64
  else
    return 32
  fi
}

bits_arch2
echo $?

# ========================================


