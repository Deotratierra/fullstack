## Modelo base para desarrollo
Esto es lo que yo uso, eres libre de tomarlo.

#### Backend
Incluye Gulp con tareas para transpilar de ES6 a ES5, de Jade a HTML, de Sass a CSS y `gulp-nodemon`, además de un ejemplo de rutas modulares con el router de `express`. 

#### Fontend
Está preparado para trabajar con Angular-Material, incluye un ejemplo de Sidenav reutilizable.

### Preparación
Primero configurar el archivo `src/config.js` (con las variables de entorno) y luego instalar las devependencias: `npm i`. 

### Servir
Para correrlo: `npm start` o `gulp`.

Para comprobar que esta corriendo accede a `localhost:<PUERTO>/admin/home`

### Estructura
La estructura de directorios está basada en componentes, al estilo de ReactJS. Esto se consigue recorriendo recursivamente los directorios de escenas y componentes para servir desde ellos las rutas a los archivos estáticos, para poder linkearlos fácilmente desde el cliente (ver `src/app.js`). 

Las plantillas se comunican entre si mediante el sistema de herencias de Jade y las hojas de estilo mediante el sistema de importaciones de Sass. El truco está en mantener una relación coherente entre escenas y componentes locales y globales en toda la aplicación.

Esta estructura permite:
- Reutilizar los componentes en cualquier parte de la aplicación (el cambio de un componente global afecta a todos las páginas que lo necesitan).
- Desplegar grandes aplicaciones sin sufrimiento.
- Poder efectuar cambios rápidamente.
- Servir únicamente los archivos estáticos necesarios.
- Renderizar lo mínimo las plantillas en producción, mejorando la velocidad (a ser posible obtener información a través de una API).
- Fácil migración de backend (veáse el [ejemplo de servidor con Python/Tornado](../../python/tornado_server/complex_server_2)).

Por ejemplo, si quieres cambiar el menú lateral, vas a `src/components/MenuLateral` y allí está todo lo necesario. Como es un componente global se linkea desde `src/templates/index`.