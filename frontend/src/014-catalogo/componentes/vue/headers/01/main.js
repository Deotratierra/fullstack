Vue.component("header-1", {
    template: `
      <header id="header-1">
        <div id="header-1--container">
          <a href="#">
            <img src="img/logo.png" id="header-1--logo"></img>
          </a>

          <social-menu
           prestyle="hoverOpacity"
           containerId="header-1--social"
          >
          </social-menu>
          <lang-selector containerId="header-1--lang-selector">
            <pre>{{ $data }}</pre>
          </lang-selector>

          <main-menu containerId="header-1--menu"
                     :secondaryMenu="true">
          </main-menu>
          </ul>
        </div>
      </header>
    `
});