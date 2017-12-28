"use strict"

// Reemplaza Singleton por tu clase

class Singleton {
    constructor() {
        if (!Singleton.instance) {
            Singleton.instance = this;
        }
        return Singleton.instance;
    }
}

if (require.main == module) {
    var instance1 = new Singleton();
    var instance2 = new Singleton();
    console.log( "Same instance? " +
    	(instance1 === instance2) );
}