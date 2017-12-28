"use strict"

class Contexto {
    // Mantiene una instancia de una subclase
    // EstadoConcreto que define el estado actual
    constructor(estado) {
        this.estado = estado
    }

    peticion() {
        this.estado.manejar();
    }
}

class Estado {
    // Interfaz para encapsular el comportamiento
	// asociado a un estado particular del contexto
	constructor() {
        if (this.constructor === Estado) {
            var msg = "La clase asbtracta Estado " +
                "no puede ser instanciada directamente."
            throw new TypeError(msg);
        }
              // Método abstracto
        if (this.manejar === undefined) {
            var msg = "Debes declarar el método" +
                + "manejar() en" + this.constructor.name;
            throw new TypeError(msg);
        }
	}
}

class EstadoConcretoA extends Estado {
    manejar() {
        console.log("Manejador de " + this.constructor.name);
    }
}

class EstadoConcretoB extends Estado {
    manejar() {
        console.log("Manejador de " + this.constructor.name);
    }
}

if (require.main == module) {
    var estado_concreto_A = new EstadoConcretoA();
    var contexto = new Contexto(estado_concreto_A);
    contexto.peticion();
}