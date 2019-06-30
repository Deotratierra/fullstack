

: '
    Para extraer el texto de un archivo PDF, la mejor forma usando programas
      open source es usar la utilidad de línea de comandos incluída en Linux
      `gs`. Este comando invoca Ghostscript, un intérprete de los lenguajes
      de Adobe Systems PostScript y PDF (Portable Document Format).

    Para más información ejecutar: `man gs`

'

# Con este comando, convertimos de las páginas 3 al 5 de un documento PDF
#   a texto y lo mostramos en la salida estándar
gs \
   -dBATCH \
   -dNOPAUSE \
   -sDEVICE=txtwrite \
   -dFirstPage=3 \
   -dLastPage=5 \
   -sOutputFile=- \
   /ruta/al/archivo.pdf

