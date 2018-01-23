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

# Ejemplo con constructor a nivel C

# Funciones de la API de CPython para gestionar la memoria
from cpython.mem cimport PyMem_Malloc, PyMem_Free #PyMem_Realloc

cdef class Matrix:
    cdef:
        unsigned int nfilas, ncolumnas
        double *_matrix

    # El lugar correcto para colocar la asignación dinámica de espacio
    # en memoria a self._matrix es un método __cinit__

    def __cinit__(self, nf, nc):
        self.nfilas = nf
        self.ncolumnas = nc

        # Casting a número decimal
        self._matrix = <double*>PyMem_Malloc(nf * nc * sizeof(double))

        # Esto:
        #self._matrix = <double*>malloc(nf * nc * sizeof(double))
        # ... produce el siguiente error durante la compilación:
        # Storing unsafe C derivative of temporary Python reference

        # http://docs.cython.org/en/latest/src/tutorial/memory_allocation.html
        # Parafraseando a la documentación de Cython:
        #     "Las funciones de la API de CPython para asignar memoria en el stack
        #     de Python generalmente son preferibles sobre las funciones C de bajo nivel,
        #     ya que la memoria que proporcionan se contabiliza en el sistema de
        #     administración de memoria interna de Python.
        #     También tienen optimizaciones especiales para bloques de memoria más pequeños,
        #     lo que acelera su asignación al evitar costosas llamadas al sistema operativo."

        print("Espacio asignado a la matriz dentro del constructor __cinit__")

        if self._matrix == NULL:
            raise MemoryError()

    def __init__(self, nf, nc):
        # La definición de atributos de instancia podemos realizarla
        # en el método __cinit__ y es lo más correcto en este caso,
        # así no es necesario pasarlos a ambos constructores,
        # pero quiero dejar claro que realizarla aquí también sería posible,
        # pero no es lo más seguro:

        #self.nfilas = nf
        #self.ncolumnas = nc
        print("Constructor __init__ llamado")

    def __dealloc__(self):
        if self._matrix != NULL:
            PyMem_Free(self._matrix)
            print("Espacio desasignado a la matrix en __dealloc__")


# ================================================================


# Ejemplo con Herencia

# ================================================================