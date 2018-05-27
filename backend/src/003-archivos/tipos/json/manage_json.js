"use strict"

// Abrir un archivo JSON (NodeJS)
var fs = require('fs');
var archivo = JSON.parse(fs.readFileSync('fichero.json', 'utf8'));

console.log(archivo.py)  // 178

// --------------------------------

// Parsear cadenas de texto JSON
var texto = '{"hola": "que tal"}'
console.log(typeof(texto));  //  string

var response = JSON.parse(texto); // <---- ¡Igual que en Ruby!
console.log(typeof(response));  //  object

console.log(response.hola);  //  que tal
