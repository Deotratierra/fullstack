## Empaquetado y distribución en Python
El proceso de empaquetado y distribución no es uno de los fuertes de este lenguaje. Seguramente puedes encontrarte cientos de tutoriales en la web desactualizados. Si esta lo está [avisame](https://github.com/mondeja/fullstack/issues) y la actualizaré enseguida.

________________________________

### Archivo de instalación
Realizarlo con [setuptools](https://setuptools.readthedocs.io/en/latest/), ([aquí tienes un ejemplo](https://github.com/mondeja/pymarketcap/blob/master/setup.py)). Recomiendo añadir una lista de clasificadores (`classifiers`) ([aquí tienes todos los posibles](https://pypi.python.org/pypi?%3Aaction=list_classifiers)) para que el proyecto esté clasificado correctamente en [PyPi](https://pypi.python.org/pypi).

Esa es la web oficial de Python para la distribución de paquetes (el famoso `pip`). Si quieres que tus proyectos se instalen mediante `pip install <tu-proyecto>` debes subirlos ahí. Si es así, primero crea una cuenta en [PyPi](https://pypi.python.org/pypi). Cuando hayas creado el archivo de instalación y tengas tu cuenta, sigue estos pasos:

##### 1. `.pypirc`
En la carpeta de tu usuario del sistema (`/home/<tu-usuario>` en Linux) crea un archivo llamado `.pypirc` e inserta el siguiente contenido personalizándolo con tu nombre de usuario y contraseña de PyPi:
```
[distutils]
index-servers =
    pypi

[pypi]
repository: https://upload.pypi.org/legacy/
username: <tu-usuario>
password: <tu-contraseña>
```

Tras guardarlo, protégelo con `sudo chmod 600 .pypirc` (Linux).

##### 2. Creando la distribución
Ahora prueba a ejecutar `python setup.py sdist`. Verás que se crea una carpeta `dist/` en la cual existe un archivo comprimido. Ábrelo o extráelo e inspecciona su contenido. Probablemente observarás que faltan algunos archivos necesarios para que tu programa funcione (por ejemplo el `requirements.txt`).

Para solventar esto, crea un archivo `MANIFEST.in` y añade: `include requirements.txt`. Ahora cuando crees de nuevo la distribución deberías ver que se ha incluido el archivo en tu distribución.

##### 3. Distribuyendo con PyPi
Ten en cuenta que al subir tu distribución a PyPi no podrás volver a subir la misma versión, así que no olvides nunca [versionar tu software](https://es.wikipedia.org/wiki/Versi%C3%B3n_de_software) (en el apartado Versionado encontrarás un script que lo realiza).

Para subir archivos comprimidos a PyPi, primero instala `twine` con el comando `pip install twine`. Entonces ejecuta `twine upload dist/pymarketcap-<version>.tar.gz` donde `<version>` es la versión actual de tu programa.

>Si todo ha salido bien, deberías poder instalar tu programa con `pip install <nombre-de-tu-programa>`.

________________________________

