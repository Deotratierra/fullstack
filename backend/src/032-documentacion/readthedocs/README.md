## [Readthedocs](http://readthedocs.io/)
Es un servicio de hosting gratuito para la documentación de los proyectos. Tiene un buen soporte para `sphinx`, lo cual nos permite construirla fácilmente.

### Cómo publicar
Para publicar proyectos debemos hacernos una cuenta. Podemos importar directamente los proyectos de Github desde el panel de nuestra cuenta.

La forma más fácil de configurar la construcción de la documentación es [mediante un archivo `.readthedocs.yml`](http://docs.readthedocs.io/en/latest/yaml-config.html). Simplemente seleccionamos en que versión de Python queremos, si debemos instalar el paquete mediante `pip` o `setup.py install`, elegimos de donde obtenemos las dependencias... etc.

Dentro de nuestra cuenta podemos editar varias opciones a la hora de construir la documentación. El proyecto se construirá automáticamente de nuevo en cada `push` por defecto.