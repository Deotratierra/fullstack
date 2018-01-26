## Pug/Jade
#### [Referencia](http://jade-lang.com/reference/attributes)

En Jade no tenemos que cerrar las etiquetas HTML, lo que cuenta es la indentación del código (2/4 espacios):
```jade
div
  h1 Titulo del componente
  ul
    li Primer valor de lista
    li Segundo Valor de lista
  p.
    Cuando añadimos un . a la etiqueta Jade para de tratar
    cada línea como una etiqueta hasta que el bloque del párrafo termina.
  p Volvemos a un texto normal.
```

_____________________________________

### Compilación
Los archivos Jade tienen la extensión `.jade`, la cual no reconocen los navegadores. Para compilar los archivos `.jade` en `.html` hay que compilarlos.

En este directorio tienes un ejemplo con el plugin `gulp-jade` de Gulp. Para ejecutarlo primero instala las dependencias `npm i` y luego ejecuta `gulp`.

______________________________________

### Javascript
Jade está implementado en Javascript, así que podemos usarlo añadiendo `-` antes del código:
```jade
- var x = 3
div
  ul
    - for (var i=1; i<=x; i++) {
        li Hola
    - }
```

Esto compila así:
```html
<div>
  <ul>
    <li>Hola</li>
    <li>Hola</li>
    <li>Hola</li>
  </ul>
</div>
```

______________________________________

### Comentarios
Los comentarios en jade pueden escribirse mediante sintaxis `//` o la sintaxís `<!-- -->`. Ambas permiten comentarios multilínea. También pueden agregarse [comentarios condicionales](http://jade-lang.com/reference/comments).

Para evitar que los comentarios sean renderizados en el HTML, incluir un caracter `-` después de las barras inclinadas:
```jade
//- Este comentario no se renderizará
```

___________________________

### Atributos
Los atributos en jade son pasados como parámetros de una función:
```jade
a(class='button', href='google.com') Google
```

Compilado: `<a href="google.com" class="button">Google</a>`

Los atributos de estilo van en un hash:
```jade
a(style={color: 'red', background: 'green'})
```

Las clases e identificadores pueden definirse como en CSS:
- `a.button` --> `<a class="button"></a>`
- `.content` --> `<div class="content"></div>`  (div si omitimos la etiqueta)
- `a#main-link` --> `<a id="main-link"></a>`
- `#content` --> `<div id="content"></div>`

_____________________________________________

### Condicionales

#### Case
```jade
- var tareas = 0
case tareas
when 0
when 1
p Tienes pocas tareas
default
p Tienes #{tareas} tareas
```

Compilado: `<p>Tienes pocas tareas</p>`

```jade
- var tareas = 1
case tareas
when 0: p No tienes tareas
when 1: p Tienes una tarea
default: p Tienes #{tareas} tareas
```

Compilado: `<p>Tienes una tarea</p>`

#### If - else if
```jade
- var foo = 1
if foo == 1
  p #{foo}
else if foo == 0
  p No hay foo que valga
else
  p foo es mayor que 1
```

___________________________________________________

### Combinación de plantillas

La [herencia](http://jade-lang.com/reference/inheritance) se lleva a cabo mediante las instrucciones `block` y `extends`.

#### Extends
Para extender una plantilla padre con nuevos bloques usamos `extends`.
```jade
//- layout.jade
doctype html
html
  head
    block title
      title Título por defecto
  body
    block content
```

```jade
//- index.jade
extends ./layout.jade

block title
  title Título del artículo

block content
  h1 Contenido del artículo
```

#### Include
Para incluir el contenido de una plantilla extarna usamos `include`.
```jade
//- index.jade
doctype html
html
  include ./includes/head.jade
  body
    h1 Título del sitio
    p Bienvenido a mi sitio.
    include ./includes/foot.jade
```

>También podemos [incluir texto plano o usando filtros](http://jade-lang.com/reference/includes).

__________________________________________

### Loops
Jade posee una sintaxis sencilla para las iteraciones, mediante las sintaxis `each` y `while`.

#### Each
```jade
ul
each val in [1, 2, 3]
  li= val
```

Compilado:
```html
<ul>
<li>1</li>
<li>2</li>
<li>3</li>
</ul>
```

También podemos iterar enumerando los índices:
```jade
ul
each val, index in ['cero', 'uno', 'dos']
  li= index + ': ' + val
```

Compilado:
```html
<ul>
<li>0: zero</li>
<li>1: one</li>
<li>2: two</li>
</ul>
```

#### While
```jade
- var n = 0
ul
while n < 3
  li= n++
```

Compilado:
```html
<ul>
  <li>0</li>
  <li>1</li>
  <li>2</li>
</ul>
```

______________________________________________

### Funciones ([mixins](http://jade-lang.com/reference/mixins))
Podemos crear bloques reusables de código mediante funciones. Para llamar a las funciones usamos el carácter `+` antes de la llamada.

```jade
mixin article(title)
  .article
    .article-wrapper
      h1= title
      if block
        block
      else
        p Sin contenido

+article('Hola mundo')

+article('Hola mundo con bloque')
  p Este es el bloque del artículo
```

Compilado:
```html
<div class="article">
  <div class="article-wrapper">
    <h1>Hola mundo</h1>
    <p>Sin contenido</p>
  </div>
</div>

<div class="article">
  <div class="article-wrapper">
    <h1>Hola mundo con bloque</h1>
    <p>Este es el bloque del artñiculo</p>
  </div>
</div>
```

Para definir funciones con un número indeterminado de argumentos:
```jade
mixin list(id, ...items)
  ul(id=id)
    each item in items
      li= item

+list('my-list', 1, 2, 3)
```

```html
<ul id="my-list">
  <li>1</li>
  <li>2</li>
  <li>3</li>
</ul>
```

>También podemos [pasar atríbutos implícitos](http://jade-lang.com/reference/mixins) para usarlos dentro de las etiquetas de los mixins.


_____________________________


## Colección de plantillas útiles
- [HTML5](https://github.com/mondeja/fullstack/tree/master/frontend/src/001-entorno_de_ejecucion/html/preprocessor/pug/coleccion/html5.jade)
- [Angular-Material](https://github.com/mondeja/fullstack/tree/master/frontend/src/001-entorno_de_ejecucion/html/preprocessor/pug/coleccion/angular-material.jade)