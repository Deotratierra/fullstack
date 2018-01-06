"use strict"

// La biblioteca loglevel provee un sistema de logs simple,
// mínimo y ligero, perfecto para pequeños proyectos.
// Funciona en el frontend y en NodeJS

// Referencia: https://github.com/pimterry/loglevel
var log = require('loglevel');  // npm install loglevel

// Establecer el nivel de logs
log.setLevel("debug");

// Mensajes de log
log.trace("Mensaje de trace");
log.debug("Mensaje de debug");
log.info("Mensaje de información");
log.warn("Mensaje de aviso");
log.error("Mensaje de error");

// Activar todos los mensajes de log
log.enableAll();  // Equivalente a log.setLevel("trace")

// Desactivar todos los mensajes de log
//log.disableAll(); // Equivalente a log.setLevel("silent")

// Obtener el nivel actual de log, desde 0 (trace) hasta 5 (silent)
console.log(log.getLevel());  // 5

// Encadenar y/o formatear mensaje
log.debug("Hola %s", "Álvaro");

// Obtener un nuevo log
var nuevo_log = log.getLogger("log_de_mi_aplicación");

// Obtener todos los loggers
console.log(log.getLoggers());
