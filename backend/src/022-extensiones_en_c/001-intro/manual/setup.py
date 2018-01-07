from distutils.core import setup, Extension

# Definimos el modulo de extension
summa_module = Extension('lib_c', sources=['lib_c.c'])

# Ejecutar el setup
setup(ext_modules=[summa_module])