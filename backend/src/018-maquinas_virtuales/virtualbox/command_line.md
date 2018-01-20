## VBoxManage

### Básico
- Listar todas las máquinas virtuales: `vboxmanage list vms`
- Encender una máquina: `vboxmanage startvm <nombre_de_la_máquina>`
- Apagar una máquina: `vboxmanage controlvm <nombre_de_la_máquina> poweroff`
- Obtener información de una máquina: `vboxmanage showvminfo <nombre_de_la_máquina>`

### Configurar máquinas
- Redimensionar RAM: `vboxmanage modifyvm <nombre_de_la_máquina> --memory <mb>`
