import express from "express";
import path from "path";
import walk from "walk";

import { config } from "./config";
import { success } from "./utils/printers";

const app = express();

// ========  Variables globales / configuración  ========

app.set("ROOT_DIR", config.ROOT_DIR);

// ========================================


// ========  Archivos estáticos globales  ========

app.use( "/static", express.static( path.join(__dirname, "assets", "static") ) );

// ===============================================



// ========   ROUTER   ========

app.use(require("./router"));

// ============================


// ========================================================

// Servir directorios de archivos estáticos 
// de los componentes y las escenas
const ignore_folders = ["templates", "components", "admin"];

// En el primer nivel del directorio templates no habrá
// lo mismo que en el caso de las carpetas components
// Los archivos HTML se sirven directamente desde los routers.

const options = {
    listeners: {
        directory: (root, dirStats, next) => {
            if ( ignore_folders.indexOf(dirStats.name) < 0) {
                let endpoint = path.join( root.split("scenes")[1], dirStats.name );
                let folder = path.join( root, dirStats.name );
                // Servimos los directorios
                app.use( endpoint, express.static(folder) );
            }
            next();
         }
    }
};

const walker = walk.walkSync( path.join(__dirname, "scenes"), options );

// =======================================================


// ===========   CONFIGURACIÓN DE PRODUCCIÓN   ===========

// No mostrar los errores del servidor al usuario
if (app.get("env") != "development"){
    app.use( (err, req, res, next) => {
        res.status(err.status || 500);
        res.render("error", {
            message: err.message,
            error: {}
        });
    });
}

// =======================================================

// Función para comenzar la aplicación
export default function start_app(){
    const server = app.listen(config.server.PORT, config.server.HOST, () => {
        success("App listening at " + config.server.HOST + ":" + config.server.PORT);
    });
}
