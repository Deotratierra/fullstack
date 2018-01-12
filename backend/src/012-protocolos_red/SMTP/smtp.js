"use strict"

var SENDER = process.env.EMAIL_SENDER,
    PASSWORD = process.env.EMAIL_PASSWORD,
    RECEIVERS = [],
    SUBJECT = "Email de prueba",
    MESSAGE = "Esto es un email de prueba usando la biblioteca ";

// ---   OPCIÓN 1   --- emailjs
// https://github.com/eleith/emailjs

var emailjs = require("emailjs");  // npm install emailjs

var send_emailjs = function(sender, password, receivers, subject, message,
                            host="smtp.gmail.com", ssl=true) {
    var server     = emailjs.server.connect({
       user:    sender, 
       password: password, 
       host:    host, 
       ssl:     ssl
    });

    var _receivers = ""
    for (var i = 0; i < receivers.length; i++) {
        _receivers += receivers[i];
        if (i + 1 < receivers.lenght){
            _receivers += ",";
        }
        _receivers += " ";
        
    };

    // Envía el correo y obtiene un callback con un error con detalles del mensaje enviado
    server.send({
       text:    message, 
       from:    sender, 
       to:      _receivers,
       cc:      sender,
       subject: subject
    }, function(error, message) { 
        if (error) {
            console.error("Error enviando un mail con emailjs: " + error);
        } else {
            console.log("Email enviado correctamente con emailjs");
        }
    });
        
};

if (require.main == module){
    send_emailjs(SENDER, PASSWORD, RECEIVERS, SUBJECT, MESSAGE + "emailjs");
};
