"use strict"

function rs() {
    for (var i=0; i<process.argv[2]; i++) {
        var string = "Salida de emergencia",
            pattern = "Salida",
            substitution = "Entrada";
        var result = string.replace(pattern, substitution);
    }

}

if (require.main == module){
    rs()
}
