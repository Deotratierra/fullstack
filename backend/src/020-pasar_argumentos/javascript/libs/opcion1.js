
// Obtenemos el script por su identificador
var etiqueta_del_script = document.getElementById("identificador");
// Obtenemos el atributo donde se guardan los argumentos
var arg = etiqueta_del_script.getAttribute("data-search");

// Mostramos el argumento en el HTML
var mostrador = document.getElementById("mostrador");
mostrador.innerHTML = arg;

console.log(arg);