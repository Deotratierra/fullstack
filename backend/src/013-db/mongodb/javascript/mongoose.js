"use strict"

var mongoose = require('mongoose'); // npm install mongoose

var USER = "",
    PASSWORD = "",
    HOST = "",
    PORT = "",
    DATABASE_NAME = "";

var URI = "mongodb://" + USER + ":" + PASSWORD + "@" + HOST + ":" + PORT + "/" + DATABASE_NAME;

// Conexión con la base de datos
mongoose.connect(URI);
