
/* Renderiza un menú con botones sociales.

- Requiere de Font Awesome.

Por defecto los iconos están cada uno con su color
  y cuando el ratón es pasado por encima disminuye
  su opacidad.
*/
Vue.component("social-menu", {
    data() {
        return {
            menu: [
                {slug: "youtube", href: "#", color: "#cc181e"},
                {slug: "medium", href: "#", color: "#00aced"},
                {slug: "facebook", href: "#", color: "#3b5998"},
                {slug: "twitter", href: "#", color: "#00aced"},
            ],
        }
    },
    methods: {
        buildIconFaClass(slug) {
            return "fa fa-" + slug;
        },
        buildInlineStyle(color) {
            return "color:" + color;
        },
        buildIconId(slug) {
            return slug + "-icon";
        },
        getSocialIconBySlug(slug) {
            return document.getElementById(slug + "-icon");
        },
        socialIconOnMouseOver(slug) {
            this.getSocialIconBySlug(slug).style.opacity = 0.7;
        },
        socialIconOnMouseOut(slug) {
            this.getSocialIconBySlug(slug).style.opacity = 1;
        }
    },
    props: ["containerId"],
    template: `
        <ul :id="containerId">
          <li v-for="entry in menu">
            <a :href="entry.href">
              <i :style="buildInlineStyle(entry.color)"
                 :class="buildIconFaClass(entry.slug)"
                 :id="buildIconId(entry.slug)"
                 @mouseover="socialIconOnMouseOver(entry.slug)"
                 @mouseout="socialIconOnMouseOut(entry.slug)">
              </i>
            </a>
          </li>
        </ul>
    `

})

/* Menu principal */
Vue.component("main-menu", {
    data() {
        return {
            menu: [
                {title: "Home",    href: "#"},
                {title: "Contact", href: "#"},
                {title: "Blog",    href: "#"},
                {title: "Login",   href: "#"}
            ]
        }
    },
    props: ["containerId"],  // Esta propiedad es para pasar el estilo
                             //   de cada instancia de menú
    template: `
        <ul :id="containerId">
          <li v-for="entry in menu">
            <a :href="entry.href" class="menu-item">
              {{ entry.title }}
            </a>
          </li>
        </ul>
    `
})


vm = new Vue({
    el: "header-1",
})

