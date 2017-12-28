
var funcion = function(){
    console.log("Función de un módulo en el mismo directorio");
}

// La estructura de cada exportación es:
// nombre_de_funcion_al_usarla: nombre_usado_en_este_archivo
module.exports = {
    funcion_mismo_directorio: funcion
}
