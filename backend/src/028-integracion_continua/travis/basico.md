## Integración contínua con [TravisCI](https://travis-ci.org/)
Travis es un servicio alojado de [integración continua](https://es.wikipedia.org/wiki/Integraci%C3%B3n_continua) que se integra con Github. Esto permite loguearnos con nuestra cuenta de Github e importar aquellos proyectos para los que queramos ejecutar tareas de IC.

### Uso básico
Lo primero que necesitamos para usar TravisCI es conectarlo con nuestra cuenta de Github accediendo a [este enlace](https://travis-ci.org/auth). Se sncronizarán los proyectos de tu cuenta de Github con tu cuenta de TravisCI.

Desde allí, activamos los proyectos donde queremos usar Travis. Ya sólo queda crear un archivo `travis.yml`, [configurarlo](https://docs.travis-ci.com/user/customizing-the-build) para [uno de los lenguajes soportados](https://docs.travis-ci.com/user/languages/) y ejecutar `git push`.

Si en este momento vamos a la página del proyecto en nuestra cuenta de Travis veremos el proceso de construcción en tiempo real. Podemos indicar en nuestro proyecto de Github el estado de la construcción de Travis añadiendo y personalizando el siguiente link:
```
[![Build Status](https://travis-ci.org/your-user/your-project.svg?branch=master)](https://travis-ci.org/your-user/your-project)
```

#### ¿Cómo ahorrar una multitud de pull requests?
Separando por ramas y [limitando la ejecución de travis a algunas de ellas](https://blog.travis-ci.com/2012-08-13-build-workflow-around-pull-requests).