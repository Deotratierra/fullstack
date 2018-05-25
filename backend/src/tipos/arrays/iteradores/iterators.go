package main

import (
    "fmt"
    "log"
)

// Iterador por todos los números pares hasta un máximo
//
//   Uso:
// -----------------------------------------------------
// err := IteradorNumerosPares(max, func(n int) error {
//     fmt.Printf("%d\n", n)
//     return nil
// })
// -----------------------------------------------------
//
func IteradorNumerosPares(max int, cb func(n int) error) error {
	if max < 0 {
		return fmt.Errorf("'max' is %d, must be >= 0", max)
	}
	for i := 2; i <= max; i += 2 {
		err := cb(i)
		if err != nil {
			return err
		}
	}
	return nil
}

func imprimeNumerosPares(max int) {
	err := IteradorNumerosPares(max, func(n int) error {
		fmt.Printf("%d\n", n)
		return nil
	})
	if err != nil {
		log.Fatalf("Error: %s\n", err.Error())
	}
}


func main() {
    imprimeNumerosPares(10)

}

/* Fuentes:
https://ewencp.org/blog/golang-iterators/index.html
https://blog.kowalczyk.info/article/1Bkr/3-ways-to-iterate-in-go.html
https://github.com/kjk/go-cookbook/blob/master/3-ways-to-iterate/callback.go
*/
