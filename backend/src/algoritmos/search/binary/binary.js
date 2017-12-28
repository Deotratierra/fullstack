"use strict"

function binary_search(array, query){
    var lo = 0, hi = array.length - 1;
    while (lo <= hi){
        var mid = parseInt(lo + (hi - lo) / 2);
        var val = array[mid];
        if (val == query) {
            return mid;
        } else if (val < query){
            lo = mid + 1;
        } else {
        	hi = mid - 1;
        }
    }
    return null;
}


function main() {
    var array = [1, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 6]
    console.log(array)
    console.log("Encontrado", 5, "en el índice:", binary_search(array, 5))
    console.log("Encontrado", -1, "en el índice:", binary_search(array, -1))
}


if (require.main == module){
    main()
}