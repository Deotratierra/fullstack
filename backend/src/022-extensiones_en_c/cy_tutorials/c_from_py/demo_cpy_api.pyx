# ===================================================

from cpython.version cimport (
	PY_VERSION_HEX,
    PY_MAJOR_VERSION,
    PY_MINOR_VERSION
)
from libc.stdio cimport printf
# https://github.com/cython/cython/blob/master/Cython/Includes/cpython/version.pxd

def demo_version():
    # Python version >= 3.2 final ?
    print(PY_VERSION_HEX >= 0x030200F0)  # Versión en hexadecimal

    printf("%d\n", PY_MAJOR_VERSION)
    printf("%d\n", PY_MINOR_VERSION)

# ===================================================

# Ejemplo usando la API de CPython
from cpython.number cimport PyNumber_Check
# PyNumber_Check comprueba si una variables sigue los protocolos de los
# objetos numéricos (devuelve 1 si es así, 0 en caso contrario)
# https://github.com/cython/cython/blob/master/Cython/Includes/cpython/number.pxd

def demo_number():
    cdef int numero
    cdef int resultado
    numero = 5
    # Preguntamos si una variable de C podría ser un objeto numérico en Python
    printf("Dado el valor %d ¿podríamos decir que es un número?\n", numero)
    resultado = PyNumber_Check(numero)
    print(bool(resultado))  # True

    # Comprobamos si un objeto de cadena de caracteres de Python podría ser un objeto númerico
    cadena = "hola"
    print("Dado el objeto %s ¿podríamos decir que es un número?" % cadena)
    resultado = PyNumber_Check(cadena)
    print(bool(resultado))  # False

    # ¿Y si la cadena parece un número?
    cadena = "97"
    print("Dado el objeto %s ¿podríamos decir que es un número?" % cadena)
    resultado = PyNumber_Check(cadena)
    print(bool(resultado))  # False

# ===================================================
