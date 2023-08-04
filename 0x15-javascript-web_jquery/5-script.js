// Use the JQuery API to add a click event handler to DIV#add_item
$(document).ready(function() {
    $('DIV#add_item').click(function() {
      // Create a new <li> element with the text "Item"
      var newItem = $('<li>Item</li>');
  
      // Append the new <li> element to the <ul class="my_list">
      $('ul.my_list').append(newItem);
    });
  });  