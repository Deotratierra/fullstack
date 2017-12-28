#!bin/bash

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


# Cambiamos a la rama staging
#git stash save .
#git checkout staging
# Fusionamos en ella los cambios realizados en la rama principal
git add .
git commit -m "$1"
git push origin master

