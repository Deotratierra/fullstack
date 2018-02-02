## Cadenas en Cython

De forma similar a las semánticas de cadenas en Python3, Cython separa estrictamente las cadenas de bytes de las cadenas unicode. Por encima de todo, esto significa que por defecto no hay una conversión automática entre las cadenas de bytes y las unicode. Toda la codificación y decodificación debe hacerse de forma explícita.

Para facilitar la conversión entre las cadenas de Python y de C en los casos más simples, las directivas a nivel de módulo `c_string_type` y `c_string_encoding` pueden ser usadas para insertar estas conversiones de forma implícita al compilar.

### Tipos de cadenas de Python en código Cython
Cython soporta cuatro tipos de cadenas de Python: `bytes`, `str`, `unicode` y `basestring`. Los tipos `bytes` y `unicode` son los tipos especificados en Python 2.x, llamados `bytes` y `str` en Python3. Adicionalmente Cython también soporta el tipo `bytearray` el cual se comporta como el tipo `bytes` con la diferencia de ser inmutable.

El tipo `str` es especial ya que es el tipo de cadena binaria en Python2 y el de cadena unicode en Python3.

The str type is special in that it is the byte string in Python 2 and the Unicode string in Python 3 (for Cython code compiled with language level 2, i.e. the default). Meaning, it always corresponds exactly with the type that the Python runtime itself calls str. Thus, in Python 2, both bytes and str represent the byte string type, whereas in Python 3, both str and unicode represent the Python Unicode string type. The switch is made at C compile time, the Python version that is used to run Cython is not relevant.

When compiling Cython code with language level 3, the str type is identified with exactly the Unicode string type at Cython compile time, i.e. it does not identify with bytes when running in Python 2.

Note that the str type is not compatible with the unicode type in Python 2, i.e. you cannot assign a Unicode string to a variable or argument that is typed str. The attempt will result in either a compile time error (if detectable) or a TypeError exception at runtime. You should therefore be careful when you statically type a string variable in code that must be compatible with Python 2, as this Python version allows a mix of byte strings and unicode strings for data and users normally expect code to be able to work with both. Code that only targets Python 3 can safely type variables and arguments as either bytes or unicode.

The basestring type represents both the types str and unicode, i.e. all Python text string types in Python 2 and Python 3. This can be used for typing text variables that normally contain Unicode text (at least in Python 3) but must additionally accept the str type in Python 2 for backwards compatibility reasons. It is not compatible with the bytes type. Its usage should be rare in normal Cython code as the generic object type (i.e. untyped code) will normally be good enough and has the additional advantage of supporting the assignment of string subtypes. Support for the basestring type was added in Cython 0.20.



__________________________

> Fuentes:
> - http://cython.readthedocs.io/en/latest/src/tutorial/strings.html