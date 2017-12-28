## Hola mundo en LaTeX

### Ejemplo simple ([ver](https://drive.google.com/open?id=1RmolhSj8WL5CAUHYtb_-t1OfYt56A614))
```latex
\documentclass{article}

\begin{document}
Primer documento. Este es un simple ejemplo, sin parámetros o paquetes extra incluidos.
\end{document}
```

Con `\documentclass{article}` especificamos que el documento es de la clase artículo. Con `\begin{document}` `\end{document}` indicamos el principio y el final del documento.

Puedes observar que la tilde en la *a* de `parámetros` no se renderiza. Para solcuionarlo debemos especificar la codificación `utf-8` en el documento (ver siguiente).

### Ejemplo medio ([ver](https://drive.google.com/open?id=1VNuELUhbEpTpdHybiEyy7eDRCa6lh7Lz))
```latex
\documentclass{article}
\usepackage[utf8]{inputenc}

\title{Título del documento}
\author{Álvaro Mondéjar}
\date{Fecha del documento}

\begin{document}

Segundo documento, este es un ejemplo con título, autor fecha y comentarios no renderizados. La codificación del documento es UTF-8.

% Contenido del documento
% En LaTeX escribimos comentarios con el carácter %

% Las representaciones matemáticas en LaTeX se escriben entre los caracteres `\[` y `\]`.
\end{document}
```

Con `\usepackage[utf8]{inputenc}` indicamos codificación UTF-8. Con `\title` `\author` y `\date` indicamos el título autor y la fecha del documento, lo cual se renderizará al principio. Para escribir comentarios usamos el caracter `%`.

### [Ejemplo complejo](https://www.sharelatex.com/project/5a25184892eaa2389b411a8d)

