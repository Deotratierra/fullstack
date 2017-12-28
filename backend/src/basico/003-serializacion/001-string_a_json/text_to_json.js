
var texto = '{"hola": "que tal"}'
console.log(typeof(texto));  //  string

var response = JSON.parse(texto); // <---- ¡Igual que en Ruby!
console.log(typeof(response));  //  object

console.log(response.hola);  //  que tal
