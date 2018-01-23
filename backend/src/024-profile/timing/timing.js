"use strict"

// ================================================

function fn_timer(func, miliseconds=false) {
    return function(x) {
        var t1 = new Date().getTime();
        var response = func(x);
        var t2 = new Date().getTime();
        console.log(t1, t2);
        var unit_time = "miliseconds",
            time_elapsed = t2 - t1;
        if (miliseconds == false){
            unit_time = "seconds";
            time_elapsed /= 1000;
        }
        console.log("Total time running " + func.name + "(): "
                    + time_elapsed + " " + unit_time);
        return response;
    };
};

// ===============================================

var slow_function = function(){
	var response = [];
	var nums_list = Array.apply(null, Array(10000)).map(function (_, i) {return i;});
	for (var i = nums_list.length - 1; i >= 0; i--) {
		response.push(nums_list[i]);
	};
	return response
	
};

// Le pasamos una función
slow_function = fn_timer(slow_function, false);
var res = slow_function();

/* Como usar:
 * Si tenemos una funcion que se llama slow()
 * slow = fn_timer(slow);
 * slow()
 */


// Fuente:
// https://javascript.info/call-apply-decorators
