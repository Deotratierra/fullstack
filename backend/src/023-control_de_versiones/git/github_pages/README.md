## Páginas con Github

Con Github podemos crear páginas muy útiles, tanto para subir la documentación del proyecto y organizarla fácilmente mediante Markdown, como para crear un portfolio personalizado de proyectos.
Para crear una página simplemente vamos, dentro de nuestro repositorio a `Settings` -> `Github Pages`.

### Crear una página
Hay varias formas de crear una página. Podemos seleccionar la rama `master` del proyecto y subir nuestros cambios directamente ahí. También podemos seleccionar la carpeta `docs` dentro de la rama master. El problema es que no se actualizan directamente los cambios subidos.

La opción más pro sería crear una nueva rama con el nombre de `gh-pages` mediante el comando `git branch gh-pages`. Luego vamos a `Settings` -> `Github Pages` para seleccionar esta rama.

- Para igualar la rama `gh-pages` con `master`: `git branch -f gh-pages master`
- Luego subimos la rama `gh-pages` con: `git push origin gh-pages`

Ya debería estar actualizada nuestra página con el respositorio de la rama `master`.

