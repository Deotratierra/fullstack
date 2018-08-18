## Opciones avanzadas al correr contenedores

### Vinculación bidireccional de directorios host-contenedor
Al lanzar el contenedor pasamos la opción `-v` y tras ella indicamos `<ruta/al/directorio/en/el/host>:<ruta/al/directorio/en/el/contenedor>`. Esto hará que podamos acceder a los directorios montados en el host desde el contenedor. La vinculación es bidireccional, por lo que si editamos los datos en el contenedor también se editarán en el host.

#### Comprobación
1. Creamos un directorio en local: `mkdir prueba`
2. Creamos un archivo dentro del directorio y le añadimos datos: `echo "Información establecida en el host" >> prueba/archivo.txt`
3. Creamos un directorio dentro del directorio: `mkdir prueba/directorio`
4. Otro archivo: `echo "Más información establecida desde el host" >> prueba/directorio/archivo.txt`
5. Lanzamos el contenedor montando el directorio y nos logueamos: `docker run -it -v $(pwd)/prueba:/prueba ubuntu:14.04 bash`
6. Comprobamos si podemos acceder a los datos del directorio: `cat /prueba/archivo.txt && cat /prueba/directorio/archivo.txt`
7. Editamos el archivo: `echo "Información establecida desde el contenedor" >> /prueba/archivo.txt`
8. Salimos: `exit`
9. Comprobamos si la edición desde el contenedor se realizó correctamente: `cat prueba/archivo.txt`. Si vemos la línea `Información establecida desde el contenedor` quiere decir que todo ha funcionado correctamente.
10. Limpiamos: `rm -rf prueba`
