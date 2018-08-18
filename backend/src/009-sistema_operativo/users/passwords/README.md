## Contraseñas en Linux
Las contraseñas se almacenan encriptadas en el archivo `/etc/shadow`. Cada línea en el archivo contiene una sintaxis como: `user:H7e9JL:10063:0:30:7:1::`. Cada uno de los campos separados por `:` son explicados en la siguiente tabla:

![Contraseñas en Linux](https://s20.postimg.org/fhey4qb7h/passwords_linux.png)

El archivo `/etc/gshadow` guarda la información encriptada de la información sensible de los grupos como las contraseñas encriptadas.

_____________________________________________

### Gestión de contraseñas
> Para comprobar información relacionada a la contraseña de un usuario podemos ejecutar `chage -l <nombre_de_usuario>`.

#### Cambiar
Usamos el comando **`passwd`** para cambiar contraseñas de un usuario espcificando `passwd [-opciones] <nombre_de_usuario>`. Opciones:

- `-l`: Bloquea la cuenta.
- `-u`: Desbloquea la cuenta.
- `-n`: Fija el número mínimo de días necesarios antes de que una contraseña se pueda cambiar.
- `-x`: Fija el número de días hasta la expiración de la contraseña. Por ejemplo `passwd x30 <nombre_de_usuario>` (en 30 días).
- `-w`: Fija el día antes de la expiración de la contraseña una advertencia que será enviada al usuario.
- `-i`: Fija el número de díaś después de la expiración de la contraseña en el que se bloquea la cuenta.
- `-s`: Muestra información sobre las contraseñas.

#### Problemas comunes
##### `user is not in the sudoers file`

```bash
su -
visudo
```
Añadimos la siguiente línea al archivo, donde `username` debe ser reemplazado por el nombre de tu usuario:

```bash
username    ALL=(ALL)   ALL
```

_____________________________________________

### Seguridad
#### Cambiar la contraseña root sin tenerla
Si quieres hackear un ordenador Linux al cual tienes acceso físico o si tu usuario se ha quedado sin acceso de superusuario (`<usuario> is not in the sudoers file`) y además tu contraseña de administrador no te funciona (has trasteado mal o estás siendo hackeado) puedes volver a cambiar la contraseña de tu usuario raíz siguiendo los siguientes pasos (necesitas tener configurado el cargador de arranque GRUB):

1. Inicia el sistema, cuando aparezca el panel de GRUB, pulsa <kbd>E</kbd>.
2. Ve hacia la línea que comienza con `linux`, agrégale al final `init=/bin/bash` y pulsa <kbd>F10</kbd>.
3. Vuelve a montar el sistema de archivos con `mount -o remount rw /`.
4. Ejecuta `nano /etc/shadow` y en la línea que empieza por `root` déjala tal que: `root::<número>:0:<número>:7:::`. Reinicia con `reboot`.
5. Ahora el superusuario no tendrá contraseña. Ponle una con `passwd` tal y como se explica arriba.