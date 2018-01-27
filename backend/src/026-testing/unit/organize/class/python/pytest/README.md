## Encapsulamiento de tests en clases con pytest
La forma en la que pytest descubre los tests sigue las convenciones de Python para el descubrimiento de tests, así que todas las funciones que empiecen con `test*` dentro de las las clases que empiecen con `Test*` dentro de los archivos que cumplan una de las expresiones `test_*` o `*_test` serán considerados test y ejecutados.
