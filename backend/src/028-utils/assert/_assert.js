"use strict"

// En los navegadores, si falla una aserción, el mensaje será impreso en consola
// pero no se detendrá la ejecucíón del programa. Sin embargo, en NodeJS, la
// ejecución fallará y se producirá un error un AssertionError

try {
    // Realizar una aserción
    console.assert(1 + 2 == 3,
    	           "Mensaje de error formateado como en %s", "C");
} catch (err) {  // Cazar una aserción
    console.log("Se produjo un error en la aserción");
    console.error(err.stack);
}
