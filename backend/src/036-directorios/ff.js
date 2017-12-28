// Sólo en NodeJS

"use strict"
const path = require("path");

// Obtener el path del archivo actual
console.log(__filename);

// Obtener el path al directorio del archivo actual
console.log(__dirname);

// Obtener el nombre del archivo de un path
//path.basename("<path>", ["<ext>"]);
// Si añadimos extensión la elimina del archivo devuelto
console.log(path.basename(__filename, ".js")); // files_and_folders

// Delimitar varios paths concatenados por ":" (Unix) o ";" (Windows)
//console.log("<path>".split(path.delimiter));
console.log( (__filename + ":" +  __dirname).split(path.delimiter) );

// Obtener el directorio de un path
// path.dirname("<path>");
console.log( path.dirname(__filename) === __dirname ); // true

// Obtener la extensión del archivo de un path
// path.extname("<path>");
console.log( path.extname(__filename) );  // .js

// Saber si un path es absoluto
// path.isAbsolute("<path>");
console.log( path.isAbsolute(__filename),                   // true
	         path.isAbsolute(path.basename(__filename)) );  // false

// Unir partes de un path
// path.join( ["<paths>"] );
console.log( path.join("ruta", "al", "arhivo.txt") );  // ruta/al/arhivo.txt

// Separar partes de un path en un array
// "<path>".split(path.sep);
console.log(__dirname.split(path.sep))

// Normalizar un path (corregir errores):
// path.normalize("<path>");
console.log( path.normalize("normalizar//el/path.txt")); // normalizar/el/path.txt

// =================================================================

// Parsear un path.
// Se convierte en un objeto con las siguientes propiedades:
//     root           ┌─────────────────────┬────────────┐
//     dir            │          dir        │    base    │
//     base           ├──────┬              ├──────┬─────┤
//     ext            │ root │              │ name │ ext │
//     name           "  /    home/user/dir / file  .txt "
//                    └──────┴──────────────┴──────┴─────┘
// path.parse("<path>");
//
//   ^
//   |  Operación contraria
//   v
//
// path.format(<pathObject>);

// =================================================================

// Iterar por todos los subdirectorios de un directorio
// https://www.npmjs.com/package/walk

const walk = require("walk");   // npm install walk

const directory = path.dirname(path.dirname(__filename));
var count_files = 0, count_dirs = 0;

const walker = walk.walk(directory); // Función asíncrona


walker.on("file", function(root, fileStats, next){
	count_files += 1;
	next();
});

walker.on("directory", function(root, dirStats, next) {
	count_dirs += 1;
	next();
});

walker.on("end", function(){
	console.log("Número de archivos: " + count_files);
    console.log("Número de directorios " + count_dirs);
});

// ================================================================
