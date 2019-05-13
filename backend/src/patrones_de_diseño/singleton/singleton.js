"use strict"

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
    console.log( "¿Es la misma instancia? " +
    	(instance1 === instance2) );
}