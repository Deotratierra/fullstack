
cpdef int summa(x):
    cdef int y = 0
    cdef int i
    for i in range(x):
        y += i + 1
    return y

