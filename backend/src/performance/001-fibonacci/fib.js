"use strict"

function fib(n) {
    var a = 0,
        b = 1;
    var tmp;
    for (var i=0; i<=n; i++) {
        tmp = a
        a = a + b
        b = tmp
    }
    return a
}

if (require.main == module){
    var arg = process.argv[2];
    fib(arg)
}
