
var funcion = function(){
    console.log("Función de un módulo desde otro directorio");
}

// La estructura de cada exportación es:
// nombre_de_funcion_al_usarla: nombre_usado_en_este_archivo
module.exports = {
    funcion_otro_directorio: funcion
}
