Vue.component("button-counter", {
    data: function(){   // La propiedad 'data' de un componente debe ser una función en
        return {        //   lugar de un objeto como lo es en las instancias de Vue.
            count: 0
        }
    },
    template: '<button @click="count++">Me has dado click {{ count }} veces.</button>'
});

/* Las plantillas de los componentes deben partir de un elemento
    HTML raíz, por lo que si tienes varios elementos en un componente
    debes encapsularlos en un contenedor.
*/
Vue.component("blog-post", {
    props: ["title"],
    template: `
      <div class="post">
        <h3>{{ title }}</h3>
        <p>Blablabla... soy un párrafo largo.</p>
      </div>
    `
});

const vm = new Vue({
	el: "#app",
    data: {
        customTitle: "Soy un título y vengo desde el modelo"
    }
});
