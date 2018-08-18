"use strict"

var mysql = require('mysql');  // npm install mysql

var USER = "root",
    PASSWORD = "",
    HOST = "localhost",
    PORT = 3306,
    DATABASE_NAME = "";

var conn = mysql.createConnection({
  host: HOST,
  port: PORT,
  user: USER,
  password: PASSWORD,
  database: DATABASE_NAME
});

conn.connect(function(err) {
  if (err) throw err;
  console.log("Connected!");
});

/* Fuente:
 * https://www.w3schools.com/nodejs/nodejs_mysql.asp
 */
