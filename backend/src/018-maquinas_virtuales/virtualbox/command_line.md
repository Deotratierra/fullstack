## VBoxManage
> Máquinas invitadas son las máquinas virtuales manejadas por VirtualBox, en contraposición con la máquina anfitriona.

### Básico
- Listar todas las máquinas virtuales: `vboxmanage list vms`
- Encender una máquina: `vboxmanage startvm <nombre_de_la_máquina>`
- Apagar una máquina: `vboxmanage controlvm <nombre_de_la_máquina> poweroff`
- Obtener información de una máquina: `vboxmanage showvminfo <nombre_de_la_máquina>`

### Configurar máquinas invitadas
- Redimensionar RAM: `vboxmanage modifyvm <nombre_de_la_máquina> --memory <mb>`

### Control de máquinas invitadas
- Ejecutar archivo: `vboxmanage guestcontrol <nombre_de_la_máquina> --username <usuario> --password <contraseña> -v run <ruta/al/archivo/en/la/máquina/invitada.ext>`
- Crear directorio: `vboxmanage guestcontrol <nombre_de_la_máquina> --username <usuario> --password <contraseña> -v mkdir <ruta/al/directorio/>`