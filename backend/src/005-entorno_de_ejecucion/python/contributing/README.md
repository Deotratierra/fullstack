## Contribuyendo a Python

#### [Documentación de referencia](https://devguide.python.org/)

### Forking
1. Ve al [código fuente de CPython](https://github.com/python/cpython) y haz un fork del mismo a tu cuenta.
2. Clónalo localmente: `git clone https://github.com/<TU_USUARIO>/cpython`
3. Constrúyelo (en Unix): `./configure --with-pydebug && make -j`
4. Ejecuta los tests: `./python -m test -j8`

### Flujo básico de trabajo
1. Crea una nueva rama donde trabajarás para un problema, por ejemplo: `git checkout -b fix-issue-12345 master`
> Si un problema no existe, [créalo](https://bugs.python.org/) (necesitas loguearte).

2. Resuelve el problema y ejecuta `make patchcheck`. Si todo está OK entonces haz commit.
3. Haz push a tu rama en Github y crea un pull request. Incluye el número del problema usando `bpo-NNNNN` in en la descripción del pull request. Por ejemplo: `bpo-12345: Fix some bug in spam module`

> Si contribuyes por primera vez debes firmar y enviar la licencia. [Sigue este pequeño tutorial](https://devguide.python.org/pullrequest/#licensing).


