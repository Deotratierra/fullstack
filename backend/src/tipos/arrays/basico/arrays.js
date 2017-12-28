"use strict"

// INICIALIZACIÓN

var lista1 = ["uno", "dos", "tres"];
var lista2 = new Array(4); // Array con 4 elementos undefined
var lista3 = [1, 2, 3, 4];

// ---------------------------------------------------------

// ACCESO A SUS ELEMENTOS Y MODIFICACIÓN

console.log(lista1[0]) // uno

console.log(lista1.length);  // 3  <--- Número de elementos

console.log(lista1.sort()); // [ 'dos', 'tres', 'uno' ] <--- Ordenación

// Obtener el índice de un elemento
console.log(lista1.indexOf("uno")) // 0

// Agregar un elemento al final de la lista
console.log(lista1.push("cuatro")); // 4  (Devuelve length)
console.log(lista1); // [ 'dos', 'tres', 'uno', 'cuatro' ]

// También así:
lista1[lista1.length] = 5;

// Eliminar un elemento del final de la lista
lista1.pop();

// Eliminar un elemento por su índice
lista1.pop(1);

// Eliminar un elemento del inicio de la lista
lista1.shift();
console.log(lista1);  // [ 'tres', 'uno' ]

// Convertir un elemento a undefined
delete lista1[1];
console.log(lista1);  // [ 'tres', , ]

// Agregar varios elementos
lista1.splice(2, 0, 7, "ocho");
// El primer parámetro (2) es el lugar donde irán los nuevos
// El segundo parámetro (0) es el número de elementos que son eliminados
console.log(lista1); // [ 'tres', , 7, 'ocho' ]

// Concatenar varias listas
lista1 = lista1.concat(lista2); // Podemos agregar las listas que queramos
console.log(lista1);  // [ 'tres', , 7, 'ocho', , , ,  ]

// Cortar un array
var lista3 = lista1.slice(3); // Índice como parámetro
console.log(lista3); // [ 'ocho', , , ,  ]

// Ordenar array
lista1.sort();

// Revertir array
lista1.reverse()

// Saber si existe un elemento en un array:
console.log(lista1.indexOf("ochenta") > -1); // false

// ============================================================

console.log("----------------------------")

// Saber si es una lista        Así no lo sabremos:
console.log(typeof(lista1));         // object   ¿?

// Esta solución no funciona en navegadores antiguos
console.log(Array.isArray(lista1));  // true

// Solución:
function isArray(x) {
    return x.constructor.toString().indexOf("Array") > -1;
}
console.log(isArray(lista1)); // true

// Solución más simple:
console.log(lista1 instanceof(Array)); // true


// Modificar los elementos del array
lista3.forEach(function(element) {
    element += 1;
});
console.log(lista3)  // [2, 3, 4, 5]

// ---------------------------------------------------------

/* Para profundizar:
https://www.w3schools.com/js/js_array_sort.asp
*/
