## Línea de comandos Vagrant

- Obtener un archivo `Vagrantfile` para una máquina virtual: `vagrant init <nombre_de_la_imagen>`
- Levantar una máquina virtual: `vagrant up`
- Detener una máquina virtual: `vagrant halt`

### Iniciar una máquina virtual paso a paso
1. Creamos un archivo llamado `Vagrantfile` que se encargará de levantar la máquina virtual. Para crearlo buscamos la máquina virtual que deseamos instalar y ejecutamos `vagrant init <nombre_de_la_imagen>`
2. Levantamos la máquina virtual con `vagrant up`. Se instalará si no está instalada. Luego vamos a nuestro proveedor y ejecutamos la máquina.
3. Para loguearnos usamos el usuario y contraseña por defecto de Vagrant (a no ser que los hayas cambiado) que son: usuario -> `vagrant`, contraseña -> `vagrant`.