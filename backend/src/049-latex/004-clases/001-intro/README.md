## Clases
Cuando escribimos `\documentclass{article}` en un documento `.tex`, estamos incluyendo el archivo `article.cls`. Este define todos los comandos específicos de la clase como `\section` o `\title` que [estructuran tu documento](https://es.wikibooks.org/wiki/Manual_de_LaTeX/La_estructura_de_un_documento_en_LaTeX).

- Para cargar una clase: `\documentclass{clase}`

### Creando tu propio archivo de clase
La forma más ordenada de personalizar el formato de un documento es mantener toda la información del formato en un archivo `.cls`. Esto mantiene la estructura de tu documento separada limpiamente del estilo y facilita la reusabilidad.

El primer ejemplo lo puedes ver en este mismo directorio. En el archivo `.tex` hay secciones propias de una clase `article`, pero estamos usando la clase `clase`. Dentro del archivo `clase.cls` importamos la clase `article`.

- Cargar una clase en un documento `.cls`: `\LoadClass{clase}`

Lo que hacemos en el primer ejemplo es crear una clase personalizada partiendo de la clase `article`.

_________________________________

### ¿Clases o paquetes?
Si tu archivo contiene comandos que controlan la apariencia de un tipo especial de documento, entonces escribe una clase, pero si añade características que son independientes del tipo de documento (pueden ser usadas en libros, reportajes, artículos...) entonces escribe un paquete.


> Fuentes:
> - https://es.sharelatex.com/blog/2011/03/27/how-to-write-a-latex-class-file-and-design-your-own-cv.html