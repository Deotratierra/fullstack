## [Laravel](https://laravel.com/)

Es el framework de desarrollo para PHP que hasta la fecha tiene mejor calidad.

### Comenzar un proyecto con Laravel
Ejecutamos el siguiente comando `composer create-project --prefer-dist laravel/laravel my_app` donde `my_app` es el nombre del directorio donde se guardará nuestra aplicación.

Para ver que todo está en marcha entramos al directorio que se ha creado y ejecutamos `php artisan serve --port=8001`. El parámetro del puerto es opcional (por defecto corre en el puerto 8000). Ahora accedemos a `http://localhost:8001` y deberíamos ver la pantalla inicial de Laravel.
