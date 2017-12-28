"use strict"

// Lanzar y cazar errores en Javascript
try {
    throw new Error("Hemos lanzado un error")
} catch(err) {
    console.log(err);
} finally {  // La cláusula finally se ejecuta siempre
	console.log("...pero la vida sigue.")
}


// Lanzar errores específicos
try {
    throw new TypeError("Hola soy un error de tipo")
} catch(error) {
    console.log(error.name);  // Imprimir el tipo de error
    // Existen únicamente 6 tipos de errores en Javascript
    // y puedes consultarlos en esta página:
    // https://www.w3schools.com/js/js_errors.asp

    console.log(error.stack); // Imprimir el traceback completo
    console.trace();          // Imprimir la zona del error (sin el cabecero)
}

