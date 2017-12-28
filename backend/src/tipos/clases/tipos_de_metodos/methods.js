"use strict"

class Base {}  // Clase abstracta
    constructor() {
        if (this.constructor === Base) {
            var msg = "La clase asbtracta Base " +
                "no puede ser instanciada directamente."
            throw new TypeError(msg);
        }
              // Método abstracto
        if (this.metodo_abstracto === undefined) {
            var msg = "Debes declarar el método" +
                + "methodo_abstracto() en" + this.constructor.name;
            throw new TypeError(msg);
        }
    }
;

class Ejemplo extends Base {

	// Constructor
	constructor(atributo) {
		this.atributo = atributo;
	}

	normal() {
		console.log("\nSoy un método normal");
		console.log(this);
	}

	// Getter
	get atributo() {
		return this._atributo;
	}

	// Setter
	set atributo(value){
		if (value.length < 4) {
			console.log("Atributo muy corto");
			return
		}
		this._atributo = value;
	}

	// Estático
	static estatico() {
		console.log("\nSoy un método estático");
		console.log("Debes llamarme desde la clase");
		console.log("En Python me llamarías método de clase");
	}

	metodo_abstracto(){
		console.log("Mira en la clase padre.")
		console.log("Cámbiame el nombre en Ejemplo y verás lo que pasa.")
	}

}

// Instanciar
var ej = new Ejemplo("a");   // Atributo muy corto

var ej = new Ejemplo("Soy un atributo");

// Inspeccionar clase   -->  [ 'constructor', 'normal', ... ]
console.log(Object.getOwnPropertyNames(Ejemplo.prototype));

// Acceso a atributos
console.log(ej.atributo);  // Soy un atributo

// Método normal
ej.normal();  // Soy un método normal

// Método estático
Ejemplo.estatico();  // Soy un método estático
                     // Debes llamarme desde la clase
                     // En Python me llamarías método de clase

// Ḿétodo abstracto
ej.metodo_abstracto() // Mira en la clase padre.
                      // Cámbiame el nombre en Ejemplo y verás lo que pasa.