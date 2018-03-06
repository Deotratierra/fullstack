#!/bin/sh

# Instala el siguiente tema gráfico para Jupyter Notebook:
# https://github.com/powerpak/jupyter-dark-theme
#    ¡Cuidado porque sobrescribirá tu tema actual!

wget https://raw.githubusercontent.com/powerpak/jupyter-dark-theme/master/custom.css

CUSTOM_DIR="~/.jupyter/custom"
if [ ! -d "$CUSTOM_DIR" ]; then
  mkdir "$CUSTOM_DIR"
fi

mv custom.css "$CUSTOM_DIR/custom.css"
