/* Podemos cambiar las propiedades del modelo desde la consola.
    Por ejemplo, en este caso podemos ejecutar 'logged = true'
    y el campo 'logged' del modelo cambiaría. */

const vm = new Vue({
    el: "main",
    data: {
        logged: false,
        age: 30,
    }
});