// Use the JQuery API to fetch the character name from the URL
$(document).ready(function() {
  $.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function(data) {
    // Extract the character name from the fetched data
    var characterName = data.name;

    // Display the character name in the HTML tag <div id="character">
    $('#character').text(characterName);
  });
});
