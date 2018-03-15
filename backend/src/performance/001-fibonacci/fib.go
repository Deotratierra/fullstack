package main

import (
    "os"
    "strconv"
)

func fib(n int64) (int) {
    a, b := 0, 1
    var i int64
    for i=0; i<=n; i++ {
        a, b = a + b, a
    }
    return a
}

func main() {
    arg, _ := strconv.ParseInt(os.Args[1], 10, 0)
    fib(arg)
}
