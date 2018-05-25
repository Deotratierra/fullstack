## Logging en Golang
EL logging en Golang hacia la salida estandar del sistema se puede realizar a través de las funciones `log.Print[f|ln]` (o `fmt.Print[f|ln]`), `log.Fatal[f|ln]`, y `log.Panic[f|ln]`. La función `log.Fatal` llama a `os.Exit` cuando es invocada y la función `log.Panic` llama a `panic` cuando es invocada.

