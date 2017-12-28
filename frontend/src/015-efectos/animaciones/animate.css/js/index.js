"use strict";

$(document).ready(function () {

  $("#animacion1").click(function () {
    $("#animacion1").addClass("animated shake").one("animationend", function () {
      $("#animacion1").removeClass("animated shake");
    });
  });
});