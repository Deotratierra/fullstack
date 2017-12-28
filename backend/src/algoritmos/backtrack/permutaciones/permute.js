"use strict"

function permutations(lista) {
    var n = lista.length;
    var response = n;
    for (var i = 1; i < n; i++) {
        response = i*response
    }
    return response
}

var test = ["h", "o", "l"];
console.log(test);

console.log(permutations(test));