#!bin/bash

: '
Este script debe colocarse dentro de un directorio "scripts", en el primer nivel
de subdirectorios de un proyecto.

Este script realiza las siguientes tareas:
  1. Testea un archivo .travis.yml para comprobar que no tiene fallos de sintaxis.
  2. Realiza un pull al repositorio origen.
  3. Realiza un push al repositorio origen.

Uso:
  Argumentos obligatorios:
    - Mensaje de commit
  Argumentos opcionales:
    - Usuario de github
    - Constraseña de github
  Notas:
    Si pasamos el usuario debemos pasar la contraseña.
'


# Si ejecutamos build.sh desde el directorio scripts
CURRENT_DIR=${PWD##*/}
if [ $CURRENT_DIR = "scripts" ];
then
  cd ..  # salimos a la raíz del proyecto
  CURRENT_DIR=${PWD##*/}
else  # Pero si lo ejecutamos desde otro lugar
  if ! [ -d "scripts" ]; # comprobamos si no existe el directorio
  then  # lo cual indica que no estamos en la raíz
    echo "Por favor, ejecuta el script desde la raíz del proyecto"
    exit 1
  fi
fi

# Si no hemos pasado un primer argumento (mensaje del commit)
if [ -z "$1" ];
then
  echo "Debes incluir un mensaje de commit como argumento del script."
  exit 1
fi

# Ejecutamos el lint del archivo de configuración travis
# Gracias al parámetro -x devuelve el código de error 1
# si existe alguna advertencia:
# https://github.com/travis-ci/travis.rb/blob/master/lib/travis/cli/lint.rb#L8
travis lint ".travis.yml" -x -q
if [ $? -gt 0 ];
then
  travis lint ".travis.yml"
  exit 1
fi

# Comprobamos si hemos pasado el nombre de usuario y la contraseña
# de github como segundo y tercer parámetros respectivamente
if [ -z $2 ] || [ -z $3 ];
then
  ORIGIN=origin
else  # Si es así configuramos el push con ambos parámetros
  ORIGIN="https://$2:$3@fullstack.git"
fi


# Actualizamos nuestro repositorio local con el origen
git pull origin master

# Subimos los cambios al repositorio remoto de la rama principal
git add .
git commit -m "$1"
git push $ORIGIN master
