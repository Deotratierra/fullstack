package main

import (
    "fmt"
    "os"
    "encoding/csv"
    "strings"
    "io"
)

func main() {
    path := "fichero.csv"

    // Abrimos el archivo
    f, err := os.OpenFile(path, os.O_RDWR, os.ModeAppend)
    if err != nil {
        fmt.Printf("Ocurrió un error al abrir el archivo '%s'.\n%s\n",
        	       path, err.Error())
        os.Exit(1)
    }

    // Situamos el cursor al principio del archivo
    _, err = f.Seek(0, 0)  // Reiniciamos la posición del buffer al archivo
    if err != nil {
        fmt.Printf("Error reiniciando el archivo '%s' " +
                   "a su posición inicial.\n%s\n", path, err.Error())
        os.Exit(1)
    }

    // Leemos el contenido del archivo
    var n uint16 = 1024      // Tamaño del buffer
    buff := make([]byte, n)  // Creamos un buffer de bytes
    _, err = f.Read(buff)    // Leemos el contenido en el buffer
    if err != nil {
        fmt.Printf("Error al leer el archivo '%s'.\n%s\n",
        	       path, err.Error())
        os.Exit(1)
    }

    content := string(buff[:n])  // Contenido del buffer como cadena

    // Creamos un lector de CSV que actúa como parser
    // https://golang.org/pkg/encoding/csv/#NewReader
    csvFile := csv.NewReader(strings.NewReader(content))

    // Inicializamos una matriz vacía donde almacenar
    //   las filas del archivo CSV.
    rows := [][]string{}
    for {
		record, err := csvFile.Read()
		if err == io.EOF {   // Fin de cadena
			break
		}
		if err != nil {   // Error no crítico
			fmt.Printf("Ocurrió un error parseando el contenido " +
				       "del archivo '%s' a CSV.\n%s\n", path, err.Error())
		    break
		}

        // Añadimos la nueva fila a la matriz
		rows = append(rows, record)
	}

    // Mostramos el resultado final
	fmt.Printf("\nLa matriz de elementos extraída del archivo " +
		       "CSV es la siguiente:\n%v\n", rows)
}

/* Fuentes:
https://golang.org/pkg/encoding/csv/#example_Reader
*/
*