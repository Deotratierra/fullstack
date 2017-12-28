## SASS
#### [Referencia](http://sass-lang.com/documentation/file.SASS_REFERENCE.html)

Los archivos `.scss` no pueden ser compilados por el navegador. Para transpilarlos podemos usar `gulp-sass`. En este mismo directorio hay un ejemplo de como usarlo.

### Variables
Podemos establecer variables con Sass, para ello, usamos la sintaxis 
```
$<nombre_de_variable>: <valor>;
```

De esta forma podríamos crear una paleta de colores:
```scss
$azul: #1565C0;
$azul_claro: #5e92f3;
$azul_oscuro: #003c8f;
```

Y luego asignarla a nuestros elementos:

```scss
h1.title {
    color: $azul_oscuro;
}
```

### Mixins
Podemos pensar en los mixins como si fueran una versión simplificada de un constructor de clase en un lenguaje de programación. Podemos escribir en ellos un grupo de declaraciones CSS para reusarlas donde queramos. Los mixins pueden aceptar argumentos, incluso con la opción de establecer valores por defecto.

La sintaxis para crear un mixin es:
``` 
@mixin <nombre>($<arg1>, $<arg2>, ...) {
    ...
}
```
Y para aplicarlo usamos: `@include <nombre> ($<arg1>, $<arg2>, ...)`

Ejemplo:
```scss
@mixin square($size, $color) {
  width: $size;
  height: $size;
  background-color: $color;
}

.small-blue-square {
  @include square(20px, rgb(0,0,255));
}

.big-red-square {
  @include square(300px, rgb(255,0,0));
}
```

### Extend
Con Sass, podemos extender las propiedades de un selector a otro, sin enfangarnos en complejos `a>li>div`... En su lugar, usamos la sintaxis `@extend` para incluir las propiedades de un selector en el que lo usamos, por ejemplo:

```scss
.dialog-button {
  box-sizing: border-box;
  color: #ffffff;
  box-shadow: 0 1px 1px 0 rgba(0, 0, 0, 0.12);
  padding: 12px 40px;
  cursor: pointer;
}

.confirm {
  @extend .dialog-button;
  background-color: #87bae1;
  float: left;
}

.cancel {
  @extend .dialog-button;
  background-color: #e4749e;
  float: right;
}
```

### Anidaciones
Con Sass, podemos anidar los selectores unos dentros de otros, asemejándonos más a la estructura del HTML.

``` scss
ul {
  list-style: none;

  li {
    padding: 15px;
    display: inline-block;

    a {
      text-decoration: none;
      font-size: 16px;
      color: #444;
    }

  }

```

### Operaciones
Con Sass podemos hacer operaciones matemáticas básicas directamente en la hoja de estilos:
```scss
$width: 800px;

.column-half {
  width: $width / 2;
}

.column-fifth {
  width: $width / 5;
}
```

### Funciones
Sass provee una [larga lista de funciones](http://sass-lang.com/documentation/Sass/Script/Functions.html) embebidas dentro del lenguaje. Podemos ver un ejemplo en el cual el color de un link se oscurece un 10% con la función `darken()`:
```scss
$awesome-blue: #2196F3;

a {
  padding: 10px 15px;
  background-color: $awesome-blue;
}

a:hover {
  background-color: darken($awesome-blue,10%);
}
```

### Referenciar al selector padre
Usando el caracter `&` podemos referenciar al selector en el cual estamos aplicando estilos. Este ejemplo en Sass:
```scss
a {
  font-weight: bold;
  &:hover { text-decoration: underline; }
}
```
Compila a este en CSS:
```css
a {
  font-weight: bold;
}
a:hover {
    text-decoration: underline; 
}
```

__________________________________________

### Flags

#### `!default`
Se usa después de una variable para definirla con el valor provisto a no ser que ya haya sido provisto con anterioridad. Se puede usar, por ejemplo, para definir paletas de colores que puedan ser [sobreescritas por el usuario](https://robots.thoughtbot.com/sass-default).

>Fuentes:
http://sass-lang.com/documentation/file.SASS_REFERENCE.html
https://tutorialzine.com/2016/01/learn-sass-in-15-minutes