#!/bin/bash

# Para cambiar permisos en Linux se usa el comando chmod

# ===============================================================

# Eliminar permisos (símbolo - antes de los tipos de permisos)
chmod -w archivo.txt

# Otorgar permisos: (símbolo + antes de los tipos de permisos)
chmod +wr archivo.txt

# Establecer permisos (símbolo = antes de los tipos de permisos)
chmod =rwx archivo.txt  # Se establecen para todos los usuarios

# ===============================================================

# Chuleta de permisos por usuarios
: '
x-------------x-------------x
|  permisos   |  pertenece  |
x-------------x-------------x
|  rwx------  | usuario     |
|  ---r-x---  | grupo       |
|  ------r-x  | otros       |
x-------------x-------------x
'

# Estableciendo permisos por usuarios
chmod g-x,o-x archivo.txt  # Ni el grupo ni otros pueden ejecutar
chmod u-x+w archivo.txt    # El propietario no puede ejecutar pero si escribir

# ===============================================================

# Chuleta de permisos en octal:
: '
x-----x-----x-----------------------------------x
| rwx |  7  | Lectura, escritura y ejecución    |
| rw- |  6  | Lectura, escritura                |
| r-x |  5  | Lectura y ejecución               |
| r-- |  4  | Lectura                           |
| -wx |  3  | Escritura y ejecución             |
| -w- |  2  | Escritura                         |
| --x |  1  | Ejecución                         |
| --- |  0  | Sin permisos                      |
x-----x-----x-----------------------------------x

Por lo tanto:

x------------------------x-----------x
|chmod u=rwx,g=rwx,o=rx  | chmod 775 |
|chmod u=rwx,g=rx,o=     | chmod 760 |
|chmod u=rw,g=r,o=r      | chmod 644 |
|chmod u=rw,g=r,o=       | chmod 640 |
|chmod u=rw,go=          | chmod 600 |
|chmod u=rwx,go=         | chmod 700 |
x------------------------x-----------x
'

# ===============================================================

        # Comprobar los permisos de los archivos

# Permisos de un archivo
stat -c %A archivo.txt

: '
Para comprobar por los permisos de algún tipo para cierto tipo de usuario
tan sólo hay que cambiar el caracter a obtener en la función cut del
siguiente fragmento de código:
'
if [ `stat -c %A archivo.txt | cut -c4` == "x" ] 
then
  echo "El propietario tiene permisos de ejecución"
else
  echo "El propietario no tiene permisos de ejecución"
fi

# ===============================================================
