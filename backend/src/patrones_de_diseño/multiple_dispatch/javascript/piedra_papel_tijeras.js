"use strict"

class Outcome {
	constructor(value, name){
		this.value = value
		this.name = name
	}

	toString(){
		return this.name;
	}

	static WIN(){ return new Outcome(0, "win") };
	static LOSE(){ return new Outcome(1, "lose") };
    static DRAW(){ return new Outcome(2, "win") };

}

Outcome.WIN = Outcome.WIN();
Outcome.LOSE = Outcome.LOSE();
Outcome.DRAW = Outcome.DRAW();


class Item {
	toString(){
		return this.constructor.name;
	}
};

class Paper extends Item {
	compete(item){ return item.evalPaper(); };
	evalPaper(item){ return Outcome.DRAW; };
	evalScissors(item){ return Outcome.WIN; };
	evalRock(item){ return Outcome.LOSE; };
}

class Scissors extends Item {
	compete(item) { return item.evalScissors(); };
	evalPaper(item) { return Outcome.LOSE; };
	evalScissors(item) { return Outcome.DRAW; };
	evalRock(item) { return Outcome.WIN };
}

class Rock extends Item {
	compete(item) { return item.evalRock(); };
	evalPaper(item) { return Outcome.WIN; };
	evalScissors(item) { return Outcome.LOSE; };
	evalRock(item) { return Outcome.DRAW; };
}



function match(item1, item2) { 
	var ready = item1 + " <--> " + item2 + " : ";
	console.log(ready + item1.compete(item2));
}

// Función para obtener un elemento al azar de un array
Array.prototype.sample = function() {
    return this[Math.floor(Math.random() * this.length)]
}

function itemPairGen(n) {
	var items = [Paper, Scissors, Rock], // Hardcoded :(
	    response = new Array;
	for (var i = 0; i < n; i++) {
		response.push([ items.sample(),
			            items.sample() ]
			          );
	};
	return response
};


/*
var matchs = itemPairGen(20);

console.log(matchs);

var item1 = matchs[0], item2 = matchs[1];

console.log(item1);
*/


for (var i = 0, matchs = itemPairGen(20); 
	     i < matchs.length; i++) {
    var item1 = matchs[i][0], item2 = matchs[i][1];
    //console.log(new item1);
    match(new item1, new item2);
};


