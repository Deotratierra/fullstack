"use strict";

import {info} from "./utils/printers";
info("Inicializando la aplicación...");

import start_app from "./app";


if (require.main == module){
	// Ponemos al servidor en escucha
	start_app();
}
