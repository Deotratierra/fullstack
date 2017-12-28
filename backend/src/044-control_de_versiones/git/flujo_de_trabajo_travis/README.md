## Flujo de trabajo completo de cualquier proyecto
El siguiente artículo cubre todos los aspectos de un sistema de trabajo integrado con TravisCI.

Desplegando aplicaciones en Github para cualquier tipo de proyecto he observado varias tareas comunes que sería muy útil automatizar, por lo que he creado un sistema de trabajo el cual se cubre en el siguiente artículo. Los capítulos están desarrollados en el orden de ejecución de los scripts que le acompañan.

Para mantener el orden del conjunto de scripts es útil llevar un orden de ejecución por etapas. La integración con TravisCI nos permite realizar tests de fin a fin sin sobrecargar nuestra máquina, automatizar la distribución de los paquetes, desplegar matadatos del proyecto... todo tras ejecutar los costosos tests de fin a fin, o en varios sistemas operativos con Docker, etc.

### Resumen
Así que el flujo de trabajo básico sería:
1. Ejecutamos un script de construcción: `scripts/build.sh`. Este realiza las siguientes tareas:
    - 1.1 Ejecutamos los tests unitarios.
    - 1.2 Si pasan sin fallos, hacemos `push` a la rama `staging` del proyecto.
2. En TravisCI, el proyecto estará configurado para que esta rama ejecute:
    - 2.1 Borrar archivos de cache.
    - 2.2 
_________________________________________________



