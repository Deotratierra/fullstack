package main


import (
    "fmt"
)

func Contador(start, end int) chan int {
    ch := make(chan int)

    go func(ch chan int) {
        for i:= start; i <= end; i++ {
            ch <- i
        }
        close(ch)
    }(ch)

    return ch
}

func main() {
    for i := range Contador(3, 10) {
        fmt.Printf("%d-", i)    // 3-4-5-6-7-8-9-10-
    }
    fmt.Printf("\n")
}

