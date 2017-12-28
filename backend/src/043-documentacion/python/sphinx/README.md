## Sphinx
#### [Referencia](http://www.sphinx-doc.org/en/stable/contents.html)

### Comandos
- Instalación: `pip3 install sphinx`
- Comenzar la documentación: `sphinx-quickstart`
- Construcción: `sphinx-build -b html sourcedir builddir` ó `make html`

### Estructura
Cuando comenzamos un proyecto con Sphinx (recomendado hacerlo en un directorio `doc`) se crean varios archivos, de los cuales:
- `conf.py`: Configuración
- `_static`: Archivos estáticos
- `_templates`: Plantillas personalizadas
- `_build`: Archivos necesarios para la construcción de la documentación, como plantillas html, imágenes, archivos Javascript...
- `index.<rst/txt>`: Es el documento maestro. Sirve como página de inicio.

>También se incluyen archivos ejecutables los cuales sirven para generar los documentos.

### Sintaxis (ReStructuredText)
#### [Referencia](http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html)

Sphinx usa como reglas de escritura el lenguaje [ReStructuredText](https://es.wikipedia.org/wiki/ReStructuredText). Este fue creado para poder generar documentos equivalentes en HTML, LaTex, docbook... etc. Para poder automatizar la documentación, debemos escribir los docstrings según las reglas de este lenguaje.


### Guía de estilo Google
#### [Referencia](http://sphinxcontrib-napoleon.readthedocs.io/en/latest/index.html)

Seguir las [guía de estilo de Google para la documentación Python](http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html) es una gran opción. Para usar su sintaxis incluimos la extensión en el archivo de configuración:
```python
extensions = [...,
'sphinx.ext.napoleon']
```


### Automatizar la documentación
Con Sphinx podemos automatizar la documentación. A partir de un paquete podemos generar la documentación usando los docstrings (`__doc__`) de sus funciones y clases.

Para ello usamos el script `sphinx-apidoc -o <[opciones]> <carpeta_de_salida> <paquete_de_python>`. Este comando generará documentación de los módulos con archivos `.rst` (o los que le indiquemos). Estos archivos pueden incluirse luego fácilmente en el proyecto. [Desde aquí](http://www.sphinx-doc.org/en/stable/invocation.html#invocation-apidoc) podemos consultar todas las opciones del script.

#### Buenas prácticas
Al generar la documentación automáticamente con `sphinx-apidoc`, incluir en el comando:
`sphinx-apidoc -o docs <paquete> -f -F -T -H <nombre_del_proyecto> -A <autor> -V <version> -R <release>`

Desde `-H`, las opciones podemos configurarlas desde el archivo `conf.py`. Para construir usar el siguiente comando: `sphinx-build -b html docs docs/_build`. Luego podemos restructurar las carpetas cuando la documentación esté lista, ya que seguramente necesitará algunos retoques.

### Theme
Podemos cambiar el aspecto de la documentación fácilmente desde el archivo `conf.py`, en la variable `html_theme`.

Por ejemplo, si queremos que el estilo sea el de [ReadTheDocs](https://readthedocs.org/) podemos importar el tema e incluirlo:
```
import sphinx_rtd_theme
html_theme = 'sphinx_rtd_theme'
```
