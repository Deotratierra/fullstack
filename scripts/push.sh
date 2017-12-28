#!/bin/bash

# ====================================================================
echo "Preparados para hacer push a la rama principal"

                    #     PUSH BACK     #


# Obtenemos el último mensaje del último commit de la rama staging
LAST_COMMIT_MESSAGE=$(git log --oneline -n 1 staging | cut -d" " -f 2-)
echo "LAST_COMMIT_MESSAGE: $LAST_COMMIT_MESSAGE"


# Configuramos el entorno de TravisCI para hacer commit
git config --global user.email "travis@travis-ci.org"
git config --global user.name "travis-ci"

# Cambiamos a la rama principal
git add -A .
git commit -m "$LAST_COMMIT_MESSAGE"

# Subimos el proyecto a la rama principal
git push origin master


# ====================================================================

exit 0
