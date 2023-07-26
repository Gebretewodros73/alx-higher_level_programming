#!/usr/bin/node
const fs = require('fs');

function getMovieTitle (movieId) {
  const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

  fs.get(url)
    .then((response) => {
      const movieTitle = response.data.title;
      console.log(movieTitle);
    })
    .catch((error) => {
      if (error.response && error.response.status === 404) {
        console.error(`Movie with ID ${movieId} not found.`);
      } else {
        console.error(`Error: ${error.message}`);
      }
    });
}

// Check if the script is run from the command line with the movie ID argument
if (process.argv.length !== 3) {
  console.error('Usage: ./3-starwars_title.js <movie_ID>');
} else {
  const movieId = process.argv[2];
  getMovieTitle(movieId);
}
