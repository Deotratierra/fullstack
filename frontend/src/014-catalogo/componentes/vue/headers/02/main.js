Vue.component("header-2", {
    template: `
      <header id="header-2">
        <div id="header-2--container">
          <social-menu
           prestyle="hoverColor"
           containerId="header-2--social">
          </social-menu>
          <a href="#">
            <img src="img/logo.png" id="header-2--logo"></img>
          </a>

          <!--
          <main-menu containerId="header-1--menu"></main-menu>
          </ul>
          -->
        </div>
      </header>
    `
});