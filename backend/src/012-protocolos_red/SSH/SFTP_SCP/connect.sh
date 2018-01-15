#!/bin/bash

# =======================================

     #####     SSH     #####

# Conexión a una máquina remota
# sudo apt-get install ssh
ssh <username>@<ip>

# Cambiando de puerto
ssh <username>@<ip> -p <port>

# Conexión directa pasando la contraseña

# Opción 1 (sshpass) -> sudo apt-get install sshpass
sshpass -p <password> ssh <username>@<ip>

# Opción 2 (generar llaves):
ssh-keygen -b 4096 -t rsa
ssh-copy-id <username>@<ip>

# =======================================

     #####     SFTP     #####

# Conexión a máquina remota
sftp <username>@<ip>

# Descargar un fichero
get <fichero>

# Descargar directorio
get -r <directorio>

# Subir un fichero
put <fichero>

# Más información: 
# https://www.digitalocean.com/community/tutorials/how-to-use-sftp-to-securely-transfer-files-with-a-remote-server

# ======================================

     #####     SCP     #####

# Subir un archivo 
scp </ruta/al/fichero-origen> <username>@<ip>:</ruta/al/fichero-destino/>

# Descargar un archivo
scp <username>@<ip>:</ruta/al/fichero-destino/> </ruta/al/fichero-origen>

# Más información: 
# https://www.garron.me/es/articulos/scp.html

# ======================================
