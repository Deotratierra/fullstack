
# Esto debe ser realizado después de crear la máquina virtual para Mac en VirtualBox.
# Reemplaza "Mac" por el nombre que le pusiste a la máquina al crearla y ejecuta
# el siguiente código línea por línea en una terminal (ve copiando y pegando cada línea).

VBoxManage modifyvm "Mac" --cpuidset 00000001 000106e5 00100800 0098e3fd bfebfbff
VBoxManage setextradata "Mac" "VBoxInternal/Devices/efi/0/Config/DmiSystemProduct" "iMac11,3"
VBoxManage setextradata "Mac" "VBoxInternal/Devices/efi/0/Config/DmiSystemVersion" "1.0"
VBoxManage setextradata "Mac" "VBoxInternal/Devices/efi/0/Config/DmiBoardProduct" "Iloveapple"
VBoxManage setextradata "Mac" "VBoxInternal/Devices/smc/0/Config/DeviceKey" "ourhardworkbythesewordsguardedpleasedontsteal(c)AppleComputerInc"
VBoxManage setextradata "Mac" "VBoxInternal/Devices/smc/0/Config/GetKeyFromRealSMC" 1