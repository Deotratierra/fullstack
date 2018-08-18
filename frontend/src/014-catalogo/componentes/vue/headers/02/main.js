Vue.component("header-02", {
    template: `
      <header id="header-02">
        <div id="header-02--container">
          <date-info containerId="header-02--date-info"></date-info>

          <social-menu
           prestyle="hoverColor"
           containerId="header-02--social">
          </social-menu>
          <a href="#">
            <img src="img/logo.png" id="header-02--logo"></img>
          </a>

          <main-menu containerId="header-02--menu"></main-menu>
        </div>
      </header>
    `
});