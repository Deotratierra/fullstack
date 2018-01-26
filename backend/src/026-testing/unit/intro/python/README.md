## Testing en Python con pytest
> [Código fuente](https://github.com/pytest-dev/pytest)

La diferencia fundamental de [`pytest`](https://docs.pytest.org/en/latest/) con la bibilioteca estándar `unittest` es que los tests son funciones simples de Python en lugar de forzar a los desarrolladores a incluir sus tests dentro de largas clases.

- Instalación:
    + Linux: `pip3 install pytest`
    + Windows: `pip3 install colorama pytest`

### Introducción
Para escribir tests con `pytest` simplemente crea un archivo que cuadre con la expresión regular `test_*.py` o `*_test.py` y dentro escribe funciones que del estilo `test*()`.

> [Aquí tienes algunos ejemplos](https://github.com/mondeja/fullstack/tree/master/backend/src/026-testing/unit/intro/python/pytest/ejemplos)

Para ejecutar los tests en un directorio simplemente muévete dentro del directorio y ejecuta `pytest`. El programa descubrirá en todos los directorios, desde la raíz donde te encuentras, los archivos donde se encuentran tus tests y los ejecutará.