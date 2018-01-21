## Introducción a Docker Machine
Docker Machine es una herramienta que nos ayuda a crear, configurar y manejar máquinas (virtuales o físicas). Con Docker Machine podemos iniciar, parar o reiniciar los nodos Docker, actualizar el cliente o el demonio Docker y configurar el cliente Docker para acceder a los distintos Docker Engine de máquinas (virtuales o físicas) locales o remotas.

Docker Machine utiliza distintos drivers que nos permiten crear y configurar Docker Engine en distintos entornos y proveedores, por ejemplo virtualbox, AWS, VMWare, OpenStack, …

Las tareas fundamentales que realiza Docker Machine, son las siguientes:

- Crea una máquina en el entorno que hayamos indicado (VirtualBox, OpenStack, ...) donde instala y configura Docker Engine.
- Genera los certificados TLS para la comunicación segura.

También podemos utilizar un driver genérico (generic) que nos permite manejar máquinas que ya están creadas (físicas o virtuales) y configurarlas por SSH.

______________________________________________

### Funcionamiento
El funcionamiento básico de Docker Machine es crear una máquina virtual y conectarnos a ella, para manejar Docker como si estuviéramos dentro de esa máquina.

Siguiendo los siguientes pasos podemos entenderlo mejor (necesitas instalar VirtualBox: `sudo apt-get install virtualbox`).

1. Creamos una máquina con el driver de VirtualBox: `docker-machine create -d virtualbox maquina1`.
2. Listamos las máquinas creadas gestionadas por Docker Machine y la veremos: `docker-machine ls`
3. Mostramos las máquinas de VirtualBox: `vboxmanage list vms`. Deberemos ver nuestra máquina con el nombre `maquina1` creada.
4. Mostramos la información de la máquina: `vboxmanage`. Los archivos necesarios para el funcionamiento de la máquinas creadas de esta forma se guardan (en Linux) en la ruta `/root/.docker/machine/machines/`.
5. Para usar una máquina debemos cargar sus variables de entorno. Si ejecutamos `docker-machine env maquina1` veremos las de `maquina1`. Para trabajar con ella ejecutamos: `eval $(docker-machine env maquina1)`.
6. Ahora si ejecutamos `docker-machine active` veremos el nombre de la máquina activa (`maquina1`).