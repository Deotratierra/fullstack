
/* Renderiza un menú con botones sociales.

- Requiere de Font Awesome.

Por defecto los iconos están cada uno con su color
  y cuando el ratón es pasado por encima disminuye
  su opacidad. Este preestilo se llama 'hoverOpacity'.
Debes pasar un preestilo en la propiedad 'prestyle'
  desde la instancia del componente (en el HTML).
*/
const socialMenu = Vue.component("social-menu", {
    data() {
        return {
            menuData: [
                {slug: "youtube", href: "#", color: "#cc181e"},
                {slug: "medium", href: "#", color: "#66cdaa"},
                {slug: "facebook", href: "#", color: "#3b5998"},
                {slug: "twitter", href: "#", color: "#00aced"},
                {slug: "google", href: "#", color: "#008744"}
            ],
        }
    },
    methods: {
        buildIconFaClass(slug) { return "fa fa-" + slug; },
        buildInlineStyle(color) { return "color:" + color; },
        buildIconId(slug) { return slug + "-icon"; },

        getSocialIconBySlug(slug) {
            this.sourceIconsColor = null;
            var icons = document.getElementsByClassName("social-icon");
            for (var i=0; i<icons.length; i++) {
                if (icons[i].id == this.buildIconId(slug)) {
                    this.sourceIconsColor = icons[i].style.color;
                    return icons[i];
                }
            }

        },
        socialIconOpacityOnMouseOver(slug) {
            this.getSocialIconBySlug(slug).style.opacity = 0.7;
        },
        socialIconOpacityOnMouseOut(slug) {
            this.getSocialIconBySlug(slug).style.opacity = 1;
        },
        socialIconColorOnMouseOver(slug, color) {
            this.getSocialIconBySlug(slug).style.color = color;
        },
        socialIconColorOnMouseOut(slug, color) {
            this.getSocialIconBySlug(slug).style.color = this.sourceIconsColor;
        }
    },
    props: ["containerId", "prestyle"],
    template: `
        <ul :id="containerId">
          <li v-for="entry in menuData">
            <a :href="entry.href">
              <i v-if="prestyle == 'hoverOpacity'"
                 :style="buildInlineStyle(entry.color)"
                 :class="buildIconFaClass(entry.slug) + ' social-icon'"
                 :id="buildIconId(entry.slug)"
                 @mouseover="socialIconOpacityOnMouseOver(entry.slug)"
                 @mouseout="socialIconOpacityOnMouseOut(entry.slug)">
              </i>
              <i v-if="prestyle == 'hoverColor'"
                 :style="buildInlineStyle(entry.color)"
                 :class="buildIconFaClass(entry.slug) + ' social-icon'"
                 :id="buildIconId(entry.slug)"
                 @mouseover="socialIconColorOnMouseOver(entry.slug, entry.color);"
                 @mouseout="socialIconColorOnMouseOut(entry.slug)">
              </i>
            </a>
          </li>
        </ul>
    `

})

/* Menu principal */
const mainMenu = Vue.component("main-menu", {
    data() {
        return {
            menu: [
                {slug: "home",    href: "#"},
                {slug: "contact", href: "#"},
                {slug: "blog",    href: "#"},
                {slug: "login",   href: "#"}
            ]
        }
    },
    props: ["containerId"],  // Esta propiedad define el identificador
                             //   del estilo del elemento raíz (ul) del menú
    template: `
        <ul :id="containerId">
          <li v-for="entry in menu">
            <a :href="entry.href" class="menu-item">
              {{ $t("mainMenu." + entry.slug) }}
            </a>
          </li>
          <i class="fa fa-bars" id="main-menu--toggle"></i>
        </ul>
    `,
});

const translations = {
	"es-ES": {
        mainMenu: {
            home: "Inicio",
            contact: "Contacto",
            blog: "Blog",
            login: "Entrar"
        }
    },
    "en-US": {
        mainMenu: {
            home: "Home",
            contact: "Contact",
            blog: "Blog",
            login: "Login"
        }
    },
    "fr-FR": {
        mainMenu: {
            home: "Accueil",
            contact: "Contact",
            blog: "Blog",
            login: "Entrer"
        }
    },
    "ru-RU": {
        mainMenu: {
            home: "домашний",
            contact: "контакт",
            blog: "блог",
            login: "логин"
        }
    }
}

const i18n = new VueI18n({
    locale: "es-ES",
    messages: translations
})

const langSelector = Vue.component("lang-selector", {
    data() {
        return {
             current: "es-ES",
             langs: Object.keys(translations),
        }
    },
    props: ["containerId"],
    methods: {
        buildOptionId(lang) { return "option-" + lang; },
        changeLang() {
            let select = document.getElementById(this.containerId);
            this.current = this.langs[select.options.selectedIndex];
            i18n.locale = this.current;
        }
    },
    template: `
        <select :id="containerId"
            @change="changeLang();">
          <option :value="index+1"
            v-for="(lang, index) in langs"
            :id="'option-' + lang">
            {{ lang.split("-")[1] }}
          </option>
        </select>
    `
});


const vm = new Vue({ i18n }).$mount('main');

