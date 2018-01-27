## Escribir unicode desde el teclado en Linux

1. Configurar la tecla `Compose`. Para ello ejecutamos: `setxkbmap -option compose:rctrl` donde `rctrl` es la tecla <kbd>Ctrl</kbd> derecho. Puedes elegir la que quieras entre las siguientes (elige una que no utilices nunca):
    - `ralt`: Alt derecho
    - `lwin`: Windows izquierdo
    - `rwin`: Windows derecho
    - `menu`: Menu
    - `lctrl`: Control izquierdo
    - `rctrl`: Control derecho
    - `caps`: Caps Lock
    - `102`: Menor que/Mayor que
    - `paus`: Pause
    - `prsc`: PrtSc
    - `sclk`: Scroll Lock
2. Probar si funciona: escribe en la terminal `♥` pulsando <kbd>TECLA_ELEGIDA</kbd>+<kbd><</kbd>+<kbd>3</kbd>.
3. Ya que esta configuración sólo es válida para la sesión actual, debes configurarla para que se ejecute al iniciar el sistema con un script en `/etc/init.d/` con permisos de ejecución (por ejemplo `755`), aunque esto dependerá de dónde se guardan los scripts de inicio del sistema en tu distribución.
4. La lista completa de símbolos está en `/usr/share/X11/locale/en_US.UTF-8/Compose`, pero de forma más manejable en [esta lista](https://help.ubuntu.com/community/GtkComposeTable).


> Fuentes:
> - https://paraisolinux.com/escribir-caracteres-especiales-linux/