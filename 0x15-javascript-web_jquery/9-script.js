// Use the JQuery API to fetch the translation of "hello" in French
$(document).ready(function() {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', function(data) {
    // Extract the translation from the fetched data
    var translation = data.hello;

    // Display the translation in the HTML tag <div id="hello">
    $('#hello').text(translation);
  });
});
