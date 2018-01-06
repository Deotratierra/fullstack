## Entorno de desarrollo LaTeX
- Instalación (Debian): `sudo apt-get install texlive-full`

### Compilar
La forma más fácil de compilar un documento `.tex` en `.pdf` es usando `pdflatex`:

```bash
pdflatex documento.tex
```

Esto creará un documento `.pdf` con el mismo nombre que el original.

> Para abrir documentos `.pdf` en Debian podemos usar `xdg-open documento.pdf`.

________________________________________________

Usando el programa `latex` podemos compilar a `.dvi`, simplemente ejecutamos:

```bash
latex documento.tex
```

Los [archivos DVI](https://es.wikipedia.org/wiki/DVI_(TeX)) son formatos de archivo utilizados como salida de `TeX`. Pueden ser leídos sin importar el tipo de archivo utilizado, ya sea una impesora o un programa.
Podemos leer los archivos DVI en Linux con el programa `xdvi`. Simplemente ejecutamos `xdvi dcoumento.dvi`.
