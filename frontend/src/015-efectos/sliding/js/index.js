"use strict";

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

$(document).ready(function () {
  // Panel desplegable

  var Panel = function () {
    function Panel() {
      var _this = this;

      _classCallCheck(this, Panel);

      this.open = false;
      this.opener = $("#opener");
      this.opener.click(function () {
        if (_this.open == false) {
          _this.desplegar();
        } else {
          _this.replegar();
        }
      });
    }
    // Acciones

    Panel.prototype.desplegar = function desplegar() {
      $("#panel").slideDown("slow");
      this.open = true;
    };

    Panel.prototype.replegar = function replegar() {
      $("#panel").slideUp(2500);
      this.open = false;
    };

    return Panel;
  }();

  var panel = new Panel();
});