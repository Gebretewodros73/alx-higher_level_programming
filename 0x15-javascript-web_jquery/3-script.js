// Use the JQuery API to add a click event handler to DIV#red_header
$(document).ready(function() {
    $('DIV#red_header').click(function() {
      // Toggle the "red" class on the <header> element
      $('header').toggleClass('red');
    });
  });  