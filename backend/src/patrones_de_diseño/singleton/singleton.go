package main

import (
    "fmt"
    "sync"
)

// La función 'sync.Once()' crea un objeto once,
// el cual cuenta con un método 'Do()' que garantiza
// que la función que recibe como callback sólo
// es invocada si lo ha sido antes

// Creamos un mapas con cadenas como claves y valores
type singleton map[string]string

var (
    once sync.Once
    instance singleton
)

// Esta función sólo devuelve la instancia
// al ser llamada por primera vez. Sucesivas
// invocaciones devuelven siempre la primera
// instancia.
func New() singleton {
	once.Do(func() {
		instance = make(singleton)
	})

	return instance
}

func main() {
    // Creamos un nuevo mapa singleton
    s := New()

    // Introducimos un par clave-valor
    s["this"] = "that"

    // Intentamos crear un nuevo objeto singleton
    s2 := New()

    // pero se puede comprobar que devuelve el primero
    fmt.Printf("This is %s.\n", s2["this"])  // This is that.
}

/* Fuentes:
https://github.com/tmrts/go-patterns/blob/master/creational/singleton.md
https://golang.org/pkg/sync/#Once
*/
