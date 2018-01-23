## Comandos útiles para Git (Ubuntu/Debian)
- Iniciar un nuevo repositorio local: `git init`

### Commits
- Añadir cambios a un nuevo commit `git add <ruta(s)>`
- Crear un nuevo commit: `git commit -m <mensaje_del_commit>`
- Enmendar el commit (agregar otros archivos antes de subirlo o cambiar el mensaje): `git commit --amend`
- Eliminar el commit anterior (no subido) sin deshacer los cambios: `git reset HEAD~1 --soft`

______________________________

### Información
- Obtener estado del repositorio local: `git status`
- Comparar el estado con el commit anterior: `git diff`
- Obtener historial de commits: `git log`
- Obtener el último commit: `git log -1 <rama>`
- Obtener el mensaje del último commit: `git log --oneline -n 1 <rama> | cut -d" " -f 2-`
- Obtener el primer commit: `git log --reverse` (Para verlo en github -> github.com/<usuario>/<repo>/commit/<hash>)

______________________________

### Configuración
#### Repositorio
- Añadir repositorio remoto: `git remote add origin <url>`
- Cambiar de repositorio remoto: `git remote set-url origin <url>`
- Bajar los cambios del repositorio remoto: `git pull origin <nombre_de_rama>`
- Ver el repositorio remoto al que estamos conectados: `git remote -v`

#### Global
- Ver la configuración establecida: `git config --list`
- Establecer usuario global: `git config --global user.name "<usuario>"`
- Establecer email global: `git config --global user.email <email>`
- Establecer editor por defecto: `git config --global core.editor <editor>` (por ejemplo nano)
- Almacenar credenciales x cantidad de segundos: `git config --global credential.helper 'cache --timeout=<segundos>'`

#### Aliases
- Establecer alias para los comandos de git:
```
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit

# Ahora hariamos commit con:
git ci -m "Mensaje de commit"

git config --global alias.unstage 'reset HEAD --'
# El alias anterior hace a los siguientes comandos equivalentes:
git unstage <archivo>
git reset HEAD -- <archivo>
```


________________________________

### Ramas (branchs)

- Ver el listado de ramas y en la que estamos:`git branch`
- Crear una rama: `git branch <nombre_de_rama>`
- Cambiar de rama: `git checkout <nombre_de_rama>`
- Crear y cambiar a la nueva rama: `git checkout -b <nombre_de_rama>`
- Borrar una rama en local: `git branch -D <nombre_de_rama>`
- Borrar una rama en remoto: `git push origin :<nombre_de_rama>`
- Renombrar una rama: `git branch -m <antiguo_nombre> <nuevo_nombre>`
- Unir dos ramas: `git merge <nombre_de_rama_a_absorber>`


________________________________

### Archivos
#### Información
-Listar los archivos de un repositorio: `git ls-files`
- Contar número de líneas por archivo en repositorio: `git ls-files | xargs wc -l`
- Filtrando por tipo de archivos: `git ls-files | grep <extension> | xargs wc -l`

______________________________

### [Tags](https://github.com/mondeja/fullstack/tree/master/backend/src/044-control_de_versiones/git/tutoriales/tags.md)
- Mostrar todos los tags: `git tag`
- Mostrar tags por patrón: `git tag -l "v1.8.5*"`
- Crear un tag ligero: `git tag <nombre>`
- Crear un tag anotado: `git tag -a <nombre> -m "<mensaje>"`
- Mostrar un tag: `git show <nombre>`
- Compartir tags: `git push origin <nombre>`
