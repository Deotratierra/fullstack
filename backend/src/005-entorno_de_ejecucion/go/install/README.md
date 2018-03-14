## Instalar Golang

### Linux
#### Debian
1. Instalar el paquete con tu gestor de paquetes: `sudo apt-get install golang`
2. Actualizar a la versión 1.10:
  ```
  git clone https://go.googlesource.com/go
  cd go
  git checkout go1.10
  cd src
  ./all.bash
  ```
3. Todos los tests se ejecutarán, si todos pasan el lenguaje estará instalado correctamente. Sólo queda comprobar que está en el `PATH` del sistema, así que ejecutamos el [`hello_world.go`](https://github.com/mondeja/fullstack/tree/master/backend/src/basico/001-hola_mundo) con `go run hello_world.go` y debe funcionar.

> Podemos controlar opciones al momento de construir Go [estableciendo ciertas variables de entorno](https://golang.org/doc/install/source#environment). También podemos seleccionar otra versión, para ver las disponibles ejecutar `git tag` y cambiar a otra versión de lanzamiento con `git checkout`.
