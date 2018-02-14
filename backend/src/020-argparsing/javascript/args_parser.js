"use strict"

// =====================================================

// OPCIÓN 1: SIN BIBLIOTECAS EXTERNAS

// Obtener los argumentos pasados por línea de comandos:
process.argv.forEach( function(val, index, array) {
    console.log(index + ": " + val);
});
/* node args_parser.js arg1 arg2 -o

0: /ruta/al/binario/node
1: /ruta/completa/al/archivo/args_parser.js
2: arg1
3: arg2
4: -o
*/

/* Como los dos primeros son la ruta al binario de node
   y al archivo ejecutado, podemos ignorarlos: */
var args = process.argv.slice(2);
console.log(args);  // [ 'arg1', 'arg2', '-o' ]

// ====================================================

// OPCIÓN 2: CON BIBLIOTECAS EXTERNAS

/* Esta biblioteca nos permite obtener fácilmente
   los argumentos por tipo (posicionales y opcionales): */
var minimist = require('minimist');  // npm install minimist

var argv = minimist(process.argv.slice(2));
console.log(argv);  // { _: [ 'arg1', 'arg2' ], o: true }
