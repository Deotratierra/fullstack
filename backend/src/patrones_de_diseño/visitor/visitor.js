"use strict"

// Demostración del patrón visitor en Javascript

class NoModificable {};

// La superclase de flor no puede ser modificada
class Flor extends NoModificable {
    aceptar(visitante) {
        visitante.visitar(this);
    }
    polinizar(polinizador) {
        console.log(this, "polinizado por", polinizador)
    }
    depredar(depredador) {
        console.log(this, "depredado por", depredador)
    }
    inspect() {
    	return this.constructor.name;
    }
}
//Flor.prototype.inspect = function(){
//	return this.constructor.name;
//}

class Gladiolo extends Flor{}
class Tulipan extends Flor{}
class Crisantemo extends Flor{}

class Visitante {
    inspect() {
        return this.constructor.name;
    }
}

class Insecto extends Visitante {}
class Polinizador extends Insecto {}
class Depredador extends Insecto {}

class Abeja extends Polinizador {
    visitar(flor) {
        flor.polinizar(this);
    }
}
class Mosquito extends Polinizador {
    visitar(flor) {
        flor.polinizar(this);
    }
}
class Gusano extends Depredador {
    visitar(flor) {
        flor.depredar(this);
    }
}

function randomChoice(choices) {
    var index = Math.floor(Math.random() * choices.length);
    return choices[index];
}

function flowerGen(n) {
    var response = [];
    var flores = [Gladiolo, Tulipan, Crisantemo];
    for (var i=1; i<=n; i++){
        var flor = randomChoice(flores);
        response.push(new flor);
    }
    return response
}


var abeja = new Abeja();
var mosquito = new Mosquito();
var gusano = new Gusano();

var flores = flowerGen(10);
for (var i=0; i<flores.length; i++){
    flores[i].aceptar(abeja);
    flores[i].aceptar(mosquito);
    flores[i].aceptar(gusano);
}
