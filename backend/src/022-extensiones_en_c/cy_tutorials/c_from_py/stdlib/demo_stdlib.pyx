# ===============================================================

# Importamos funciones de la biblioteca estándar
from libc.stdlib cimport atoi
from libc.string cimport strcpy

def demo_intro_stdlib():
    # Definimos un número como entero y una cadena de caracteres
    cdef int numero
    cdef char cadena[20]
    # Copiamos dentro de la dirección de la cadena un número como cadena
    strcpy(cadena, "98993489");
    numero = atoi(cadena); # Convertimos el número en tipo entero

    print(type(cadena))  # <class 'bytes'>
    print(type(numero))  # <class 'int'>

# ================================================================

# Usando el módulo matemático de C desde Python
from libc.math cimport sqrt
from libc.stdio cimport printf

def demo_math():
    cdef double numero
    numero = 423.67
    printf("Raíz cuadrada de %f = %f\n", numero, sqrt(numero))

# ================================================================
