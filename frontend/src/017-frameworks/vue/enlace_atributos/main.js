const vm = new Vue({
    el: "main",
    data: {
        tasks: [
            {name: "Ver una película", completed: false},
            {name: "Realizar ejercicios de matemáticas", completed: false},
            {name: "Ir a la playa", completed: false},
            {name: "Desayunar", completed: false}
        ]
    },
    methods: {
        completeTask(task) { task.completed = !task.completed; }
    },
    computed: {
        completedTasks() {
            return this.tasks.filter(function(task){
                return task.completed;
            })
        }
    }
})