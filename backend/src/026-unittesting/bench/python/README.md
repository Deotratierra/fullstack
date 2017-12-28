## Benchmarking en tests unitarios con Python
Para medir el tiempo que tardan los tests en ejecutarse usamos la biblioteca `nose` con el plugin `nose-timer`: `pip3 install nose nose-timer`.

> [Documentación de nose](http://nose.readthedocs.io/en/latest)

Funciona con tests unitarios escritos con el módulo `unittest` de la biblioteca estándar.

El comportamiento de los plugins puede ser [personalizado](https://stackoverflow.com/questions/24150016/how-to-benchmark-unit-tests-in-python-without-adding-any-code).

### Comandos
- Testear módulo: `nosetests test.py --with-timer`

### Ejemplos
Puedes ver un ejemplo de cómo guardar el benchmarking en un archivo `.json` desde [aquí](https://github.com/mondeja/pymarketcap/blob/master/tests/test.py).
