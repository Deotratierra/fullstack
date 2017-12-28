
var sentencias = [
    "abcdefGHIJKLMNopqrstuvwxyz",
    "abcdefGHIJKLwNopqrstuvwxyz",
    "Texto de ejemplo",
    "The quick brown fox jumps over the lazy dog",
]

var abecedario_ingles = "abcdefghijklmnopqrstuvwxyz";

var pangrama = function(string){
    var letras = [];
    for (i = 0; i < string.length; i++){
        var letra = string[i].toLowerCase();
        if (letras.indexOf(letra) < 0){
            if (abecedario_ingles.indexOf(letra) >= 0){
                letras.push(letra);            
            }    
        }
    }
    if (letras.length == abecedario_ingles.length){
        return true;
    }
    return false;
};

for (x = 0; x < sentencias.length; x++){
    console.log(pangrama(sentencias[x]));
}
/* Es muy común declarar una variable i en como 
índice en los loops, pero si colocamos la misma letra
dentro del bucle de la función, se pisarán y sólo procesará 
la primera sentencia. Cuidado con la sobrescritura
de variables. Esto nos lo ahorramos con ámbitos locales
de variables en lenguajes como C++ y Ruby.
*/

