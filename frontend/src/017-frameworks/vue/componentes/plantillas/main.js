Vue.component("select-winner", {
    props: ["listing"],

    // Dentro de esta propiedad podemos especificar un identificador
    // de elemento para indicar donde se encuentra nuestra plantilla
    // o embeberla directamente en una cadena como es el caso.
    template: `
        <div>
            <h1 v-if="winner">El ganador es {{ winner }}</h1>
            <template v-else>
                <h1>Participantes</h1>
                <ul>
                    <li v-for="person in listing"> {{ person }} </li>
                </ul>
            </template>
            <button @click="selectWinner">Elegir ganador</button>
        </div>
    `,
    methods: {
        selectWinner() {
            let nParticipants = this.participants.length;
            let index = Math.floor(Math.random()*nParticipants);
            this.winner = this.participants[index-1];
        }
    },
    data() {
        return {
             winner: false,
             participants: this.listing
        }
    }
});

const vm = new Vue({
    el: "main",
    data: {
        persons: ["Juan", "Alicia", "Pedro", "Javier", "Marcos"]
    }
})