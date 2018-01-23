## Sistema de permisos en Linux

En Linux, el acceso de los usuarios y grupos de usuarios a ciertos recursos del sistema se determina mediante una consulta de admisión que puede ser afirmativa o negativa. Los usuarios, directorios, archivos y hasta los dispositivos son manejados como un archivo al que se le asignan derechos de acceder a ciertos contenidos., con el fin de permitir o no a un usuario leer, modificar y/o ejecutar archivos según sea el caso.

Un usuario normal en Linux (no root o superusuario), no tiene todos los tipos de accesos habilitados a una gran cantidad de directorios con el objetivo de administrar de manera eficiente y a la vez proteger la integridad del sistema. Por ejemplo, un usuario normal tiene derechos de lectura de la ruta `/etc/hosts`, pero no de escritura sobre el archivo.

### Tipos de permiso
- Lectura: `r` (también incluye la posibilidad de listarlo con `ls`)
- Escritura: `w`
- Ejecución: `x`

Es una tríada binaria porque cada permiso puede tener dos estados 1 ó 0. Si algún permiso está desactivado veremos un guión (`-`) al ejecutar `ls -l`.

### Categorías de los permisos
- Usuario o propitario: `u`
- Grupo: `g`
- Otros `o`
![permisos_notacion_simbólica](https://s20.postimg.org/a9jnvg5zh/permisos-notacion-simbolica.jpg)

Cada categoría de permisos se representa con un máximo de 3 caracteres, cada uno de los caracteres representa los permisos de lectura, escritura y ejecución.

Los sistemas de persmisos pueden ser representados fácilmente mediante [notación octal](https://github.com/mondeja/fullstack/tree/master/backend/src/bajo_nivel/notaciones/octal), siendo que los permisos de lectura valen 4, escritura 2 y ejecución 1.

#### Ejemplos
- `rwxr-xr-x`: Todos los permisos para su propietario, permisos de lectura y ejecución para el grupo y el resto de usuarios. En octal es 755 (4+2+1 | 4+1 | 4+1).
- `r-x——`: Lectura y ejecución sólo para su propietario. En octal es 500.
- `rw-rw-r—`: Lectura y escritura para el propietario y el grupo pero sólo lectura para el resto. En octal es 644.

