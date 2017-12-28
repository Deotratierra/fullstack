## Comandos útiles para Git (Ubuntu/Debian)

### Archivos
-Listar los archivos de un repositorio: `git ls-files`
- Contar número de líneas por archivo en repositorio: `git ls-files | xargs wc -l`
- Sólo los archivos C++: `git ls-files | grep cpp | xargs wc -l`

### Branchs

- Ver el listado de ramas y en la que estamos:`git branch`
- Crear una rama: `git branch <nombre_de_rama>`
- Cambiar de rama: `git checkout <nombre_de_rama>`
- Borrar una rama: `git branch -D <nombre_de_rama>`
- Renombrar una rama: `git branch -m <antiguo_nombre> <nuevo_nombre>`
- Unir dos ramas: `git merge <nombre_de_rama_a_absorber>`

### Remoto
- Añadir repositorio remoto: `git remote add origin <url>`
- Bajar los cambios del repositorio remoto: `git pull origin <nombre_de_rama>`
- Ver si estamos conectados a un repositorio remoto: `git remote -v`
