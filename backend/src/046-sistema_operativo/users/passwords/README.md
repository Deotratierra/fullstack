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