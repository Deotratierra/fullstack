# ===============================================================

# Función llamable desde Python y desde código Cython.
def py_compiled_factorial_not_typed(n):
    """Calcula el factorial del número pasado como parámetro."""
    if n <= 1:
        return 1
    return n * py_compiled_factorial_not_typed(n-1)

# ===============================================================

# Función llamable desde Python y desde código Cython.

# Cuando es llamada desde Python Cython convierte el argumento
# n de un entero de Python a un long de C automáticamente.
# Esta conversión desde entero de Python a long de C toma tiempo, y,
# al ser recursiva la función, se produce muchas veces por lo cual
# tiparla estáticamente no tiene sentido ya que no se gana
# rendimiento (habría que hacerla no recursiva)
def py_compiled_factorial_typed(long n):
    """Calcula el factorial del número pasado como parámetro."""
    if n <= 1:
        return 1
    return n * py_compiled_factorial_typed(n-1)

# ===============================================================

# Función llamable sólo desde Cython.
cdef long c_factorial(long n):
    """Calcula el factorial del número pasado como parámetro."""
    if n <= 1:
        return 1
    return n * c_factorial(n-1)

# Para que la función anterior pueda ser llamada desde Cython
# hemos de envolverla con una función def
def envoltura_c_factorial(long n):
    """Calcula el factorial del número pasado como parámetro."""
    return c_factorial(n)

# ===============================================================

# Función llamable desde Python y desde código Cython.
# Su rendimiento será idéntico a la versión envoltura_c_factorial()
cpdef long c_py_factorial(long n):
    if n <= 1:
        return 1
    return n * c_py_factorial(n-1)