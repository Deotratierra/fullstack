
/*                social-menu
  Renderiza un menú con botones sociales.

  Dependencias: 'font-awesome'.

  Por defecto los iconos están cada uno con su color
  y cuando el ratón es pasado por encima disminuye
  su opacidad. Este preestilo se llama 'hoverOpacity'.
  Debes pasar un preestilo en la propiedad 'prestyle'
  desde la instancia del componente (en el HTML).

  Expone la clase 'social-menu--icon' para todos los
  iconos en el menú.

  @param {string} containerId Indica el identificador
    del elemento raíz del componente (ul).
  @param {string, optional} prestyle Indica el preestilo
    que usará el componente. Este es opcional y define
    qué color tendrán los iconos por defecto así como el
    color que tomarán cuando se dispare un evento 'hover'
    sobre cada uno.
    Existen 2 preestilos definidos:
      - 'hoverOpacity' (por defecto): Otorga a cada icono
        su color, tal como está definido en 'menuData',
        y baja la opacidad del icono cuando se dispara 'hover'.
      - 'hoverColor': Los iconos en negro y se vuelven del
        color definido en 'menuData' cuando se dispara 'hover'.

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
        buildIconId(slug, containerId) {
        	return slug + "-icon" + "__" + containerId;
        },
        getSocialIcon(slug, containerId, sourceColor) {
            var icons = document.getElementsByClassName("social-menu--icon");
            for (var i=0; i < icons.length; i++) {
                if (icons[i].id == this.buildIconId(slug, containerId)) {
                    if (sourceColor) {
                        this.sourceIconsColor = sourceColor;
                    }
                    return icons[i];
                }
            }

        },
        socialIconOpacityOnMouseOver(slug, containerId) {
            this.getSocialIcon(slug, containerId).style.opacity = 0.7;
        },
        socialIconOpacityOnMouseOut(slug, containerId, sourceColor) {
            this.getSocialIcon(slug, containerId, sourceColor).style.opacity = 1;
        },
        socialIconColorOnMouseOver(slug, containerId, color) {
            this.getSocialIcon(slug, containerId).style.color = color;
        },
        socialIconColorOnMouseOut(slug, containerId) {
            this.getSocialIcon(slug, containerId, "#000").style.color = this.sourceIconsColor;
        }
    },
    props: ["containerId", "prestyle"],
    computed: {
        _prestyle() {
            if (this.prestyle === undefined) {
                 return "hoverOpacity";
            }
            return this.prestyle;
        }
    },
    template: `
        <ul :id="containerId">
          <li v-for="entry in menuData">
            <a :href="entry.href">
              <i v-if="_prestyle == 'hoverOpacity'"
                 :style="buildInlineStyle(entry.color) + ';'"
                 :class="buildIconFaClass(entry.slug) + ' social-menu--icon'"
                 :id="buildIconId(entry.slug, containerId)"
                 @mouseover="socialIconOpacityOnMouseOver(entry.slug, containerId)"
                 @mouseout="socialIconOpacityOnMouseOut(entry.slug, containerId, entry.color)">
              </i>
              <i v-if="_prestyle == 'hoverColor'"
                 :style="buildInlineStyle('#000')+ ';'"
                 :class="buildIconFaClass(entry.slug) + ' social-menu--icon'"
                 :id="buildIconId(entry.slug, containerId)"
                 @mouseover="socialIconColorOnMouseOver(entry.slug, containerId, entry.color);"
                 @mouseout="socialIconColorOnMouseOut(entry.slug, containerId)">
              </i>
            </a>
          </li>
        </ul>
    `
});

/*               main-menu

  Dependencias: 'vue-i18n'.

  Este componente crea un menú de navegación básico.
  Cada entrada del menu (li>a) contiene la clase
  'main-menu--item' y después de todas las entradas (li)
  existe un icono 'fa-bars' el cual actúa como toggle
  entre el menú reducido formato móvil y el extendido.
  Puedes usar las media queries para alternar entre la
  aparición de este botón y el menú (ver ejemplos).

  @param {string} containerId Indica el identificador
    del elemento raíz del componente (ul).
*/
const mainMenu = Vue.component("main-menu", {
    data() {
        return {
            menuData: [
                {slug: "home",    href: "#"},
                {slug: "contact", href: "#"},
                {slug: "blog",    href: "#"},
                {slug: "login",   href: "#"}
            ],
        }
    },
    props: ["containerId", "secondaryMenu"],
    methods: {
        showSecondaryMenu() {
            var toggle = {
            	"inline-block": "none",
                "":             "inline-block",
                "none":         "inline-block"
            };
            elem = document.querySelector("#main-menu--secondary");
            elem.style.display = toggle[elem.style.display];
        }
    },
    computed: {
        includeSecondaryMenu() {
            if (this.secondaryMenu == true) {
                return true;
            }
            return false;
        }
    },
    template: `
        <div :id="containerId">
          <ul id="main-menu">
            <li v-for="entry in menuData">
              <a :href="entry.href" class="main-menu--item">
                {{ $t("mainMenu." + entry.slug) }}
              </a>
            </li>
            <i v-if="includeSecondaryMenu"
               @click="showSecondaryMenu"
               class="fa fa-bars"
               id="main-menu--toggle">
            </i>
          </ul>
          <ul v-if="includeSecondaryMenu" id="main-menu--secondary">
            <li v-for="entry in menuData">
              <a :href="entry.href"
                 class="main-menu--secondary-item">
                {{ $t("mainMenu." + entry.slug) }}
              </a>
            </li>
          </ul>
        </div>
    `,
});

/*                     date-info

  Dependencias: 'vue-i18n'.

  Renderiza la fecha actual según la localización
  definida (ver 'lang-selector').

  @param {string} containerId Indica el identificador
    del elemento raíz del componente (span).

*/
const dateInfo = Vue.component("date-info", {
    props: ["containerId"],
    template: `
        <span :id="containerId" class="date-info">
            {{ $d(new Date(), 'short') }}
        </span>
    `
})

const dateTimeFormats = {
    'es-ES': {
        short: { year: 'numeric', month: 'short', day: 'numeric' },
        long: {
            year: 'numeric', month: 'short', day: 'numeric',
            weekday: 'short', hour: 'numeric', minute: 'numeric', hour12: true
        }
    },
    'en-US': {
        short: { year: 'numeric', month: 'short', day: 'numeric' },
        long: {
            year: 'numeric', month: 'short', day: 'numeric',
            weekday: 'short', hour: 'numeric', minute: 'numeric'
        }
    },
    'fr-FR': {
        short: { year: 'numeric', month: 'short', day: 'numeric' },
        long: {
            year: 'numeric', month: 'short', day: 'numeric',
            weekday: 'short', hour: 'numeric', minute: 'numeric'
        }
    },
    'ru-RU': {
        short: { year: 'numeric', month: 'short', day: 'numeric' },
        long: {
            year: 'numeric', month: 'short', day: 'numeric',
            weekday: 'short', hour: 'numeric', minute: 'numeric'
        }
    },
}


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
    messages: translations,
    dateTimeFormats
})

/*                     lang-selector

  Dependencias: 'vue-i18n', 'flag-icon'.

  Crea un selector de lenguaje mediante un elemento 'select'
  conectado a la configuración de localización para el usuario.
  Todos los mensajes traducidos desplegados en la página
  cambian dinámicamente al seleccionar otro color, sin necesidad
  de renderizar la página.

  @param {string} containerId Indica el identificador
    del elemento raíz del componente (select).

 */
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
