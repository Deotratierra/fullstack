
var num1 = 4511, num2 = 369301;

var digits_sum = function(number){
    var response = "", total = 0;
    var rest;
    while (number != 0){
        rest = number % 10;
        response += rest.toString();
        total += rest;
        number = parseInt(number / 10); // Redondeo a int
        if (number > 0){ response += " + "; }
    }
    response += " = " + total.toString();
    return response;
};

console.log(digits_sum(num1));
console.log(digits_sum(num2));

