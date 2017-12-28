"use strict"

// En javascript, al comparar dos arrays con los
// mismos valores, no obtenemos true.

//console.log([1, 2, 3] == [1, 2, 3])

// Por ello, creamos la siguiente función
// para compararlos

Array.prototype.compare = function(testArr) {
    if (this.length != testArr.length) return false;
    for (var i = 0; i < testArr.length; i++) {
        if (this[i].compare) { //To test values in nested arrays
            if (!this[i].compare(testArr[i])) return false;
        }
        else if (this[i] !== testArr[i]) return false;
    }
    return true;
}

//console.log([1, 2, 3].compare([1, 2, 3]));

// =========================================================


var garage = function(initial, end){
    var steps = 0,
        len_initial = initial.length;
    while ( !initial.compare(end) ){
        var zero = initial.indexOf(0);
        if (zero != end.indexOf(0)){
            var car_to_move = end[zero];
            var pos = initial.indexOf(car_to_move);
            [initial[zero], initial[pos]] = [initial[pos], initial[zero]];
        } else {
            for (var i = 0; i < len_initial; i++){
                if (initial[i] != end[i]){
                    [initial[zero], initial[i]] = [initial[i], initial[zero]];
                    break
                }
            }
        }
        steps += 1
        //console.log(initial);
    }
    return steps
}

if (require.main == module){
    var initial = [1, 2, 3, 0, 4],
        end =   [0, 3, 2, 1, 4];
    console.log("initial:", initial)
    console.log("final:", end)
    console.log(garage(initial, end))
}


/* Fuentes:
https://stackoverflow.com/questions/6229197/how-to-know-if-two-arrays-have-the-same-values
https://docs.onux.com/en-US/Developers/JavaScript-PP/Language/Reference/Modifiers/final
*/