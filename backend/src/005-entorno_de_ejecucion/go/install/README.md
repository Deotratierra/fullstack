## Instalar Golang

### Linux

1. Dscargar un archivo comprimido con la última versión del lenguaje: `wget https://dl.google.com/go/go1.10.linux-amd64.tar.gz`.
2. Descomprimir el paquete: `tar -xvf go1.10.linux-amd64.tar.gz`.
3. Eliminar el archivo comprimido: `rm go1.10.linux-amd64.tar.gz`.
4. Mover el directorio descomprimido a la ruta donde queremos alojarlo, por ejemplo yo opté por ejecutar `sudo mv go /usr/local`.
5. Determinar la ruta de la biblioteca estándar de Go: `export GOROOT=/usr/lib/go` (puedes ponerla donde quieras).
6. Determinar la ruta de tu directorio de trabajo: `export GOPATH=$HOME/go` (mira el apartado [Administración de dependencias](https://github.com/mondeja/fullstack/tree/master/backend/src/005-entorno_de_ejecucion/go/packages) para entender las variables de entorno `GOPATH` y `GOROOT`).
7. Establecer en el `PATH` del sistema las rutas hacia los directorios donde se ubican los archivos binarios: `export PATH=$GOPATH/bin:$GOROOT/bin:$PATH`.
8. Insertar los tres anteriores comandos en el perfil de la consola de tu usuario (puedes abrirlo con `nano ~/.profile`) para que se establezcan de forma permanente.
9. Comprobar la instalación ejecutando `go version`.
10. Crear la estructura básica de un directorio de trabajo: `mkdir $GOPATH/src $GOPATH/pkg $GOPATH/bin`.
