"use strict"

///   Decorador simple   ///

var decorador = function(f) {
    return function(arg) {
        console.log("Antes de la función");
        var resultado = f(arg);
        console.log("Después de la función");
        return resultado
    }
}

var funcion = function(arg) {
    console.log("Función, argumento: " + arg);
    return "Valor de retorno"
};

funcion = decorador(funcion);

console.log(funcion(123));
/*
Antes de la función
Función, argumento: 123
Después de la función
Valor de retorno
 */

// ====================================