## Benchmarking en tests con pytest

#### [Documentación de referencia](http://pytest-benchmark.readthedocs.io/en/stable/)

Para agregar una función de benchmarking en cada módulo de nuestros tests con pytest seguimos los siguientes pasos:

1. Instalamos el módulo: `pip3 install pytest-benchmark`.
2. Escribimos una función en nuestros tests que toma como argumento el parámetro `benchmark` y luego con ese parámetro ejecutamos la función a cronometrar. Algo así:

```python
def test_x(benchamrk):
    benchmark(funcion_larga, arg1, arg2)
```

3. Ejecutamos pytest como de costumbre y debe aparecer un cronometrado bastante completo de la función.


> Fuentes:
> - https://mgeisler.github.io/pyzurich/talks/2017-07-06-pytest-benchmark/#13

