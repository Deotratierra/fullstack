from libc.stdio cimport printf

cpdef cadena_c():
    cdef char *c_string = "Soy una cadena de c"
    return c_string

cpdef cadena_py_desde_c():
    cdef char *c_string = "Soy una cadena de c"
    printf("\nConversión de cadena C: '%s' ...\n", c_string)
    cdef bytes py_string1 = c_string
    printf("... en bytes Python con variable de tipo bytes: '%s'\n",
            py_string1)

    py_string2 = <bytes> c_string
    printf("... en bytes Python con casting: '%s'\n",
    	   py_string2)
