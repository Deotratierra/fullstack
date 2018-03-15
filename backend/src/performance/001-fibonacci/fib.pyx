def fib(long n):
    cdef long i
    cdef long a=0, b=1
    for i in range(n):
        a, b = a + b, a
    return a
