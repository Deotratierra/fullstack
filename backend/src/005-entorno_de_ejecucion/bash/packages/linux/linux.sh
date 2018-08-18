#!/bin/bash

:'
Dentro de Linux hay dos sistemas principales de paquetes: DEB y RPM.
Los DEB son empleados por distribuciones Debian y derivaciones como Ubuntu
y los RPM son usado por SuSE, Fedora y otras.

Se pueden gestionar paquetes mediante aplicaciones gráficas o mediante
comandos de consola. En las siguientes líneas se definen ambos métodos:
'

# ===========================   DEB   ===================================

# Instalar paquetes
#    - Sin descargar:
#        - Ubuntu ---> Centro de software de Ubuntu
#        - Debian ---> Synaptic
apt-get install <nombre_del_paquete>
aptitude install
#    - Descargados:
dpkg -i <nombre_del_paquete.deb>

# Eliminar paquetes
dpkg -r <nombre_del_paquete>

# Comprobar si un paquete está instalado
dpkg -s <nombre_del_paquete>

# Listar los paquetes instalados
dpkg --get-selections
dpkg -l # <--- Con más información

# Desinstalar paquetes rotos
dpkg --force-all -P <nombre_del_paquete>

# Solucionar dependencias rotas
dpkg --remove --force-remove-reinstreq <nombre_del_paquete>


# =======================================================================



# ===========================   RPM   ===================================

# Instalar paquetes
#    - Sin descargar
#        - SuSE, RedHat... ---> Click en "Sistema" -> "YaST" -> "Instalar/desinstalar software"
zypper install <nombre_del_paquete> # <-- Opción desde consola
#        - Fedora, CentOS:
yum install <nombre_del_paquete> -y
#    - Descargados
rpm -i <nombre_del_paquete.rpm>

# Actualizar paquetes
rpm -U <nombre_del_paquete.rpm>

# Eliminar paquetes
rpm -e <nombre_del_paquete>

# Comprobar si un paquete existe
rpm -q <nombre_del_paquete>

# Listar los paquetes instalados
yum list installed

# =======================================================================

:'
Existen otras formas de instalar paquetes en otras distribuciones (ver la fuente):

Fuente:
https://www.linuxadictos.com/tutorial-como-instalar-cualquier-paquete-en-gnulinux.html
https://www.linuxtotal.com.mx/index.php?cont=info_admon_020
http://www.ubuntu-es.org/node/140572#.WkpZ0K1KN_Q
'

