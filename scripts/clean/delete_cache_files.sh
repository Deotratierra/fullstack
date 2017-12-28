#!/bin/bash

# Borrar todos los directorios de checkpoints de JupyterNotebook
find -name ".ipynb_checkpoints" -exec rm -rf {} \;

# Borrar todos los directorios de cache de Python
find -name "__pycache__" -exec rm -rf {} \;
