## Instalar Python en MacOSX

### Instalador gráfico
La forma más fácil de instalar Python en MacOSX es ir a https://www.python.org/downloads/mac-osx/, elegir la versión, descargarla y ejecutarla con el instalador por defecto.

### Instalar por línea de comandos
1. [Buscar aquí](https://www.python.org/ftp/python/) el número de versión (dentro de su carpeta) y el patch que queremos.
2. Ejecutar los siguientes comandos, dependiendo del número de versión/patch que queremos:
```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
brew install wget
wget https://www.python.org/ftp/python/<NUMERO.DE.VERSIÓN>/<nombre_del_archivo_comprimido_con_patch>-macosx10.6.pkg
sudo installer -pkg <nombre_del_archivo_comprimido_con_patch>-macosx10.6.pkg -target /
```