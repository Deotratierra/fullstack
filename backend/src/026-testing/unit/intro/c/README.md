## Unittesting para C en Python
Cuando testeamos código C no hace falta que escribamos los tests en el mismo lenguaje ya que no necesitamos una herramienta de tan bajo nivel para una tarea que la mayoría de ocasiones es bastante simple.

Así que podemos usar [cffi](https://pypi.python.org/pypi/cffi) paa generar un pequeño puente entre C y Python. Usa la función `load` ubicada en el archivo `utils.py` de este directorio para crear este simple puente.

Esta función crea un archivo llamado `biblioteca_.c` y otro archivo con extensión `.so` que pueden ser molesto dejarlos, como es el caso. Para eliminarlos usamos una función que envuelve a los tests del módulo usando los decoradores [`fixtures`](https://docs.pytest.org/en/latest/fixture.html#automatic-grouping-of-tests-by-fixture-instances) de `pytest`.

> Fuentes:
> - https://www.youtube.com/watch?v=zW_HyDTPjO0