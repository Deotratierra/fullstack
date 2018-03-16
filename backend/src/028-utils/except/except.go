package main

import "os"

/*                 Excepciones en Golang
Golang no tiene excepciones a la manera 'try/cactch' de Python.
   Los errores son lanzados al estilo de C como abortos, así que
   tenemos que manejar los valores que pasamos, aunque hay algunas
   formas de manejar y producir errores.*/

func main() {
    /* Panic
    Un uso común de panic es para abortar si una función devuelve un
    valor que no sabemos o no queremos manejar.
    Aquí hay un ejemplo de como abortarlo si tenemos un error
    creando un nuevo archivo: */
     _, err := os.Create("/@tmp/file/hweugheqwv")
    if err != nil {
        panic(err)
    }
}

/* Fuentes:
https://blog.golang.org/defer-panic-and-recover
https://play.golang.org/p/c86oXzfQOt
*/