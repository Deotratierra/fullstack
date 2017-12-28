"use strict"

class Operacion {
	// Define una operación en dos pasos
    // abstractos que cada subclase concretará
    constructor() {
        if (this.constructor === Operacion) {
            var msg = "La clase asbtracta Operacion " +
                "no puede ser instanciada directamente."
            throw new TypeError(msg);
        }

        var metodos_abstractos = [
            this.suboperacion_1,
            this.suboperacion_2
        ]

        for (var i=0; i < metodos_abstractos.length; i++){
            if (metodos_abstractos[i] === undefined) {
                var msg = "Debes declarar los métodos " +
                     "de la clase Padre Operacion en " +
                    this.constructor.name;
                throw new TypeError(msg);
            }
        }
    }

    ejecutar() {
        this.suboperacion_1();
        this.suboperacion_2();
    }
}

class OperacionConcreta extends Operacion {
    /* Implementa las operaciones
    para seguir los pasos del algoritmo
    específicos para esta subclase */
    suboperacion_1() {
        console.log("Primer paso en la operación");
    }

    suboperacion_2() {
        console.log("Segundo paso en la operación");
    }
}

if (require.main == module) {
    var operacion_concreta = new OperacionConcreta();
    operacion_concreta.ejecutar();
}
