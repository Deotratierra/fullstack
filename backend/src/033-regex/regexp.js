"use strict"

var texto = `Las expresiones regulares en Javascript
se representan entre caracteres / `

var expresion = /.a../;

// Después de la expresión pueden aparecer modificadores:

var expresion2 = /.a../i,  // Coincidencias flexibles
    expresion3 = /.a../g,  // Buscar por todas las coincidencias,
                           //     sin detenerse en la primera
    expresion4 = /.a../m;  // Búqueda multilínea

// -----------------------------------------------

// Compilar expresiones regulares:
var patron = RegExp(expresion3);
// Podemos añadir como segundo parámetro los modificadores

// -----------------------------------------------

// Buscar por la primera coincidencia
var coincidencia = patron.exec(texto);

// Output:
//     [ 'Las ',
//     index: 0,
//     input: 'Las expresiones regulares en Javascript\nse representan entre caracteres / ' ]

// -----------------------------------------------

// Buscar si existe alguna coincidencia:
var coincidencia = patron.test(texto); // true

// -----------------------------------------------

// Buscar todas las coincidencias (con modificador g):
var coincidencias = texto.match(patron); // [ 'Las ', 'lare', 'Java', 'tan ', 'cara' ]

// -----------------------------------------------

// Índice de la primera coincidencia
var indice = texto.search(patron);  // 0

// -----------------------------------------------