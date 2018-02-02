## Testing multiversión con Tox
Tox es una herramienta de administración de entornos virtuales para diferentes versiones de Python y línea de comandos para testing.

Se puede usar para:
- Comprobar que tu paquete se instala correctamente con diferentes versiones de Python.
- Ejecutar tus tests en cada uno de los entornos virtuales, configurándola con la herramienta de tests de tu elección.
- Actuar como un frontend para los servidores de integración contínua, reduciendo bastante los sitemas de planificación por plantillas y el testing basado en scripts de Shell.

### Instalación y configuración
- Instalación: `pip install tox`

Para configurarlo hay que crear un archivo `tox.ini`. Se puede generar personalizo respondiendo preguntas ejecutando `tox-quickstart`.

- [Ejemplo de un archivo `tox.ini`](https://github.com/mondeja/fullstack/tree/master/backend/src/026-testing/multiversion/intro/tox/tox.ini).

Para instalar tu paquete distribuido en forma `sdist` y ejecutarlo en las diferentes versiones de Python que has indicado en el archivo de configuración simplemente debes ejecutar: `tox`

#### [Documentación con ejemplos](https://tox.readthedocs.io/en/latest/examples.html)

### Instalación de bibliotecas antes de ejecutar tests
- [Documentación de referencia](https://tox.readthedocs.io/en/latest/example/basic.html#depending-on-requirements-txt-or-defining-constraints)

Para añadir depedencias que deben ser instaladas antes de ejecutar los tests en cada entorno podemos añadir `-rrequirements.txt` al parámetro `deps` del archivo `tox.ini`. Tox ejecutar `python install -r requirements.txt` antes de iniciar los tests.

_______________________

> Fuentes:
> - https://tox.readthedocs.io/en/latest/
> - - https://github.com/yaml/pyyaml/blob/master/tox.ini