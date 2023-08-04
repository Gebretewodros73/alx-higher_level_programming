// Use the JQuery API to add a click event handler to DIV#update_header
$(document).ready(function() {
    $('DIV#update_header').click(function() {
      // Update the text of the <header> element to "New Header!!!"
      $('header').text('New Header!!!');
    });
  });  