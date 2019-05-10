"use strict"

const main = function() {

	// Comparando caracteres con switch
    const caracter = 'C';

    switch(caracter) {
        case 'A':
            console.log("Buena nota\n");
            break;
        case 'B':
            console.log("Nota media\n");
            break;
        case 'C':  // Especificamos varios casos para el mismo código
        case 'D':
            console.log("Mala nota\n");  // Esta sería la ejecutada
            break;  // Sin este break también imprime "Muy mala nota"
        default:
            console.log("Muy mala nota\n");
    }

    return 0;
}

if (require.main == module){
    main();
}
