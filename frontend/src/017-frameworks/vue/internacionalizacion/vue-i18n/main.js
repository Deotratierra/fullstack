// =========================================================

//                       Uso básico
//                       ~~~~~~~~~~

// Mensajes ya traducidos dependiendo de su localización
const messages = {
  "en-US": {
    message: {
      hello: "Hello world",
      // Paso de parámetros individuales
      helloparam: "{msg} world",
      // Paso de listas (parámetros capturados por índices)
      hellolistparam: "{0} world"
    },
    // Pluralización
    car: "car | cars",
    apple: "no apples | one apple | {count} apples",
  },
  "es-ES": {
    message: {
      hello: "Hola mundo",
      helloparam: "{msg} mundo",
      hellolist: "{0} mundo",
    },
    car: "coche | coches",
    apple: "ninguna manzana | una manzana | {count} manzanas",
  }
  //
}

// ------------------------------------------------------------

// Localización de fechas
const dateTimeFormats = {
  'en-US': {
    short: {
      year: 'numeric', month: 'short', day: 'numeric'
    },
    long: {
      year: 'numeric', month: 'short', day: 'numeric',
      weekday: 'short', hour: 'numeric', minute: 'numeric'
    }
  },
  'es-ES': {
    short: {
      day: 'numeric', month: 'long', year: 'numeric'
    },
    long: {
      day: 'numeric', month: 'long', year: 'numeric', era: "long",
      weekday: 'long', hour: 'numeric', minute: 'numeric'
    }
  }
}            /*
      Propiedad        Posibles valores
      ~~~~~~~~~        ~~~~~~~~~~~~~~~~
        weekday        "narrow", "short", "long"
            era        "narrow", "short", "long"
           year        "2-digit", "numeric"
          month        "2-digit", "numeric", "narrow", "short", "long"
            day        "2-digit", "numeric"
           hour        "2-digit", "numeric"
         minute        "2-digit", "numeric"
         second        "2-digit", "numeric"
   timeZoneName        "short", "long"
*/

// ------------------------------------------------------------

// Creamos una instancia 'VueI18n'
const i18n = new VueI18n({
  locale: 'es-ES', // Establecemos la localización
  messages,     // y le pasamos los mensajes
  dateTimeFormats,
})


// Creamos instancia de Vue con las opciones de localización
new Vue({ i18n }).$mount('#app');

