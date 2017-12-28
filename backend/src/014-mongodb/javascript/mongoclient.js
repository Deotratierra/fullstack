"use strict"

var MongoClient = require('mongodb').MongoClient; // npm install mongodb --save
var assert = require('assert');

var USER = "",
    PASSWORD = "",
    HOST = "",
    PORT = "",
    DATABASE_NAME = "";

var URI = "mongodb://" + USER + ":" + PASSWORD + "@" + HOST + ":" + PORT + "/" + DATABASE_NAME;
var db = MongoClient.connect(URI, function(err, db) {
  assert.equal(null, err);
  console.log("Connected correctly to server.");
  return db;
});

/*
Modelo de ruta en mlab.com:

mongodb://<dbuser>:<dbpassword>@ds119395.mlab.com:19395/<dbname>

-------------------------------------------------------

Ejemplo de conexión para la ruta anterior:

var USER = <dbuser>,
    PASSWORD = <dbpassword>,
    HOST = "ds119395.mlab.com",
    PORT = 19395,
    DATABASE_NAME = <dbname>;
*/

// ====================================================

/* Fuente:
https://docs.mongodb.com/getting-started/node/client/
*/
