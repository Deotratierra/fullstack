## Personalizar el entorno Bash
En la mayoría de distribuciones de Linux, podemos editar la apariencia de la terminal que viene instalada en el sistema por defecto. Simplemente abrir el menú preferencias y editar.

### Editar el prompt
El prompt es lo que aparece cuando inicializamos una consola Bash. En Debian y derivados tiene la forma de `usuario@nombre_del_host:` por defecto, pero esto puede ser personalizado.

Para ello abre el archivo `~/.bashrc`:

Existe una línea que por defecto puede viene comentada: `force_color_prompt=yes`. Si la descomentamos y ejecutamos `source ~/.bashrc` podremos ver los colores. Pera editar estos colores vamos unas líneas abajo hasta un condicional:
```
if [ "$color_prompt" = yes ]; then
    PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '
else
    PS1='${debian_chroot:+($debian_chroot)}\u@\h:\w\$ '
fi
```

Estas líneas indican: si está activado e coloreado del prompt, coloreamos la salida según [las secuencias de escape ANSI](https://github.com/mondeja/fullstack/tree/master/backend/src/036-stdout/color/stdout_color.sh) que estamos indicando, si no, no coloreamos la salida. Por lo tanto, para editar el color sólo debemos cambiar estas secuencias.

Observa también que en lugar de colocar tu nombre aparecen los caracteres `u` para el usuario y `h` para el host, detrás de una barra `\`. Estos códigos podemos editarlos también, aquí tienes la lista completa:

- `d`: Muestra la fecha con formato “día de la semana mes y número de día”.
- `h`: Muestra el nombre del host.
- `H`: Muestra el nombre del host y el dominio.
- `n`: Salto de linea.
- `r`: Retorna al inicio de la linea.
- `s`: Muestra el nombre del interprete de comandos.
- `t`: Muestra la hora en formato de 24 horas.
- `T`: Muestra la hora en formato de 12 horas.
- `@`: Muestra la hora en formato de 12 horas con indicador am o pm.
- `u`: Nombre del usuario actual.
- `v`: Versión del interprete de comandos.
- `V`: Distribución del interprete de comandos.
- `w`: Nombre del directorio actual.
- `W`: Nombre del directorio actual recortado.
- `!`: Número en el historial del comando tecleado.
- `#`: Número de comando tecleado.
- `$`: Si eres superusuario muestra una `#` si no, muestra una `$`.

> En el ejemplo de arriba se usa el patrón `\033...` para determinar una secuencia de escape, pero también se puede usar `\e` en su lugar.

### Mostrar un mensaje al iniciar la consola
Cuando abre una consola se ejecuta el script que hemos estado editando: `~/.bashrc`. Por lo tanto, sólo tienes que insertar al final del archivo el mensaje que quieres mostrar.


> Fuentes:
> - https://blog.desdelinux.net/terminales-con-estilo-personaliza-tu-prompt/