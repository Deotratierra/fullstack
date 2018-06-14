package main

import (
    "fmt"
    "log"
    "os/exec"
)

func main() {
    // Inicializar comandos del sistema
    cmd1 := exec.Command("date")
    cmd2 := exec.Command("whereis", "go")
    cmd3 := exec.Command("sleep", "1")
    cmd4 := exec.Command("sleep", "3")

    // -------------------------------------------------------------

    // Ejecutar un comando y obtener stdout y stderr
	stdoutStderr, err1 := cmd1.CombinedOutput()
	if err1 != nil {
		log.Fatal(err1)
	}
	fmt.Printf("La salida (o error) del proceso es: '%s'.\n", stdoutStderr)

	// Ejecutar un comando y obtener sólo la salida estándar (stdout)
	_stdout, err2 := cmd2.Output()
	if (err2 != nil) {
        log.Fatal(err2)
	}
	fmt.Printf("La salida del proceso es: '%s'.\n", _stdout)

	// -------------------------------------------------------------

    // Ejecutar un comando esperando a que se complete
    fmt.Printf("\nEjecutando el comando y esperando a que se complete...\n")
    err3 := cmd3.Run()
    fmt.Printf("Comando finalizado con error: %v\n", err3)

    // Ejecutar un comando sin esperar a que se complete
    fmt.Printf("\nLanzando un comando...\n")
    err4 := cmd4.Start()       // Luego podemos esperar a que se complete
    if (err4 != nil) {         //   mediante la función Wait()
        log.Fatal(err4)
    }
    fmt.Printf("Esperando a que el comando se complete...\n")
    err5 := cmd4.Wait()
    fmt.Printf("Comando finalizado con error: %v\n", err5)

    // -------------------------------------------------------------

    /* Existen otras funciones para conectarnos a la entrada estándar
        o a la salida de error mediante un comando está corriendo,
        así como la posibilidad de correr comandos bajo un determinado
        contexto. En la documentación de la fuente hay más información.
    */
}

/* Fuentes:
https://golang.org/pkg/os/exec/#Command
*/
