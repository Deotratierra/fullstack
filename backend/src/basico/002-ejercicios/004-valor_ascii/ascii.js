'use strict'

if (require.main == module){
    var caracter = "a";
    var caracter_en_ascii = caracter.charCodeAt(0);
    console.log("El caracter '" + caracter + "' en ASCII ---> " + caracter_en_ascii);

    var numero = 87;
    var numero_en_caracter = String.fromCharCode(numero);
    console.log("El número " + numero + " en caracter ---> " + numero_en_caracter);
}

