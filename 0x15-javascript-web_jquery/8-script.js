// Use the JQuery API to fetch the list of Star Wars movies
$(document).ready(function() {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function(data) {
    // Extract the list of movies from the fetched data
    var movies = data.results;

    // Append the titles to the <ul id="list_movies"> element
    $.each(movies, function(index, movie) {
      $('#list_movies').append('<li>' + movie.title + '</li>');
    });
  });
});
