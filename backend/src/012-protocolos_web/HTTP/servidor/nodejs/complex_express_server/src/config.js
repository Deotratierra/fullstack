
// =========   GLOBAL CONFIGURATION   ========

const global_config = {
	ROOT_DIR: __dirname
};

// ======   ENVIRONMENT CONFIGURATION   ======

const development = {
	server: {
		HOST: "localhost",
		PORT: process.env.SERVER_PORT
	}
};

const stage = {
	server: {
		HOST: "0.0.0.0",
		PORT: process.env.SERVER_PORT
	}
};

const production = {
    server: {
		HOST: "0.0.0.0",
		PORT: process.env.SERVER_PORT
	}
};

// ===========================================

// Seleccionamos la configuración según la variable 
// de entorno NODE_ENV  ("development", "stage", "production")
// y añadimos la configuración global a la de entorno
const config = Object.assign( {}, eval(process.env.NODE_ENV), global_config );

module.exports = {config};