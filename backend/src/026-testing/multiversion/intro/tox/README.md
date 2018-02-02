## Testing multiversión con Tox
Tox es una herramienta de administración de entornos virtuales para diferentes versiones de Python y línea de comandos para testing.

Se puede usar para:
- Comprobar que tu paquete se instala correctamente con diferentes versiones de Python.
- Ejecutar tus tests en cada uno de los entornos virtuales, configurándola con la herramienta de tests de tu elección.
- Actuar como un frontend para los servidores de integración contínua, reduciendo bastante los sitemas de planificación por plantillas y el testing basado en scripts de Shell.

### Instalación y configuración
- Instalación: `pip install tox`

Para configurarlo hay que crear un archivo `tox.ini`. Se puede generar personalizo respondiendo preguntas ejecutando `tox-quickstart`.

- Ejemplo de un archivo `tox.ini`.
```
[tox]
envlist = py26,py27,pypy,py33,py34,py35,py36

[testenv]
deps =
    Cython
commands =
    python setup.py test
```

Para instalar tu paquete distribuido en forma `sdist` y ejecutarlo en las diferentes versiones de Python que has indicado en el archivo de configuración simplemente debes ejecutar: `tox`

#### [Documentación de referencia con ejemplos](https://tox.readthedocs.io/en/latest/examples.html)

_______________________

>Fuentes:
- https://tox.readthedocs.io/en/latest/
- https://github.com/yaml/pyyaml/blob/master/tox.ini