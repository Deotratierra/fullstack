"use strict"

var STRING='{"clave": "valor 1", "num": 2}'

function ej() {
    var result = JSON.parse(STRING)[process.argv[2]]
    //console.log(result);
}

if (require.main == module){
    ej();
}
