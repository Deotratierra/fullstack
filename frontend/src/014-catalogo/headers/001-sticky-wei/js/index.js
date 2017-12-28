"use strict";

var _typeof = typeof Symbol === "function" && typeof Symbol.iterator === "symbol" ? function (obj) { return typeof obj; } : function (obj) { return obj && typeof Symbol === "function" && obj.constructor === Symbol ? "symbol" : typeof obj; };

$(document).ready(function () {

    // ====================================================================
    // Función para redimensionar el menú y fijarlo al hacer scroll
    // https://codepen.io/chrissp26/pen/wfsvy
    function sticker(panel) {
        if ((typeof panel === "undefined" ? "undefined" : _typeof(panel)) !== undefined) {
            var pos = panel.offset().top,
                win = $(window);
            win.on("scroll", function () {
                win.scrollTop() >= pos ? on_stick(panel) : on_unstick(panel);
            });
        }
    };

    // Callback si el panel se pega en la parte superior de la pantalla
    function on_stick(panel) {
        $("#main-menu > ul > li").css({ padding: "1.5em .8em 1.5em .8em" }); // Cambio de padding en eje Y de los elementos del menú
        panel.css({
            position: "fixed",
            top: 0,
            right: 0,
            left: 0,
            height: "4em",
            "background-color": "rgba(0, 0, 0, .35)"
        });
        $("#main-menu-res").css({ position: "fixed", top: "65px" }); // Menú responsive
    }

    // Callback si el panel se despega de la parte superior de la pantalla
    function on_unstick(panel) {
        $("#main-menu > ul > li").css({ padding: "3em .8em 3em .8em" });
        panel.css({
            position: "static",
            "background-color": "rgba(0, 0, 0, 0)"
        });
        $("#main-menu-res").css({ position: "relative", top: "0px" });
        if ($(window).width() > 860) {
            panel.css({ height: "7.25em" });
        }
    }

    sticker($("#header-main-panel"));

    // ==================================================================

    // Toggle del menú responsive
    $("#main-menu-res-toggle").click(function () {
        $("#main-menu-res").toggle("fast");
    });
});