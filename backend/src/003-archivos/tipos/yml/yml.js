
var yaml = require("js-yaml"),  // npm install js-yaml
    fs = require("fs");

// Insertar datos en un archivo .yml

data = {
    primero: 1,
    segundo: {hola: "adios"}
}

data = yaml.dump(data);
fs.writeFileSync("data.yml", data, "utf8");

// ============================================

// Leer datos de un archivo .yml

try {
  var data = yaml.safeLoad(fs.readFileSync("fichero.yml", "utf8"));
  console.log(data);
} catch (e) {
  console.error(e);
};

/* Fuentes:
 * https://www.npmjs.com/package/js-yaml
 * https://github.com/nodeca/js-yaml/tree/master/examples
 */
