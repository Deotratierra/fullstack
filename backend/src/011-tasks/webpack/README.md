# [Webpack](https://webpack.github.io/)

Webpack es un bundler de archivos que sirve para que puedan ser encapsulados en paquetes preparados para servirlos a través de internet, en páginas web. Internamente, construye un grafo de dependencias que mapea cada módulo que un proyecto necesita y genera uno o más paquetes.

Gracias a Webpack, podemos escribir código ES6 de lado de servidor usando bibliotecas e importaciones al igual que si estuviéramos en backend, y luego podemos construir un paquete con esas dependencias para servirlo en la web.

- Instalación: ``npm install -g webpack webpack-cli``

## Conceptos básicos

Webpack puede parecer complicado al principio, y su documentación es bastante extraña, pero entendiendo los conceptos básicos con ejemplos podemos empezar a usarlo rápidamente y darnos cuenta de lo útil que es.


### [Puntos de entrada](https://webpack.js.org/configuration/entry-context/#entry)

La configuración en webpack se realiza a través de un archivo ``webpack.config.js``. En este se definen *puntos de entrada* (entry points) a través de la propiedad ``entry``. Por ejemplo:

```javascript
entry: {
    external: path.resolve(__dirname, "web", "static", "src", "external.js"),
    internal: path.resolve(__dirname, "web", "static", "src", "internal.js"),
},
```

Este código indica a webpack que debe buscar dos archivos situados en el directorio ``web/static/src/`` con los nombres ``internal.js`` y ``external.js``. Dentro de estos archivos, podemos importar no sólo otros módulos ``.js`` que serán añadidos al paquete, si no que también podemos importar archivos ``.css`` que serán inyectados en nuestra aplicación al cargar. Lo más chocante de entender de Webpack al principio es que todo los tipos de archivos se tratan como módulos. Podemos importar cualquier cosa, incluso ``.json`` o imágenes, además de archivos de frameworks CSS como Sass.

### [Salidas](https://webpack.js.org/configuration/output/)

El archivo resultante para cada módulo se especifica en la propiedad ``output``. Siguiendo el ejemplo anterior, podríamos la siguiente configuración de salida:

```javascript
output: {
   filename: "[name].bundle.js",
   path: path.resolve(__dirname, "web", "static", "dist", "js")
},
```

El nombre de los archivos de salida se construirá reemplazando ``[name]`` por el nombre de cada entrada. Por lo tanto, siguiendo esta configuración tendríamos dos archivos de salida llamados ``internal.bundle.js`` y ``external.bundle.js`` dentro del directorio ``web/static/dist/js``.

### [Contexto](https://webpack.js.org/configuration/entry-context/#context)

Por defecto, webpack trata el contexto (el lugar desde donde cargará las dependencias necesarias) como el directorio desde donde se lanza el comando de compilación (más adelante se explica como lanzarlo), pero este comportamiento puede personalizarse con la propiedad ``context``:

```javascript
module.exports = {
  //...
  context: path.resolve(__dirname, 'app')
};
```

### [Módulos](https://webpack.js.org/configuration/module/)

Dentro de la propiedad ``module``, especificamos cómo webpack procesará los archivos, utilizando reglas que podemos diferenciar por tipo de archivo. En ``module.rules``, especificamos las reglas a seguir: ``test`` indica la expresión regular que debe cumplir el archivo para que sea usado un ``loader`` u otro, los cuales definimos en la propiedad ``use``. 

Un ejemplo de configuración que nos permitiría cargar los tipos de archivo ``.css``, ``scss`` e imágenes de tipos ``png|woff|woff2|eot|ttf|svg`` sería el siguiente:

```javascript
module: {
    rules: [
      {
        test: /\.css$/,
        use: [ 'style-loader', 'css-loader' ]
      },
      {
        test: /\.(scss)$/,
        use: [{
          loader: 'style-loader', // inject CSS to page
        }, {
          loader: 'css-loader', // translates CSS into CommonJS modules
        }, {
          loader: 'postcss-loader', // Run post css actions
          options: {
            plugins: function () { // post css plugins, can be exported to postcss.config.js
              return [
                require('precss'),
                require('autoprefixer')
              ];
            }
          }
        }, {
          loader: 'sass-loader' // compiles Sass to CSS
        }]
      },
      {
        test: /\.js$/,
        use: ["source-map-loader"],
        enforce: "pre"
      },
      {
        test: /\.(png|woff|woff2|eot|ttf|svg)$/,
        use: "url-loader?limit=100000"
      }
    ]
  },
```

Como podrás intuir, los ``loaders`` son cargadores/procesadores de archivos. Los cargadores deben ser instalados aparte mediante NPM. Para usar la configuración anterior, tendríamos que instalar los cargadores usados con:

```
npm install --save-dev css-loader node-sass sass-loader postcss-loader precss source-map-loader style-loader url-loader
```

¿Y no hay un loader para escribir Javascript ES6? Webpack ya lo integra, lo único que debes hacer es instalar las bibliotecas ``babel-cli``, ``babel-core`` y ``babel-preset-es2015``. No necesitas especificar en la configuración un cargador Babel, Webpack es listo y si descubre código ES6 en tus dependencias, usará ``babel`` para compilarlo.

### [Modos de compilación](https://webpack.js.org/concepts/mode/)

Siguiendo la propiedad ``mode``, podemos decir a Webpack que optimizaciones integradas usar. Por ejemplo, si estamos en desarrollo no conviene hacer una minificación del código, pero en producción si. Podemos indicarle el modo de compilación de dos formas: o pasándolo como parámetro opcional al lanzar webpack con ``webpack --mode=production`` o estableciéndolo en la propiedad ``mode``:

```javascript
module.exports = {
  mode: 'production'
};
```

Si estamos en producción Webpack minifica todos tus módulos por defecto. Dependiendo del modo en que se ejecute, se cargarán unos [plugins](https://webpack.js.org/concepts/plugins/) u otros, [aquí](https://webpack.js.org/concepts/mode) puedes comprobar cuales se cargan en cada modo.

### Ejecución

Para ejecutar el proceso de empaquetado simplemente ejecuta ``webpack``, es muy simple. Una de las más útiles en el proceso de desarrollo es ``--watch`` la cual comprueba entre tus dependencias si han sido editadas y las compila de nuevo automáticamente. [Aquí](https://webpack.js.org/api/cli/) se explican todas las opciones que podemos pasar el ejecutar desde línea de comandos.

### Plugins

Webpack permite la integración de plugins de terceros para añadir funcionalidades extras al proceso de compilación. Estos se pasan en la propiedad ``plugins``. Por ejemplo, si queremos añadir una barra de progreso al proceso de compilación, podemos añadir el plugin ``ProgressPlugin``, que viene integrado en Webpack:

```javascript
const webpack = require('webpack');

module.exports = {
  //...,
  plugins: [
    new webpack.ProgressPlugin()
  ]
}
```

