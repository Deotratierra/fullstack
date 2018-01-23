# ================================================================

# Ejemplo con atributos de clase

cdef class Punto:
    """Clase para representar un punto en 3 dimensiones"""

    # Los atributos de clase se inicializan en el cuerpo
    cdef public int x      # Miembro accesible para lectura y sobreescritura
    cdef readonly int y    # Mimebro sólo accesible en forma de lectura
    cdef int z             # Mimebro no accesible desde el exterior (por defecto privado)

    # Si intentamos acceder a un atributo privado nos lanzará:
    #     AttributeError: 'Punto' object has no attribute 'z'
    # Si intentamos acceder a un atributo no sobreescribible nos lanzará:
    #    AttributeError: attribute 'y' of 'punto.PuntoA' objects is not writable

    def __init__(self, int x, int y, int z):
        self.x = x
        self.y = y
        self.z = z

# ================================================================

# Ejemplo con Herencia

# ================================================================