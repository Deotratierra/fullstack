## Usuarios en Linux
- El archivo `/etc/login.defs` contiene la configuración del programa `/etc/login` así como toda la configuración de gestión de contraseñas y usuarios. El valor por defecto para las cuentas con respecto a la longitud de la contraseña, los días máximos antes de que la contraseña deba de ser cambiada, el mínimo de días entre los cambios de contraseñas, el algoritmo de cifrado de contraseñas a usar...

- El archivo `/etc/passwd` almacena la información de los usuarios del sistema.
- El archivo `/etc/group` almacena la información de los grupos del sistema.

___________________________________________

### Gestión de usuarios

#### Agregar usuarios
Usamos el comando **`useradd`** especificando `useradd [-opciones] <nombre_de_usuario>`. Opciones:

- `-u`: Indica un ID para el usuario (cada usuario en Linux tiene un identificador numérico único).
- `-g`: Indica la ID del grupo para el usuario a crear.
- `-G`: Indica varios grupos por ID para el usuario separados por `,`.
- `-d`: Especificar el directorio `/home/usuario` del usuario. Por ejemplo, `useradd -d /otro/directorio nombre_de_usuario`.
- `-M`: Crear usuario sin directorio `/home` (el directorio raíz será su punto de comienzo).
- `-e`: Crear usuario con fecha de caducidad. Por ejemplo `useradd -e 2018-12-31`.
- `-f`: Crear usuario con fecha de expiración de contraseña.
- `-c`: Agregar comentarios a la configuración del usuario dentro del archivo `/etc/passwd` (útil para guardar nombres completos o números de teléfono).
- `-s`: Esteblecer la shell por defecto del nuevo usuario.

#### Modificar usuarios
El comando **`usermod`** permite editar a un usuario. Opciones:

- `-c`: Agregar un comentario en el archivo `/etc/passwd` junto a la entrada del usuario.
- `-d`: Modificar el directorio `/home` del usuario.
- `-e`: Establecer la fecha de expiración del usuario.
- `-g`: Cambiar el grupo principal.
- `-G`: Agregar grupos suplementarios al existente. En la forma `usermod -G <grupo1,grupo2...> <usuario>`.
- `-l`: Cambiar el nombre de login.
- `-L`: Bloquear la cuenta de un usuario.
- `-m`: Mover el contenido del directorio home a otro directorio.
- `-p`: Usar una contraseña sin encriptación especificándola (no es seguro).
- `-u`: Asignar una ID al usuario (de 0 a 999).
- `-U`: Desbloquear un usuario.

#### Eliminar un usuario
Usamos el comando **`userdel`**. Opciones:

- `-r`: Se eliminará también el directorio `/home`, así como la información almacenada en `/etc/passwd` y `/etc/shadow`.