var acc = document.getElementsByClassName("accordion");
var i;

for (i = 0; i < acc.length; i++) {
  acc[i].addEventListener("click", function() {
    /* Toggle between adding and removing the "active" class,
    to highlight the button that controls the panel */
    this.classList.toggle("accordionActive");

    /* Toggle between hiding and showing the active panel */
    var accordionPanel = this.nextElementSibling;
    if (accordionPanel.style.display === "block") {
      accordionPanel.style.display = "none";
    } else {
      accordionPanel.style.display = "block";
    }
  });
}

var acc = document.getElementsByClassName("trAccordion");
var i;

for (i = 0; i < acc.length; i++) {
  acc[i].addEventListener("click", function() {
    /* Toggle between adding and removing the "active" class,
    to highlight the button that controls the panel */
    this.classList.toggle("accordionActive");

    /* Toggle between hiding and showing the active panel */
    var accordionRow = this.nextElementSibling;
    if (accordionRow.style.display === "table-row") {
      accordionRow.style.display = "none";
    } else {
      accordionRow.style.display = "table-row";
    }
  });
}
