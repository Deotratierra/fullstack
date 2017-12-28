"use strict"

// ============     ALGORITMO     ==============

function selection_sort(seq) {
    // Ordena array en orden ascendente
    var seqlen = seq.length;
    for (var i=0; i<seqlen; i++) {
    	var elem = seq[i];
    	var min = i;
        var j = seqlen;
        while ( --j > i ) {
        	if (seq[j] < elem) {
        		min = j;
        		elem = seq[min];
        	}
        }
        if (min != i) {
            var temp = seq[i];
            seq[i] = seq[min];
            seq[min] = temp;
        }
    }
    return seq
}

// ============     TESTING     ==============

function is_sorted(seq) {
    var seqlen = seq.length;
    for (var i = 1; i <= seqlen; i++) {
    	if (seq[i-1] > seq[i]) { return false; }
    }
    return true;
}

// ============================================

if (require.main == module) {
    var lista = [22, 2, 44, 4];
    console.log("Array desordenado:")
    console.log(lista);

    var lista_ordenada = selection_sort(lista);
    if (is_sorted(lista_ordenada)) {
    	console.log("Array ordenado")
    	console.log(lista_ordenada)
    }
}
