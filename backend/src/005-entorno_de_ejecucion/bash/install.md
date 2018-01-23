## Instalación/emulación de Bash por sistema operativo
En Linux y MacOSX, Bash está configurada como la consola por defecto del sistema. En sistemas Windows necesitas instalarla (Windows 10) o emularla.

> [Git para Windows](https://github.com/mondeja/fullstack/tree/master/backend/src/044-control_de_versiones/git/install/windows.md) proporciona una versión minimalista de Bash.

### Instalación en Windows 10
1. Ve al buscador -> `Actualizaciones` + <kbd>ENTER</kbd> -> Para programadores -> Activa el "Modo de programador". Pulsa sí y espera a que se instalen las actualizaciones necesarias (puedes reiniciar o apagar sin problemas).
2. Panel de Control -> Programas -> Activar o desactivar las características de Windows -> Activa el "Subsistema de Linux para Windows" -> <kbd>ENTER</kbd> y se reiniciará el sistema.
3. Ve al buscador -> `cmd` + <kbd>ENTER</kbd> -> Ejecuta `bash.exe` y se instalará Ubuntu en Windows. Sigue los pasos de instalación (tarda un rato). Al final nos pedirá un nombre de usuario y una contraseña para la cuenta de Unix. Este no hace falta que coincida con el usuario de tu cuenta.
4. Si todo sale bien serás logueado en Bash automáticamente. Para salir ejecuta `exit` y para entrar ejecuta `bash`.

> Se instala todo un entorno Ubuntu Xenial incluyendo muchos programas como `git`, `python`, `ruby`, `tesseract`... etc. Sin embargo tiene limitaciones, como el no poder correr aplicaciones gráficas como KDE o Gnome.


