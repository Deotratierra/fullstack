package main

// Para ejecutar:
//     go test -run ""

import (
    "github.com/stretchr/testify/assert"
    "testing"
)

func TestSomething(t *testing.T) {
    var a string = "Hello"
    var b string = "Hello"

    assert.Equal(t, a, b, "The two words should be the same.")

}

/* Fuentes:
https://godoc.org/github.com/stretchr/testify/assert
https://golang.org/pkg/testing/
*/