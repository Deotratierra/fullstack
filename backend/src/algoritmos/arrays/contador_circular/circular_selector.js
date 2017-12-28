"use strict"

var a = ['1','2','3','4','5','6','7','8','9']

var circular_selector = function(int_list, skip){
    skip = skip - 1;
    var idx = 0, response = [];
    var len_list = int_list.length;
    while (len_list > 0){
        idx = (skip + idx) % len_list;
        response.push(int_list[idx]);
        int_list.splice(idx, 1);
        len_list -= 1;
    }
    return response
}

console.log(circular_selector(a, 3));
