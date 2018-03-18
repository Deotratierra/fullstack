package main

import (
    "os"
    "encoding/json"
    "fmt"
)

func main() {
    STRING := []byte(`{"clave": "valor 1", "num": 2}`)
    var dict map[string]interface{}
    json.Unmarshal(STRING, &dict)
    result := dict[os.Args[1]]
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