## PLugins para mejorar el funcionamiento de VirtualBox
Integración del puntero, compartir clipboard, habilitar las carpetas compartidas... etc

Despues de instalarlo (ver abajo) dentro de cada máquina virtual debemos ir a Dispositivos -> Insertar imagen de CD de las <<Guest Aditions>>. Esto insertará un CD virtual en la máquina. Luego hay que instalar lo que viene en el CD y listo.

### Instalar en Linux
```
sudo apt-get install linux-headers-$(uname -r) virtualbox-guest-dkms virtualbox-guest-x11
```