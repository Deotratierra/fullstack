## Administración de paquetes en Golang
La palabra clave `import` es usada en Go para importar un paquete en otros. Cuando importas paquetes, el compilador de Go busca en las localizaciones especificadas por las variables de entorno `GOROOT` y `GOPATH` (puedes consultarlas ejecutando `go env <variable>`). Los paquetes de la biblioteca estándar se encuentran en la ruta definida en `GOROOT` y los paquetes de terceros se encuentran en la ruta definida en `GOPATH`.

### Instalando paquetes de terceros
Podemos descargar e instalar paquetes de terceros de Go usando el comando `go get`. Este obtiene los paquetes del repositorio fuente y pone los paquetes en la localización de `GOPATH`.

Por ejemplo, ejecutando `go get gopkg.in/mgo.v2` se instalará el driver de MongoDB para Go y podremos importar el paquete:

```
import (
    "gopkg.in/mgo.v2"
    "gopkg.in/mgo.v2/bson"
)
```

### Inyección de dependencias
Go requiere colocar código en un espacio de trabajo. Un espacio de trabajo es sólo un directorio con tres subdirectorios: `src`, `pkg` y `bin`. Se recomienda mantener todos tus proyectos bajo un solo espacio de trabajo. De ésta forma pueden depender mutuamente y compartir paquetes de terceros.

Cuándo creas un programa o biblioteca en Go, puedes instalarla ejecutando `go install`. Los programas van al directorio `bin` de tu espacio de trabajo, y las bibliotecas van al directorio `pkg` del espacio de trabajo.