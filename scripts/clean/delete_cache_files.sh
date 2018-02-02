#!/bin/bash

# Borrar todos los directorios de checkpoints de JupyterNotebook
find . -type d -name ".ipynb_checkpoints" -exec rm -r {} +

# Borrar todos los directorios de cache de Python
sudo find . -type d -name "__pycache__" -exec rm -r {} +
