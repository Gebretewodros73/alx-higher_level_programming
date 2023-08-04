// Use the JQuery API to add a click event handler to DIV#toggle_header
$(document).ready(function() {
    $('DIV#toggle_header').click(function() {
      // Toggle the "red" class on the <header> element
      $('header').toggleClass('red');
  
      // If the "red" class is present, remove the "green" class, and vice versa
      if ($('header').hasClass('red')) {
        $('header').removeClass('green');
      } else {
        $('header').removeClass('red');
        $('header').addClass('green');
      }
    });
  });  