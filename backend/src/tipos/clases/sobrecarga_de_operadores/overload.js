"use strict"

class Pareja {
    constructor(n1, n2){
        this.n1 = n1, this.n2 = n2;
    };

    // Sobrecarga de salida como cadena
    inspect() {
        return this.constructor.name + "(" + this.n1 + ", " + this.n2 + ")"; 
    }
};

// Sobrecarga de salida como cadena
// para objetos inicializados
Pareja.prototype.inspect = function(){
    return this.constructor.name + "(" + this.n1 + ", " + this.n2 + ")"; 
}


var pareja1 = new Pareja(3, 5);
console.log(pareja1);  // Pareja(3, 5)
