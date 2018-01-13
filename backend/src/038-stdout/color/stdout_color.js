"use strict"

const colors = require("colors"); // npm install colors

// Para consultar todos los estilos y colores:
console.log(colors.styles);

// Aplicar color
console.log("Texto verde".green)
console.log("Texto rojo".red)

// Aplicar color de fondo
console.log("Texto azul con el fondo blanco".blue.whiteBG)

// Aplicar estilos:
console.log("Texto subrayado".underline)
console.log("Texto amarillo en negrita".yellow.bold)
console.log("Texto cursivo en magenta".magenta.italic)

// Para desabilitar los colores en el script 
// podemos ejecutarlo con la opción --no-color

// Para más opciones como temificar consultar la documentación
// https://github.com/marak/colors.js/