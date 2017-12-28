"use strict";

$(document).ready(function () {
  // Mostrar y ocultar elementos
  function ocultar_rojo() {
    $("#texto_rojo").hide("slow", function () {
      $("#texto_azul").show(2000);
    });
  }

  function ocultar_azul() {
    $("#texto_rojo").show(3000, function () {
      $("#texto_azul").hide("slow");
    });
  }

  $("#texto_rojo").click(ocultar_rojo);
  $("#texto_azul").click(ocultar_azul);
  ocultar_azul();

  // Pasando opciones
  function prueba() {
    var options = {
      duration: 5000,
      easing: "easeOutExpo"
    };
    $("#prueba").hide(options);
  }

  $("#prueba").click(prueba);
});