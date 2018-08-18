## Instalación de servicios VMWare

1. Primero hemos de [registrarnos en la página de VMWare](https://my.vmware.com/en/group/vmware/evalcenter?p=free-esxi6).

### VMWare Workstation 14 Pro (30 días de prueba)

> Con VMware Workstation puedes comenzar a crear tus maquinas virtuales, y VMware Player te permite ejecutarlas. Después de los 30 días de prueba no podrás crear nuevas máquinas virtuales pero si podrás ejecutar las ya creadas.

1. Descargamos la versión de nuestra plataforma desde la [página de descarga](https://www.vmware.com/products/workstation-pro/workstation-pro-evaluation.html)
2.  En caso de Windows ejecutamos el `.exe`. En caso de Linux debemos otorgar permisos al archivo con `chmod +x` y ejecutar el binario.
3. Al instalar seleccionamos la versión de prueba gratuita de 30 días.

- Desinstalar (Linux): `sudo vmware-installer -u vmware-workstation`

### VMPlayer

1. Accedemos a la [página de descargas de VMWare Workstation](https://my.vmware.com/en/web/vmware/free#desktop_end_user_computing/vmware_workstation_player/12_0|PLAYER-1210|product_downloads) y elegimos la instalación acorde a nuestra máquina y sistema operativo.
2. Si estamos en Windows simplemente ejecutamos el `.exe` descargado, si estamos en Linux le otorgamos permisos con `chmod 500` y ejecutamos el `.bundle`.
3. En Windows debería aparecer un icono en el escritorio si has marcado esa opción. Para comprobar que está instalado en Linux ejecuta `vmplayer --version`

- Desinstalar (Linux): `sudo vmware-installer -u vmware-player`
