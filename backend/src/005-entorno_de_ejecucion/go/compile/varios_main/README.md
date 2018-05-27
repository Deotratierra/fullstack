### Compilación condicional por línea de comandos con Golang

En este directori se encuentran dos archivos cuyos nombres son `main1.go` y `main2.go`. Dentro de estos archivos, en la primera línea, puedes ver la directiva de compilación `// +build main1` y `// +build main2` respectivamente. Gracias a esto, podemos controlar que archivo se compilará mediante:
- Compilar `main1.go`: `go build -tags "main1"`
- Compilar `main2.go`: `go build -tags "main2"`

