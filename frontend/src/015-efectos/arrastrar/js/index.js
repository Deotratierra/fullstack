"use strict";

$(document).ready(function () {

  // Elemento movible normal
  $("#movible").draggable();

  // Elemento movible con otro cursor
  $("#movible2").draggable({
    cursor: "move"
  });

  // Elemento movible con delay
  $("#movible3").draggable({
    cursor: "move",
    grid: [50, 50]
  });

  // Elemento movible con límites
  $("#movible4").draggable({
    cursor: "move",
    containment: "parent"
  });
});