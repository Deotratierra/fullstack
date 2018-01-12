## Máquinas virtuales con Qemu
Qemu nos permite tener varios sistemas operativos instalados en el mismo ordenador mediante máquinas virtuales.

- Instalación: `sudo apt-get install qemu`

Funciona con el uso de imágenes, debemos crear una imagen del sistema operativo el cual queramos emular y luego empezar la instalación desde algún medio donde iremos llenando u ocupando con datos esa imagen.

Para empezar es conveniente crear una carpeta donde guardar todas las imágenes, así en Linux no es mala idea colocarla en `~/quemu_vms`.

### Crear imágenes
- Ejecutamos: `qemu-img create <nombre_de_la_imagen>.img 2G`

El nombre de la imagen podemos inventárnoslo, simplemente es para identificar cada sistema y `2G` indica el tamaño de la imagen, en este caso 2 gigabytes.

### Máquinas soportadas por el ordenador
Para comprobar los tipos de arquitecturas soportadas por nuestra máquina podemos ejecutar: `qemu-system-arm -machine help`