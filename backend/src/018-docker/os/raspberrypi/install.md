## Docker en RaspberryPi

### Instalación
```bash
sudo apt install docker.io
sudo systemctl enable docker
sudo systemctl start docker
sudo usermod -aG docker pi
sudo reboot
```

>`pi` es el nombre de usuario de la máquina en el código anterior. Si todo ha salido bien deberías poder ejecutar `docker info` sin ser superusuario.

____________________

### Uso
Si ejecutas `uname -m` verás que el nombre de hardware de la RaspberryPi es `armv7l`, así que todas las imágenes basadas en otras arquitecturas no funcionarán.