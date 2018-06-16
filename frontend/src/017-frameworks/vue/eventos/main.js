const vm = new Vue({
    el: "main",
    data: {
        newTask: null,
        tasks: [
            "Jugar al fútbol",
            "Estudiar matemáticas",
            "Realizar un tutorial"
        ]
    },
    methods: {
        addTask() {
            this.tasks.push(this.newTask);
            this.newTask = null;
        }
    }
})