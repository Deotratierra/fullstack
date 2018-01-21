#!/bin/bash

# ====================================================

# Saber si existe un comando
command_exists() {
	command -v "$@" > /dev/null 2>&1
}

if command_exists docker; then
  echo "El comando 'docker' existe en tu sistema."
else
  echo "El comando 'docker no existe en tu sistema."
fi

# ====================================================
