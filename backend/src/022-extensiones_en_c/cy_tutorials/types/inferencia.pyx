cimport cython

# Decorador para inferenciar las variables
# como si fueran estáticas en tiempo de compilación:
@cython.infer_types(True)
def funcion_inferida(x):
    i = 1
    j = 2.0
    response = 0.0
    for _ in range(x):
        response += i*j
    return i + j

def funcion_no_inferida(x):
    i = 1
    j = 2.0
    response = 0.0
    for _ in range(x):
        response += i*j
    return i + j
