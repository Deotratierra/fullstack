package main

import (
    "fmt"
    "github.com/robertkrimen/otto"
)

func main() {

    // Ejecutar javascript desde Golang
    vm := otto.New()
    vm.Run(`
    abc = 2 + 2;
    console.log("El valor de 'abc' es " + abc);
`)      // El valor de 'abc' es 4

    // Obtener una variable del código Javascript
    if value, err := vm.Get("abc"); err == nil {
        if value_int, err := value.ToInteger(); err == nil {
            fmt.Printf("%d\n", value_int)  // 4
        }
    }

    // Establecer una variable del código Javascript
    vm.Set("def", 11)
    vm.Run(`
        console.log("El valor de 'def' es " + def);
`)      // El valor de 'def' es 11
}

/* Fuentes:
https://github.com/robertkrimen/otto
*/
