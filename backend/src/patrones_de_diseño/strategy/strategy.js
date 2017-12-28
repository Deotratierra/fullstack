"use strict"

class Contexto {
    constructor(estrategia) {
        this._estrategia = estrategia;
    }
    ejecutar() {
        this._estrategia.algoritmo();
    }
}

class Estrategia {
    constructor() {
        // Construimos una clase base abstracta
        // con un método abstracto
        if (this.constructor === Estrategia) {
            var msg = "Abstract class Estrategia " +
                "cannot be instantiated directly."
            throw new TypeError(msg);
        }

        if (this.algoritmo === undefined) {
            var msg = "You must declare algoritmo() "
                + "method in" + this.constructor.name;
            throw new TypeError(msg);
        }
    }
}

class EstrategiaConcretaA extends Estrategia {
    algoritmo() {  // Cambia el nombre y no funciona
        console.log("Algoritmo de", this.constructor.name);
    }
}

class EstrategiaConcretaB extends Estrategia {
    algoritmo() {
    	console.log("Algoritmo de", this.constructor.name);
    }
}

if (require.main == module) {
    var estrategia_concreta_A = new EstrategiaConcretaA();
    var contexto = new Contexto(estrategia_concreta_A)
    contexto.ejecutar();
}
