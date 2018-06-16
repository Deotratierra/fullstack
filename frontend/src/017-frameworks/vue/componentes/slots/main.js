Vue.component('alerta', {
    props: ['tipo', 'posicion'],
    /* Mediante los 'slots' podemos agregar editar partes de la plantilla
        sustituyendo partes del código original. Simplemente hay que crear
        elementos '<slot>' dandoles un nombre con el atributo 'name'.
       El elemento '<slot>' sin atributo 'name' correspondrá al código sin
        atributo 'slot' en el HTML.
    */
    template: `
            <section class="alerta" :class="[tipo, posicion]">
                <header class="alerta__header">
                        <slot name="header">Hola</slot>
                </header>
                <div class="alerta__contenido">
                        <slot>
                            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus dictum dui justo, at molestie orci dapibus
                            vitae.
                        </slot>
                </div>
                <footer class="alerta__footer">
                        <slot name="footer">Este es el texto del footer</slot>
                </footer>
            </section>`,
});

new Vue({
    el: 'main',
});