package main

/* Los canales son un tipo nativo de Golang.
    Funcionan de manera análoga a los slices,
    pero con algunas diferencias.

   Podemos enviar valores al canal y recibirlos
    del mismo con los operadores de flecha: <-, ->.
    El flujo de la información se produce en la
    dirección que apunta la flecha.

   Los canales se definen mediante el tipo 'chan'
    y, al igual que los slices y los maps,
    también debemos crearlos antes de usarlos.

   Por defecto, los envíos y recepciones bloquean
    hasta que el otro extremo está preparado.
    Esto permite a corrutinas sincronizarse sin
    definir explícitamente locks o condicionales.
*/

import (
   "fmt"
)

func sumatorio(s []int, c chan int){
    sum := 0
    for _, v := range s {
        sum += v
    }
    // Enviamos el resultado del sumatorio al canal
    c <- sum
}

func main(){
    // CANALES SIN BUFFER

    // Creamos slice de enteros
    s := []int{1, 2, 3, -1, -2, -3}

    // Creamos un canal
    c := make(chan int)

    // Lanzamos dos gorrutinas en paralelo
    //   con la función sumatoria
    go sumatorio(s[len(s)/2:], c)
    go sumatorio(s[:len(s)/2], c)

    // Obtenemos los valores del canal
    //   (bloquea hasta que los valores son devueltos)
    x, y := <-c, <-c

    fmt.Println(x, y)  // 6, -6

    // ================================================

    // CANALES CON BUFFER

    /* Los canales pueden ser con buffer. Envíos a canales
        con buffer bloquean sólo cuando el buffer está lleno.
        Recepciones bloquean sólo cuando el buffer está vacío.
       Para crear un canal con buffer simplemente pasa su
        número máximo de elementos como tercer valor de la
        función 'make()'.
    */
    
}

/* Ejemplos de uso:
https://tour.golang.org/concurrency/5
 */