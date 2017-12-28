"use strict"

var fs = require("fs");

// Abrir un archivo para escritura
fs.open("ejemplo.txt", "w", (error, archivo) => {
    if (error) {
        if (error.code === "EEXIST") {
            console.error("El archivo ya existe");
            return;
        } else {
            throw error;
        }
    }

    // Escribir en archivo
    fs.write(archivo, "Contenido del archivo\n");
    fs.close(archivo);
})


// Leer el contenido de un archivo
fs.readFile("ejemplo.txt", "utf8", (error, contenido) => {
    if (error) {
        throw error;
    } else {
        console.log(contenido);
    }
});
