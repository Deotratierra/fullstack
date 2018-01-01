#!/bin/bash

:'
Dentro de Linux hay dos sistemas principales de paquetes: DEB y RPM.
Los DEB son empleados por distribuciones Debian y derivaciones como Ubuntu
y los RPM son usado por SuSE, Fedora y otras.
'

# ===========================   DEB   ===================================

# Instalar paquete sin descargar
#     - Ubuntu ---> Centro de software de Ubuntu
#     - Debian ---> Synaptic
apt-get install <nombre_del_paquete>
aptitude install  # <-- También

# Instalar paquete descargado
dpkg -i <nombre_del_paquete.deb>

# =======================================================================



# ===========================   RPM   ===================================

# Instalar paquete sin descargar
#    - SuSE, RedHat... ---> Click en "Sistema" -> "YaST" -> "Instalar/desinstalar software"
zypper install <nombre_del_paquete> # <-- Opción desde consola
#    - Fedora, CentOS:
yum install <nombre_del_paquete>

# Instalar paquete descargado
rpm -i <nombre_del_paquete.rpm>

# =======================================================================

:'
Existen otras formas de instalar paquetes en otras distribuciones (ver la fuente):

Fuente:
https://www.linuxadictos.com/tutorial-como-instalar-cualquier-paquete-en-gnulinux.html
'

