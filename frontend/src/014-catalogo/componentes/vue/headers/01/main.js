Vue.component("header-01", {
    template: `
      <header id="header-01">
        <div id="header-01--container">
          <a href="#">
            <img src="img/logo.png" id="header-01--logo"></img>
          </a>

          <social-menu
           prestyle="hoverOpacity"
           containerId="header-01--social"
          >
          </social-menu>
          <lang-selector containerId="header-01--lang-selector">
            <pre>{{ $data }}</pre>
          </lang-selector>

          <main-menu containerId="header-01--menu"
                     :secondaryMenu="true">
          </main-menu>
          </ul>
        </div>
      </header>
    `
});