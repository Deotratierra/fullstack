"use strict";

$(document).ready(function () {
  // Agrandar texto
  function grande() {
    $("#texto").animate({ fontSize: "20px" }, 1000);
  }

  // Empequeñecer texto
  function enano() {
    $("#texto").animate({ fontSize: "12px" });
  }

  $("#grande").click(function () {
    return grande();
  });
  $("#enano").click(function () {
    return enano();
  });
});