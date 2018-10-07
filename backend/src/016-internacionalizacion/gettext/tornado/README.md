## Usar gettext con tornado de forma nativa

1. Añade al manejador donde quieres usar una cadena de texto traducida el código `_ = self.locale.translate` para poder usar de forma fácil cadenas traducibles.
2. Creamos una carpeta para almacenar todos los archivos de traducción: `mkdir locale`.
3. Con el script ubicado en este directorio `makemessages.ru` puedes crear archivos `.po` para los idiomas que necesites de forma fácil. Ejecuta con `bash makemessages.sh ru` (aquí `ru` es el idioma ruso, cambia por el que quieras). Verás que aparece un nuevo directorio para el idioma.
4. Edita manualmente los archivos `.po` traduciendo las cadenas desde el inglés al lenguaje del archivo.
5. Ejecuta el script `compilemessages.sh` con `bash compilemessages.sh ru` y se creará un archivo `.mo`. Si te aparece un error `Sucesión de bytes inválida` cambia en el archivo `.po` la línea `"Content-Type: ...` por `"Content-Type: text/plain; charset=UTF-8\n"`.
6. Carga las traducciones en el proyecto con la función [`tornado.locale.load_gettext_translations(<locale_dir>, <domain>)`](http://www.tornadoweb.org/en/stable/locale.html#tornado.locale.load_gettext_translations)





### Fuentes:
- http://www.lexev.org/en/2015/tornado-internationalization-and-localization/
- https://stackoverflow.com/questions/1083518/msgfmt-invalid-multibyte-sequence-error-on-a-polish-text