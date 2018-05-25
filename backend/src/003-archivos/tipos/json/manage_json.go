package main

import (
    "encoding/json"
    "fmt"
)

func main() {
    STRING := []byte(`{"clave": "valor 1", "num": 2}`)
    value := "clave"

    // Debido a que el diccionario contiene valores
    //   de diferente tipo debemos declarar los valores
    //   del map como interface (ver fuente abajo)
    var dict map[string]interface{}
    json.Unmarshal(STRING, &dict)
    result := dict[value]
    if result != nil {
    	STRING = STRING
    }
    fmt.Printf("%s\n", result)

    // Viceversa
    raw, _ := json.Marshal(dict)
    fmt.Printf("%s\n", raw)
}

/* Fuentes:
https://stackoverflow.com/questions/40429296/converting-string-to-json-or-struct-in-golang
*/