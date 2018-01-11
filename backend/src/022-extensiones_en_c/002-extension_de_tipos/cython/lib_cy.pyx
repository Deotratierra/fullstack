cdef class Punto:
    # Los atributos de clase se inicializan en el cuerpo
    cdef public double x  # Por defecto, los atributos son privados
    cdef double y
    # Si intentamos acceder a un atributo privado nos lanzará:
    #     AttributeError: 'Punto' object has no attribute 'y'

    def __init__(self, double x, double y):
        self.x = x
        self.y = y

# Si usamos la clase en una función debemos recordar que es un nuevo tipo
cdef unir(Punto a, Punto b):
    pass
