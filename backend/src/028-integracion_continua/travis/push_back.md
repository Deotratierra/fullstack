## Push back

Imagínate que quieres subir tu código a TravisCI, realizar unos tests largos y, si salen bien, volver a hacer push en el proyecto de Github.

### Configuración
Para poder realizar push desde Travis necesitamos darle a Travis nuestro token de Github encriptado. El token se crea desde https://github.com/settings/tokens. Luego instalamos el cliente de Travis (necesitas ruby): `gem install travis`. Entonces ejecutamos `travis encrypt GH_TOKEN=<nuestro_token_de_github> --add` y veremos un nuevo apartado en el archivo de configuración de travis:

```yml
env:
  global:
    <un_monton_de_números_y_letras>
```

### Script
Con el siguiente script volveremos a hacer *push* en nuestro repositorio de Github.

```
# Obtenemos el último mensaje del último commit de la rama master
LAST_COMMIT_MESSAGE=$(git log --oneline -n 1 master | cut -d" " -f 2-)

# Configuramos el entorno de TravisCI para hacer commit
git config --global user.email "travis@travis-ci.org"
git config --global user.name "travis-ci"

# Añadimos los nuevos archivos
git add -A .
git commit -m "$LAST_COMMIT_MESSAGE [ci skip]"

# Subimos el proyecto a la rama principal
git push origin HEAD:master
