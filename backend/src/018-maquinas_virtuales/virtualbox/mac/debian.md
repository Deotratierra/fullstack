## Instalar máquina virtual Mac en Debian
1. [Descarga este disco duro virtual `.vmdk`](https://drive.google.com/drive/folders/0B2BGAPbTu7vhM1M1THdhX01Jejg)
2. Crea una máquina virtual en VirtualBox de tipo `Mac OS X (64 bit)`. Como disco duro inserta el archivo descargado. Quédate con el título que le pones porque lo necesitas en el paso 4.
3. Configura la imagen a tu gusto.
4. Abre una terminal y ejecuta línea a línea el siguiente código, reemplazando "MACOS" por el nombre que le pusiste a la máquina en el paso 2:
```
VBoxManage modifyvm "MACOS" --cpuidset 00000001 000106e5 00100800 0098e3fd bfebfbff
VBoxManage setextradata "MACOS" "VBoxInternal/Devices/efi/0/Config/DmiSystemProduct" "iMac11,3"
VBoxManage setextradata "MACOS" "VBoxInternal/Devices/efi/0/Config/DmiSystemVersion" "1.0"
VBoxManage setextradata "MACOS" "VBoxInternal/Devices/efi/0/Config/DmiBoardProduct" "Iloveapple"
VBoxManage setextradata "MACOS" "VBoxInternal/Devices/smc/0/Config/DeviceKey" "ourhardworkbythesewordsguardedpleasedontsteal(c)AppleComputerInc"
VBoxManage setextradata "MACOS" "VBoxInternal/Devices/smc/0/Config/GetKeyFromRealSMC" 1
```

5. Ejecuta tu máquina virtual y sigue los pasos de instalación, debería funcionar sin problemas.