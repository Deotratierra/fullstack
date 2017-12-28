"use strict"

var bubble_sort = function(array) {
    var n = array.length,
        intercambiado = true,
        temp;
    while (intercambiado) {
        intercambiado = false;
        for (var i = 1; i < n; i++) {
            //console.log(array[i - 1])
            if (array[i - 1] > array[i]) {
                temp = array[i - 1];
                array[i - 1] = array[i];
                array[i] = temp;
                intercambiado = true;
            }
        }
    }
}

if (require.main == module){
    var array = [1, 5, 65, 23, 57, 1232, -1, -5, -2, 242, 100,
                 4, 423, 2, 564, 9, 0, 10, 43, 64, 32, 1, 999]
    console.log(array.toString());
    bubble_sort(array)
    console.log(array.toString())
}