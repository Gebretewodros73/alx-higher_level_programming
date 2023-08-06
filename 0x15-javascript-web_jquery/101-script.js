// Add a new <li> element to the list when the user clicks on DIV#add_item
$('#add_item').click(function() {
  $('.my_list').append('<li>Item</li>');
});

// Remove the last <li> element from the list when the user clicks on DIV#remove_item
$('#remove_item').click(function() {
  $('.my_list li:last-child').remove();
});

// Clear all elements from the list when the user clicks on DIV#clear_list
$('#clear_list').click(function() {
  $('.my_list').empty();
});
