## Instalar máquina virtual Mac Sierra 10.12 en VirtualBox
1. [Descarga este disco duro virtual `.vmdk`](https://drive.google.com/drive/folders/0B2BGAPbTu7vhM1M1THdhX01Jejg)
2. Crea una máquina virtual en VirtualBox de tipo `Mac OS X (64 bit)`. Como disco duro inserta el archivo descargado. Quédate con el título que le pones porque lo necesitas en el paso 4.
3. Configura la imagen a tu gusto.
4. Abre una terminal y ejecuta línea a línea el siguiente código, reemplazando "MACOSX" por el nombre que le pusiste a la máquina en el paso 2:
```
vboxmanage modifyvm "MACOSX" --cpuidset 00000001 000106e5 00100800 0098e3fd bfebfbff
vboxmanage setextradata "MACOSX" "VBoxInternal/Devices/efi/0/Config/DmiSystemProduct" "iMac11,3"
vboxmanage setextradata "MACOSX" "VBoxInternal/Devices/efi/0/Config/DmiSystemVersion" "1.0"
vboxmanage setextradata "MACOSX" "VBoxInternal/Devices/efi/0/Config/DmiBoardProduct" "Iloveapple"
vboxmanage setextradata "MACOSX" "VBoxInternal/Devices/smc/0/Config/DeviceKey" "ourhardworkbythesewordsguardedpleasedontsteal(c)AppleComputerInc"
vboxmanage setextradata "MACOSX" "VBoxInternal/Devices/smc/0/Config/GetKeyFromRealSMC" 1
```

5. Ejecuta tu máquina virtual y sigue los pasos de instalación, debería funcionar sin problemas.

> Necesitas VirtualBox 5 o superior para que el código del paso 4 funcione.