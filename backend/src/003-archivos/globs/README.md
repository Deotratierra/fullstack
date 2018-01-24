## Globs

En los entornos Unix, los patrones **glob** especifican un conjunto de nombres de archivos con caracteres comodines. For ejemplo, el comando Unix `mv *.txt textfiles/` mueve todos los archivos del directorio actual cuyos nombres terminan en `.txt`  al directorio `textfiles`. 

### `*`
Representa cualquier caracter cualquier número de veces. Por ejemplo `*foo` coincide con `foo`, `foobar`, `foo123`... etc. Nunca coincide con los caracteres de comienzo de un archivo oculto.

### `?`
Representa cualquier caracter sólo una vez. Por ejemplo `???` coincide con `foo` pero no con `foobar`. El glob `???*` coincide con todos los nombres que tengan 3 o más caracteres de largo.

### `[]`
Los caracteres encerrados entre `[` `]` representan todo lo que coincida con su contenido, una sóla vez. 

Por ejemplo `[Abc]` coincidirá con `A`, con `b` y con `c`, cada uno por separado, pero nunca con `a` ni con `Abc`. Si quisieramos buscar por los caracteres `abc` y que diera igual que cada letra fuera mayúscula o minúscula usaríamos: `[aA][bB][cC]` y coincidiría con `aBc`, `ABC`, `abC`... etc.

Si queremos añadir caracteres más arbitrarios podemos usar:
- Cualquier letra minúscula: `[[:lower:]]`
- Cualquier letra mayúscula: `[[:upper:]]`
- Cualquier caracter alfanumérico: `[[:aplha:]]`

### Escapando comodines
- `echo "*"`
- `echo '*'`
- `echo \*`

>Referencias
- http://teaching.idallen.com/cst8207/15w/notes/190_glob_patterns.html
- https://en.wikipedia.org/wiki/Glob_(programming)