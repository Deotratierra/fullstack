## Tipos de archivos comprimidos

### Zip
Comprime los ficheros de forma separada, lo que no implica una compresión completa. Permite extraer cada archivo sin leer el resto, lo que aumenta la velocidad de descompresión. Es débil ante ataques de texto plano, ataque de diccionario y fuerza bruta.

### Tar
El programa [**tar**](https://es.wikipedia.org/wiki/Tar) es usado para almacenar archivos y directorios en un solo archivo, no para comprimilos. Para comprimirlos lo usamos junto a [**gzip**](https://es.wikipedia.org/wiki/Gzip), que es un compresor pero no archivador. El resultado de esta mezcla es lo que se conoce como un **tarball**.

### Bzip2
Este formato es más lento pero la compresión es mayor respecto al algoritmo que usan los anteriores.

>Fuentes:
- https://es.wikipedia.org/wiki/Formato_de_compresi%C3%B3n_ZIP
- https://es.wikipedia.org/wiki/Tar
- https://es.wikipedia.org/wiki/Gzip
- https://es.wikipedia.org/wiki/Bzip2