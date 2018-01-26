## Compilar Sass
Los archivos `.scss` de Sass no pueden ser leídos directamente por los navegadores, por lo que hay que procesarlos en tiempo de desarrollo.

_________________________

### Javascript
#### gulp
[Tutorial específico de Gulp](https://github.com/mondeja/fullstack/tree/master/backend/src/011-flujo_de_trabajo/tasks/gulp).

- [Ejemplo](https://github.com/mondeja/fullstack/tree/master/frontend/src/001-entorno_de_ejecucion/css/preprocessor/sass/compilar/gulp)

Para compilar con Gulp instalamos el plugin `gulp-sass` ejecutando `npm i --save-dev gulp-sass`. En el ejemplo puedes ver como configurar el archivo `gulpfile.js` para realizar una compilación básica.

_________________________

### Python
#### libsass-python
> [Documentación](https://sass.github.io/libsass-python/) [Código fuente](https://github.com/sass/libsass-python)

- Instalar: `pip3 install libsass`



