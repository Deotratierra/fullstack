"use strict";

$(document).ready(function () {

  $("#arrastrable").draggable({
    cursor: "move"
  });

  // Elemento "soltable"
  $("#soltable").droppable({
    drop: function drop(evento, ui) {
      console.log($(undefined));
      $("#informador").html("Lo has insertado, prueba a sacarlo");
      $("#informador").removeClass("red-text").addClass("green-text");
    },
    out: function out(evento, ui) {
      $("#informador").html("Ahora ha salido");
      $("#informador").removeClass("green-text").addClass("red-text");
    }
  });
});