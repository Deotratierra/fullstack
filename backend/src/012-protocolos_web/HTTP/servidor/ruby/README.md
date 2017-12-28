## Desarrollo en Ruby on Rails

___________________________________________

### Rails CLI
- Crear aplicación: `rails new <nombre_de_aplicacion>`
- Lanzar servidor Puma en _`localhost:3000`_: `rails server` / `rails s`
- Generar código: `rails generate <generador> <*args>` / `rails g ...`
    + Por ejemplo, para generar un _controlador_ de nombre WelcomeController con una función _index()_:
    ```bash
    rails generate controller welcome index
    ```
    + Para acceder a la lista de generadores: `rails generate`
- Entrar en la consola de Rails: `rails console`

______________________________________________

### Controladores
Crear controlador: `rails generate controller <nombre> <método>`

Todos los controladores de Ruby on Rails heredan del controlador principal, denominado `application_controller`. Todos los archivos de controladores deben terminar con el nombre `_controller`

Para pasar variables a las vistas usamos la notación de atributos de clase (`@atributo`). Por ejemplo:
```ruby
class ArticlesController < ApplicationController

    def index
        @articles = Article.all  # Llamada a la DB mediante el modelo
    end
end
```

_____________________________________________

### Rutas
Para controlar las rutas, podemos hacerlo desde `config/routes.rb`.
- Para establecer la ruta principal: `root :to => "welcome#index"` (donde _welcome_ es un controlador de nombre WelcomeController e _index_ es su método).

La forma más sencilla de crear rutas en el archivo es `<verbo> "</ruta>"` (siendo verbo: get, post, put...). 
Para redireccionar podemos escribir: `<verbo> "</ruta>", to: "</otra_ruta>"`. 

Podemos establecer todos los verbos para una ruta escribiendo: `resources :<recurso>`. Por ejemplo, el comando `resources :articles` es lo mismo que:
```ruby
get "/articles"        # index
post "/articles"       # create
delete "/articles"     # delete
get "/articles/:id"    # show
get "articles/:new"    # new
patch "/articles/:id"  # update
put "/articles/:id"    # update
```
Cada uno de los recursos tiene la acción asociada a su comentario definido arriba. Al definir los controladores usaremos esas acciones para definir las funciones y en las vistas las crearemos dentro de la carpeta `app/views/articles` pasando los nombres así: `<accion>.html.erb`. 
Podemos [limitar estos recursos](https://richonrails.com/articles/understanding-rails-routing) para establecer sólo ciertos recursos con `only` o `except` y el nombre de la acción.
 
- Para ver todas las rutas definidas: `rake routes`

_______________________________________________

### Vistas
Los archivos que genera RoR para las vistas son HTMLs distintivos del framework, los cuales tienen la extensión `.html.erb`. En ellos podemos extender las vistas mediante un sistema de plantillas. Por ejemplo, el siguiente código imprime los números del 1 al 4 en diferentes párrafos:
```
<% [1, 2, 3, 4].each do |number| %>
    <p>Número: <%= number %></p>
<% end %>
```

- Para evaluar el código pero no imprimirlo: `<% %>`
- Para imprimir variables del código Ruby: `<%= %>`

#### Plantillas
Dentro de la carpeta `app/views/layouts` podemos ver otros archivos `.erb` como `application.html.erb`. Estos se encargan de sustituir el contenido de las vistas. Aquí irá el código común a distintas vistas en la aplicación.

#### Comandos RoR en las vistas
- Link (<a>): `<%= link_to Texto, </route/>, method :post %>`


__________________________________________

### Archivos estáticos
Los archivos estáticos se encuentran en la carpeta `app/assets`.

#### CSS
Dentro de la carpeta `app/assets/stylesheets` existe un documento llamado `application.css`. Allí se encuentra una línea que RoR agrega por defecto: ` *= require_tree .`. Gracias a esta, los archivos CSS que agregamos a la carpeta son importados en el head de cada vista. Si agregamos un archivo css a la carpeta y consultamos el código fuente de la vista en el navegador observaremos como los css son automáticamente enlazados. 

#### JS
Al igual que para las hojas de estilo, en `app/assets/javascripts` también se encuentra un archivo `application.js` que incluye los archivos javascript del directorio en las vistas.
RoR crea archivos coffescript con el mismo nombre que los controladores creados.

___________________________________________

### Modelos
Crear modelo: `rails generate model <nombre> *<campo:tipo>` 

Los modelos van en singular, RoR creará una tabla en plural para estos. 
Los campos se escriben separados de su tipo por `:`. Si el tipo no se indica, será `string` por defecto. [Aquí](https://stackoverflow.com/questions/17918117/rails-4-list-of-available-datatypes) puedes consultar la lista de títulos disponibles.

Ror creará un archivo con el nombre del modelo dentro de `app/models` con el siguiente código:
```
class Article < ApplicationRecord
end
```

___________________________________________

### Bases de datos
Dentro del archivo `app/config/database.yml` podemos editar la configuración de la base de datos para los diferentes entornos. Desde este archivo cammbiamos fácilmente de base sin editar el código de la aplicación.

Después de crear un modelo, dentro de la carpeta `db/migrate` podemos encontrar archivos de ruby con las migraciones de la base de datos pendientes. 

- Para aplicar migraciones: `rake db:migrate`
- Para volver atrás en la migración: `rake db:rollback` 

Si creamos una tabla con `rake db:migrate` (el cual aplica el método `create_table()` en la migración, al aplicar `rake db:rollback` se ejecutará su inverso, en este caso `drop_table()`. El comando rollback es como aplicar <kbd>Ctrl</kbd> + <kbd>Z</kbd> con las migraciones, vuelve atrás una vez por ejecución en las migraciones.

Dentro del archivo `db/schema.rb` se encuentran los esquemas de las tablas creadas. 

Para ver el contenido de un modelo en la base de datos lo hacemos desde la consola de Rails. Entramos en ella con `rails console`:
- Obtener todos los registros de un modelo: `<Modelo>.all`
- Buscar un registro por id (número): `<Modelo>.find(<id>)` 
- Crear un registro (ejemplo Article): 
```
Article.create( title: "Título", body: "Cuerpo del artículo" )
```