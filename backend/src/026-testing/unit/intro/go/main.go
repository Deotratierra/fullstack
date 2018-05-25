package main

import (
	"fmt"
)

// Devuelve x + 2.
func Calculate(x int) (result int) {
	result = x + 2
	return result
}

func main() {
	fmt.Println("Hello World")
}

/* $ go test
PASS
ok  	_/home/.../unit/intro/go	0.001s
*/
