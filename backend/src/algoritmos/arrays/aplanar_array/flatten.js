"use strict"

var a = ["elem1"],
    b = [2, 1, [3, [4, 5], 6], 7, [8]];

var flatten = function(l, source){
    if ( !source || !(source instanceof Array) ){ source = [] }
    for (var i = 0; i < l.length; i++){
        if (l[i] instanceof Array){ 
			flatten(l[i], source) 
		}
        else { source.push(l[i]) };
    };
    return source;
};

console.log( flatten(b, a) );
