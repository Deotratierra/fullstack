package main

import "fmt"

//               Arrays en Golang
/* En Go los arrays están implementados dentro del lenguaje.
    No son objetos, ni abstracciones externas si no que
    orman parte intrínseca de Go.
   Los arrays ocupan el tamaño del tipo multiplicado
    por el número de elementos. No podemos modificar el
    tamaño de un array.
*/

func main() {
    // Inicialización
    var enteros [2]int               // Array de dos ceros
    //                                  Array de dos elementos
    //var eb [2]string = [2]string{"Epi", "Blas"}
    //var eb = [2]string{"Epi", "Blas"} // más simple
    eb := [2]string{"Epi", "Blas"}    // Tipado implícito

    // Acceso a sus elementos
    fmt.Printf("%d\n", enteros[1])  // 0
    fmt.Printf("%s\n", eb[0])       // Epi

    // Recorrer arrays
    for i, val := range eb {
        fmt.Printf("%d - %s\n", i, val)
    }

    /*
    - Cuando se asigna un array a una variable, se obtiene
        un nuevo array independiente del anterior.
    - Cuando se asigna un array a una variable, se copia
        todo el contenido del array (con el impacto en
        rendimiento que esto puede tener).
    - Cuando se pasa como parámetro un array a una función,
        se le pasa una copia. Esto tiene dos implicaciones:
        - El rendimiento de la llamada (sobre todo si es
            recursiva) puede ser peor del esperado.
        - Las modificaciones que se hagan al array dentro de
            la función desaparecerán al salir de la función.
    */

    // ----------------------------------------------------
    //                       Slices
    /* Ya que los array no pueden modificar su tamaño podemos
        utilizar slices ("trozos"), que se definen igual que
        los arrays pero sin especificar su tamaño.
    */

    // Inicialización
    letras :=[]string{"a", "b", "c"}
    // También podemos inicializarlos con la funcion make()
    var s []byte    // params: len and cap
    s = make([]byte, 3, 5)    // s == []byte{0, 0, 0, 0, 0}

    // ----------------------------------------------------

    // Obtener el largo de un slice         len()
    //    (cantidad de elementos al inicializar el slice)
    fmt.Printf("Largo de 'letras' == %d\n", len(letras)) // 3

    // Obtener la capacidad de un slice
    //    (número de espacios disponibles para almacenar)
    fmt.Printf("Capacidad de 's' == %d\n", cap(s)) // 5

    slice[a:b] //Acceder a los alementos desde a-b
    slice[:b] //Acceder a los alementos desde 0-b
    slice[a:] //Acceder a los alementos desde a-len(a)
    slice[:] //Acceder a todos los elementos
    /* En Go no podemos acceder a los elementos de un slice
        especificando índices negativos. */
    slice[a:len(a)-1] // Primero hasta el penúltimo


    // Añadir elementos
    letras = append(letras, "d", "e", "f")


    // Crear una copia
    //copy(slice_destino, slice_original)

    // ================================================
    /* Para otros trucos con slices:
    https://github.com/golang/go/wiki/SliceTricks
    */


}


/* Fuentes:
https://blog.golang.org/go-slices-usage-and-internals
https://gopadawan.wordpress.com/2013/10/09/tipos-de-datos-ii-arrays/
https://codingornot.com/12-go-to-go-slices-trozos-en-golang
*/