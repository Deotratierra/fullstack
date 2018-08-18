## Internacionalización con [Gettext](https://www.gnu.org/software/gettext/manual/html_node/PO-Files.html)

- [Manual de gettext](https://www.gnu.org/software/gettext/manual/html_node/index.html#SEC_Contents)

### Archivos `.po` (Portable Object)
La traducción con gettext se realiza principalmente mediante archivos con extensión `.po`, los cuales son archivos de texto plano editables.

Un archivo `.po` está compuesto de numerosas entradas, y cada entrada almacena la relación entre la cadena de texto original no traducida y su correspondiente traducción. Todas las entradas en un archivo usualmente corresponden a un mismo lenguaje. Esta clase de archivos tienen la siguiente estructura:

```

#  Comentarios del traductor
#. Comentarios extraídos
#: Referencia
#, Flag...
#| msgid cadena-de-texto-previa-no-traducida
msgid cadena-de-texto-no-traducida
msgstr cadena-de-texto-traducida
```

### Ficheros `.mo` (Machine Object)
Los fichero `.mo` son ficheros compilados para la lectura por parte del programa y son de tipo binario. El formato de los ficheros mo es a menudo diferente de sistema a sistema y cada sistema debe tener sus propias utilidades para convertir po’s a mo’s.


_____________________

- [Ejemplo con Gettext + Tornado](https://github.com/mondeja/fullstack/tree/master/backend/src/038-internacionalizacion/gettext/tornado)