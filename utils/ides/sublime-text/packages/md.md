## Paquetes Markdown para SublimeText


### MarkdownEditing
Sirve para editar en Markdown desde SublimeText, proporcionando resalto de sintaxis y un fondo claro contra unas letras oscuras. Imprescindible.

_____________________

### MarkdownPreview
Sirve para configurar un comando de teclas para abrir el archivo que estamos escribiendo en el navegador ya renderizado. Después de instalarlos nos vamos a `Preferences` -> `Key bindings - User` y añadimos la siguiente combinación de teclas dentro de la lista:

```json
{ "keys": ["alt+m"], "command": "markdown_preview", "args": {"target": "browser", "parser":"markdown"} }
```

Tras esto, pulsando <kbd>Alt</kbd> + <kbd>M</kbd> se nos abrirá el navegador donde observaremos el archivo renderizado.

____________________