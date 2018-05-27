## Compilación de código fuente en Golang

Una bandera de compilación es un comentario que comienza con: `// +build` que lista las condiciones por las que un archivo debe ser incluido en el paquete. las restricciones pueden aparecer en cualquier tipo de archivo fuente (no sólo Go), pero deben aparecer en la parte de arriba del archivo. En los archivos  `.go` deben aparecer antes del la sentencia `package`.

> Para distinguir a las restricciones de compilación de comentarios, una serie de banderas debe estar seguida por una línea en blanco.

________________________________

### Reglas básicas de compilación
- Para ignorar un archivo en la compilación añadir: `// +build ignore`
- Opciones separadas por ` ` (espacios): evaluan como sentencia `OR`.
- Opciones separadas por `,` (comas): evaluan como sentencia `AND`. Por ejemplo, `// +build linux,386 darwin,!cgo` corresponde a la fórmula booleana `(linux AND 386) OR (darwin AND (NOT cgo))`
- Opciones en la siguiente línea: evaluan como sentencia `AND`. Por ejemplo, la fórmula booleana `(linux OR darwin) AND 386` corresponde a:
```go
// +build linux darwin
// +build 386`
```

______________________________

- [Compilación condicional por línea de comandos](https://github.com/mondeja/fullstack/tree/master/backend/src/005-entorno_de_ejecucion/go/compile/varios_main)