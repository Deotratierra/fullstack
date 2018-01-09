## Sistema de permisos en Linux

En Linux, el acceso de los usuarios y grupos de usuarios a ciertos recursos del sistema se determina mediante una consulta de admisión que puede ser afirmativa o negativa. Los usuarios, directorios, archivos y hasta los dispositivos son manejados como un archivo al que se le asignan derechos de acceder a ciertos contenidos., con el fin de permitir o no a un usuario leer, modificar y/o ejecutar archivos según sea el caso.

Un usuario normal en Linux (no root o superusuario), no tiene todos los tipos de accesos habilitados a una gran cantidad de directorios con el objetivo de administrar de manera eficiente y a la vez proteger la integridad del sistema. Por ejemplo, un usuario normal tiene derechos de lectura de la ruta `/etc/hosts`, pero no de escritura sobre el archivo.

### Tipos de permiso
- Lectura: `r` (también incluye la posibilidad de listarlo con `ls`)
- Escritura: `w`
- Ejecución: `x`

Es una tríada binaria porque cada permiso puede tener dos estados 1 ó 0. Si algún permiso está desactivado veremos un guión (`-`) al ejecutar `ls -l`.

![permisos_notacion_simbólica](https://s20.postimg.org/a9jnvg5zh/permisos-notacion-simbolica.jpg)