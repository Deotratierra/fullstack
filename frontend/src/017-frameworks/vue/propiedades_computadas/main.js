const vm = new Vue({
    el: "main",
    data: {
        message: "hola",
        numbers: [3, 6, 4, 3, 9, 5, 7]
    },
    methods: {
         evenNumbersMethod() {
             return this.numbers.filter(function(number){
                return number % 2 == 0;
            });
         }
    },
    computed: {
        messageReverse() {
            return this.message.split("").reverse().join("");
        },
        evenNumbers() {
            return this.numbers.filter(function(number){
                return number % 2 == 0;
            });
        }
    }
});